# Knowledge Index Renamer Troubleshooting

## Output root already contains files
Symptom:
`Output root already contains files ... Use --clean-output or --overwrite.`

Fix:
1. Use `--clean-output` to regenerate from scratch.
2. Or use a different `--output-root`.
3. Or use `--overwrite` if replacing same targets intentionally.

## Date format validation error
Symptom:
`--date must be in YYYYMMDD format.`

Fix:
Pass date as 8 digits:
`--date 20260307`

## No files found
Symptom:
`No files found inside sub-folders of input root.`

Fix:
1. Confirm input root path is correct.
2. Ensure files are inside subfolders, not only at root level.

## Permission denied
Symptom:
Cannot create output files or report.

Fix:
1. Verify write permissions for output/report parent.
2. Choose writable paths under your user home.

## Skill import issues in another app
Fix:
1. Validate folder:
```bash
python3 /home/gabri/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /path/to/new_app/skills/knowledge-index-renamer
```
2. Ensure `scripts/run_indexing.sh` has execute permission:
```bash
chmod +x /path/to/new_app/skills/knowledge-index-renamer/scripts/run_indexing.sh
```
