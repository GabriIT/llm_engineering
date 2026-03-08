# PostgreSQL + pgvector Setup on My Ubuntu (`myRAG_threads`)

This document captures the setup flow used for local thread memory in `myRAG_app`.

## Why you saw `Thread memory is disabled`

`myRAG_app` only enables thread memory when this env var is set:

```bash
MYRAG_THREADS_ENABLED=1
```

If it is missing (or `0`), initializer output is:
`Thread memory is disabled. Set MYRAG_THREADS_ENABLED=1 to enable.`

## Setup Commands Followed

Run from shell on Ubuntu.

### 1) Detect PG16 cluster port (or create/start cluster first)

```bash
sudo pg_lsclusters
```

If no PG16 cluster exists:

```bash
sudo pg_createcluster 16 myrag --start
sudo pg_lsclusters
```

Set port variable from the cluster list:

```bash
PG16_PORT="$(sudo pg_lsclusters | awk '$1==16 {print $3; exit}')"
echo "$PG16_PORT"
```

If you have multiple PG16 clusters (`main`, `myrag`, etc.), verify which one contains the
`postgresql` role + `myRAG_threads` DB and use that port in `.env`.
The command above returns the first PG16 cluster only (often `5432`).
If your app DB is on cluster `myrag`, select explicitly:

```bash
PG16_PORT="$(sudo pg_lsclusters | awk '$1==16 && $2==\"myrag\" {print $3; exit}')"
echo "$PG16_PORT"   # expected: 5433 when using the myrag cluster
```

### 2) Create app role and database

```bash
sudo -u postgres psql -p "$PG16_PORT" -c "DO \$\$ BEGIN IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname='postgresql') THEN CREATE ROLE postgresql LOGIN PASSWORD 'postgresql'; END IF; END \$\$;"
sudo -u postgres psql -p "$PG16_PORT" -c "SELECT 'CREATE DATABASE \"myRAG_threads\" OWNER postgresql' WHERE NOT EXISTS (SELECT 1 FROM pg_database WHERE datname='myRAG_threads')\\gexec"
```

### 3) Create `vector` extension as superuser

```bash
sudo -u postgres psql -p "$PG16_PORT" -d myRAG_threads -c "CREATE EXTENSION IF NOT EXISTS vector;"
sudo -u postgres psql -p "$PG16_PORT" -d myRAG_threads -c "\dx vector"
```

### 4) Grant privileges to app role

```bash
sudo -u postgres psql -p "$PG16_PORT" -d myRAG_threads -c "GRANT ALL PRIVILEGES ON DATABASE \"myRAG_threads\" TO postgresql;"
sudo -u postgres psql -p "$PG16_PORT" -d myRAG_threads -c "GRANT USAGE, CREATE ON SCHEMA public TO postgresql;"
```

### 5) Configure `.env` for `myRAG_app`

In `/home/gabri/udemy/llm_engineering/.env`:

```bash
MYRAG_THREADS_ENABLED=1
MYRAG_THREADS_HOST=127.0.0.1
MYRAG_THREADS_PORT=<PG16_PORT>
MYRAG_THREADS_DB=myRAG_threads
MYRAG_THREADS_USER=postgresql
MYRAG_THREADS_PASSWORD=postgresql
MYRAG_THREADS_EMBEDDING_MODEL=text-embedding-3-large
MYRAG_THREADS_EMBEDDING_DIMS=3072
MYRAG_THREADS_RECENT_MESSAGES=10
MYRAG_THREADS_SEMANTIC_TOP_K=6
MYRAG_THREADS_MAX_HISTORY=24
```

Replace `<PG16_PORT>` with your real port value.

### 6) Initialize thread-memory schema

```bash
cd /home/gabri/udemy/llm_engineering
.venv/bin/python -m myRAG_app.api.init_thread_memory --json
```

### 7) Start API with env file

```bash
cd /home/gabri/udemy/llm_engineering
.venv/bin/uvicorn myRAG_app.api.server:app --host 0.0.0.0 --port 8000 --env-file .env
```

Health check:

```bash
curl -s http://127.0.0.1:8000/api/health | jq .
```

Expect thread memory fields with `"thread_memory_enabled": true`.
Important: `uvicorn` runs in foreground, so run the `curl` command from a second terminal.
If you do not see a `GET /api/health` log line in the server terminal, the health request did not run.

## Troubleshooting Notes

1. `enabled=true` but `ready=false` with password error:
   - Your `.env` port may point to the wrong cluster.
   - Check with:
     ```bash
     pg_lsclusters
     PGPASSWORD=postgresql psql -h 127.0.0.1 -p <PORT> -U postgresql -d myRAG_threads -c "select current_database();"
     ```

2. `column cannot have more than 2000 dimensions for ivfflat index`:
   - This can occur with `text-embedding-3-large` (`3072` dims) on some pgvector builds.
   - Current app behavior skips IVFFlat index creation automatically for vectors above `2000` dims, so initialization remains functional.

3. `init_thread_memory --json` is `ready=true` but API health does not show thread memory as ready:
   - Confirm API was started with `.env`:
     ```bash
     .venv/bin/uvicorn myRAG_app.api.server:app --host 0.0.0.0 --port 8000 --env-file .env
     ```
   - Then run health check from another terminal:
     ```bash
     curl -s http://127.0.0.1:8000/api/health | jq .
     ```

## One-shot Idempotent Bootstrap (Role + DB + Extension)

Use this when starting from scratch or re-running safely:

```bash
PG16_PORT="$(sudo pg_lsclusters | awk '$1==16 {print $3; exit}')"
if [ -z "$PG16_PORT" ]; then
  sudo pg_createcluster 16 myrag --start
  PG16_PORT="$(sudo pg_lsclusters | awk '$1==16 {print $3; exit}')"
fi

sudo -u postgres psql -p "$PG16_PORT" <<'SQL'
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname='postgresql') THEN
    CREATE ROLE postgresql LOGIN PASSWORD 'postgresql';
  END IF;
END $$;

SELECT 'CREATE DATABASE "myRAG_threads" OWNER postgresql'
WHERE NOT EXISTS (SELECT 1 FROM pg_database WHERE datname='myRAG_threads')\gexec
SQL

sudo -u postgres psql -p "$PG16_PORT" -d myRAG_threads <<'SQL'
CREATE EXTENSION IF NOT EXISTS vector;
GRANT ALL PRIVILEGES ON DATABASE "myRAG_threads" TO postgresql;
GRANT USAGE, CREATE ON SCHEMA public TO postgresql;
SQL

echo "PG16_PORT=$PG16_PORT"
```

Then set `.env` (`MYRAG_THREADS_ENABLED=1`, port, db, user, password) and run:

```bash
cd /home/gabri/udemy/llm_engineering
.venv/bin/python -m myRAG_app.api.init_thread_memory --json
```
