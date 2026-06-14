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
- date: 2026-06-15
- commit: `1cc0b2a2ebdeb35c9dc418eec10e20f1442cf236`
- checked by: flow-memory-sync post-task sync
