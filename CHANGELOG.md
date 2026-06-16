# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and adapter versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]


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
