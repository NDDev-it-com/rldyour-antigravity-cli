<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: 56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c chore(release): prepare antigravity 1.7.5 tracked context
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
- commit: `56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c`
- checked by: antigravity 1.7.5 tracked-context migration
