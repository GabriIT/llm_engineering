#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-$ROOT_DIR/.venv/bin/python}"

if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "Python interpreter not found at: $PYTHON_BIN" >&2
  exit 2
fi

if [[ -f "$ROOT_DIR/.env" ]]; then
  set -a
  # shellcheck source=/dev/null
  source "$ROOT_DIR/.env"
  set +a
fi

# shellcheck source=/dev/null
source "$ROOT_DIR/myRAG_app/scripts/knowledge_root_bootstrap.sh"
myrag_set_knowledge_roots "$ROOT_DIR"

MARKDOWN_OUTPUT_DIR="$ROOT_DIR/myRAG_app/markdown_knowledge"
EXPORT_REPORT_PATH="/tmp/myrag_markdown_export_report.json"
INDEX_REPORT_PATH="${MYRAG_KNOWLEDGE_INDEX_REPORT:-/tmp/myrag_knowledge_index_report.json}"
INDEX_STATE_PATH="${MYRAG_KNOWLEDGE_INDEX_STATE_PATH:-$ROOT_DIR/myRAG_app/.state/knowledge_index_state.json}"
TRACKING_CSV_PATH="${MYRAG_KNOWLEDGE_INDEX_TRACKING_CSV:-/tmp/myrag_knowledge_index_tracking.csv}"
INDEX_MODE="full"
STRICT_EXPORT=0
USER_KNOWLEDGE_ROOT=""

UPGRADE_ARGS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help)
      cat <<USAGE
Usage: build_vectorstore_markdown_first.sh [options] [markdown_upgrade_cli options]

Pipeline:
  1) Rebuild myRAG_knowledge_index from myRAG_knowledge
  2) Export markdown from indexed knowledge
  3) Build/promote markdown vectorstore

Options:
  --knowledge-root PATH       Must be myRAG_knowledge_index (optional; defaults to indexed root)
  --index-mode MODE           full|incremental (default: full)
  --index-report-path PATH    Indexing report JSON (default: /tmp/myrag_knowledge_index_report.json)
  --index-state-path PATH     Incremental index state (default: $ROOT_DIR/myRAG_app/.state/knowledge_index_state.json)
  --tracking-path PATH        CSV tracking list source->indexed (default: /tmp/myrag_knowledge_index_tracking.csv)
  --output-dir PATH           Markdown output dir (default: $ROOT_DIR/myRAG_app/markdown_knowledge)
  --export-report-path PATH   Markdown export report (default: /tmp/myrag_markdown_export_report.json)
  --strict-export             Run markdown export in strict mode
  -h, --help                  Show this help

Any other arguments are forwarded to:
  python -m myRAG_app.vector.markdown_upgrade_cli

Defaults for markdown_upgrade_cli:
  --active-db-path from MYRAG_DB_PATH (or $ROOT_DIR/myRAG_app/vector_db_markdown)
  --collection from MYRAG_COLLECTION (or myrag_docs_markdown)
USAGE
      exit 0
      ;;
    --knowledge-root)
      USER_KNOWLEDGE_ROOT="$2"
      shift 2
      ;;
    --knowledge-root=*)
      USER_KNOWLEDGE_ROOT="${1#--knowledge-root=}"
      shift
      ;;
    --output-dir)
      MARKDOWN_OUTPUT_DIR="$2"
      shift 2
      ;;
    --output-dir=*)
      MARKDOWN_OUTPUT_DIR="${1#--output-dir=}"
      shift
      ;;
    --index-mode)
      INDEX_MODE="$2"
      shift 2
      ;;
    --index-mode=*)
      INDEX_MODE="${1#--index-mode=}"
      shift
      ;;
    --index-report-path)
      INDEX_REPORT_PATH="$2"
      shift 2
      ;;
    --index-report-path=*)
      INDEX_REPORT_PATH="${1#--index-report-path=}"
      shift
      ;;
    --index-state-path)
      INDEX_STATE_PATH="$2"
      shift 2
      ;;
    --index-state-path=*)
      INDEX_STATE_PATH="${1#--index-state-path=}"
      shift
      ;;
    --tracking-path)
      TRACKING_CSV_PATH="$2"
      shift 2
      ;;
    --tracking-path=*)
      TRACKING_CSV_PATH="${1#--tracking-path=}"
      shift
      ;;
    --export-report-path)
      EXPORT_REPORT_PATH="$2"
      shift 2
      ;;
    --export-report-path=*)
      EXPORT_REPORT_PATH="${1#--export-report-path=}"
      shift
      ;;
    --strict-export)
      STRICT_EXPORT=1
      shift
      ;;
    *)
      UPGRADE_ARGS+=("$1")
      shift
      ;;
  esac
