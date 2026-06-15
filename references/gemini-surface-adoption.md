# Antigravity Surface Adoption

## Current Baseline

The adapter targets Antigravity CLI (`agy`) `1.0.8` and adopts native Antigravity CLI
surfaces: context files, project settings, extension manifest, TOML commands,
Agent Skills, subagents, hooks, policies, MCP servers, model routing, and
headless prompt smoke mode.

Antigravity built-in `browser_agent` is intentionally disabled in `1.5.0`; browser
work remains routed through Webwright, Playwright CLI + Skills, and Chrome
DevTools MCP until a separate provider model and validator prove otherwise.

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
