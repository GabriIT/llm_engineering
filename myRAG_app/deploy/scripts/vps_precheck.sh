#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
if [[ -f "$REPO_ROOT/.env" ]]; then
  set -a
  source "$REPO_ROOT/.env"
  set +a
fi
# Prefer deployment env when available (VPS runtime configuration).
if [[ -f "$REPO_ROOT/myRAG_app/deploy/.env.vps" ]]; then
  set -a
  source "$REPO_ROOT/myRAG_app/deploy/.env.vps"
  set +a
fi

KNOWLEDGE_ROOT="/home/$USER/myrag-deploy/myRAG_knowledge"
VECTOR_DB_PATH="${MYRAG_DB_PATH:-/home/$USER/myrag-deploy/vector_db}"
PYTHON_BIN="python3"
OUTPUT="/tmp/myrag_vps_precheck_$(date +%Y%m%d_%H%M%S).log"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --knowledge-root)
      KNOWLEDGE_ROOT="$2"
      shift 2
      ;;
    --vector-db-path)
      VECTOR_DB_PATH="$2"
      shift 2
      ;;
    --python-bin)
      PYTHON_BIN="$2"
      shift 2
      ;;
    --output)
      OUTPUT="$2"
      shift 2
      ;;
    -h|--help)
      cat <<USAGE
Usage: vps_precheck.sh [options]
  --knowledge-root PATH   VPS path where myRAG_knowledge is/will be stored
  --vector-db-path PATH   VPS path for Chroma vector_db (default: MYRAG_DB_PATH or /home/<user>/myrag-deploy/vector_db)
  --python-bin PATH       Python interpreter for dependency checks
  --output PATH           Output log path
USAGE
      exit 0
      ;;
    *)
      echo "Unknown arg: $1" >&2
      exit 2
      ;;
  esac
done

mkdir -p "$(dirname "$OUTPUT")"
: > "$OUTPUT"

FAILURES=0
WARNINGS=0

log() {
  echo "$*" | tee -a "$OUTPUT"
}

ok() {
  log "[OK] $*"
}

warn() {
  WARNINGS=$((WARNINGS + 1))
  log "[WARN] $*"
}

fail() {
  FAILURES=$((FAILURES + 1))
  log "[FAIL] $*"
}

has_cmd() {
  command -v "$1" >/dev/null 2>&1
}

size_bytes() {
  local path="$1"
  if [[ -e "$path" ]]; then
    du -sb "$path" 2>/dev/null | awk '{print $1}'
  else
    echo 0
  fi
}

human_bytes() {
  local bytes="$1"
  numfmt --to=iec --suffix=B "$bytes" 2>/dev/null || echo "${bytes}B"
}

log "=== myRAG VPS Precheck ==="
log "Timestamp: $(date -Iseconds)"
log "Host: $(hostname)"
log "User: $(id -un)"
log "Knowledge root: $KNOWLEDGE_ROOT"
log "Vector DB path: $VECTOR_DB_PATH"
log "Python: $PYTHON_BIN"
log "Output log: $OUTPUT"

if has_cmd lsb_release; then
  log "OS: $(lsb_release -ds)"
else
  log "OS: $(uname -a)"
fi

