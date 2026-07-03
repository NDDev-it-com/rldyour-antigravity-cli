# Changelog

## [1.7.7] - 2026-06-27

- Align the Antigravity settings schema snapshot with the `1.0.13` runtime baseline.

## [1.7.6] - 2026-06-27

- Refresh the Antigravity CLI runtime baseline from `1.0.12` to `1.0.13` using the official upstream release.

## [1.7.5] - 2026-06-27

### Changed

- Refresh shadcn MCP runtime pin to the latest published 4.12.0 release.

## [1.7.4] - 2026-06-26

### Changed

- Sync Serena release memories after runtime and MCP refresh.

## [1.7.3] - 2026-06-26

### Changed

- Refresh CLI runtime and MCP pins to latest stable versions.

## [1.7.2] - 2026-06-26

### Fixed

- Align README memory heading and supported-version wording with the tracked-context line.

## [1.7.1] - 2026-06-26

### Fixed

- Sync generated cmux worker/orchestrator skill projections with the tracked-context branch model.

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and adapter versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]


## [1.7.14] - 2026-07-03

### Fixed

- Refresh runtime and dependency baselines.

## [1.7.13] - 2026-07-01

### Changed

- Refresh Codex CLI 0.142.5 and Playwright CLI 0.1.15 adapter baselines.
- Align Playwright CLI browser provider pin to 0.1.15.

## [1.7.12] - 2026-06-30

### Fixed

- Refresh Antigravity CLI runtime baseline to 1.0.14.

## [1.7.11] - 2026-06-30

### Fixed

- Fix published release artifact proof and Antigravity MCP parity.

## [1.7.10] - 2026-06-29

### Fixed

- Install pytest dependencies in required CI validation workflows.

## [1.7.9] - 2026-06-29

### Fixed

- Enforce five-adapter validation parity and structured release evidence

## [1.7.8] - 2026-06-29

### Fixed

- Enforce five-adapter validation parity and structured release evidence

## [1.7.0] - 2026-06-26

### Changed

- Track durable Serena context on `main` and retire the separate `fullrepo`
  branch model for Antigravity CLI adapter releases.
- Update Antigravity commands, skills, subagents, docs, branch-protection
  policy, and validators to treat `.serena/project.yml` and
  `.serena/memories/` as normal source while keeping runtime-local cache,
  review scratch files, diagnostics, markers, tokens, cookies, and credentials
  ignored.

### Removed

- Removed the `fullrepo` branch-protection policy and active fullrepo
  publication guidance from current Antigravity adapter surfaces.

## [1.6.1] - 2026-06-25

### Changed

- Refresh CLI runtime baselines to latest (Claude Code 2.1.190, Codex 0.142.0, OpenCode 1.17.9, Antigravity CLI 1.0.11, MiMoCode 0.1.3); resolve adapter instruction-doc and surface-adoption drift.
- Advance Antigravity CLI runtime baseline from `1.0.8` to `1.0.11` (upstream `google-antigravity/antigravity-cli` GitHub release `1.0.11`, published 2026-06-24, non-draft; `/releases/latest` resolves to `1.0.11`). Verified `2026-06-25`.

## [1.6.0] - 2026-06-24

### Changed

- cmux worker v3 projections and latest MCP runtime pins (chrome-devtools-mcp 1.4.0, context7 3.2.2)

## [1.5.5] - 2026-06-17

### Fixed

- patch: antigravity audit-resolution tuple sync

## [1.5.4] - 2026-06-16

### Fixed

- patch: antigravity instruction docs tuple sync

## [1.5.3] - 2026-06-16

### Fixed

- patch: advance past system-instruction tracking (.gemini/, AGENTS.md) and empty-tree fullrepo fix

## [1.5.2] - 2026-06-16

### Fixed

- MCP URL fixes for Antigravity CLI runtime:
  - **openai-docs**: replace invalid `mcp.openai.com` with `https://developers.openai.com/mcp` (typo in earlier URL; the MCP server is at the official `developers.openai.com` host, not `mcp.openai.com`).
  - **figma**: replace local Figma desktop bridge `http://127.0.0.1:3845/mcp` with cloud-hosted `https://mcp.figma.com/mcp` (authenticates with `FIGMA_PAT` environment variable; no local desktop process required).
  - **deepwiki**: bump tool-call timeout from 120000ms to 180000ms to accommodate slower repository wiki generation.
- Mirror the MCP URL fixes in `config/mcp-version-policy.json` (policy source of truth) and the tracked module source `.gemini/antigravity-cli/mcp_config.json` so the runtime and policy stay in sync.

