# Audit Resolution Notes

This document records the current verified Antigravity CLI adapter state for the 2026-06-11 release-readiness, browser-provider, and offline-first `/ry-repair` repair pass. It is derived documentation; the root control-plane `config/repositories.json`, this adapter's `VERSION`, adapter changelog, validators, git state, and live GitHub state override this document when they disagree.

## Current Verified Adapter State

- Antigravity CLI adapter version: local `VERSION`.
- Antigravity CLI runtime baseline: `config/gemini-baseline.json`.
- Coordinated five-adapter tuple: root control-plane `config/repositories.json`.

This adapter document intentionally does not duplicate literal current heads or
versions for the other adapters. The root control plane owns the coordinated
tuple, and root docs regenerate their own tuple surfaces from
`config/repositories.json`.

Stable line: the root control plane records the current coordinated
five-adapter tuple and exact adapter versions. Antigravity CLI keeps only its
own local adapter version and runtime baseline in this repository.

## Resolved Since Earlier Audit Notes

- Earlier bootstrap-era and audit-archive current-state notes have been replaced with the root-owned verified tuple; this adapter no longer duplicates other adapters' current versions or heads.
- Root `.gitmodules`, root `config/repositories.json`, root README module table, adapter `VERSION` files, and adapter release changelogs agree on the current tuple.
- Approved active inventories: current MCP and browser/provider surfaces are validated from `config/mcp-version-policy.json`, `config/browser-automation-policy.json`, and `config/rldyour-system-contract.json`. Current docs and memories should not retain one-off absence claims for removed tools.
- `/ry-repair` system convergence is now documented in `docs/ry-repair-sync.md` and governed by `config/ry-repair-sync-contract.json` plus `scripts/ry_repair_sync.py`.
- Root Serena memories must be normalized after the final root commit so `Last verified` and `Evidence` commit references point only to the verified root control-plane commit.

## Principal Release Audit 39 (2026-06-13) Resolution

A principal release audit ("rldyour-ai-cli-tools 39") graded the system
`release-certified: no` on five P1 findings. That audit ran inside a sandbox
without `gh`/`GITHUB_TOKEN`, without the `timeout` binary, with DNS resolution
failures, and under a constrained process budget. Re-verified on the owner
workstation against current code and live GitHub state, all five P1 findings are
environmental artifacts of that sandbox, not control-plane defects:

- F-001 / F-002 (aggregate lane and adapter-health "hang/not-bounded"): not
  reproduced. `validate_all.py --lane static-only` is 87/87, `--lane adapter-fast`
  is green, and `validate_adapter_health.py --timeout 20 --total-timeout 85`
  completes deterministically. `validate_all.py` and `validate_adapter_health.py`
  already use `start_new_session` process groups with SIGTERM→SIGKILL teardown
  and have regression tests; the sandbox hang came from its missing `timeout`
  binary and process budget. F-017 (subprocess robustness) is therefore already
  satisfied; no refactor was applied to avoid risk to working release-critical code.
- F-003 (adapter full pytest not bounded-green): all five adapter suites plus
  root pytest run bounded-green (root 183; Claude 150; Codex 128; OpenCode 558;
  Gemini 17; MiMoCode 8).
- F-004 (GitHub CI provenance) and F-005 (GitHub Releases): proven green live -
  `collect_github_ci_provenance.py`/`validate_github_ci_provenance.py --strict`
  PASS for root plus five adapters, and every adapter numeric tag resolves
  exactly to its `expected_head` GitHub Release. The live-network lane already
  wired CI provenance; releases are now persisted as evidence (below).
- F-006 (Webwright strict provenance): proven green live; the sandbox failure was
  DNS only.

Durable hardening applied (root control plane only - no adapter source needed):

- F-005 / F-018: `validate_github_releases.py` and `validate_live_runtime_latest.py`
  gained `--json` evidence persistence, wired into the live-network lane to match
  the existing CI-provenance/browser-provider/public-repo-settings evidence pattern.
- F-011: new `validate_live_mcp_runtime_versions.py --strict-proven --json` MCP
  registry-freshness gate; every version-pinned MCP package is confirmed published
  with registry latest recorded as informational drift.
- F-009: installed-runtime lane gained `mimocode-version` and
  `mimocode-runtime-doctor`, closing the four-of-five adapter asymmetry.
- F-012: the executable adapter-fast lane now includes the four MiMoCode delegated
  native-surface checks declared in `config/adapter-test-lanes.json`; all five
  adapter native harnesses were re-run green.
