# PPTX Skill Development Runbook

## Purpose
This document explains the logic used to add PPTX parsing for RAG in `myRAG_app`, why the architecture was changed from the demo pipeline, and how to run/export/import the new skill.

## Inputs used for design
1. Reference deck:
`/home/gabri/udemy/llm_engineering/myRAG_knowledge/Metal_Replacement/202401 - Metal Replacement.pptx`
2. Reference demo pipeline:
`/home/gabri/udemy/llm_engineering/PPT_RAG_pipeline_test/pptx_hybrid_rag_demo.py`

## Why the architecture was modified
The demo pipeline is useful for experimentation, but production ingestion in `myRAG_app` needs parser-grade reliability, standardized metadata, and integration with existing audit/chunk/vector commands.

Main changes:
1. Moved PPTX parsing into core parser (`myRAG_app/parser/parsers.py`) so `.pptx` is treated like `.pdf/.docx/.xlsx`.
2. Switched to text-first extraction by default.
3. Kept vision enrichment optional/selective to avoid expensive all-slide multimodal calls.
4. Added issue taxonomy and strict-mode compatibility for CI/deployment gating.
5. Kept all output as LangChain `Document` objects with shared metadata contract.

## Parsing logic implemented
1. Primary parser path: `python-pptx`
- extracts slide text, table cells, and speaker notes
- emits one `Document` per slide with metadata:
`slide_number`, `slide_title`, `slide_has_notes`, `visual_enriched`, plus common source metadata
2. Fallback parser path: PPTX XML extraction from ZIP internals
- parses `a:t` text from slide XML and notes XML
3. Quality checks:
- per-slide low-text classification (`min_chars_pptx_slide`)
- deck-level minimum chars (`min_chars_pptx`)
4. Optional vision enrichment:
- triggers only when enabled or when low-text ratio crosses threshold
- uses Ollama vision model to add `Visual summary` + `Visual key facts` to selected slides

## Files added/updated
1. Updated:
- `myRAG_app/parser/parser_config.py`
- `myRAG_app/parser/parsers.py`
- `myRAG_app/parser/export_chunks.py`
- `myRAG_app/tests/test_parser_unit.py`
2. Added:
- `myRAG_app/parser/pptx_probe.py`
- `myRAG_app/tests/test_pptx_parser_unit.py`
- `myRAG_app/tests/test_pptx_parser_integration.py`
- `myRAG_app/skills/pptx-rag-parser/...`

## Local setup
Run from repo root:
`/home/gabri/udemy/llm_engineering`

Python dependencies:
```bash
uv pip install --python .venv/bin/python python-pptx requests
```

Optional vision prerequisites:
```bash
sudo apt update
sudo apt install -y libreoffice poppler-utils
ollama serve
ollama pull qwen3.5:9b
```

## Command workflow in this app
1. Incremental source -> markdown -> chunks (new files only):
```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/run_incremental_source_markdown_chunks.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --markdown-output-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge_incremental \
  --chunks-output-path /tmp/myrag_chunks_incremental.jsonl \
  --state-path /home/gabri/udemy/llm_engineering/myRAG_app/.state/incremental_source_manifest.json \
  --report-path /tmp/myrag_incremental_pipeline_report.json \
  --strict
```

Behavior:
1. Processes only newly added files by default.
2. Runs `run_pptx_probe.sh` automatically for newly added `.pptx`.
3. If newly added `.ppt` exists, pipeline attempts temporary conversion and runs probe for diagnostics; `.ppt` still requires conversion to `.pptx` for ingestion.
4. Add `--include-modified` when you also want changed files processed.

2. Probe single PPTX manually:
```bash
.venv/bin/python -m myRAG_app.parser.pptx_probe \
  --pptx-path "/home/gabri/udemy/llm_engineering/myRAG_knowledge/Metal_Replacement/202401 - Metal Replacement.pptx" \
  --report-path /tmp/myrag_pptx_probe.json
```

3. Probe with selective vision:
```bash
.venv/bin/python -m myRAG_app.parser.pptx_probe \
  --pptx-path "/home/gabri/udemy/llm_engineering/myRAG_knowledge/Metal_Replacement/202401 - Metal Replacement.pptx" \
  --report-path /tmp/myrag_pptx_probe_vision.json \
  --enable-vision \
  --max-vision-slides 6 \
  --vision-model qwen3.5:9b
```

4. Full parser audit:
```bash
.venv/bin/python -m myRAG_app.parser.audit \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --report-path /tmp/myrag_parse_report.json \
  --strict
```

5. Build vectorstore:
```bash
.venv/bin/python -m myRAG_app.vector.ingest_cli \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --reset \
  --strict-parse
```

