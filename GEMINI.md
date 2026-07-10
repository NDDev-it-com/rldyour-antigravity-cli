# rldyour Antigravity CLI Context

You are operating inside the `rldyour-antigravity-cli` adapter repository (now
Antigravity CLI-targeted). This adapter configures Antigravity CLI with
native surfaces for the rldyour AI CLI control plane.

## Current Facts

- Adapter version: `1.7.28`.
- Runtime: Antigravity CLI `1.1.0`.
- MCP refresh: Sequential Thinking `2026.7.4`; Context7 `3.2.3`.
- Install owner: `rldyour-new-mac-or-ubuntu` generation-pinned artifact channel
- Config path: `~/.gemini/antigravity-cli/settings.json`
- MCP config: `~/.gemini/antigravity-cli/mcp_config.json`
- Hooks: `.gemini/hooks/hooks.json` projected into the Antigravity native namespace.
- Binary: `agy` (not `gemini`)
- Supported access target: enterprise, paid API-key, Vertex AI, Google Cloud, or
  explicitly owner-approved authenticated environments.
- Consumer OAuth availability after June 18, 2026 is not promised because Google
  transitioned unpaid and Google One users to Antigravity CLI.

## Operating Rules

- Use Antigravity CLI-native configuration files: `GEMINI.md`,
  `.gemini/antigravity-cli/settings.json`, `.gemini/antigravity-cli/mcp_config.json`,
  `gemini-extension.json`, TOML commands, skills, agents, hooks, and policies.
- Configure only providers listed in the approved active inventory; removed or
  historical tools require an explicit inventory and release-policy update.
- Keep browser routing split: Webwright for long-horizon workflows, Playwright
  CLI for screenshots/flows/visual evidence, Chrome DevTools MCP for debugging.
- All browser providers must attach to bootstrap-owned CloakBrowser. The only
  configured browser MCP transport is the managed
  `~/.local/bin/chrome-devtools-mcp` wrapper. Direct `bunx`/`npx` Chrome DevTools
  package transport is forbidden. Raw, stock, and in-app browser fallback is
  forbidden.
- Antigravity built-in `browser_agent` is disabled for this release; do not enable it
  unless it is modeled as a separate explicit provider with validators.
- In standard mode, the owner/user remains the orchestration layer.
- In cmux mode, orchestration exists only as visible terminal sessions.
- Antigravity subagents are internal Antigravity CLI delegation, not cmux workers.
- Headless `antigravity-cli -p` is allowed for smoke, doctor, and CI checks only.
- Never commit secrets, OAuth state, service-account files, browser artifacts,
  runtime caches, or temporary evidence.

## Required Report Shape

When reporting work, include exact files changed, commands run, pass/fail
results, and any `NOT PROVEN` gaps. Do not claim release certification unless
the root control plane and all adapter gates pass.
