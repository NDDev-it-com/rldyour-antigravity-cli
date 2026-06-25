<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: f031b9ecb437c92579b84aa967cc6d0d7b0cfe8c chore(release): antigravity 1.6.1
Scope: Antigravity CLI MCP inventory
Area: MCP
-->

# MCP-01-TOOLS

## Purpose

Record the active Gemini MCP inventory.

## Current Facts

- Gemini active MCP inventory has 11 servers.
- Active aliases are `serena`, `chrome-devtools`, `sequential-thinking`,
  `shadcn`, `dart-flutter`, `context7`, `github`, `deepwiki`, `grep`, `figma`,
  and `openai-docs`.
- MCP aliases are dash-separated and contain no underscores.

## Evidence

- `.gemini/settings.json`
- `gemini-extension.json`
- `config/rldyour-contract.json`
- `config/mcp-runtime-versions.env`

## Operational Rules

- Configure only MCP servers listed in the approved active inventory.
- Keep Chrome DevTools MCP active.

## Last Verified

2026-06-13

## Last verified
- date: 2026-06-25
- commit: `f031b9ecb437c92579b84aa967cc6d0d7b0cfe8c`
- checked by: antigravity 1.7.0 tracked-context migration
