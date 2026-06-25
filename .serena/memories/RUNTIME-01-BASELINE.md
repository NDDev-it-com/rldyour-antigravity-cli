<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: 56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c chore(release): prepare antigravity 1.7.0 tracked context
Scope: Antigravity CLI runtime baseline
Area: RUNTIME
-->

# RUNTIME-01-BASELINE

## Purpose

Record Antigravity CLI runtime baseline and source-of-truth policy.

## Current Facts

- Runtime is `antigravity-cli`.
- Runtime binary is `agy`.
- Target runtime version is `1.0.11`.
- Primary latest source is `agy --version`, with GitHub Releases as release provenance.
- Legacy Gemini CLI `0.46.0` remains compatibility context only for enterprise legacy users.
- Installed runtime smoke requires authentication and is not mandatory for
  source-only validation.

## Evidence

- `config/gemini-baseline.json`
- `README.md`
- `references/gemini-surface-adoption.md`

## Operational Rules

- Do not use unscoped package names such as `antigravity-cli` or `gemini/cli`.
- Do not fail source-only validation because preview models are unavailable.

## Last Verified

2026-06-11


## Last verified
- date: 2026-06-25
- commit: `56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c`
- checked by: antigravity 1.7.0 tracked-context migration