6. Inspect:
```bash
.venv/bin/python -m myRAG_app.vector.inspect_cli \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --sample 5
```

## Important: markdown candidate build and PPTX processing
Your command:
```bash
CANDIDATE_DB="/home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown_candidate_$(date -u +%Y%m%d_%H%M%S)"
.venv/bin/python -m myRAG_app.vector.markdown_upgrade_cli \
  --markdown-root /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown \
  --candidate-db-path "$CANDIDATE_DB" \
  --collection myrag_docs_markdown \
  --build-only ; echo "exit=$?"
```
does **not** parse PPTX directly. It only reads existing markdown files.

To ensure the PPTX is processed through the new `pptx-rag-parser` logic, run this sequence.

### Path A: full rebuild candidate vectorstore
Use this when you want a brand-new markdown vectorstore with all knowledge files.

1. Confirm PPTX parser path with probe:
```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/run_pptx_probe.sh \
  --pptx-path "/home/gabri/udemy/llm_engineering/myRAG_knowledge/Metal_Replacement/202401 - Metal Replacement.pptx" \
  --report-path /tmp/myrag_pptx_probe.json
```

2. Rebuild markdown snapshots from `myRAG_knowledge` (this step invokes core parser, including `.pptx`):
```bash
.venv/bin/python -m myRAG_app.parser.export_markdown \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --report-path /tmp/myrag_markdown_export_report.json \
  --strict
```

3. Build markdown candidate vectorstore:
```bash
CANDIDATE_DB="/home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown_candidate_$(date -u +%Y%m%d_%H%M%S)"
.venv/bin/python -m myRAG_app.vector.markdown_upgrade_cli \
  --markdown-root /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown \
  --candidate-db-path "$CANDIDATE_DB" \
  --collection myrag_docs_markdown \
  --build-only ; echo "exit=$?"
```

4. Validate candidate:
```bash
.venv/bin/python -m myRAG_app.vector.inspect_cli \
  --db-path "$CANDIDATE_DB" \
  --collection myrag_docs_markdown \
  --sample 5
```

5. Promote candidate to active markdown vectorstore:
```bash
.venv/bin/python -m myRAG_app.vector.markdown_upgrade_cli \
  --markdown-root /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db_markdown \
  --collection myrag_docs_markdown ; echo "exit=$?"
```

### Path B: incremental parsing (new files only)
Use this when you added a few files and want efficient delta processing before ingestion.

```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/run_incremental_source_markdown_chunks.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --markdown-output-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge_incremental \
  --chunks-output-path /tmp/myrag_chunks_incremental.jsonl \
  --state-path /home/gabri/udemy/llm_engineering/myRAG_app/.state/incremental_source_manifest.json \
  --report-path /tmp/myrag_incremental_pipeline_report.json \
  --strict
```

Notes:
1. Only newly added files are parsed by default.
2. `run_pptx_probe.sh` is auto-triggered when new `.pptx` exists.
3. New `.ppt` files are probed through temporary conversion and reported, but should be converted to `.pptx` for ingestion.

If you want a new vectorstore directly from source files (without markdown intermediary), use:
```bash
.venv/bin/python -m myRAG_app.vector.upgrade_cli \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --active-db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --strict-parse \
  --build-only ; echo "exit=$?"
```

## Skill usage
Skill path:
`/home/gabri/udemy/llm_engineering/myRAG_app/skills/pptx-rag-parser`

Wrapper commands:
```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/run_incremental_source_markdown_chunks.sh ...
bash myRAG_app/skills/pptx-rag-parser/scripts/run_pptx_probe.sh ...
bash myRAG_app/skills/pptx-rag-parser/scripts/run_pptx_audit.sh ...
bash myRAG_app/skills/pptx-rag-parser/scripts/build_vectorstore_with_pptx.sh ...
```

## Export skill to other apps
From repo root:
```bash
cd /home/gabri/udemy/llm_engineering
tar -czf /tmp/pptx-rag-parser-skill.tgz myRAG_app/skills/pptx-rag-parser
```

## Import skill into another app
```bash
mkdir -p /path/to/other_app/skills
tar -xzf /tmp/pptx-rag-parser-skill.tgz -C /path/to/other_app
```

Validate in target:
```bash
python3 /home/gabri/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /path/to/other_app/skills/pptx-rag-parser
```

## Notes about `PPT_RAG_pipeline_test`
`PPT_RAG_pipeline_test` remains useful as an exploratory benchmark. Production ingestion should use `myRAG_app` parser/audit/vector CLIs so all file formats share one consistent data contract and strictness behavior.
