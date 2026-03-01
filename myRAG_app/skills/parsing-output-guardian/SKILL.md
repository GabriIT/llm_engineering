---
name: parsing-output-guardian
description: Run and safeguard the myRAG parsing and vector-ingestion pipeline for mixed knowledge files (.pdf, .docx, .xlsx) with fallback-aware auditing, OCR recovery checks, JSONL chunk export, chunk validation, Chroma build, collection inspection, and query smoke tests. Use when creating, verifying, or troubleshooting local RAG data readiness in myRAG_app.
---

# Parsing Output Guardian

## Overview
Use this skill to keep parsing outputs reliable and vector-ready.

## Core Workflow
1. Run parser audit:
Use `scripts/run_parser_audit.sh` to generate a structured report and confirm parse status by file.

2. Export vector-ingestion chunks:
Use `scripts/export_parser_chunks.sh` to produce JSONL records with `id`, `text`, and rich `metadata`.

3. Validate chunk output:
Use `scripts/validate_chunks_jsonl.py` to detect malformed lines, missing required fields, duplicate IDs, empty text, and large chunks.

4. Build/update Chroma vectorstore:
Use `scripts/build_vectorstore.sh` to parse, chunk, and index into local Chroma with OpenAI embeddings.

5. Inspect collection:
Use `scripts/inspect_vectorstore.sh` to view counts, metadata keys, and sample records.

6. Run query smoke test:
Use `scripts/query_vectorstore.sh` for a local end-to-end retrieval and answer check.

7. Decide strictness:
Use strict mode for CI or release gates.
Use non-strict mode for exploratory runs where warnings/failures should still produce reports.

## Commands
Run from repository root (`/home/gabri/udemy/llm_engineering`).

```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/run_parser_audit.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --report-path /tmp/myrag_parse_report.json
```

```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/export_parser_chunks.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-path /tmp/myrag_chunks.jsonl
```

```bash
.venv/bin/python myRAG_app/skills/parsing-output-guardian/scripts/validate_chunks_jsonl.py \
  --input /tmp/myrag_chunks.jsonl
```

```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/build_vectorstore.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --reset
```

```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/inspect_vectorstore.sh \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --sample 3
```

```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/query_vectorstore.sh \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --question "Summarize the ACS Grilamid LBV-50H certification." \
  --k 12 \
  --search-type mmr \
  --fetch-k 60 \
  --lambda-mult 0.25 \
  --doc-type Certifications \
  --source-contains "LBV-50H"
```

## Failure Handling Rules
1. If any file reports `failed`, inspect issue codes in the report first.
2. If a PDF is scan-like, verify OCR fallback usage (`parser_used=rapidocr_onnxruntime` and `pdf_ocr_applied`).
3. If chunk validation fails, regenerate chunks and fix parser metadata or splitter settings before loading into vector DB.
4. If vector build fails, verify `.env` has `OPENAI_API_KEY` and embedding model access.
5. If running in CI, enable strict mode and fail pipeline on parser failures or chunk validation errors.

## References
1. Use `references/workflow.md` for full runbook and recommended thresholds.
2. Use `references/troubleshooting.md` for dependency and parser-backend troubleshooting.
