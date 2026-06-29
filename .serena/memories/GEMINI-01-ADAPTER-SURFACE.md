<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: 56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c chore(release): prepare antigravity 1.7.5 tracked context
Scope: Antigravity CLI adapter implementation surface
Area: GEMINI
-->

# GEMINI-01-ADAPTER-SURFACE

## Purpose

Describe the Antigravity CLI-native adapter surface, including the
official Google replacement for the sunset `gemini` CLI.

## Current Facts

- Adapter version is `1.7.10`.
- Runtime configuration uses Gemini-native surfaces, not Claude, Codex, or OpenCode runtime files.
- Native surfaces include `GEMINI.md`, settings JSON, extension manifest, TOML commands, Agent Skills, subagents, hooks, policies, MCP servers, and headless prompt smoke mode.
- Runtime binary is `agy`; target runtime version is `1.0.13`.
- Adapter HEAD is governed by the root control-plane `config/repositories.json`.

## Operational Rules

- Use `agy` (Antigravity CLI) for gemini adapter work.
- Apply the rldyour system AGENTS.md to `~/.config/antigravity/` via the install script.
- Keep the legacy `gemini` CLI binary on disk for the 3-day migration window.

## Last Verified
2026-06-18
- date: 2026-06-25

- date: 2026-06-25
- commit: `56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c`
- checked by: antigravity 1.7.10 tracked-context migration

## Evidence

- `commit:56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c`
- `path:modules/rldyour-antigravity-cli/AGENTS.md`
- `path:modules/rldyour-antigravity-cli/GEMINI.md`
- `path:modules/rldyour-antigravity-cli/.gemini/settings.json`
- `path:modules/rldyour-antigravity-cli/gemini-extension.json`
- `path:modules/rldyour-antigravity-cli/.gemini/commands/`
