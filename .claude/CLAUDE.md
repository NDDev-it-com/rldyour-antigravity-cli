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
- `config/mcp-runtime-versions.env` pins Sequential Thinking `2026.7.4` and
  Context7 `3.2.3`; all active MCP projections and contract claims must match.

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

Before every browser action, run exact
`$HOME/.local/bin/cloakbrowser-cdp-health`. Execute only exact managed
`$HOME/.local/bin/playwright-cli` or the configured exact managed
`$HOME/.local/bin/chrome-devtools-mcp` transport; missing health stops as
`NOT_PROVEN` and no fallback is allowed.

`webwright-task` is compatibility intent only. Webwright runtime,
`browser_agent`, `node_repl`, computer-use, MCP-based Playwright browser
control, raw/stock/in-app Browser, direct packages, alternate
CDP/executables/configs, `run-code`, and `--filename` are forbidden.

## CI runner selection

This repository is public, so `pull_request` executes untrusted fork code.
Every caller of a `NDDev-OpenNetwork/ci-workflows` reusable that exposes a `runner`
input passes `runner: ubuntu-latest` explicitly, and must keep it. Several of
those reusables default `runner` to the estate's self-hosted `amsterdam`
label, and a default is a property of the **pinned commit**, not of this
repository — so dropping the explicit value would let a routine pin bump route
fork PRs onto trusted private infrastructure with no diff here to review. On
any ci-workflows pin bump, diff `inputs.runner.default` between the old and
new commit before merging.
