# myRAG Deployment Runbook (VPS)

Target: `http://154.12.245.254/RAG-mat`

This runbook deploys `myRAG_app` with:
1. Reverse-proxy path routing at `/RAG-mat`
2. Docker Compose runtime (preferred)
3. VPS-side vector DB build as primary path
4. Local vector DB copy as controlled fallback
5. Non-disruptive behavior for already running VPS apps

## 1. Deployment Strategy

1. Reuse existing reverse proxy (Nginx/Caddy/Apache) if present.
2. Install missing components only.
3. Do not force package upgrades that can break current apps.
4. Bind app containers to localhost only:
- API: `127.0.0.1:18000`
- UI: `127.0.0.1:18001`
5. Publish only through reverse proxy path `/RAG-mat`.

## 2. Files Added for Deployment

1. `myRAG_app/deploy/Dockerfile.api`
2. `myRAG_app/deploy/Dockerfile.ui`
3. `myRAG_app/deploy/docker-compose.yml`
4. `myRAG_app/deploy/.env.example`
5. `myRAG_app/deploy/nginx/location-rag-mat.conf`
6. `myRAG_app/deploy/nginx/ui-container.conf`
7. `myRAG_app/deploy/caddy/rag-mat.caddy`
8. `myRAG_app/deploy/apache/rag-mat.conf`
9. `myRAG_app/deploy/scripts/vps_precheck.sh`
10. `myRAG_app/deploy/scripts/build_vector_db_vps.sh`
11. `myRAG_app/deploy/scripts/copy_vector_db_from_local.sh`
12. `myRAG_app/deploy/scripts/deploy_compose.sh`

## 3. Precheck Matrix and Decision Gate

Run precheck first on VPS:

```bash
bash myRAG_app/deploy/scripts/vps_precheck.sh \
  --knowledge-root /srv/myrag/myRAG_knowledge \
  --vector-db-path /srv/myrag/vector_db \
  --python-bin python3
```

Expected gates:
1. Knowledge root exists.
2. `OPENAI_API_KEY` exists.
3. Parser + ingestion dependencies available.
4. Disk free satisfies 3x estimated vector DB requirement.
5. No hard conflicts with existing proxy/service ownership.

Decision:
1. If precheck passes, continue with VPS build path.
2. If precheck fails and cannot be remediated quickly, use fallback copy path.

## 4. Prepare VPS Environment

Assume SSH user with sudo.

### 4.1 Install missing tools only

Check first:

```bash
command -v docker || echo "docker missing"
docker compose version || echo "compose missing"
command -v rsync || echo "rsync missing"
```

Install only missing packages (example Ubuntu):

```bash
sudo apt update
sudo apt install -y rsync curl
```

Install Docker/Compose only if absent and required by your chosen runtime.

### 4.2 Create deployment env

```bash
cd /path/to/repo/myRAG_app/deploy
cp .env.example .env.vps
```

Edit `.env.vps`:

1. `OPENAI_API_KEY`
2. `MYRAG_DB_PATH=/srv/myrag/vector_db`
3. `MYRAG_COLLECTION=myrag_docs`
4. `MYRAG_ALLOWED_ORIGINS=http://154.12.245.254`
5. `VITE_BASE_PATH=/RAG-mat/`
6. `VITE_API_BASE_URL=/RAG-mat`

## 5. Knowledge Base on VPS

Sync local knowledge to VPS:

```bash
rsync -az --delete /home/gabri/udemy/llm_engineering/myRAG_knowledge/ \
  user@154.12.245.254:/srv/myrag/myRAG_knowledge/
```

Validate on VPS:

```bash
find /srv/myrag/myRAG_knowledge -type f | wc -l
du -sh /srv/myrag/myRAG_knowledge
```

## 6. Primary Path: Build Vector DB on VPS

Run on VPS from repo root:

