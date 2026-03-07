# PPTX RAG Troubleshooting

## Symptom: `pptx_primary_parser_unavailable`
Cause:
`python-pptx` is missing.

Fix:
```bash
uv pip install --python .venv/bin/python python-pptx
```

## Symptom: `pptx_xml_fallback_failed`
Cause:
Corrupt/partial PPTX or malformed internal XML.

Fix:
1. Open in PowerPoint/LibreOffice and re-export to a fresh `.pptx`.
2. Retry `pptx_probe`.

## Symptom: `pptx_low_text`
Cause:
Many slides have little extractable text.

Fix:
1. Use `--enable-vision` in `pptx_probe` for selective visual enrichment.
2. If needed, add speaker notes or export to PDF and OCR separately.

## Symptom: `pptx_vision_failed`
Cause:
Vision path prerequisites missing or model endpoint unavailable.

Fix:
1. Install binaries:
```bash
sudo apt update
sudo apt install -y libreoffice poppler-utils
```
2. Ensure Ollama is running and model exists:
```bash
ollama serve
ollama pull qwen3.5:9b
curl -s http://127.0.0.1:11434/api/tags
```
3. Optionally set endpoint:
```bash
export OLLAMA_URL=http://127.0.0.1:11434
```

## Symptom: strict ingestion fails after adding PPTX
Cause:
`--strict-parse` blocks promotion when parser status is failed.

Fix:
1. Run `pptx_probe` on failing file.
2. Resolve parser issue or remove broken file.
3. Re-run strict ingest/upgrade.

## Symptom: incremental pipeline says "No new files detected"
Cause:
Files were already tracked in state manifest.

Fix:
1. Confirm manifest:
`/home/gabri/udemy/llm_engineering/myRAG_app/.state/incremental_source_manifest.json`
2. If you need full rebuild, remove state file and rerun incremental pipeline.
3. If file was modified (not newly added), rerun with `--include-modified`.

## Symptom: new `.ppt` file is not ingested
Cause:
Core parser supports `.pptx`, not `.ppt`.

Fix:
1. Convert source `.ppt` to `.pptx` and store it in knowledge root.
2. Re-run incremental pipeline.
