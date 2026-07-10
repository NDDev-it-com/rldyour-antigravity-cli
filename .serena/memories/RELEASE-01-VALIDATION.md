<!-- Memory Metadata
Last updated: 2026-07-10
Last verified: 2026-07-10
Last commit: c74adf6766b1fb1c88c019d20f78dab65ae5e932 feat(browser): enforce managed CloakBrowser skill boundary
Scope: release readiness, versioning, and artifact hygiene
Area: RELEASE
-->

# RELEASE-01-VALIDATION

## Purpose
Maintain durable Antigravity CLI adapter knowledge for `RELEASE-01-VALIDATION`.

## Current Facts
- Current facts are recorded in the source-of-truth, facts, and evidence sections below.

## Operational Rules
- Current code, configuration, tests, and live runtime evidence override stale memory text.
- Keep this memory fact-only and update it after verified Antigravity adapter changes.

## Last Verified
2026-07-10


## Scope
release readiness, versioning, and artifact hygiene

## Current source of truth
- `path:VERSION`
- `path:CHANGELOG.md`
- `path:.github/workflows/release.yml`

## Last verified
- date: 2026-07-10
- commit: `c74adf6766b1fb1c88c019d20f78dab65ae5e932`
- checked by: Antigravity adapter 1.7.31 release validation

## Facts
- Current adapter release version is `1.7.31`; `VERSION`, `pyproject.toml`,
  `uv.lock`, `gemini-extension.json`, policy projections, hook fallbacks,
  contract claims, docs, and security support metadata must agree.
- Antigravity CLI remains pinned to `1.1.1`; this adapter release changes the
  browser execution boundary without moving runtime or provider versions.
- `scripts/validate_release.sh` includes strict browser policy, projection, instruction-doc, Serena, pytest, Python compile, and diff hygiene gates.

## Evidence
- `commit:c74adf6766b1fb1c88c019d20f78dab65ae5e932`
- `path:VERSION`
- `path:CHANGELOG.md`
- `path:.github/workflows/release.yml`
- `path:scripts/validate_release.sh`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.
