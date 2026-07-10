# Antigravity Surface Adoption

## Current Baseline

The adapter targets Antigravity CLI (`agy`) `1.1.0` and adopts native Antigravity CLI
surfaces: context files, project settings, extension manifest, TOML commands,
Agent Skills, subagents, hooks, policies, MCP servers, model routing, and
headless prompt smoke mode.

Antigravity built-in `browser_agent` is intentionally disabled in `1.7.27`; browser
work remains routed through Webwright, Playwright CLI + Skills, and Chrome
DevTools MCP until a separate provider model and validator prove otherwise.

All browser providers must attach to bootstrap-owned CloakBrowser. The only
configured browser MCP transport is the managed
`~/.local/bin/chrome-devtools-mcp` wrapper. Direct `bunx`/`npx` Chrome DevTools
package transport is forbidden. Raw, stock, and in-app browser fallback is
forbidden.

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
