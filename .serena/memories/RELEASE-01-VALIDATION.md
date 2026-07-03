<!-- Memory Metadata
Last updated: 2026-07-03
Last verified: 2026-07-03
Last commit: 62d3934d280dc2ffb3e57debe9a54b0de9869b98 chore(release): gemini 1.7.15 (other)
Scope: Antigravity CLI release validation
Area: RELEASE
-->

# RELEASE-01-VALIDATION

## Purpose

Record release validation requirements for the current Antigravity adapter release.

## Current Facts

- Current adapter release is `1.7.15`.
- Initial adapter release was recorded in the changelog.
- Previous stable adapter releases are historical changelog facts, not current release targets.
- Only exact current numeric tags are supported.
- Public CI must use GitHub-hosted runners and full SHA-pinned actions.
- Source archives must exclude caches, runtime state, secrets, and local browser
  artifacts.

## Evidence

- `VERSION`
- `CHANGELOG.md`
- `SECURITY.md`
- `references/release-version-policy.md`
- `references/public-ci-policy.md`
- `.github/workflows/validate.yml`

## Operational Rules

- Do not certify release without local validators, pytest, GitHub Release
  evidence, and clean archive hygiene.

## Last Verified

2026-07-03

## Last verified
- date: 2026-07-03
- commit: `62d3934d280dc2ffb3e57debe9a54b0de9869b98`
- checked by: antigravity 1.7.15 tracked-context migration and tracked memory refresh
