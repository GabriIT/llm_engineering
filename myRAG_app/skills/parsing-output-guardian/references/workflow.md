# Parsing Workflow

## Standard Run
1. Run parser audit to inspect file-level statuses.
2. Export chunk JSONL after successful audit.
3. Validate JSONL structure before vector ingestion.
4. Build or refresh Chroma vectorstore.
5. Inspect Chroma collection and run query smoke test.

## Commands
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
  --question "What does the certification say about Grilamid LBV-50H?" \
  --k 12 \
  --search-type mmr \
  --fetch-k 60 \
  --lambda-mult 0.25 \
  --doc-type Certifications \
  --source-contains "LBV-50H"
```

## Strict CI Run
```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/run_parser_audit.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --report-path /tmp/myrag_parse_report.json \
  --strict

bash myRAG_app/skills/parsing-output-guardian/scripts/export_parser_chunks.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-path /tmp/myrag_chunks.jsonl \
  --strict

.venv/bin/python myRAG_app/skills/parsing-output-guardian/scripts/validate_chunks_jsonl.py \
  --input /tmp/myrag_chunks.jsonl \
  --strict

bash myRAG_app/skills/parsing-output-guardian/scripts/build_vectorstore.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --reset \
  --strict-parse
```

## Output Contracts
1. Parse report JSON contains `summary` and `files`.
2. Chunk JSONL line format:
- `id` (stable hash)
- `text` (non-empty chunk text)
- `metadata` with parse provenance and chunk fields.
3. Vectorstore contains embeddings in collection `myrag_docs` (or configured value).
