# PPTX RAG Workflow

## Purpose
Parse `.pptx` files with text-first extraction, optionally enrich low-text slides with vision, and ingest into Chroma using the existing myRAG flow.

## 1) Incremental source -> markdown -> chunks (new files only)
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
1. Only newly added files are processed by default.
2. Add `--include-modified` to process changed files too.
3. If a new `.pptx` is detected, the pipeline runs `run_pptx_probe.sh` automatically.
4. If a new `.ppt` is detected, pipeline attempts temporary conversion for probing and reports guidance.

## 2) Probe one PPTX manually
```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/run_pptx_probe.sh \
  --pptx-path "/home/gabri/udemy/llm_engineering/myRAG_knowledge/Metal_Replacement/202401 - Metal Replacement.pptx" \
  --report-path /tmp/myrag_pptx_probe.json
```

Optional selective vision on probe:
```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/run_pptx_probe.sh \
  --pptx-path "/home/gabri/udemy/llm_engineering/myRAG_knowledge/Metal_Replacement/202401 - Metal Replacement.pptx" \
  --report-path /tmp/myrag_pptx_probe_vision.json \
  --enable-vision \
  --max-vision-slides 6 \
  --vision-model qwen3.5:9b
```

## 3) Full parser audit
```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/run_pptx_audit.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --report-path /tmp/myrag_parse_report.json \
  --strict
```

## 4) Export chunks
```bash
.venv/bin/python -m myRAG_app.parser.export_chunks \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-path /tmp/myrag_chunks.jsonl \
  --strict
```

## 5) Build vectorstore
```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/build_vectorstore_with_pptx.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --reset \
  --strict-parse
```

## 6) Inspect and smoke query
```bash
.venv/bin/python -m myRAG_app.vector.inspect_cli \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --sample 5
```

```bash
.venv/bin/python -m myRAG_app.vector.query_cli \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --question "Summarize key messages from Metal Replacement presentation."
```
