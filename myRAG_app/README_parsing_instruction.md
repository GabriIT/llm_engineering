# myRAG Parsing and Vector Upgrade Instructions

This guide explains how to parse updated source files from `myRAG_knowledge`, build a new vector store safely, and roll back if needed.

## Scope
Use this flow whenever you add/replace files under:
`/home/gabri/udemy/llm_engineering/myRAG_knowledge`

## 1) Pre-check (recommended)
Run parser audit first:

```bash
cd /home/gabri/udemy/llm_engineering
.venv/bin/python -m myRAG_app.parser.audit \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --report-path /tmp/myrag_parse_report_pre_upgrade.json
```

## 2) Build new vector store with backup + promotion
Recommended command (strict parse gate + explicit exit code):

```bash
cd /home/gabri/udemy/llm_engineering
.venv/bin/python -m myRAG_app.vector.upgrade_cli \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --strict-parse \
  --quiet-parser-warnings ; echo "exit=$?"
```

Interpretation:
1. `exit=0`: success, new candidate promoted to active DB.
2. `exit=1`: strict parse or promotion/validation failure.
3. `exit=2`: argument/validation error.

## 3) What the upgrade command does
1. Builds a second candidate vector store in a timestamped folder.
2. Validates parser results and vector count.
3. Moves current active DB to backup folder.
4. Promotes candidate to active DB.
5. Keeps only the latest N backups (default: 5).

Backup location:
`/home/gabri/udemy/llm_engineering/myRAG_app/vector_db_backups`

## 4) Verify active vector store
```bash
cd /home/gabri/udemy/llm_engineering
.venv/bin/python -m myRAG_app.vector.inspect_cli \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --sample 3
```

## 5) Roll back to previous vector store (if needed)
Restore latest backup:

```bash
cd /home/gabri/udemy/llm_engineering
bash myRAG_app/deploy/scripts/rollback_vector_db.sh \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --backup-root /home/gabri/udemy/llm_engineering/myRAG_app/vector_db_backups
```

Restore a specific backup:

```bash
cd /home/gabri/udemy/llm_engineering
bash myRAG_app/deploy/scripts/rollback_vector_db.sh \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --backup-root /home/gabri/udemy/llm_engineering/myRAG_app/vector_db_backups \
  --backup-name vector_db_backup_YYYYMMDD_HHMMSS
```

Dry-run rollback plan:

```bash
cd /home/gabri/udemy/llm_engineering
bash myRAG_app/deploy/scripts/rollback_vector_db.sh --dry-run
```

## 6) Noise reduction for parser warnings
If your terminal shows many PDF backend warnings (e.g., font/xref diagnostics), use:
`--quiet-parser-warnings`

This suppresses parser stderr noise during build while preserving parse result checks.
