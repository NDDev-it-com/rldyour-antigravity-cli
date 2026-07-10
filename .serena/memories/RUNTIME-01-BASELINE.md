<!-- Memory Metadata
Last updated: 2026-07-10
Last verified: 2026-07-10
Last commit: d527419c9c727aa54ef49e9a71e09203469f5ca0 fix(browser): enforce managed Cloak transport policy
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
- commit: `d527419c9c727aa54ef49e9a71e09203469f5ca0`
- checked by: Antigravity runtime and MCP refresh boundary validation

## Facts
- The supported runtime binary is `agy` from Antigravity CLI `1.1.0`.
- Runtime installation remains a bootstrap-owned generation-pinned artifact with digest verification; this adapter does not execute remote installer scripts.
- Adapter patch `1.7.28` refreshes two MCP packages without changing the Antigravity runtime baseline.

## Evidence
- `commit:d527419c9c727aa54ef49e9a71e09203469f5ca0`
- `path:README.md`
- `path:config/gemini-baseline.json`
- `path:references/gemini-antigravity-transition.md`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.
