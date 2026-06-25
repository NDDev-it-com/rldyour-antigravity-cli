<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: f031b9ecb437c92579b84aa967cc6d0d7b0cfe8c chore(release): antigravity 1.6.1
Scope: Antigravity CLI security posture
Area: SECURITY
-->

# SECURITY-01-POSTURE

## Purpose

Record security posture for Gemini config, hooks, MCP, and auth.

## Current Facts

- Committed settings use `default` approval mode.
- YOLO/full-auto is launcher-only and not silently enabled by repository config.
- Real Gemini API keys, Google API keys, OAuth state, token files, service
  accounts, and ADC files must not be committed.
- Hooks are synchronous and bounded.

## Evidence

- `.gemini/settings.json`
- `.gemini/hooks/hooks.json`
- `.env.example`
- `SECURITY.md`
- `references/authentication.md`

## Operational Rules

- Fail closed on hook safety parsing errors.
- Redact auth diagnostics.

## Last Verified

2026-06-11


## Last verified
- date: 2026-06-25
- commit: `f031b9ecb437c92579b84aa967cc6d0d7b0cfe8c`
- checked by: antigravity 1.7.0 tracked-context migration
