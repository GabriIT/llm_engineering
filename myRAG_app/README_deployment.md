# myRAG Deployment Runbook (VPS)

Target: `http://154.12.245.254/RAG-mat`

This runbook deploys `myRAG_app` with:
1. Reverse-proxy path routing at `/RAG-mat`
2. Docker Compose runtime (preferred)
3. VPS-side vector DB build as primary path
4. Local vector DB copy as controlled fallback
5. Non-disruptive behavior for already running VPS apps

## Script Default Behavior (`.env`-first)
1. Deployment scripts auto-load repo `.env` when present.
2. `MYRAG_DB_PATH` and `MYRAG_COLLECTION` are used as defaults where applicable.
3. Explicit flags always override defaults.
4. Affected scripts:
- `myRAG_app/deploy/scripts/vps_precheck.sh`
- `myRAG_app/deploy/scripts/build_vector_db_vps.sh`
- `myRAG_app/deploy/scripts/copy_vector_db_from_local.sh`
- `myRAG_app/deploy/scripts/rollback_vector_db.sh`

### Quick Env Check (VPS)
Run this before ingest/query/deploy to confirm the active DB/collection:
```bash
cd /home/ubuntu/myrag-deploy
set -a; source myRAG_app/deploy/.env.vps; set +a
echo "MYRAG_DB_PATH=$MYRAG_DB_PATH"
echo "MYRAG_COLLECTION=$MYRAG_COLLECTION"
```

For full local ingest mode commands, see:
`myRAG_app/README_Ingest.md`

## Fast Update (Existing VPS Deployment)

Use this when `/RAG-mat` is already deployed and you want the newest code.

Assumed VPS paths:
1. Repo root: `/home/ubuntu/myrag-deploy`
2. Deploy folder: `/home/ubuntu/myrag-deploy/myRAG_app/deploy`
3. Knowledge folder: `/home/ubuntu/myrag-deploy/myRAG_knowledge`
4. Vector DB folder: `/home/ubuntu/myrag-deploy/vector_db`

1. SSH to VPS and update repo:
```bash
ssh ubuntu@154.12.245.254
cd /home/ubuntu/myrag-deploy
git fetch --all
git pull --ff-only
```

2. Ensure deploy env exists and includes current values:
```bash
cd /home/ubuntu/myrag-deploy/myRAG_app/deploy
test -f .env.vps || cp .env.example .env.vps
```

For Ollama-backed chat model options (`qwen3.5:9b`, `llama3.2:latest`), set:
```bash
echo "OLLAMA_URL=http://172.17.0.1:11434" >> .env.vps
```

3. Rebuild and restart only myRAG stack:
```bash
cd /home/ubuntu/myrag-deploy/myRAG_app/deploy
bash scripts/deploy_compose.sh
```

4. Validate:
```bash
cd /home/ubuntu/myrag-deploy
curl -i http://127.0.0.1:18000/api/health
curl -i http://154.12.245.254/RAG-mat/api/health
curl -I http://154.12.245.254/RAG-mat/
```

5. Rebuild and rotate vector DB with backup (only if knowledge corpus changed):
```bash
cd /home/ubuntu/myrag-deploy
.venv/bin/python -m myRAG_app.vector.upgrade_cli \
  --knowledge-root /home/ubuntu/myrag-deploy/myRAG_knowledge \
  --active-db-path /home/ubuntu/myrag-deploy/vector_db \
  --collection myrag_docs \
  --strict-parse \
  --quiet-parser-warnings ; echo "exit=$?"
```

This keeps the previous vectorstore in:
`/home/ubuntu/myrag-deploy/vector_db_backups/`

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
13. `myRAG_app/deploy/scripts/rollback_vector_db.sh`

## 3. Precheck Matrix and Decision Gate

Run precheck first on VPS:

```bash
cd /home/ubuntu/myrag-deploy
bash myRAG_app/deploy/scripts/vps_precheck.sh \
  --knowledge-root /home/ubuntu/myrag-deploy/myRAG_knowledge \
  --python-bin /home/ubuntu/myrag-deploy/.venv/bin/python
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
cd /home/ubuntu/myrag-deploy/myRAG_app/deploy
cp .env.example .env.vps
```

Edit `.env.vps`:

1. `OPENAI_API_KEY`
2. `MYRAG_DB_PATH=/home/ubuntu/myrag-deploy/vector_db`
3. `MYRAG_COLLECTION=myrag_docs`
4. `MYRAG_ALLOWED_ORIGINS=http://154.12.245.254`
5. `VITE_BASE_PATH=/RAG-mat/`
6. `VITE_API_BASE_URL=/RAG-mat`

Important:
1. `MYRAG_DB_PATH` and `MYRAG_COLLECTION` define the active vectorstore for RAG at runtime.
2. API health exposes the active values: `GET /api/health`.

## 5. Knowledge Base on VPS

Sync local knowledge to VPS:

```bash
rsync -az --delete /home/gabri/udemy/llm_engineering/myRAG_knowledge/ \
  ubuntu@154.12.245.254:/home/ubuntu/myrag-deploy/myRAG_knowledge/
```

