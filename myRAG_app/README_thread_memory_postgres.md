# Thread Memory (PostgreSQL + pgvector)

## Purpose
Enable server-side thread memory per `username + thread_id` so follow-up queries can use prior dialog context persisted in PostgreSQL.

This works with your local Ubuntu + Ollama chat setup.  
Chat model can be Ollama; thread-memory semantic recall uses embeddings (default: `text-embedding-3-large`).

## 1) Local Ubuntu Setup
Run from terminal on local machine.

### 1.1 Install PostgreSQL
```bash
sudo apt update
sudo apt install -y postgresql postgresql-contrib
sudo systemctl enable --now postgresql
```

### 1.2 Install pgvector extension package
```bash
PG_MAJOR="$(psql -V | awk '{print $3}' | cut -d. -f1)"
sudo apt install -y "postgresql-${PG_MAJOR}-pgvector"
```

If package is unavailable, install pgvector from source:
```bash
sudo apt install -y git build-essential postgresql-server-dev-"$PG_MAJOR"
git clone --depth 1 https://github.com/pgvector/pgvector.git /tmp/pgvector
cd /tmp/pgvector
make
sudo make install
sudo systemctl restart postgresql
```

### 1.3 Create role/database (as requested)
User: `postgresql`  
Password: `postgresql`  
Database: `myRAG_threads`

```bash
sudo -u postgres psql <<'SQL'
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'postgresql') THEN
    CREATE ROLE postgresql LOGIN PASSWORD 'postgresql';
  ELSE
    ALTER ROLE postgresql WITH LOGIN PASSWORD 'postgresql';
  END IF;
END
$$;
SQL
```

```bash
sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname='myRAG_threads'" | grep -q 1 || \
sudo -u postgres createdb -O postgresql myRAG_threads
```

Enable pgvector in the DB:
```bash
PGPASSWORD=postgresql psql -h 127.0.0.1 -U postgresql -d myRAG_threads -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

### 1.4 Install Python driver dependency
```bash
cd /home/gabri/udemy/llm_engineering
uv pip install --python .venv/bin/python "psycopg[binary]"
```

### 1.5 Configure app env
Add to `/home/gabri/udemy/llm_engineering/.env`:
```bash
MYRAG_THREADS_ENABLED=1
MYRAG_THREADS_DB_HOST=127.0.0.1
MYRAG_THREADS_DB_PORT=5432
MYRAG_THREADS_DB_NAME=myRAG_threads
MYRAG_THREADS_DB_USER=postgresql
MYRAG_THREADS_DB_PASSWORD=postgresql
MYRAG_THREADS_DB_SSLMODE=disable
MYRAG_THREADS_VECTOR_DIMS=3072
MYRAG_THREADS_RECENT_MESSAGES=10
MYRAG_THREADS_SEMANTIC_TOP_K=6
MYRAG_THREADS_MAX_HISTORY_MESSAGES=24
```

### 1.6 Initialize/check schema
```bash
cd /home/gabri/udemy/llm_engineering
.venv/bin/python -m myRAG_app.api.init_thread_memory --json
```

Expected:
1. `"enabled": true`
2. `"ready": true`
3. `"db_name": "myRAG_threads"`

### 1.7 Start backend
```bash
cd /home/gabri/udemy/llm_engineering
.venv/bin/uvicorn myRAG_app.api.server:app --host 0.0.0.0 --port 8000 --env-file .env
```

### 1.8 Verify thread memory in API
```bash
curl -s http://localhost:8000/api/health | jq
```

Check:
1. `thread_memory_enabled: true`
2. `thread_memory_ready: true`

## 2) How UI Uses It
UI now sends:
1. `username`
2. `thread_id`
with each query.

Server behavior:
1. Reads prior messages from PostgreSQL for that user/thread.
2. Adds recent + semantic matches (pgvector similarity).
3. Calls LLM with that memory context.
4. Persists current user question + assistant response back to DB.

## 3) Inspect Stored Dialog in PostgreSQL
```bash
PGPASSWORD=postgresql psql -h 127.0.0.1 -U postgresql -d myRAG_threads -c \
"SELECT username, thread_id, role, left(content,120) AS preview, created_at FROM myrag_thread_messages ORDER BY id DESC LIMIT 20;"
```

## 4) VPS Deployment Commands
Use this when deploying thread memory on VPS.

### 4.1 Install PostgreSQL + pgvector on VPS
```bash
ssh ubuntu@154.12.245.254
sudo apt update
sudo apt install -y postgresql postgresql-contrib
PG_MAJOR="$(psql -V | awk '{print $3}' | cut -d. -f1)"
sudo apt install -y "postgresql-${PG_MAJOR}-pgvector"
sudo systemctl enable --now postgresql
```

### 4.2 Create role/database on VPS
```bash
sudo -u postgres psql <<'SQL'
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'postgresql') THEN
    CREATE ROLE postgresql LOGIN PASSWORD 'postgresql';
  ELSE
    ALTER ROLE postgresql WITH LOGIN PASSWORD 'postgresql';
  END IF;
END
$$;
SQL
```

```bash
sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname='myRAG_threads'" | grep -q 1 || \
sudo -u postgres createdb -O postgresql myRAG_threads
PGPASSWORD=postgresql psql -h 127.0.0.1 -U postgresql -d myRAG_threads -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

### 4.3 Set deployment env
In `/home/ubuntu/myrag-deploy/myRAG_app/deploy/.env.vps` add:
```bash
MYRAG_THREADS_ENABLED=1
MYRAG_THREADS_DB_HOST=172.17.0.1
MYRAG_THREADS_DB_PORT=5432
MYRAG_THREADS_DB_NAME=myRAG_threads
MYRAG_THREADS_DB_USER=postgresql
MYRAG_THREADS_DB_PASSWORD=postgresql
MYRAG_THREADS_DB_SSLMODE=disable
MYRAG_THREADS_VECTOR_DIMS=3072
MYRAG_THREADS_RECENT_MESSAGES=10
MYRAG_THREADS_SEMANTIC_TOP_K=6
MYRAG_THREADS_MAX_HISTORY_MESSAGES=24
```

Note:
1. If API runs on host (not Docker), use `127.0.0.1`.
2. If API runs in Docker and PostgreSQL runs on host, use `172.17.0.1`.

### 4.4 Redeploy and verify
```bash
cd /home/ubuntu/myrag-deploy
bash myRAG_app/deploy/scripts/deploy_compose.sh
curl -s http://127.0.0.1:18000/api/health | jq
```

Expected:
1. `thread_memory_enabled: true`
2. `thread_memory_ready: true`

## 5) Troubleshooting
1. `thread_memory_ready=false`: check DB creds/host and run `init_thread_memory`.
2. `psycopg not installed`: `uv pip install --python .venv/bin/python "psycopg[binary]"`.
3. `extension "vector" does not exist`: install pgvector package and run `CREATE EXTENSION vector`.
