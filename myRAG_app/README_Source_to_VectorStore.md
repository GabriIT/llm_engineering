# Source to VectorStore Runbook (Indexed Source Required)

## Rule
All parsing/ingest source must come from:
`/home/gabri/udemy/llm_engineering/myRAG_knowledge_index`

Raw files in:
`/home/gabri/udemy/llm_engineering/myRAG_knowledge`
must be converted first with indexed naming.

## 0) Quick Env Check
```bash
cd /home/gabri/udemy/llm_engineering
set -a; source .env; set +a
echo "MYRAG_DB_PATH=$MYRAG_DB_PATH"
echo "MYRAG_COLLECTION=$MYRAG_COLLECTION"
echo "MYRAG_RAW_KNOWLEDGE_ROOT=${MYRAG_RAW_KNOWLEDGE_ROOT:-/home/gabri/udemy/llm_engineering/myRAG_knowledge}"
echo "MYRAG_KNOWLEDGE_ROOT=${MYRAG_KNOWLEDGE_ROOT:-/home/gabri/udemy/llm_engineering/myRAG_knowledge_index}"
```

## 1) Mandatory First Step: Build Indexed Source Tree
```bash
cd /home/gabri/udemy/llm_engineering
bash myRAG_app/skills/knowledge-index-renamer/scripts/run_indexing.sh \
  --input-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-root /home/gabri/udemy/llm_engineering/myRAG_knowledge_index \
  --report-path /tmp/myrag_knowledge_index_report.json \
  --clean-output
```

Verify:
```bash
find /home/gabri/udemy/llm_engineering/myRAG_knowledge_index -type f | wc -l
```

## 2) Wrapper Behavior (updated)
These wrappers now enforce indexed source:
1. They refresh `myRAG_knowledge_index` from `myRAG_knowledge` first.
2. They inject `--knowledge-root myRAG_knowledge_index` if missing.
3. They reject any non-indexed `--knowledge-root`.

Affected wrappers:
1. `myRAG_app/skills/parsing-output-guardian/scripts/run_parser_audit.sh`
2. `myRAG_app/skills/parsing-output-guardian/scripts/export_parser_chunks.sh`
3. `myRAG_app/skills/parsing-output-guardian/scripts/build_vectorstore.sh`
4. `myRAG_app/skills/folder-markdown-exporter/scripts/export_folder_markdown.sh`
5. `myRAG_app/skills/pptx-rag-parser/scripts/run_pptx_audit.sh`
6. `myRAG_app/skills/pptx-rag-parser/scripts/build_vectorstore_with_pptx.sh`
7. `myRAG_app/skills/pptx-rag-parser/scripts/run_incremental_source_markdown_chunks.sh`
8. `myRAG_app/skills/pptx-rag-parser/scripts/run_pptx_probe.sh` (requires indexed `--pptx-path`)

Optional speed flag when you already refreshed index in the same session:
```bash
export MYRAG_SKIP_INDEX_REFRESH=1
```

## 3) Optional: PPTX Probe (from indexed root)
Pick a PPTX from indexed tree:
```bash
find /home/gabri/udemy/llm_engineering/myRAG_knowledge_index -type f -iname "*.pptx" | head -n 1
```

Probe:
```bash
PPTX_FILE="$(find /home/gabri/udemy/llm_engineering/myRAG_knowledge_index -type f -iname '*.pptx' | head -n 1)"
bash myRAG_app/skills/pptx-rag-parser/scripts/run_pptx_probe.sh \
  --pptx-path "$PPTX_FILE" \
  --report-path /tmp/myrag_pptx_probe.json
```

## 4) Alternative A (Recommended): Safe Upgrade With Backup
```bash
.venv/bin/python -m myRAG_app.vector.upgrade_cli \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge_index \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --strict-parse \
  --quiet-parser-warnings ; echo "exit=$?"
```

## 5) Alternative B: Fast Append (No Reset)
```bash
.venv/bin/python -m myRAG_app.vector.ingest_cli \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge_index \
  --strict-parse \
  --quiet-parser-warnings ; echo "exit=$?"
```

## 6) Alternative C: Full Rebuild In Place (`--reset`)
```bash
.venv/bin/python -m myRAG_app.vector.ingest_cli \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge_index \
  --reset \
  --strict-parse \
  --quiet-parser-warnings ; echo "exit=$?"
```

## 7) Alternative D: Incremental Source -> Markdown -> Chunks
Wrapper auto-refreshes indexed source first.

```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/run_incremental_source_markdown_chunks.sh \
  --markdown-output-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge_incremental \
  --chunks-output-path /tmp/myrag_chunks_incremental.jsonl \
  --state-path /home/gabri/udemy/llm_engineering/myRAG_app/.state/incremental_source_manifest.json \
  --report-path /tmp/myrag_incremental_pipeline_report.json \
  --strict ; echo "exit=$?"
```

Include modified files:
```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/run_incremental_source_markdown_chunks.sh \
  --include-modified \
  --markdown-output-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge_incremental \
  --chunks-output-path /tmp/myrag_chunks_incremental.jsonl \
  --state-path /home/gabri/udemy/llm_engineering/myRAG_app/.state/incremental_source_manifest.json \
  --report-path /tmp/myrag_incremental_pipeline_report.json \
  --strict ; echo "exit=$?"
```

## 8) Alternative E: Markdown Vectorstore Build/Promote
```bash
.venv/bin/python -m myRAG_app.vector.markdown_upgrade_cli \
  --markdown-root /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown \
  --collection myrag_docs_markdown ; echo "exit=$?"
```

## 9) Wrapper-Only Daily Flow (short)
Audit:
```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/run_parser_audit.sh \
  --report-path /tmp/myrag_parse_report.json
```

Build vectorstore:
```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/build_vectorstore.sh \
  --reset \
  --strict-parse \
  --quiet-parser-warnings
```

Inspect:
```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/inspect_vectorstore.sh --sample 5
```

## 10) Verify New PPTX Chunks Exist
```bash
set -a; source .env; set +a
.venv/bin/python - <<'PY'
import os
from pathlib import Path
from langchain_chroma import Chroma

needle = ".pptx"
db = Path(os.environ["MYRAG_DB_PATH"]).expanduser().resolve()
collection = os.environ["MYRAG_COLLECTION"]
vs = Chroma(persist_directory=str(db), collection_name=collection)
data = vs._collection.get(include=["metadatas"])
count = 0
for m in data.get("metadatas", []):
    if isinstance(m, dict) and needle in str(m.get("source", "")):
        count += 1
print(f"pptx_chunks={count}")
PY
```

## 11) Rollback
```bash
bash myRAG_app/deploy/scripts/rollback_vector_db.sh
```

Specific backup:
```bash
bash myRAG_app/deploy/scripts/rollback_vector_db.sh \
  --backup-name vector_db_backup_YYYYMMDD_HHMMSS
```

## 12) Recommended Default Sequence
1. Run Step 1 (build indexed source).
2. Run Step 4 (safe upgrade).
3. Run inspect check:
```bash
.venv/bin/python -m myRAG_app.vector.inspect_cli --sample 5
```

This is the default production-safe path after any new raw file is added.
