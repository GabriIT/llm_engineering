# myRAG App - Parsing Agent Runbook

## Purpose
This app contains a robust parsing pipeline for a mixed-format RAG knowledge base, a reusable parsing skill module, and local Chroma vectorstore integration for retrieval with LangChain.

## Vectorstore Env Defaults
1. Wrapper scripts auto-load repo `.env` and use `MYRAG_DB_PATH` and `MYRAG_COLLECTION` when `--db-path`/`--collection` are omitted.
2. This applies to:
- `myRAG_app/skills/parsing-output-guardian/scripts/build_vectorstore.sh`
- `myRAG_app/skills/parsing-output-guardian/scripts/inspect_vectorstore.sh`
- `myRAG_app/skills/parsing-output-guardian/scripts/query_vectorstore.sh`
- `myRAG_app/skills/pptx-rag-parser/scripts/build_vectorstore_with_pptx.sh`
- `myRAG_app/deploy/scripts/rollback_vector_db.sh`
- `myRAG_app/deploy/scripts/build_vector_db_vps.sh`
- `myRAG_app/deploy/scripts/copy_vector_db_from_local.sh`
- `myRAG_app/deploy/scripts/vps_precheck.sh`
3. Any explicit CLI flag overrides `.env` defaults.

### Quick Env Check
Run this before ingest/query to confirm active DB target:
```bash
cd /home/gabri/udemy/llm_engineering
set -a; source .env; set +a
echo "MYRAG_DB_PATH=$MYRAG_DB_PATH"
echo "MYRAG_COLLECTION=$MYRAG_COLLECTION"
```

## Current Parsing Capabilities
1. Parse `.pdf`, `.docx`, `.xlsx`, and `.pptx` from:
`/home/gabri/udemy/llm_engineering/myRAG_knowledge`
2. Apply format-specific fallback strategies.
3. Apply OCR fallback for scan-like/image-only PDFs.
4. Produce structured parse audit JSON.
5. Export chunked JSONL records for vector ingestion.
6. Validate chunk JSONL integrity before indexing.
7. Build and inspect local Chroma vectorstore.
8. Run local RAG query CLI using the same models as week5 (`gpt-4.1-nano`, `text-embedding-3-large`).

## Step-by-Step Commands Executed
Run commands from repository root:
`/home/gabri/udemy/llm_engineering`

### 1. Install primary parser libraries
```bash
uv pip install --python .venv/bin/python pypdf docx2txt openpyxl python-pptx requests
```

### 2. Verify imports
```bash
.venv/bin/python -c "import pypdf, docx2txt, openpyxl, pptx; print('imports_ok')"
```

### 3. Run parser audit (before OCR fallback integration)
```bash
.venv/bin/python -m myRAG_app.parser.audit \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --report-path /tmp/myrag_parse_report_after_libs.json
```

### 4. Install OCR dependencies for scan-like PDFs
```bash
UV_HTTP_TIMEOUT=180 uv pip install --python .venv/bin/python \
  pymupdf rapidocr-onnxruntime pillow
```

### 5. Validate OCR extraction on previously failing PDF
```bash
.venv/bin/python - <<'PY'
from pathlib import Path
import fitz, numpy as np
from rapidocr_onnxruntime import RapidOCR

pdf = Path("/home/gabri/udemy/llm_engineering/myRAG_knowledge/Certifications/ACS Grilamid LBV-50H FWA black 9225 18-12.pdf")
ocr = RapidOCR()
doc = fitz.open(pdf)
combined = []
for page in doc:
    pix = page.get_pixmap(matrix=fitz.Matrix(2,2), alpha=False)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    result, _ = ocr(img)
    if result:
        combined.extend([r[1] for r in result if len(r) >= 2])
print("chars", len("\n".join(combined)))
PY
```

### 6. Run parser tests
```bash
.venv/bin/python -m unittest discover -s myRAG_app/tests -p 'test_*.py' -v
```

### 7. Run final parser audit (all files successful)
```bash
.venv/bin/python -m myRAG_app.parser.audit \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --report-path /tmp/myrag_parse_report.json
```

### 8. Export structured chunk JSONL for vector DB
```bash
.venv/bin/python -m myRAG_app.parser.export_chunks \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-path /tmp/myrag_chunks.jsonl
```

### 8b. Probe a single PPTX before full ingestion
```bash
.venv/bin/python -m myRAG_app.parser.pptx_probe \
  --pptx-path "/home/gabri/udemy/llm_engineering/myRAG_knowledge/Metal_Replacement/202401 - Metal Replacement.pptx" \
  --report-path /tmp/myrag_pptx_probe.json
```

