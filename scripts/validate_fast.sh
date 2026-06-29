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
python3 -m pytest -q
