<!-- Memory Metadata
Last updated: 2026-07-10
Last verified: 2026-07-10
Last commit: c74adf6766b1fb1c88c019d20f78dab65ae5e932 feat(browser): enforce managed CloakBrowser skill boundary
Scope: CLI runtime and package baselines
Area: RUNTIME
-->

# RUNTIME-01-BASELINE

## Purpose
Maintain durable Antigravity CLI adapter knowledge for `RUNTIME-01-BASELINE`.

## Current Facts
- Current facts are recorded in the source-of-truth, facts, and evidence sections below.

## Operational Rules
- Current code, configuration, tests, and live runtime evidence override stale memory text.
- Keep this memory fact-only and update it after verified Antigravity adapter changes.

## Last Verified
2026-07-10


## Scope
CLI runtime and package baselines

## Current source of truth
- `path:README.md`
- `path:config/gemini-baseline.json`
- `path:references/gemini-antigravity-transition.md`

## Last verified
- date: 2026-07-10
- commit: `c74adf6766b1fb1c88c019d20f78dab65ae5e932`
- checked by: Antigravity runtime and browser boundary validation

## Facts
- The supported runtime binary is `agy` from Antigravity CLI `1.1.1`.
- Runtime installation remains a bootstrap-owned generation-pinned artifact with digest verification; this adapter does not execute remote installer scripts.
- Adapter patch `1.7.29` hardens browser execution without changing the
  Antigravity runtime baseline.

## Evidence
- `commit:c74adf6766b1fb1c88c019d20f78dab65ae5e932`
- `path:README.md`
- `path:config/gemini-baseline.json`
- `path:references/gemini-antigravity-transition.md`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.
