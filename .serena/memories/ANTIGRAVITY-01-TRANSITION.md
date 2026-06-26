<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: 56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c chore(release): prepare antigravity 1.7.3 tracked context
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

- commit: `56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c`
- checked by: antigravity 1.7.3 tracked-context migration
