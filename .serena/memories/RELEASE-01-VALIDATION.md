<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: f031b9ecb437c92579b84aa967cc6d0d7b0cfe8c chore(release): antigravity 1.6.1
Scope: Antigravity CLI release validation
Area: RELEASE
-->

# RELEASE-01-VALIDATION

## Purpose

Record release validation requirements for the current Antigravity adapter release.

## Current Facts

- Current adapter release is `1.7.0`.
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
- commit: `f031b9ecb437c92579b84aa967cc6d0d7b0cfe8c`
- checked by: antigravity 1.7.0 tracked-context migration
