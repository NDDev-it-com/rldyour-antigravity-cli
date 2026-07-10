# rldyour-antigravity-cli Project Memory

This is the Antigravity CLI-side memory for `rldyour-antigravity-cli`.

## Source of Truth

- `GEMINI.md`
- `.gemini/antigravity-cli/settings.json`
- `.gemini/antigravity-cli/mcp_config.json`
- `gemini-extension.json`
- `config/rldyour-contract.json`
- `config/gemini-baseline.json`
- `.gemini/**`
- `scripts/*.py` and `scripts/*.sh`

## Runtime Baseline

- Antigravity runtime source is `antigravity-cli` with baseline pins in
  `config/gemini-baseline.json`.
- MCP runtime pins are fixed by the extension manifest and shell install workflow.

## Native Boundaries

Use Gemini CLI-native surfaces only:

- `.gemini/`
- `gemini-extension.json`
- `GEMINI.md`
- `commands`, `agents`, `skills`, `hooks`, `policies` under `.gemini`

Do not mix Codex/Claude/OpenCode native config formats as active Antigravity runtime
surfaces.

## Standard Runbook

```bash
bash scripts/install_system_gemini.sh --dry-run
bash scripts/install_system_gemini.sh --apply
bash scripts/doctor_system_gemini.sh --redact
```

Validation:

```bash
python3 scripts/validate_gemini_extension_manifest.py
python3 scripts/validate_gemini_projection_parity.py
python3 scripts/validate_gemini_config.py
python3 scripts/validate_instruction_docs.py --strict
```

## Browser/Provider Boundary

- Webwright: orchestration-level browser routing.
- Playwright CLI: low-level UI evidence.
- Chrome DevTools MCP: console/network/performance traces.

All browser providers must attach to bootstrap-owned CloakBrowser. The only
configured browser MCP transport is the managed
`~/.local/bin/chrome-devtools-mcp` wrapper. Direct `bunx`/`npx` Chrome DevTools
package transport is forbidden. Raw, stock, and in-app browser fallback is
forbidden.
