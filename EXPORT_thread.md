# myRAG_app Development Dialog Log

Generated on: 2026-03-07  
Project root: `/home/gabri/udemy/llm_engineering`

## Notes
1. This file captures the full working dialog timeline of the current myRAG_app build session as a project reference.
2. It is organized chronologically as request + delivered direction/outcome.

## Chronological Thread
1. Requested LangChain MVP RAG app aligned with `week5/day1.ipynb`, `day2.ipynb`, `day3.ipynb`, with knowledge source switched to `myRAG_knowledge`.
2. Requested first step plan for robust parsing module and testing.
3. Approved plan and requested implementation of parser/audit framework.
4. Asked to plan optional parser libs install (`pypdf`, `docx2txt`, `openpyxl`) and handling of scanned/image-only PDF issue.
5. Asked meaning of CLI contract:
   `python -m myRAG_app.parser.audit --knowledge-root ... --report-path ... [--strict]`.
6. Requested execution of parser plan including additional scan-related remediations.
7. Asked how to view parsed output in structured form suitable for vector DB storage.
8. Requested separate script module for structured parsed/chunk output export and run instructions.
9. Requested a parsing skill module to secure parsing output, with full app README/runbook updates.
10. Requested integration of Chroma Vectorstore (LangChain, same models), and planning for Ubuntu local run in same venv.
11. Requested inclusion of optional `inspect_cli.py`.
12. Reported “I do not know” answers despite sources; requested improvement.
13. Requested implementation of retrieval/answer quality improvements.
14. Requested TypeScript UI plan: pseudo-auth, multi-thread chat, previous threads in sidebar.
15. Approved and requested full implementation of UI + API integration plan.
16. Reported login input issue in UI; requested instructions/fix.
17. Confirmed login fix worked.
18. Requested deployment plan for VPS at `154.12.245.254/RAG-mat`, non-disruptive to existing apps, install only missing components.
19. Requested plan revision to build vector DB directly on VPS (preferred over copying local DB).
20. Approved revised deployment plan and requested implementation.
21. Reported UI register stuck on “Please wait”; requested checks/instructions.
22. Confirmed register issue resolved.
23. Requested plan for new skill to convert parsed knowledge into markdown, one markdown per top-level subfolder.
24. Approved and requested implementation of folder-level markdown exporter skill and tests.
25. Requested plan for new skill generating FAQ CSV (>=500 rows) from markdown files.
26. Approved and requested implementation of `faq-csv-generator` skill and tests.
27. Reported poor FAQ quality (useless key/entry references); requested revision for classification usefulness.
28. Requested quality-focused revision execution and then additional enhancements.
29. Requested both classification improvements and broader quality controls.
30. Reported UI backend query 404; requested diagnosis/instructions.
31. Requested model selection in UI with default existing model plus Ollama options (`qwen3`, `llama3.2`), and README local run instructions.
32. Requested deployment update instructions for newest VPS version at same address.
33. Requested exact paths for each deployment command on VPS.
34. Clarified actual VPS path is `/home/ubuntu/myrag-deploy` (not `/opt/myrag`); requested corrected instructions.
35. Requested plan for future hybrid inference routing (OpenAI vs local Ollama) for local and VPS.
36. Deferred hybrid routing; requested output structure improvement: prompt + few bullets + sources.
37. Requested immediate one-pass implementation with backward compatibility.
38. Requested compact UI toggle between Structured and Raw answer view.
39. Reported backend error concern after changes.
40. Reported API 500 request issue (`POST /api/rag/query`); requested diagnosis.
41. Reported verbose “thinking” content returned by local model; requested suppression and concise output.
42. Confirmed concise output fix worked.
43. Requested process to create second vectorstore after knowledge updates while keeping backup of previous store.
44. Requested `rollback_vector_db.sh` automation and README/README_deployment instructions.
45. While running `upgrade_cli`, reported parser warnings and asked whether trouble exists.
46. Requested running same command and explanation for many fallback messages after adding one PDF.
47. Requested `--quiet-parser-warnings` option + `README_parsing_instruction.md` with rollback and recommended command format.
48. Requested replacing `qwen3` with `qwen3.5:9b` in UI model selection and local test.
49. Requested skill plan to rename/copy all files into `myRAG_knowledge_index` using pattern:
   `subfoldername + index + today date`.
50. Requested implementation of that knowledge index renamer skill.
51. Requested dedicated `README_knowledge-index-renamer.md` with commands and explanations.
52. Asked how to commit while excluding backup vectorstores and `/samples-6-mar`.
53. Requested updated vectorstore based on markdown files and execution logic/commands.
54. Requested confirmation/action (“yes”) to proceed on markdown vectorstore CLI flow.
55. Asked how to verify which vectorstore is active and where to set it.
56. Asked if for local runs it is better to set the two variables in `.env`.
57. Confirmed `uvicorn --env-file` works; requested README + README_deployment updates and new `README_markdown_vectorstore.md`.
58. Asked if `folder-markdown-exporter` skill is actually being used.
59. Requested adding “Skill activation checklist” to markdown vectorstore README.
60. Requested `Workflow_explanation.md` with full step-by-step evolution and goals + skills list/descriptions.
61. Asked how to save full project thread conversation for later reference.
62. Requested creating this file at repo root.

## Main Artifacts Added Over Session
1. Parser/audit modules and reports.
2. OCR fallback integration for scan-like PDFs.
3. Chunk export + validation tooling.
4. Chroma ingestion/query/inspect/upgrade/rollback workflow.
5. FastAPI backend + React TypeScript multi-thread UI.
6. Structured answer format and raw/structured toggle.
7. Model selector with OpenAI + Ollama options.
8. Deployment scripts/runbooks for VPS path `/RAG-mat`.
9. Skills:
   - `parsing-output-guardian`
   - `folder-markdown-exporter`
   - `faq-csv-generator`
   - `knowledge-index-renamer`
10. Markdown-vectorstore dedicated workflow documentation.

