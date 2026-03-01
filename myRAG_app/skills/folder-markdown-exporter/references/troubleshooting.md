# Troubleshooting

## No Markdown Files Created
1. Verify `--knowledge-root` exists and is a directory.
2. Confirm top-level folders exist under `myRAG_knowledge`.
3. Check CLI output for `Validation error` (exit code `2`).

## Folder Markdown Exists But Is Mostly Empty
1. Inspect parse statuses in `/tmp/myrag_markdown_export_report.json`.
2. Look for `failed_files` records and issue codes.
3. Re-run parser audit:
```bash
.venv/bin/python -m myRAG_app.parser.audit \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --report-path /tmp/myrag_parse_report.json
```

## Parser Dependencies Missing
Install primary dependencies:
```bash
uv pip install --python .venv/bin/python pypdf docx2txt openpyxl
```

## Scan/Image PDF Quality Problems
Install OCR dependencies:
```bash
uv pip install --python .venv/bin/python pymupdf rapidocr-onnxruntime pillow
```

Then rerun export and verify the source appears in markdown with `parser_used` metadata.

## Strict Mode Fails Build
Strict mode returns exit code `1` if any file parse failed.
1. Fix failed file causes using report issue codes.
2. Re-run in strict mode until `total_failures=0`.