- F-013: added `scripts/validate_mimocode_native_boundaries.py` for naming symmetry
  with the Gemini equivalent; canonical MiMoCode validator names documented.
- F-008 / F-014: handoff-archive enforcement documented in `docs/ry-repair-sync.md`.

Doc findings already satisfied before this pass: F-007 (Claude `2.1.177` is
already described as an npm/runtime rollup with empty release notes), F-010
(OpenCode docs already state npm is authoritative and GitHub Releases are
informational), F-016 (OpenCode `permission.ask` notes already mark `v1.15.4` as
historical evidence under the current `v1.17.6` baseline), and F-015
(`validate_retired_tool_residue.py --strict-no-tool-names-in-active-docs` is green;
no retired tool names in active root docs).

Context7 registry drift (resolved): the owner directed Context7 to track the
latest published version everywhere it is used. All local-stdio adapters
(Claude, Codex, Gemini, MiMoCode) now pin `@upstash/context7-mcp@3.2.1` (npm
latest); Claude moved off its prior `2.2.5` hold after the `3.2.1` stdio MCP
`initialize` runtime smoke verified the server starts, so the Claude
`override_reason` was removed. OpenCode continues to use the always-current
hosted endpoint `https://mcp.context7.com/mcp`. The MCP registry-freshness gate
confirms every pinned Context7 version is published.

## Current Intentional Boundaries

- The control plane coordinates adapter pins, contracts, release policy, validation lanes, root maintenance skills, launcher policy, and fullrepo/Serena memory sync. Adapter implementation changes still belong in the adapter repositories first.
- Owner-standard full-auto remains intentional: Codex uses the `rldyour-yolo` legacy sandbox dialect, Claude exposes the trusted owner bypass posture, and OpenCode allows primary owner contexts to use broad native permission keys while reviewer roles remain constrained.
- Historical changelog entries may mention old runtime pins or earlier release versions. Historical entries are not current configuration.
- Live-network and installed-runtime gates require local tools, authentication, and current machine state. Static gates must not claim live GitHub or installed CLI parity unless those gates actually ran.
- OpenCode runtime freshness uses npm package `opencode-ai` as the source of truth; GitHub Releases are informational for this repository's baseline policy.

## Required Acceptance Commands

```bash
python3 scripts/validate_control_plane.py
python3 scripts/validate_active_mcp_inventory.py --scope all --strict
python3 scripts/validate_active_provider_inventory.py --scope all --strict
python3 scripts/validate_retired_tool_residue.py --only-current-docs --allow-changelog-history
python3 scripts/validate_installed_ai_cli_configs.py --scope all --target "$PWD" --strict-approved-surfaces
python3 scripts/validate_ry_repair_sync_contract.py
python3 scripts/ry_repair_sync.py --check --target "$PWD" --offline --json
python3 scripts/validate_serena_memory_schema.py --scope all --strict-mode strict-all
python3 scripts/validate_serena_memory_semantics.py --scope all --strict-current-facts --strict-metadata-dates --strict-evidence-commits
python3 scripts/validate_source_archive_hygiene.py --mode working-tree
python3 scripts/validate_required_status_check_triggers.py --scope all --strict
python3 scripts/validate_repository_settings_policy.py --scope public-adapters --strict
python3 scripts/validate_github_actions_pin_policy.py --scope all --strict
python3 scripts/validate_adapter_test_lane_policy.py --strict
python3 scripts/validate_release_line_semantics.py --line 1.3 --scope all --strict
python3 -m pytest -q
```

## Fullrepo Publication Boundary

Documentation/config changes tracked on `main` and agent-only Serena/instruction changes are released in two phases: commit the tracked source changes first, then publish or restore the `fullrepo` context so it references the new root HEAD. `validate_fullrepo_sync.py` is expected to fail on an uncommitted overlay that changes non-agent files; that is a release-process signal, not a reason to weaken the fullrepo gate.

```bash
python3 modules/rldyour-codex/plugins/rldyour-flow/scripts/fullrepo_sync.py --publish
python3 scripts/validate_fullrepo_sync.py --scope all --require-adapter-fullrepo --strict --allow-generated-artifacts --timeout 20
```

## Repair Rule

When a future audit finds a conflict, update the source of truth first, then update docs and Serena memories only with evidence-backed current facts. Unsupported current claims must be deleted or explicitly demoted to historical evidence; do not keep them as active guidance.
