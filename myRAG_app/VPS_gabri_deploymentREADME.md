# VPS Deployment Guide (Gabri) - Ubuntu 24.04

Target URL: `http://154.12.245.254/RAG-mat`

This runbook is specific to your VPS deployment and keeps existing apps safe by:
1. Discovering current services first.
2. Installing only missing components.
3. Reusing the active reverse proxy where possible.
4. Keeping vector DB upgrade/copy/rollback options explicit.

## 0) Assumed VPS Paths

```bash
/home/ubuntu/myrag-deploy
├── myRAG_app
├── myRAG_knowledge
└── vector_db
```

If your repo path differs, replace paths in commands accordingly.

## 1) Connect and Baseline Discovery (Non-Disruptive)

```bash
ssh ubuntu@154.12.245.254
cd /home/ubuntu/myrag-deploy
```

Run full discovery snapshot:

```bash
bash myRAG_app/deploy/scripts/vps_precheck.sh \
  --knowledge-root /home/ubuntu/myrag-deploy/myRAG_knowledge \
  --vector-db-path /home/ubuntu/myrag-deploy/vector_db \
  --python-bin /home/ubuntu/myrag-deploy/.venv/bin/python \
  --output /tmp/myrag_vps_discovery_$(date +%Y%m%d_%H%M%S).log
```

The report includes:
1. OS + apt sources.
2. Running services and listeners.
3. Active proxy detection (`nginx/apache2/caddy`).
4. Node/npm/pm2 status + dependency impact checks.
5. PostgreSQL versions/clusters/packages.
6. Docker/compose/container status.

## 2) Install Missing Dependencies Safely

Use bootstrap script (install only when needed):

```bash
cd /home/ubuntu/myrag-deploy
bash myRAG_app/deploy/scripts/vps_bootstrap_ubuntu24.sh
```

Dry-run preview:

```bash
bash myRAG_app/deploy/scripts/vps_bootstrap_ubuntu24.sh --dry-run
```

### What it does
1. Node 20:
   1. If global node is already `>=20`: no changes.
   2. If missing/older: installs **user-scoped** Node 20 via `nvm` (does not replace global node used by other apps).
2. PostgreSQL 15+:
   1. Reuses existing `>=15`.
   2. If older/missing: installs PostgreSQL 16 side-by-side.
3. Nginx:
   1. Installs only if missing.
   2. If Apache/Caddy already active, keeps Nginx stopped/disabled to avoid 80/443 conflicts.

## 3) Prepare Deploy Env

```bash
cd /home/ubuntu/myrag-deploy/myRAG_app/deploy
test -f .env.vps || cp .env.example .env.vps
```

Set/update these values in `.env.vps`:

```bash
OPENAI_API_KEY=...
MYRAG_DB_PATH=/home/ubuntu/myrag-deploy/vector_db
MYRAG_COLLECTION=myrag_docs
MYRAG_ALLOWED_ORIGINS=http://154.12.245.254
VITE_BASE_PATH=/RAG-mat/
VITE_API_BASE_URL=/RAG-mat
```

Keep Ollama option available (not mandatory to use now):

```bash
OLLAMA_URL=http://172.17.0.1:11434
```

## 4) Deploy Containers

```bash
cd /home/ubuntu/myrag-deploy/myRAG_app/deploy
bash scripts/deploy_compose.sh
```

Container-local checks:

```bash
curl -s http://127.0.0.1:18000/api/health | jq .
curl -I http://127.0.0.1:18001/
```

## 5) Reverse Proxy for `/RAG-mat`

Use the active proxy detected in precheck. Do not switch proxy stack unless necessary.

On your current VPS, the active public proxy is the Docker container:
1. `games-proxy` (`nginx:1.27-alpine`) on port `80`
2. Config path: `/home/ubuntu/games-proxy/default.conf`
3. Upstreams already mapped to:
   1. `/RAG-mat/` -> `127.0.0.1:18001`
   2. `/RAG-mat/api/` -> `127.0.0.1:18000`
4. System Nginx package is installed but inactive/failed and not used for live traffic.

Validate current proxy mapping:

```bash
ssh ubuntu@154.12.245.254
sed -n '1,220p' /home/ubuntu/games-proxy/default.conf
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Ports}}' | grep games-proxy
```

If you edit `default.conf`, reload only the proxy container:

```bash
cd /home/ubuntu/games-proxy
docker compose restart
```

### 5.1 Nginx active
Use snippet:
`/home/ubuntu/myrag-deploy/myRAG_app/deploy/nginx/location-rag-mat.conf`

Then reload:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

### 5.2 Apache active
Use snippet:
`/home/ubuntu/myrag-deploy/myRAG_app/deploy/apache/rag-mat.conf`

Then reload:

```bash
sudo apachectl configtest
sudo systemctl reload apache2
```

### 5.3 Caddy active
Use snippet:
`/home/ubuntu/myrag-deploy/myRAG_app/deploy/caddy/rag-mat.caddy`

Then reload:

```bash
sudo caddy validate --config /etc/caddy/Caddyfile
sudo systemctl reload caddy
```

## 6) Vector Store on VPS (Preferred)

Quick env check before upgrade:

```bash
cd /home/ubuntu/myrag-deploy
set -a; source myRAG_app/deploy/.env.vps; set +a
echo "MYRAG_DB_PATH=$MYRAG_DB_PATH"
echo "MYRAG_COLLECTION=$MYRAG_COLLECTION"
```

Preferred command (strict parse, quiet warnings, keeps backups):

```bash
cd /home/ubuntu/myrag-deploy
.venv/bin/python -m myRAG_app.vector.upgrade_cli \
  --knowledge-root /home/ubuntu/myrag-deploy/myRAG_knowledge \
  --active-db-path /home/ubuntu/myrag-deploy/vector_db \
  --collection myrag_docs \
  --strict-parse \
  --quiet-parser-warnings ; echo "exit=$?"
```

## 7) Vector Store Fallback (Copy Local Active DB)

Run from your local machine:

```bash
cd /home/gabri/udemy/llm_engineering
bash myRAG_app/deploy/scripts/copy_vector_db_from_local.sh \
  --remote-host 154.12.245.254 \
  --remote-user ubuntu \
  --remote-repo-path /home/ubuntu/myrag-deploy \
  --remote-db-path /home/ubuntu/myrag-deploy/vector_db \
  --local-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --mode compose
```

## 8) Rollback Vector DB (if needed)

Run on VPS:

```bash
cd /home/ubuntu/myrag-deploy
bash myRAG_app/deploy/scripts/rollback_vector_db.sh \
  --active-db-path /home/ubuntu/myrag-deploy/vector_db
```

Then restart myRAG containers:

```bash
cd /home/ubuntu/myrag-deploy/myRAG_app/deploy
bash scripts/deploy_compose.sh
```

## 9) Final Validation

```bash
curl -s http://127.0.0.1:18000/api/health | jq .
curl -I http://154.12.245.254/RAG-mat/
curl -s http://154.12.245.254/RAG-mat/api/health | jq .
```

Manual UI check:
1. Register/login.
2. Create/select thread.
3. Rename/delete thread.
4. Ask query and verify answer + sources.

Non-regression:
1. Verify pre-existing apps behind proxy still respond exactly as before.
