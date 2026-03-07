# myRAG Ingest CLI Guide

## Purpose
This is a straight command guide for all ingest modes available in `myRAG_app`, including safe upgrade and rollback-friendly workflows.

For a dedicated runbook specifically for "new file added" workflows:
`myRAG_app/README_Source_to_VectorStore.md`

Run commands from:
`/home/gabri/udemy/llm_engineering`

## 0) Quick Env Check (recommended first)
```bash
cd /home/gabri/udemy/llm_engineering
set -a; source .env; set +a
echo "MYRAG_DB_PATH=$MYRAG_DB_PATH"
echo "MYRAG_COLLECTION=$MYRAG_COLLECTION"
```

## 1) Direct Raw Source Ingest (`ingest_cli`)
Use this when you want a direct build from `myRAG_knowledge`.

Reset and rebuild:
```bash
.venv/bin/python -m myRAG_app.vector.ingest_cli \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --reset \
  --strict-parse \
  --quiet-parser-warnings
```

Append without reset:
```bash
.venv/bin/python -m myRAG_app.vector.ingest_cli \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --strict-parse \
  --quiet-parser-warnings
```

Override DB/collection explicitly:
```bash
.venv/bin/python -m myRAG_app.vector.ingest_cli \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --reset
```

## 2) Safe Upgrade Ingest with Backup (`upgrade_cli`)
Use this for production-safe rotation: build candidate -> validate -> backup -> promote.

```bash
.venv/bin/python -m myRAG_app.vector.upgrade_cli \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --strict-parse \
  --quiet-parser-warnings ; echo "exit=$?"
```

Candidate only (no promotion):
```bash
.venv/bin/python -m myRAG_app.vector.upgrade_cli \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --build-only
```

## 3) Markdown-Based Ingest (`markdown_upgrade_cli`)
Use this when indexing from `myRAG_app/markdown_knowledge` instead of raw files.

```bash
.venv/bin/python -m myRAG_app.vector.markdown_upgrade_cli \
  --markdown-root /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown \
  --collection myrag_docs_markdown ; echo "exit=$?"
```

Candidate only:
```bash
.venv/bin/python -m myRAG_app.vector.markdown_upgrade_cli \
  --markdown-root /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown \
  --collection myrag_docs_markdown \
  --build-only
```

## 4) Incremental New-Files Pipeline (Source -> Markdown -> Chunks)
Use this to process only newly added source files efficiently.

```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/run_incremental_source_markdown_chunks.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --markdown-output-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge_incremental \
  --chunks-output-path /tmp/myrag_chunks_incremental.jsonl \
  --state-path /home/gabri/udemy/llm_engineering/myRAG_app/.state/incremental_source_manifest.json \
  --report-path /tmp/myrag_incremental_pipeline_report.json \
  --strict
```

If new markdown should become the active markdown DB, run Section 3 afterward.

## 5) PPTX-Aware Ingest Flow
Use these checks when new `.pptx` files are added.

Probe a single PPTX:
```bash
.venv/bin/python -m myRAG_app.parser.pptx_probe \
  --pptx-path "/home/gabri/udemy/llm_engineering/myRAG_knowledge/Metal_Replacement/202401 - Metal Replacement.pptx" \
  --report-path /tmp/myrag_pptx_probe.json
```

Audit full corpus (includes `.pptx`):
```bash
.venv/bin/python -m myRAG_app.parser.audit \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --report-path /tmp/myrag_parse_report.json \
  --strict
```

Then ingest via Section 1 or Section 2.

## 6) Wrapper Scripts (Env-First Defaults)
These wrappers auto-load `.env` and use `MYRAG_DB_PATH` / `MYRAG_COLLECTION` if flags are omitted.

Build:
```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/build_vectorstore.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --reset
```

Inspect:
```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/inspect_vectorstore.sh --sample 3
```

Query:
```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/query_vectorstore.sh \
  --question "What are successful applications of HT?" \
  --k 8
```

## 7) Common Ingest Options
1. `--strict-parse`: exit non-zero when parser has failed files.
2. `--quiet-parser-warnings`: reduces parser stderr noise in terminal.
3. `--chunk-size` and `--chunk-overlap`: chunking control.
4. `--embedding-model`: embedding model override (default `text-embedding-3-large`).
5. `--db-path` / `--collection`: explicit target override.

## 8) Verify Active Store and Content
Inspect active store:
```bash
.venv/bin/python -m myRAG_app.vector.inspect_cli --sample 3
```

API health check (if backend running):
```bash
curl -s http://localhost:8000/api/health
```

## 9) Rollback
Restore latest backup of active store:
```bash
bash myRAG_app/deploy/scripts/rollback_vector_db.sh
```

Restore a specific backup:
```bash
bash myRAG_app/deploy/scripts/rollback_vector_db.sh \
  --backup-name vector_db_backup_YYYYMMDD_HHMMSS
```
