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
  source "$ROOT_DIR/.env"
  set +a
fi

has_db=0
has_collection=0
for arg in "$@"; do
  [[ "$arg" == "--db-path" ]] && has_db=1
  [[ "$arg" == "--collection" ]] && has_collection=1
done

EXTRA_ARGS=()
if [[ $has_db -eq 0 && -n "${MYRAG_DB_PATH:-}" ]]; then
  EXTRA_ARGS+=(--db-path "$MYRAG_DB_PATH")
fi
if [[ $has_collection -eq 0 && -n "${MYRAG_COLLECTION:-}" ]]; then
  EXTRA_ARGS+=(--collection "$MYRAG_COLLECTION")
fi

"$PYTHON_BIN" -m myRAG_app.vector.inspect_cli "${EXTRA_ARGS[@]}" "$@"