```bash
bash myRAG_app/deploy/scripts/build_vector_db_vps.sh \
  --knowledge-root /srv/myrag/myRAG_knowledge \
  --db-path /srv/myrag/vector_db \
  --collection myrag_docs \
  --python-bin .venv/bin/python
```

This wrapper performs:
1. strict parser audit
2. strict ingestion (`--reset --strict-parse`)
3. inspect validation with vector count > 0

Expected artifacts:
1. parser report in `/tmp/myrag_deploy_reports`
2. ingestion log
3. inspect log

## 7. Fallback Path: Copy Local vector_db

Use only if VPS build fails or is blocked.

Run locally:

```bash
bash myRAG_app/deploy/scripts/copy_vector_db_from_local.sh \
  --remote-host 154.12.245.254 \
  --remote-user user \
  --remote-db-path /srv/myrag/vector_db \
  --mode compose \
  --compose-project-dir /path/to/repo \
  --compose-file myRAG_app/deploy/docker-compose.yml \
  --remote-repo-path /path/to/repo \
  --remote-python-bin .venv/bin/python \
  --collection myrag_docs
```

The script:
1. stops only myRAG API service (mode-based)
2. rsyncs local `vector_db`
3. verifies `chroma.sqlite3`
4. restarts only myRAG API service
5. optionally runs remote inspect check

## 8. Deploy Containers

On VPS from repo root:

```bash
bash myRAG_app/deploy/scripts/deploy_compose.sh
```

Manual equivalent:

```bash
docker compose --env-file myRAG_app/deploy/.env.vps \
  -f myRAG_app/deploy/docker-compose.yml up -d --build
```

Check:

```bash
docker compose --env-file myRAG_app/deploy/.env.vps \
  -f myRAG_app/deploy/docker-compose.yml ps
curl -fsS http://127.0.0.1:18000/api/health
curl -fsSI http://127.0.0.1:18001/
```

## 9. Reverse Proxy Integration at `/RAG-mat`

Use existing proxy if present; install Nginx only if none exists.

### 9.1 Nginx (preferred if already installed)

1. Add contents of `myRAG_app/deploy/nginx/location-rag-mat.conf` inside existing `server` block for `154.12.245.254`.
2. Validate and reload:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

### 9.2 Caddy

Use `myRAG_app/deploy/caddy/rag-mat.caddy` snippet in existing site block, then reload Caddy.

### 9.3 Apache

Use `myRAG_app/deploy/apache/rag-mat.conf` snippet in existing vhost, ensure proxy modules enabled, then reload Apache.

## 10. Validation and Sign-Off

Run from any machine:

```bash
curl -i http://154.12.245.254/RAG-mat/api/health
curl -I http://154.12.245.254/RAG-mat/
```

Browser validation:
1. Open `http://154.12.245.254/RAG-mat/`
2. Register/login
3. Ask at least 2 follow-up queries
4. Verify sources appear
5. Refresh browser, verify threads persist

Non-regression validation:
1. Check existing VPS apps still reachable
2. Check existing containers/services unchanged

## 11. Rollback

1. Remove or comment `/RAG-mat` proxy routes.
2. Reload proxy.
3. Stop only myRAG compose stack:

```bash
docker compose --env-file myRAG_app/deploy/.env.vps \
  -f myRAG_app/deploy/docker-compose.yml down
```

4. Keep previous apps untouched.

## 12. Troubleshooting

1. `404` under `/RAG-mat/assets/...`
- Ensure UI built with `VITE_BASE_PATH=/RAG-mat/`.

2. API CORS blocked
- Verify `MYRAG_ALLOWED_ORIGINS` in `.env.vps`.

3. `I do not know` despite data
- Re-run VPS ingest with strict flags and inspect vector count.

4. Parser failures on VPS
- Install missing parser deps:

```bash
.venv/bin/python -m pip install pypdf docx2txt openpyxl pymupdf rapidocr-onnxruntime pillow
```

5. OpenAI failures during ingest/query
- Confirm `OPENAI_API_KEY` exported or present in `.env.vps` and visible to runtime.
