# Antigravity Surface Adoption

## Current Baseline

The adapter targets Antigravity CLI (`agy`) `1.1.0` and adopts native Antigravity CLI
surfaces: context files, project settings, extension manifest, TOML commands,
Agent Skills, subagents, hooks, policies, MCP servers, model routing, and
headless prompt smoke mode.

Antigravity built-in `browser_agent` is disabled. Every browser action requires
exact `$HOME/.local/bin/cloakbrowser-cdp-health` and may execute only through
exact managed `$HOME/.local/bin/playwright-cli` or the configured managed
`$HOME/.local/bin/chrome-devtools-mcp` transport. Missing health stops as
`NOT_PROVEN`; no fallback is allowed.

`webwright-task` is compatibility intent routed through `browser:validate`.
Webwright runtime, raw/stock/in-app Browser, package runners, alternate CDP,
executables/configs, and fallbacks are forbidden.

## Evidence

- `config/gemini-baseline.json`
- `gemini-extension.json`
- `.gemini/settings.json`
- `.gemini/commands/`
- `.gemini/skills/`
- `.gemini/agents/`
- `.gemini/hooks/hooks.json`
- `config/browser-provider-policy.json`

## Operational Rule

Do not represent Antigravity runtime configuration through Claude, Codex, or OpenCode
native files.
