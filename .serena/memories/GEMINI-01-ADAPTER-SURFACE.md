# GEMINI-01-ADAPTER-SURFACE

## Purpose

Describe the Gemini CLI-native adapter surface.

## Current Facts

- Adapter version is `1.3.7`.
- Runtime configuration uses Gemini-native surfaces, not Claude, Codex, or
  OpenCode runtime files.
- Native surfaces include `GEMINI.md`, settings JSON, extension manifest, TOML
  commands, Agent Skills, subagents, hooks, policies, MCP servers, and headless
  prompt smoke mode.

## Evidence

- `VERSION`
- `GEMINI.md`
- `.gemini/settings.json`
- `gemini-extension.json`
- `.gemini/commands/`
- `.gemini/skills/`
- `.gemini/agents/`
- `.gemini/hooks/hooks.json`
- `.gemini/policies/`
- `references/gemini-native-boundaries.md`

## Operational Rules

- Do not copy Claude slash-command, Codex plugin, or OpenCode command formats as
  Gemini runtime surfaces.

## Last Verified

2026-06-13

## Last verified
- date: 2026-06-15
- commit: `834e12d1320b0f9d966ac746385d404dcd34a4bd`
- checked by: flow-memory-sync post-task sync
