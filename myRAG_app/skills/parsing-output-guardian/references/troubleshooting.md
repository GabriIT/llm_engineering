# Troubleshooting

## Missing Primary Parsers
If report issues include `*_primary_parser_unavailable`, install dependencies:

```bash
uv pip install --python .venv/bin/python pypdf docx2txt openpyxl
```

## Scan-like PDFs
If report issues include `pdf_possible_scan_or_image_only`:
1. Confirm OCR dependencies are installed:
```bash
uv pip install --python .venv/bin/python pymupdf rapidocr-onnxruntime opencv-python
```
2. Re-run audit and verify:
- `parser_used` is `rapidocr_onnxruntime`
- issue code includes `pdf_ocr_applied`

## Chunk Validation Errors
If `validate_chunks_jsonl.py` reports errors:
1. Regenerate chunks from fresh parser output.
2. Check for manual edits in JSONL.
3. Re-run validation before ingestion.

## Vector Build Errors
If vector build fails:
1. Ensure `OPENAI_API_KEY` is present in `.env` or environment.
2. Ensure embedding model access for `text-embedding-3-large`.
3. Re-run build with:
```bash
bash myRAG_app/skills/parsing-output-guardian/scripts/build_vectorstore.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --reset
```

## Inspect/Query Issues
1. If inspect reports empty collection, rebuild vectorstore.
2. If query fails with auth errors, validate `.env` key loading.
3. If answer is `I do not know`, increase retrieval breadth and target metadata:
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
  --source-contains "LBV-50H" \
  --show-context
```

## Recommended Quality Checks Before Ingestion
1. Zero parser failures in strict mode.
2. No JSONL validation errors.
3. Spot-check top and tail chunk records.
4. Confirm metadata fields needed for filtering are present (`source`, `doc_type`, `chunk_index`).
5. Inspect vector collection samples before enabling production queries.