### 9. Create parsing skill module
```bash
python3 /home/gabri/.codex/skills/.system/skill-creator/scripts/init_skill.py \
  parsing-output-guardian \
  --path myRAG_app/skills \
  --resources scripts,references \
  --interface display_name='Parsing Output Guardian' \
  --interface short_description='Validate and secure RAG parsing output' \
  --interface default_prompt='Use $parsing-output-guardian to run parser audit, OCR-aware validation, and JSONL chunk export checks.'
```

### 10. Validate skill definition
```bash
python3 /home/gabri/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /home/gabri/udemy/llm_engineering/myRAG_app/skills/parsing-output-guardian
```

### 11. Build local Chroma vectorstore
```bash
.venv/bin/python -m myRAG_app.vector.ingest_cli \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --reset
```

### 12. Inspect local Chroma collection
```bash
.venv/bin/python -m myRAG_app.vector.inspect_cli \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --sample 3
```

### 13. Query local vectorstore with RAG
```bash
.venv/bin/python -m myRAG_app.vector.query_cli \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --question "Summarize the ACS Grilamid LBV-50H certification." \
  --k 12 \
  --search-type mmr \
  --fetch-k 60 \
  --lambda-mult 0.25 \
  --doc-type Certifications \
  --source-contains "LBV-50H" \
  --show-context
```

### 14. Upgrade vectorstore with backup (recommended for new knowledge files)
Stop backend/API first, then run:
```bash
.venv/bin/python -m myRAG_app.vector.upgrade_cli \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --strict-parse \
  --quiet-parser-warnings ; echo "exit=$?"
```

What it does:
1. Builds a second candidate vectorstore with new data.
2. Validates non-zero vectors.
3. Moves current `vector_db` into backup folder:
`/home/gabri/udemy/llm_engineering/myRAG_app/vector_db_backups/`
4. Promotes candidate to active `vector_db`.

Optional:
```bash
# Build candidate only (no promotion)
.venv/bin/python -m myRAG_app.vector.upgrade_cli \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --build-only

# Keep more historical backups
.venv/bin/python -m myRAG_app.vector.upgrade_cli \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --keep-backups 10
```

Detailed parsing + upgrade + rollback runbook:
`myRAG_app/README_parsing_instruction.md`

### 15. Roll back to previous vectorstore backup
If a new upgrade is not satisfactory, restore a backup:
```bash
cd /home/gabri/udemy/llm_engineering
bash myRAG_app/deploy/scripts/rollback_vector_db.sh
```

To restore a specific backup folder:
```bash
cd /home/gabri/udemy/llm_engineering
bash myRAG_app/deploy/scripts/rollback_vector_db.sh \
  --backup-name vector_db_backup_YYYYMMDD_HHMMSS
```

Override defaults when needed:
```bash
cd /home/gabri/udemy/llm_engineering
bash myRAG_app/deploy/scripts/rollback_vector_db.sh \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --backup-root /home/gabri/udemy/llm_engineering/myRAG_app/vector_db_backups
```

### 16. Upgrade markdown-based vectorstore with backup
Use this when indexing from markdown snapshots (`myRAG_app/markdown_knowledge`) instead of raw source files.

```bash
.venv/bin/python -m myRAG_app.vector.markdown_upgrade_cli \
  --markdown-root /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown \
  --collection myrag_docs_markdown \
  --build-only
```

Promote as active markdown DB:
```bash
.venv/bin/python -m myRAG_app.vector.markdown_upgrade_cli \
  --markdown-root /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown \
  --collection myrag_docs_markdown
```

Inspect markdown DB:
```bash
.venv/bin/python -m myRAG_app.vector.inspect_cli \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown \
  --collection myrag_docs_markdown \
  --sample 3
```

## New Parsing Agent Skill
Skill location:
`myRAG_app/skills/parsing-output-guardian`

### What the skill does
1. Standardize parsing pipeline execution.
2. Enforce audit-first workflow with explicit status visibility.
3. Export vector-ready chunk JSONL.
4. Validate JSONL structure and uniqueness.
5. Provide troubleshooting guidance for dependency and OCR issues.

### Skill resources
1. `SKILL.md`
Main workflow and invocation guidance.
2. `scripts/run_parser_audit.sh`
Wrapper for parser audit CLI.
3. `scripts/export_parser_chunks.sh`
Wrapper for chunk export CLI.
4. `scripts/validate_chunks_jsonl.py`
JSONL structural and integrity checks.
5. `scripts/build_vectorstore.sh`
Wrapper for Chroma ingestion CLI.
6. `scripts/inspect_vectorstore.sh`
Wrapper for Chroma inspect CLI.
7. `scripts/query_vectorstore.sh`
Wrapper for local RAG query CLI.
8. `references/workflow.md`
Execution runbook and strict-mode sequence.
9. `references/troubleshooting.md`
Fix guidance for parsing and OCR failures.
10. `agents/openai.yaml`
UI metadata for the skill.

