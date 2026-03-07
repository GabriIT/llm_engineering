# Markdown Vectorstore Runbook

## Purpose
This runbook defines a deterministic path from raw knowledge files to a markdown-based Chroma vectorstore, then shows how to set that store as the active one used by RAG.

## End-to-End Logic
1. Parse raw files in `myRAG_knowledge` using the existing parser pipeline.
2. Export one markdown file per top-level knowledge folder.
3. Build a candidate markdown vectorstore.
4. Validate vector count and sample content.
5. Promote candidate to active markdown vectorstore (with backup).
6. Point API runtime to the desired active store via environment variables.

## Inputs and Outputs
1. Source root:
`/home/gabri/udemy/llm_engineering/myRAG_knowledge`
2. Markdown output:
`/home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge`
3. Active markdown vector DB:
`/home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown`
4. Markdown collection:
`myrag_docs_markdown`

## Skill Activation Checklist
1. Confirm `folder-markdown-exporter` skill exists:
`/home/gabri/udemy/llm_engineering/myRAG_app/skills/folder-markdown-exporter/SKILL.md`
2. Run markdown export through the skill wrapper (not ad-hoc scripts).
3. Check `/tmp/myrag_markdown_export_report.json` for failures before vector build.
4. Build candidate first (`--build-only`), inspect it, then promote.
5. Set active store via `MYRAG_DB_PATH` and `MYRAG_COLLECTION`, then confirm with `/api/health`.

## Step 1: Export folder-level markdown from source files
This uses the `folder-markdown-exporter` skill wrapper.

```bash
cd /home/gabri/udemy/llm_engineering
bash myRAG_app/skills/folder-markdown-exporter/scripts/export_folder_markdown.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --report-path /tmp/myrag_markdown_export_report.json
```

Strict mode:
```bash
cd /home/gabri/udemy/llm_engineering
bash myRAG_app/skills/folder-markdown-exporter/scripts/export_folder_markdown.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --report-path /tmp/myrag_markdown_export_report.json \
  --strict
```

## Step 2: Build markdown candidate vectorstore (safe)
```bash
cd /home/gabri/udemy/llm_engineering
CANDIDATE_DB="/home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown_candidate_$(date -u +%Y%m%d_%H%M%S)"
.venv/bin/python -m myRAG_app.vector.markdown_upgrade_cli \
  --markdown-root /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown \
  --candidate-db-path "$CANDIDATE_DB" \
  --collection myrag_docs_markdown \
  --build-only ; echo "exit=$?"
```

## Step 3: Inspect candidate
```bash
cd /home/gabri/udemy/llm_engineering
.venv/bin/python -m myRAG_app.vector.inspect_cli \
  --db-path "$CANDIDATE_DB" \
  --collection myrag_docs_markdown \
  --sample 3
```

## Step 4: Promote candidate as active (with backup)
```bash
cd /home/gabri/udemy/llm_engineering
.venv/bin/python -m myRAG_app.vector.markdown_upgrade_cli \
  --markdown-root /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown \
  --collection myrag_docs_markdown ; echo "exit=$?"
```

## Step 5: Set active vectorstore for RAG (local API)
In `/home/gabri/udemy/llm_engineering/.env`:

```bash
MYRAG_DB_PATH=/home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown
MYRAG_COLLECTION=myrag_docs_markdown
```

Run API with env file:
```bash
cd /home/gabri/udemy/llm_engineering
.venv/bin/uvicorn myRAG_app.api.server:app --host 0.0.0.0 --port 8000 --env-file .env
```

Verify runtime store:
```bash
curl -s http://localhost:8000/api/health
```

## Step 6: Set active vectorstore for VPS Docker deployment
In `/home/ubuntu/myrag-deploy/myRAG_app/deploy/.env.vps`:

```bash
MYRAG_DB_PATH=/home/ubuntu/myrag-deploy/vector_db
MYRAG_COLLECTION=myrag_docs
```

Then redeploy:
```bash
cd /home/ubuntu/myrag-deploy
docker compose --env-file myRAG_app/deploy/.env.vps \
  -f myRAG_app/deploy/docker-compose.yml up -d --build
```

Verify:
```bash
curl -s http://127.0.0.1:18000/api/health
```

## Rollback
Restore previous active DB:
```bash
cd /home/gabri/udemy/llm_engineering
bash myRAG_app/deploy/scripts/rollback_vector_db.sh \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown \
  --backup-root /home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown_backups
```

## Repeat for future upgrades
1. Add new files to `myRAG_knowledge`.
2. Re-run Step 1 through Step 4.
3. Keep `MYRAG_DB_PATH` and `MYRAG_COLLECTION` pointing to the intended active DB.
4. Verify `/api/health` and a sample query.
