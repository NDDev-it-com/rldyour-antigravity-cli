#!/usr/bin/env bash
set -euo pipefail

input="$(cat || true)"
export RLDYOUR_GEMINI_HOOK_INPUT="$input"
printf '%s\n' "rldyour-antigravity-cli SessionStart hook received input" >&2

python3 - <<'PY'
import json
import os

_ = os.environ.get("RLDYOUR_GEMINI_HOOK_INPUT", "")
message = (
    "rldyour-antigravity-cli adapter=1.5.1 runtime=antigravity-cli@1.0.8; "
    "standard mode is owner-led; cmux orchestration is visible-terminal-only; "
    "browser routing is Webwright, Playwright CLI, and Chrome DevTools MCP; "
    "only approved inventory providers are active; supported auth is enterprise, "
    "API-key, Vertex, Google Cloud, or owner-approved."
)
print(json.dumps({"systemMessage": message, "suppressOutput": True}, separators=(",", ":")))
PY
