<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: 56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c chore(release): prepare antigravity 1.7.5 tracked context
Scope: Antigravity CLI release validation
Area: RELEASE
-->

# RELEASE-01-VALIDATION

## Purpose

Record release validation requirements for the current Antigravity adapter release.

## Current Facts

- Current adapter release is `1.7.14`.
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

2026-06-13

## Last verified
- date: 2026-06-25
- commit: `56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c`
- checked by: antigravity 1.7.14 tracked-context migration
