#!/usr/bin/env bash
set -euo pipefail

redact=false
require_runtime=false
while [[ $# -gt 0 ]]; do
  case "$1" in
    --redact)
      redact=true
      shift
      ;;
    --require-runtime)
      require_runtime=true
      shift
      ;;
    --help|-h)
      echo "Usage: scripts/doctor_system_antigravity.sh [--redact] [--require-runtime]"
      exit 0
      ;;
    *)
      echo "ERROR: unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 "$repo_root/scripts/validate_gemini_config.py" --strict >/dev/null
python3 "$repo_root/scripts/validate_gemini_runtime_baseline.py" --strict >/dev/null
python3 "$repo_root/scripts/validate_gemini_mcp_inventory.py" --strict >/dev/null

if ! command -v agy >/dev/null 2>&1; then
  if [[ "$require_runtime" == "true" ]]; then
    echo '{"status":"FAIL","runtime":"antigravity-cli","binary":"agy","reason":"agy binary is required but not installed or not on PATH"}'
    exit 1
  fi
  echo '{"status":"NOT_PROVEN","runtime":"antigravity-cli","binary":"agy","reason":"agy binary is not installed or not on PATH"}'
  exit 0
fi

version="$(agy --version 2>&1 || true)"
if [[ "$redact" == "true" ]]; then
  version="$(printf '%s' "$version" | sed -E 's/(token|key|secret|password)=([^[:space:]]+)/\1=REDACTED/Ig')"
fi
if [[ "$version" == *"1.0.13"* ]]; then
  printf '{"status":"OK","runtime":"antigravity-cli","binary":"agy","version":%s}\n' "$(python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))' <<<"$version")"
else
  printf '{"status":"NOT_PROVEN","runtime":"antigravity-cli","binary":"agy","reason":"version output does not contain 1.0.13","version":%s}\n' "$(python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))' <<<"$version")"
fi
