# myRAG App - Parsing Agent Runbook

## Purpose
This app contains a robust parsing pipeline for a mixed-format RAG knowledge base, a reusable parsing skill module, and local Chroma vectorstore integration for retrieval with LangChain.

## Current Parsing Capabilities
1. Parse `.pdf`, `.docx`, and `.xlsx` from:
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
uv pip install --python .venv/bin/python pypdf docx2txt openpyxl
```

### 2. Verify imports
```bash
.venv/bin/python -c "import pypdf, docx2txt, openpyxl; print('imports_ok')"
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
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --reset
```

### Inspect vectorstore
```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/inspect_vectorstore.sh \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --sample 3
```

### Query vectorstore
```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/query_vectorstore.sh \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --question "What does the LBV-50H ACS certificate state?" \
  --k 12 \
  --search-type mmr \
  --fetch-k 60 \
  --lambda-mult 0.25 \
  --doc-type Certifications \
  --source-contains "LBV-50H"
```

## Output Files
1. Parse audit report:
`/tmp/myrag_parse_report.json`
2. Chunk export for ingestion:
`/tmp/myrag_chunks.jsonl`
3. Local Chroma persist directory:
`/home/gabri/udemy/llm_engineering/myRAG_app/vector_db`

## TypeScript UI + API (Multi-Thread Chat)
This app now includes:
1. A FastAPI backend for RAG queries:
`myRAG_app/api`
2. A React + Vite + TypeScript frontend:
`myRAG_app/ui`
3. Local pseudo-auth + per-user local thread persistence.

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
Returns:
- `answer`
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

### Run Backend API
From repo root:
```bash
.venv/bin/python -m myRAG_app.api.server --host 0.0.0.0 --port 8000
```

### Run Frontend UI
From `myRAG_app/ui`:
```bash
echo "VITE_API_BASE_URL=http://localhost:8000" > .env.local
npm run dev
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
4. Sending a query calls backend and appends assistant reply with source list.
5. Refreshing the browser preserves user threads by username.

## Deployment
Use the dedicated deployment runbook:
`myRAG_app/README_deployment.md`
