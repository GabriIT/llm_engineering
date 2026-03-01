#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEPLOY_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
COMPOSE_FILE="$DEPLOY_DIR/docker-compose.yml"
ENV_FILE="$DEPLOY_DIR/.env.vps"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "Missing env file: $ENV_FILE" >&2
  echo "Copy .env.example to .env.vps and fill values first." >&2
  exit 2
fi

cd "$DEPLOY_DIR"

docker compose --env-file "$ENV_FILE" -f "$COMPOSE_FILE" up -d --build

echo "--- compose status ---"
docker compose --env-file "$ENV_FILE" -f "$COMPOSE_FILE" ps

echo "--- smoke checks ---"
curl -fsS http://127.0.0.1:18000/api/health
curl -fsSI http://127.0.0.1:18001/

echo "Deployment stack is up. Configure reverse-proxy route /RAG-mat next."
