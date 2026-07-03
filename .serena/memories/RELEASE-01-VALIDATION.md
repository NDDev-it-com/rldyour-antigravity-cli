<!-- Memory Metadata
Last updated: 2026-05-22
Last commit: 62d3934d280dc2ffb3e57debe9a54b0de9869b98 chore(release): gemini 1.7.16 (other)
Scope: release readiness, versioning, and artifact hygiene
Area: RELEASE
-->

# RELEASE-01-VALIDATION

## Scope
release readiness, versioning, and artifact hygiene

## Current source of truth
- `path:VERSION`
- `path:CHANGELOG.md`
- `path:.github/workflows/release.yml`

## Last verified
- date: 2026-05-22
- commit: `62d3934d280dc2ffb3e57debe9a54b0de9869b98`
- checked by: Codex ry-start memory taxonomy sync

## Facts
- Release memories record numeric versioning, tags, CI gates, and clean artifact hygiene.

## Evidence
- `commit:62d3934d280dc2ffb3e57debe9a54b0de9869b98`
- `path:VERSION`
- `path:CHANGELOG.md`
- `path:.github/workflows/release.yml`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.
