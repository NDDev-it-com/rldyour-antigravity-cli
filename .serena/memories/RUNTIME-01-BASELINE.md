<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: f031b9ecb437c92579b84aa967cc6d0d7b0cfe8c chore(release): antigravity 1.6.1
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
- commit: `f031b9ecb437c92579b84aa967cc6d0d7b0cfe8c`
- checked by: antigravity 1.7.0 tracked-context migration
