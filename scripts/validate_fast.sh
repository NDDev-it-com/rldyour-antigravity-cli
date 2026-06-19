#!/usr/bin/env bash
set -euo pipefail

python3 scripts/validate_gemini_config.py --strict
python3 scripts/validate_gemini_commands.py --strict
python3 scripts/validate_gemini_skills.py --strict
python3 scripts/validate_gemini_subagents.py --strict
python3 scripts/validate_gemini_hooks.py --strict
python3 scripts/validate_gemini_mcp_inventory.py --strict
python3 scripts/validate_gemini_browser_routing.py --strict
python3 scripts/validate_gemini_runtime_baseline.py --strict
python3 scripts/validate_instruction_docs.py --strict

if python3 - <<'PY' >/dev/null 2>&1
import pytest
import pytest_cov
PY
then
  python3 -m pytest -q
else
  printf 'skip: pytest/pytest-cov unavailable; offline fast validators completed without network installs\n'
fi