## New PPTX Parsing Skill
Skill location:
`myRAG_app/skills/pptx-rag-parser`

Use when `.pptx` decks must be parsed for RAG with text-first extraction and optional selective vision enrichment.

Quick commands:
```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/run_incremental_source_markdown_chunks.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --markdown-output-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge_incremental \
  --chunks-output-path /tmp/myrag_chunks_incremental.jsonl \
  --state-path /home/gabri/udemy/llm_engineering/myRAG_app/.state/incremental_source_manifest.json \
  --report-path /tmp/myrag_incremental_pipeline_report.json \
  --strict
```

```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/run_pptx_probe.sh \
  --pptx-path "/home/gabri/udemy/llm_engineering/myRAG_knowledge/Metal_Replacement/202401 - Metal Replacement.pptx" \
  --report-path /tmp/myrag_pptx_probe.json
```

```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/run_pptx_audit.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --report-path /tmp/myrag_parse_report.json \
  --strict
```

```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/build_vectorstore_with_pptx.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --reset \
  --strict-parse
```

## Daily Usage Commands
### Audit
```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/run_parser_audit.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --report-path /tmp/myrag_parse_report.json
```

### Export chunks
```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/export_parser_chunks.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-path /tmp/myrag_chunks.jsonl
```

### Validate chunk output
```bash
.venv/bin/python myRAG_app/skills/parsing-output-guardian/scripts/validate_chunks_jsonl.py \
  --input /tmp/myrag_chunks.jsonl
```

### Build vectorstore
```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/build_vectorstore.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --reset
```

### Inspect vectorstore
```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/inspect_vectorstore.sh \
  --sample 3
```

### Query vectorstore
```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/query_vectorstore.sh \
  --question "What does the LBV-50H ACS certificate state?" \
  --k 12 \
  --search-type mmr \
  --fetch-k 60 \
  --lambda-mult 0.25 \
  --doc-type Certifications \
  --source-contains "LBV-50H"
```

Explicit override example:
```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/query_vectorstore.sh \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --question "What does the LBV-50H ACS certificate state?"
```

## Folder-Level Markdown Export Skill
Skill location:
`myRAG_app/skills/folder-markdown-exporter`

Use this skill to export parsed knowledge into one markdown file per top-level folder in `myRAG_knowledge`.

### Export command
```bash
bash myRAG_app/skills/folder-markdown-exporter/scripts/export_folder_markdown.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --report-path /tmp/myrag_markdown_export_report.json
```

### Strict export command
```bash
bash myRAG_app/skills/folder-markdown-exporter/scripts/export_folder_markdown.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --report-path /tmp/myrag_markdown_export_report.json \
  --strict
```

### Export outputs
1. Markdown files:
`/home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge/*.md`
2. Export report:
`/tmp/myrag_markdown_export_report.json`

## FAQ CSV Generator Skill
Skill location:
`myRAG_app/skills/faq-csv-generator`

Use this skill to generate a FAQ CSV from markdown files with at least 500 rows and source traceability.
It supports two modes: `faq` (default) and `classification` (for category-supervision style answers).

### Generate FAQ CSV
```bash
bash myRAG_app/skills/faq-csv-generator/scripts/generate_faq_csv.sh \
  --input-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --output-csv /tmp/myrag_faq.csv \
  --report-path /tmp/myrag_faq_report.json \
  --min-rows 500
```

### Strict FAQ CSV generation
```bash
bash myRAG_app/skills/faq-csv-generator/scripts/generate_faq_csv.sh \
  --input-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --output-csv /tmp/myrag_faq.csv \
  --report-path /tmp/myrag_faq_report.json \
  --min-rows 500 \
  --strict
```

### Classification-focused CSV generation
```bash
bash myRAG_app/skills/faq-csv-generator/scripts/generate_faq_csv.sh \
  --input-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --output-csv /tmp/myrag_faq_classification.csv \
  --report-path /tmp/myrag_faq_classification_report.json \
  --min-rows 500 \
  --generation-mode classification
```

## Output Files
1. Parse audit report:
`/tmp/myrag_parse_report.json`
2. Chunk export for ingestion:
`/tmp/myrag_chunks.jsonl`
3. Local Chroma persist directory:
`/home/gabri/udemy/llm_engineering/myRAG_app/vector_db`
4. FAQ CSV output:
`/tmp/myrag_faq.csv`
5. FAQ generation report:
`/tmp/myrag_faq_report.json`