log "--- apt sources (deb lines) ---"
grep -R "^[[:space:]]*deb " /etc/apt/sources.list /etc/apt/sources.list.d/* 2>/dev/null | tee -a "$OUTPUT" || true

if sudo -n true 2>/dev/null; then
  ok "sudo non-interactive access is available"
else
  warn "sudo may require password prompt"
fi

if has_cmd docker; then
  ok "docker detected: $(docker --version)"
else
  warn "docker not found (systemd fallback deployment required)"
fi

if docker compose version >/dev/null 2>&1; then
  ok "docker compose plugin detected: $(docker compose version --short 2>/dev/null || echo available)"
elif has_cmd docker-compose; then
  ok "docker-compose binary detected: $(docker-compose --version)"
else
  warn "docker compose not found"
fi

for svc in nginx caddy apache2; do
  if systemctl list-unit-files "${svc}.service" >/dev/null 2>&1; then
    status=$(systemctl is-active "${svc}.service" || true)
    if [[ "$status" == "active" ]]; then
      ok "proxy service active: $svc"
    else
      warn "proxy service installed but not active: $svc (status=$status)"
    fi
  fi
done

if has_cmd node; then
  node_ver="$(node -v 2>/dev/null || true)"
  ok "node detected: $node_ver"
else
  warn "node not detected"
fi

if has_cmd npm; then
  ok "npm detected: $(npm -v 2>/dev/null || echo unknown)"
else
  warn "npm not detected"
fi

if has_cmd pm2; then
  log "--- pm2 list ---"
  pm2 list 2>/dev/null | tee -a "$OUTPUT" || true
else
  log "pm2 not detected"
fi

if has_cmd apt-cache; then
  log "--- apt policy nodejs ---"
  apt-cache policy nodejs | tee -a "$OUTPUT" || true
  log "--- apt rdepends --installed nodejs ---"
  apt-cache rdepends --installed nodejs 2>/dev/null | tee -a "$OUTPUT" || true
  log "--- apt policy postgresql/postgresql-15/postgresql-16 ---"
  apt-cache policy postgresql postgresql-15 postgresql-16 | tee -a "$OUTPUT" || true
  log "--- apt policy nginx ---"
  apt-cache policy nginx | tee -a "$OUTPUT" || true
fi

if has_cmd psql; then
  ok "psql detected: $(psql --version)"
  log "--- pg_lsclusters ---"
  pg_lsclusters 2>/dev/null | tee -a "$OUTPUT" || true
else
  warn "psql not detected"
fi

if has_cmd apt; then
  log "--- installed postgresql packages ---"
  apt list --installed 'postgresql*' 2>/dev/null | tee -a "$OUTPUT" || true
fi

if has_cmd nginx; then
  log "nginx version: $(nginx -v 2>&1)"
else
  warn "nginx binary not found"
fi

if has_cmd ss; then
  log "--- listeners (80,443,18000,18001) ---"
  ss -ltnp | awk 'NR==1 || /:80 |:443 |:18000 |:18001 /' | tee -a "$OUTPUT" || true
fi

if has_cmd docker; then
  log "--- running containers ---"
  docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Ports}}' | tee -a "$OUTPUT" || true
fi

if [[ -d "$KNOWLEDGE_ROOT" ]]; then
  file_count=$(find "$KNOWLEDGE_ROOT" -type f | wc -l | awk '{print $1}')
  knowledge_bytes=$(size_bytes "$KNOWLEDGE_ROOT")
  ok "knowledge root exists with ${file_count} files, size=$(human_bytes "$knowledge_bytes")"
else
  fail "knowledge root does not exist: $KNOWLEDGE_ROOT"
  knowledge_bytes=0
fi

if [[ -e "$VECTOR_DB_PATH" ]]; then
  existing_db_bytes=$(size_bytes "$VECTOR_DB_PATH")
  ok "existing vector DB path detected, size=$(human_bytes "$existing_db_bytes")"
else
  warn "vector DB path does not exist yet: $VECTOR_DB_PATH"
  existing_db_bytes=0
fi

check_dir="$VECTOR_DB_PATH"
while [[ ! -d "$check_dir" ]]; do
  check_dir="$(dirname "$check_dir")"
  if [[ "$check_dir" == "/" ]]; then
    break
  fi
done

if [[ -d "$check_dir" ]]; then
  avail_bytes=$(df -PB1 "$check_dir" | awk 'NR==2 {print $4}')
  if [[ "$existing_db_bytes" -gt 0 ]]; then
    expected_bytes="$existing_db_bytes"
  elif [[ "$knowledge_bytes" -gt 0 ]]; then
    expected_bytes=$((knowledge_bytes / 2))
  else
    expected_bytes=$((500 * 1024 * 1024))
  fi
  min_expected=$((500 * 1024 * 1024))
  if [[ "$expected_bytes" -lt "$min_expected" ]]; then
    expected_bytes="$min_expected"
  fi
  required_bytes=$((expected_bytes * 3))

  log "Disk check directory: $check_dir"
  log "Estimated vector DB size: $(human_bytes "$expected_bytes")"
  log "Required free (3x rule): $(human_bytes "$required_bytes")"
  log "Available free: $(human_bytes "$avail_bytes")"

  if [[ "$avail_bytes" -ge "$required_bytes" ]]; then
    ok "disk headroom satisfies 3x vector DB requirement"
  else
    fail "insufficient disk headroom for VPS-side vector build"
  fi
else
  fail "cannot resolve a valid filesystem path for disk check"
fi

if [[ -n "${OPENAI_API_KEY:-}" ]]; then
  ok "OPENAI_API_KEY is set in environment"
else
  fail "OPENAI_API_KEY is not set"
fi

if has_cmd "$PYTHON_BIN"; then
  dep_check=$("$PYTHON_BIN" - <<'PY'
import importlib
mods = [
    "pypdf",
    "docx2txt",
    "openpyxl",
    "fitz",
    "rapidocr_onnxruntime",
    "PIL",
    "langchain",
    "langchain_chroma",
    "langchain_openai",
    "chromadb",
]
missing = []
for m in mods:
    try:
        importlib.import_module(m)
    except Exception:
        missing.append(m)
if missing:
    print("MISSING:" + ",".join(missing))
else:
    print("OK")
PY
)
  if [[ "$dep_check" == OK ]]; then
    ok "python dependencies for parse + ingest appear available"
  else
    fail "python dependencies missing: ${dep_check#MISSING:}"
  fi
else
  fail "python interpreter not found: $PYTHON_BIN"
fi

if has_cmd curl; then
  http_code="$(curl -sS -o /dev/null -w '%{http_code}' -m 6 https://api.openai.com || true)"
  if [[ -n "$http_code" && "$http_code" != "000" ]]; then
    ok "basic outbound HTTPS connectivity to api.openai.com works (http_code=$http_code)"
  else
    warn "outbound HTTPS check to api.openai.com failed"
  fi
else
  warn "curl not installed; skipped outbound connectivity check"
fi

log "=== Precheck Summary ==="
log "Failures: $FAILURES"
log "Warnings: $WARNINGS"
log "Log file: $OUTPUT"

if [[ "$FAILURES" -gt 0 ]]; then
  exit 1
fi
exit 0