## [1.5.1] - 2026-06-15

### Changed

- Align SECURITY.md line label, adapter README baseline, and tracked uv.lock self-version to the 1.5.x line for the public governance gate.

## [1.5.0] - 2026-06-15

### Changed

- Owner-directed unified 1.5.0 release: perfect-sync quality wave (README baseline, ASCII hygiene, agy binary canonicalization, validator coverage).

## [1.4.0] - 2026-06-15

### Changed

- Migrated primary runtime from Gemini CLI to Antigravity CLI 1.0.8.
- Added `.gemini/antigravity-cli/settings.json` and `mcp_config.json`.
- Updated install scripts for dual-runtime support (antigravity + gemini legacy).
- Updated adapter contract with Antigravity native surfaces.
- Updated transition doc status from NOT_PROVEN to MIGRATED.

### Backward Compatibility

- Gemini CLI 0.46.0 extension manifest remains compatible.
- Enterprise users on Gemini CLI Standard/Enterprise are not impacted.
- Extension name remains `rldyour-antigravity-cli` for marketplace continuity.

## [1.3.7] - 2026-06-14

### Fixed

- Five-adapter wave (codex/opencode/gemini/mimocode): owner autonomous standard (Gemini auto_edit+launcher YOLO, MiMoCode allow-all), ry-repair canonical flags, five-adapter contract matrix, SECURITY parity, MiMoCode runtime proof, unified ASCII public README template; root cmux worker-only, coverage policies, launchers gm/mm, enforcement validators.

## [1.3.6] - 2026-06-14

### Changed

- Pin Context7 MCP to latest 3.2.1

## [1.3.5] - 2026-06-13

### Changed

- Replace active agent-facing retired-tool tombstone wording with positive
  inventory policy language while preserving Gemini-native browser/provider
  routing.

## [1.3.4] - 2026-06-12

### Fixed

- Make the Scorecard workflow run on `pull_request` and `push` so the required
  branch-protection check is emitted for protected branch updates.

## [1.3.3] - 2026-06-12

### Fixed

- Synchronize tracked Gemini Serena memories with the stabilized `1.3.x`
  release tuple so adapter memory validation stays green at the release HEAD.

## [1.3.2] - 2026-06-12

### Fixed

- Complete `.serena/project.yml` with current Serena project keys so runtime
  MCP smoke checks no longer rewrite the tracked Gemini project configuration.

## [1.3.1] - 2026-06-12

### Fixed

- Stabilize the public 1.3 line with release CI, Context7 MCP freshness, and synchronized four-adapter evidence.

## [1.3.0] - 2026-06-12

### Added

- Add Gemini-native `/ry:init`, `/ry:newp`, `/ry:review`, `/ry:deploy`, and `/ry:sync` TOML commands plus matching Agent Skills so Gemini reaches the root seven-flow lifecycle contract.

### Changed

- Align the Gemini adapter product version with the coordinated four-configuration `1.3.0` stable release contract. This intentionally advances from `1.0.3` to `1.3.0` so Claude, Codex, OpenCode, and Gemini publish the same stable adapter line while retaining Gemini CLI `0.46.0` as the runtime baseline.

## [1.0.3] - 2026-06-12

### Fixed

- Use Gemini CLI native `ui.loadingPhrases = "off"` and enforce the documented enum in settings validation.

## [1.0.2] - 2026-06-12

### Fixed

- Aligned Gemini MCP configuration with native `timeout` milliseconds.
- Converted Gemini hooks to event-keyed native configuration with JSON stdin/stdout contracts.
- Declared sensitive extension environment variables through manifest `settings`.
- Replaced cross-tool subagent shorthand with Gemini-native tool identifiers.
- Added projection parity validation for `.gemini/*` runtime surfaces.
- Documented the disabled Gemini built-in `browser_agent` policy for this release.

## [1.0.1] - 2026-06-12

### Changed

- Updated GitHub Actions dependencies: `actions/checkout` `6.0.3` and
  `github/codeql-action` `4.36.2`.


## [1.0.0] - 2026-06-11

### Added

- Initial public Gemini CLI adapter with native `GEMINI.md`, settings,
  extension manifest, TOML commands, Agent Skills, subagents, hooks, policies,
  MCP inventory, browser-provider routing, Serena memories, validators, and
  tests.
- Runtime baseline for `@google/gemini-cli` `0.46.0`.
- Antigravity transition policy documentation for Gemini CLI access channels.