## TypeScript UI + API (Multi-Thread Chat)
This app now includes:
1. A FastAPI backend for RAG queries:
`myRAG_app/api`
2. A React + Vite + TypeScript frontend:
`myRAG_app/ui`
3. Local pseudo-auth + per-user local thread persistence.
4. UI chat-model selector with options:
- `gpt-4.1-nano` (default)
- `qwen3.5:9b` (Ollama)
- `llama3.2:latest` (Ollama)

### API Endpoints
1. `GET /api/health`
Returns:
- `status`
- `collection`
- `db_path`
2. `POST /api/rag/query`
Body:
- `question`
- `history` (optional)
- `retrieval` (optional: `k`, `search_type`, `fetch_k`, `lambda_mult`, `doc_type`, `source_contains`)
- `chat_model` (optional: `gpt-4.1-nano`, `qwen3.5:9b`, `llama3.2:latest`)
Returns:
- `answer` (legacy plain text compatibility)
- `structured`:
  - `prompt`
  - `bullets` (few concise points)
  - `answer_text`
- `sources`
- `meta`

### Install Dependencies
From repo root:
```bash
uv pip install --python .venv/bin/python fastapi uvicorn
```

Frontend install:
```bash
cd /home/gabri/udemy/llm_engineering/myRAG_app/ui
npm install
```

Install Ollama bridge package for Python backend model selection:
```bash
uv pip install --python .venv/bin/python langchain-ollama
```

Install and run Ollama (if not already running):
```bash
ollama serve
```

Pull local models:
```bash
ollama pull qwen3.5:9b
ollama pull llama3.2:latest
```

Optional `.env` override for Ollama URL:
```bash
echo "OLLAMA_URL=http://127.0.0.1:11434" >> /home/gabri/udemy/llm_engineering/.env
```

### Run Backend API
Recommended (loads `.env` explicitly):
```bash
cd /home/gabri/udemy/llm_engineering
.venv/bin/uvicorn myRAG_app.api.server:app --host 0.0.0.0 --port 8000 --env-file .env
```

Set active vectorstore in `.env`:
```bash
MYRAG_DB_PATH=/home/gabri/udemy/llm_engineering/myRAG_app/vector_db
MYRAG_COLLECTION=myrag_docs
```

Example for markdown-based vectorstore:
```bash
MYRAG_DB_PATH=/home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown
MYRAG_COLLECTION=myrag_docs_markdown
```

Verify active store used by API:
```bash
curl -s http://localhost:8000/api/health
```

Alternative (if env already exported in current shell):
```bash
.venv/bin/python -m myRAG_app.api.server --host 0.0.0.0 --port 8000
```

### Run Frontend UI
From `myRAG_app/ui`:
```bash
echo "VITE_API_BASE_URL=http://localhost:8000" > .env.local
npm run dev
```

### Use Model Selector in UI
1. Login to the UI.
2. In the query composer, choose a model from the `Model` dropdown.
3. Send the query.
4. The selected model is sent per request to the backend:
- `gpt-4.1-nano` uses OpenAI chat.
- `qwen3.5:9b` and `llama3.2:latest` use Ollama chat at `OLLAMA_URL`.

Notes:
1. Retrieval embeddings still use OpenAI (`text-embedding-3-large`) for this vector DB.
2. If Ollama model calls fail, verify:
```bash
curl http://127.0.0.1:11434/api/tags
```

### Run Tests
Backend tests:
```bash
cd /home/gabri/udemy/llm_engineering
.venv/bin/python -m unittest discover -s myRAG_app/tests -p 'test_*.py' -v
```

Frontend tests:
```bash
cd /home/gabri/udemy/llm_engineering/myRAG_app/ui
npm run test:run
```

### UI Behavior Summary
1. Register/login with local pseudo-auth (`localStorage` only).
2. Left sidebar lists previous threads for current user.
3. Main pane shows full multi-turn conversation for selected thread.
4. Sending a query calls backend and appends assistant reply in this order:
- `Prompt`
- `Answer` with bullet points and short paragraph
- `Sources` list
5. Refreshing the browser preserves user threads by username.
6. Use the header toggle `Structured | Raw` to switch between formatted output and raw answer text for debugging/training review.

## Deployment
Use the dedicated deployment runbook:
`myRAG_app/README_deployment.md`

Markdown-first vectorstore workflow:
`myRAG_app/README_markdown_vectorstore.md`

PPTX skill architecture and export/import runbook:
`myRAG_app/README_pptx_skill_development.md`

Straight ingest CLI guide (all modes/options):
`myRAG_app/README_Ingest.md`

New-files workflow guide (source -> vectorstore with alternatives, incl. PPTX):
`myRAG_app/README_Source_to_VectorStore.md`