done

KR_ARGS=()
if [[ -n "$USER_KNOWLEDGE_ROOT" ]]; then
  KR_ARGS=(--knowledge-root "$USER_KNOWLEDGE_ROOT")
fi
myrag_enforce_or_inject_knowledge_root "$PYTHON_BIN" "${KR_ARGS[@]}"

if [[ "$INDEX_MODE" != "full" && "$INDEX_MODE" != "incremental" ]]; then
  echo "Invalid --index-mode: $INDEX_MODE (use full|incremental)" >&2
  exit 2
fi

INDEX_ARGS=(
  --input-root "$MYRAG_RAW_KNOWLEDGE_ROOT"
  --output-root "$MYRAG_KNOWLEDGE_ROOT"
  --report-path "$INDEX_REPORT_PATH"
  --mode "$INDEX_MODE"
  --state-path "$INDEX_STATE_PATH"
  --tracking-csv-path "$TRACKING_CSV_PATH"
)
if [[ "$INDEX_MODE" == "full" ]]; then
  INDEX_ARGS+=(--clean-output)
fi

echo "Building indexed knowledge root (mode=$INDEX_MODE)..."
bash "$ROOT_DIR/myRAG_app/skills/knowledge-index-renamer/scripts/run_indexing.sh" "${INDEX_ARGS[@]}"
echo "Tracking CSV ready: $TRACKING_CSV_PATH"

EXPORT_ARGS=(
  --knowledge-root "$MYRAG_KNOWLEDGE_ROOT"
  --output-dir "$MARKDOWN_OUTPUT_DIR"
  --report-path "$EXPORT_REPORT_PATH"
)
if [[ "$STRICT_EXPORT" -eq 1 ]]; then
  EXPORT_ARGS+=(--strict)
fi

echo "Exporting markdown from indexed knowledge root..."
"$PYTHON_BIN" -m myRAG_app.parser.export_markdown "${EXPORT_ARGS[@]}"

has_active_db=0
has_collection=0
for arg in "${UPGRADE_ARGS[@]}"; do
  [[ "$arg" == "--active-db-path" || "$arg" == --active-db-path=* ]] && has_active_db=1
  [[ "$arg" == "--collection" || "$arg" == --collection=* ]] && has_collection=1
done

DEFAULT_ACTIVE_DB_PATH="${MYRAG_DB_PATH:-$ROOT_DIR/myRAG_app/vector_db_markdown}"
DEFAULT_COLLECTION="${MYRAG_COLLECTION:-myrag_docs_markdown}"

CLI_DEFAULT_ARGS=(--markdown-root "$MARKDOWN_OUTPUT_DIR")
if [[ "$has_active_db" -eq 0 ]]; then
  CLI_DEFAULT_ARGS+=(--active-db-path "$DEFAULT_ACTIVE_DB_PATH")
fi
if [[ "$has_collection" -eq 0 ]]; then
  CLI_DEFAULT_ARGS+=(--collection "$DEFAULT_COLLECTION")
fi

echo "Building markdown vectorstore..."
"$PYTHON_BIN" -m myRAG_app.vector.markdown_upgrade_cli "${CLI_DEFAULT_ARGS[@]}" "${UPGRADE_ARGS[@]}"