Validate on VPS:

```bash
cd /home/ubuntu/myrag-deploy
find /home/ubuntu/myrag-deploy/myRAG_knowledge -type f | wc -l
du -sh /home/ubuntu/myrag-deploy/myRAG_knowledge
```

## 6. Primary Path: Build Vector DB on VPS

Run on VPS from repo root:

```bash
cd /home/ubuntu/myrag-deploy
.venv/bin/python -m myRAG_app.vector.upgrade_cli \
  --knowledge-root /home/ubuntu/myrag-deploy/myRAG_knowledge \
  --active-db-path /home/ubuntu/myrag-deploy/vector_db \
  --collection myrag_docs \
  --strict-parse \
  --quiet-parser-warnings ; echo "exit=$?"
```

This performs:
1. candidate build in a second DB folder
2. strict parse gate
3. vector count validation
4. backup of current active DB
5. promotion of candidate DB as active

Expected artifacts:
1. active DB:
`/home/ubuntu/myrag-deploy/vector_db`
2. previous backup(s):
`/home/ubuntu/myrag-deploy/vector_db_backups/`

## 7. Fallback Path: Copy Local vector_db

Use only if VPS build fails or is blocked.

Run locally:

```bash
cd /home/gabri/udemy/llm_engineering
bash myRAG_app/deploy/scripts/copy_vector_db_from_local.sh \
  --remote-host 154.12.245.254 \
  --remote-user ubuntu \
  --remote-db-path /home/ubuntu/myrag-deploy/vector_db \
  --mode compose \
  --compose-project-dir /home/ubuntu/myrag-deploy \
  --compose-file myRAG_app/deploy/docker-compose.yml \
  --remote-repo-path /home/ubuntu/myrag-deploy \
  --remote-python-bin .venv/bin/python
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
cd /home/ubuntu/myrag-deploy
bash myRAG_app/deploy/scripts/deploy_compose.sh
```

Manual equivalent:

```bash
cd /home/ubuntu/myrag-deploy
docker compose --env-file myRAG_app/deploy/.env.vps \
  -f myRAG_app/deploy/docker-compose.yml up -d --build
```

Check:

```bash
cd /home/ubuntu/myrag-deploy
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
3. Stop only myRAG API container:

```bash
cd /home/ubuntu/myrag-deploy
docker compose --env-file myRAG_app/deploy/.env.vps \
  -f myRAG_app/deploy/docker-compose.yml stop myrag-api
```

4. Roll back vector DB to latest backup:

```bash
cd /home/ubuntu/myrag-deploy
bash myRAG_app/deploy/scripts/rollback_vector_db.sh
```

To restore a specific backup:

```bash
cd /home/ubuntu/myrag-deploy
bash myRAG_app/deploy/scripts/rollback_vector_db.sh \
  --backup-name vector_db_backup_YYYYMMDD_HHMMSS
```

Explicit override example:
```bash
cd /home/ubuntu/myrag-deploy
bash myRAG_app/deploy/scripts/rollback_vector_db.sh \
  --active-db-path /home/ubuntu/myrag-deploy/vector_db \
  --backup-root /home/ubuntu/myrag-deploy/vector_db_backups
```

5. Start myRAG API container:

```bash
cd /home/ubuntu/myrag-deploy
docker compose --env-file myRAG_app/deploy/.env.vps \
  -f myRAG_app/deploy/docker-compose.yml start myrag-api
```

6. Validate:

```bash
cd /home/ubuntu/myrag-deploy
curl -i http://127.0.0.1:18000/api/health
curl -i http://154.12.245.254/RAG-mat/api/health
```

7. If full app rollback is needed, stop only myRAG compose stack:

```bash
cd /home/ubuntu/myrag-deploy
docker compose --env-file myRAG_app/deploy/.env.vps \
  -f myRAG_app/deploy/docker-compose.yml down
```

8. Keep previous apps untouched.

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
cd /home/ubuntu/myrag-deploy
.venv/bin/python -m pip install pypdf docx2txt openpyxl pymupdf rapidocr-onnxruntime pillow
```

For PPTX parsing support:
```bash
cd /home/ubuntu/myrag-deploy
.venv/bin/python -m pip install python-pptx requests
```

Optional PPTX vision enrichment support:
```bash
sudo apt update
sudo apt install -y libreoffice poppler-utils
```

5. OpenAI failures during ingest/query
- Confirm `OPENAI_API_KEY` exported or present in `.env.vps` and visible to runtime.

6. Direct API run on VPS (without Docker) for debugging
- Run with env file so runtime uses `.env.vps` values, including active vectorstore:

```bash
cd /home/ubuntu/myrag-deploy
.venv/bin/uvicorn myRAG_app.api.server:app --host 0.0.0.0 --port 8000 --env-file myRAG_app/deploy/.env.vps
```

- Verify active store:

```bash
curl -s http://127.0.0.1:8000/api/health
```

7. Markdown vectorstore flow reference
- See:
`myRAG_app/README_markdown_vectorstore.md`

8. PPTX parser skill reference
- See:
`myRAG_app/README_pptx_skill_development.md`
