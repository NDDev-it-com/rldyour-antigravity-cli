#!/usr/bin/env bash
set -euo pipefail

input="$(cat || true)"
export RLDYOUR_GEMINI_HOOK_INPUT="$input"
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$script_dir/../VERSION" ]]; then
  adapter_version="$(<"$script_dir/../VERSION")"
elif [[ -f "$script_dir/../../VERSION" ]]; then
  adapter_version="$(<"$script_dir/../../VERSION")"
else
  adapter_version="1.7.29"
fi
export RLDYOUR_ANTIGRAVITY_ADAPTER_VERSION="$adapter_version"
printf '%s\n' "rldyour-antigravity-cli SessionStart hook received input" >&2

python3 - <<'PY'
import json
import os

_ = os.environ.get("RLDYOUR_GEMINI_HOOK_INPUT", "")
version = os.environ.get("RLDYOUR_ANTIGRAVITY_ADAPTER_VERSION", "1.7.29")
message = (
    f"rldyour-antigravity-cli adapter={version} runtime=antigravity-cli@1.1.0; "
    "standard mode is owner-led; cmux orchestration is visible-terminal-only; "
    "every browser action requires exact managed CloakBrowser health; execution is limited "
    "to exact managed Playwright CLI and Chrome DevTools MCP wrappers; Webwright runtime, "
    "browser_agent, direct packages, alternate CDP/config/executables, and fallback are forbidden; "
    "only approved inventory providers are active; supported auth is enterprise, "
    "API-key, Vertex, Google Cloud, or owner-approved."
)
print(json.dumps({"systemMessage": message, "suppressOutput": True}, separators=(",", ":")))
PY
