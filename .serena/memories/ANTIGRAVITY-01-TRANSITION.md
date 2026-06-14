# ANTIGRAVITY-01-TRANSITION

## Purpose

Record Gemini CLI access risk from the Antigravity transition.

## Current Facts

- Consumer OAuth availability after `2026-06-18` is `NOT_PROVEN`.
- Supported targets are enterprise, paid API-key, Vertex AI, Google Cloud, and
  owner-approved authenticated environments.
- Antigravity CLI is out of scope for adapter `1.3.7`.

## Evidence

- `config/gemini-baseline.json`
- `references/gemini-antigravity-transition.md`
- `references/authentication.md`

## Operational Rules

- Do not promise long-term consumer OAuth support.
- Do not add an Antigravity adapter without verified upstream contracts.

## Last Verified

2026-06-13

## Last verified
- date: 2026-06-15
- commit: `834e12d1320b0f9d966ac746385d404dcd34a4bd`
- checked by: flow-memory-sync post-task sync
