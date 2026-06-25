<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: f031b9ecb437c92579b84aa967cc6d0d7b0cfe8c chore(release): antigravity 1.6.1
Scope: Antigravity CLI adapter implementation surface
Area: GEMINI
-->

# GEMINI-01-ADAPTER-SURFACE

## Purpose

Describe the Antigravity CLI-native adapter surface, including the
official Google replacement for the sunset `gemini` CLI.

## Current Facts

- Adapter version is `1.7.0`.
- Runtime configuration uses Gemini-native surfaces, not Claude, Codex, or OpenCode runtime files.
- Native surfaces include `GEMINI.md`, settings JSON, extension manifest, TOML commands, Agent Skills, subagents, hooks, policies, MCP servers, and headless prompt smoke mode.
- Runtime binary is `agy`; target runtime version is `1.0.11`.
- Adapter HEAD is governed by the root control-plane `config/repositories.json`.

## Operational Rules

- Use `agy` (Antigravity CLI) for gemini adapter work.
- Apply the rldyour system AGENTS.md to `~/.config/antigravity/` via the install script.
- Keep the legacy `gemini` CLI binary on disk for the 3-day migration window.

## Last Verified
2026-06-18
- date: 2026-06-25

- date: 2026-06-25
- commit: `f031b9ecb437c92579b84aa967cc6d0d7b0cfe8c`
- checked by: antigravity 1.7.0 tracked-context migration

## Evidence

- `commit:f031b9ecb437c92579b84aa967cc6d0d7b0cfe8c`
- `path:modules/rldyour-antigravity-cli/AGENTS.md`
- `path:modules/rldyour-antigravity-cli/GEMINI.md`
- `path:modules/rldyour-antigravity-cli/.gemini/settings.json`
- `path:modules/rldyour-antigravity-cli/gemini-extension.json`
- `path:modules/rldyour-antigravity-cli/.gemini/commands/`
