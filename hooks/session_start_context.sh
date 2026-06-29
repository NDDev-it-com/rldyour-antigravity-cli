#!/usr/bin/env bash
set -euo pipefail

input="$(cat || true)"
export RLDYOUR_GEMINI_HOOK_INPUT="$input"
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$script_dir/../VERSION" ]]; then
  export RLDYOUR_ANTIGRAVITY_ADAPTER_VERSION="$(<"$script_dir/../VERSION")"
elif [[ -f "$script_dir/../../VERSION" ]]; then
  export RLDYOUR_ANTIGRAVITY_ADAPTER_VERSION="$(<"$script_dir/../../VERSION")"
else
  export RLDYOUR_ANTIGRAVITY_ADAPTER_VERSION="1.7.9"
fi
printf '%s\n' "rldyour-antigravity-cli SessionStart hook received input" >&2

python3 - <<'PY'
import json
import os

_ = os.environ.get("RLDYOUR_GEMINI_HOOK_INPUT", "")
version = os.environ.get("RLDYOUR_ANTIGRAVITY_ADAPTER_VERSION", "1.7.9")
message = (
    f"rldyour-antigravity-cli adapter={version} runtime=antigravity-cli@1.0.13; "
    "standard mode is owner-led; cmux orchestration is visible-terminal-only; "
    "browser routing is Webwright, Playwright CLI, and Chrome DevTools MCP; "
    "only approved inventory providers are active; supported auth is enterprise, "
    "API-key, Vertex, Google Cloud, or owner-approved."
)
print(json.dumps({"systemMessage": message, "suppressOutput": True}, separators=(",", ":")))
PY
