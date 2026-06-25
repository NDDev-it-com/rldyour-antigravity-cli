<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: f031b9ecb437c92579b84aa967cc6d0d7b0cfe8c chore(release): antigravity 1.6.1
Scope: Antigravity CLI transition and access policy
Area: ANTIGRAVITY
-->

# ANTIGRAVITY-01-TRANSITION

## Purpose

Record Antigravity CLI access risk from the Antigravity transition.

## Current Facts

- Consumer OAuth availability after `2026-06-18` is `NOT_PROVEN`.
- Supported targets are enterprise, paid API-key, Vertex AI, Google Cloud, and
  owner-approved authenticated environments.
- Antigravity CLI is the primary runtime for the current adapter.

## Evidence

- `config/gemini-baseline.json`
- `references/gemini-antigravity-transition.md`
- `references/authentication.md`

## Operational Rules

- Do not promise long-term consumer OAuth support.
- Do not add an Antigravity adapter without verified upstream contracts.

## Last Verified

2026-06-19

- commit: `f031b9ecb437c92579b84aa967cc6d0d7b0cfe8c`
- checked by: structural-loop repair memory normalization
