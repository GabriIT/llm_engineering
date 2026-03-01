# Folder Markdown Export Workflow

## Purpose
Generate one markdown file per top-level folder under `myRAG_knowledge`, using parser output and metadata.

## Standard Run
```bash
bash myRAG_app/skills/folder-markdown-exporter/scripts/export_folder_markdown.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --report-path /tmp/myrag_markdown_export_report.json
```

## Strict Run (CI/Release Gate)
```bash
bash myRAG_app/skills/folder-markdown-exporter/scripts/export_folder_markdown.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --report-path /tmp/myrag_markdown_export_report.json \
  --strict
```

## Expected Output Tree
```text
myRAG_app/markdown_knowledge/
  Certifications.md
  Projects.md
  Success_Cases.md
  Technical_sheets.md
  Visit_reports.md
  competitors.md
  monthly_reports.md
```

## Verification Checklist
1. Markdown count equals the number of top-level knowledge folders.
2. `Certifications.md` contains OCR-derived file `ACS Grilamid LBV-50H FWA black 9225 18-12.pdf`.
3. Each markdown file includes:
- `## Summary`
- one or more `## Source:` sections when data exists
- `## Parse Failures` section
4. JSON report has:
- `summary.total_markdown_files`
- `folders[]`
- `failed_files[]`
