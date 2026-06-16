# Claude Code Project Memory

This repository is `rldyour-ai-cli-tools`, a Git superproject control plane for AI CLI configuration repositories.

GitHub repository: `https://github.com/NDDev-it-com/rldyour-ai-cli-tools` (`PRIVATE`).

## What This Repo Owns

- Cross-adapter coordination for Claude Code, Codex, OpenCode, Gemini CLI, and MiMoCode.
- Submodule pins under `modules/`.
- Control-plane docs under `docs/`.
- Expected module tuple in `config/repositories.json`.
- Canonical repository description template in `config/repository-description-policy.json`.
- Exact MCP runtime pin, GitHub toolset parity, and native MCP source/runtime format policy in `config/mcp-version-policy.json`.
- Default patch-bump, owner-directed minor/major, and GitHub Release publication policy in `config/release-policy.json`.
- Memory quality, evidence, and domain taxonomy rules in `config/memory-policy.json`.
- Canonical GitHub repository descriptions, homepages, and topics in `config/repositories.json`.
- README module pin table, which must match `config/repositories.json.expected_head`.
- Owner-standard launcher docs and installer: `docs/yolo-launchers.md` and `scripts/install_yolo_launchers.sh`.
- `/ry-repair` sync docs and contract: `docs/ry-repair-sync.md`, `config/ry-repair-sync-contract.json`, and `scripts/ry_repair_sync.py`. The contract `repair_modes` split is canonical: work projects get authoring repair; in this control plane and adapter config repos the system-sync goal runs consumer mode (update FROM GitHub, never author repository changes).
- OS/mode and cmux contracts: `config/os-install-policy.json`, `config/cmux-orchestrator-policy.json`, `docs/os-install-matrix.md`, `docs/cmux-orchestrator-mode.md`, and `docs/orchestrator-worker-protocol.md`.
- cmux utilities: `scripts/generate_cmux_config.py`, `scripts/validate_cmux_orchestrator_config.py`, `scripts/install_cmux_macos.sh`, and `scripts/diagnose_cmux_runtime.sh`.
- Validation and release scripts `scripts/validate_control_plane.py`, `scripts/validate_public_ci_policy.py`, `scripts/validate_public_metadata_surfaces.py`, `scripts/sync_github_metadata.py`, `scripts/validate_mcp_version_parity.py`, `scripts/validate_adapter_health.py`, `scripts/validate_skill_catalog.py`, `scripts/validate_surface_adoption_matrix.py`, `scripts/validate_owner_full_auto_policy.py`, `scripts/validate_all.py`, `scripts/validate_ci_state.py`, `scripts/validate_fullrepo_sync.py`, `scripts/validate_instruction_pin_parity.py`, `scripts/validate_serena_runtime_markers.py`, `scripts/validate_release_version_policy.py`, `scripts/validate_github_releases.py`, `scripts/validate_serena_memory_semantics.py`, `scripts/bump_adapter_versions.py`, `scripts/release_orchestrator.py`, and the release archive hygiene scripts. MCP version parity includes native source/runtime format metadata; adapter health delegates high-signal adapter checks. `validate_fullrepo_sync.py` is the local/release gate for root and adapter `fullrepo` overlays; the static lane uses a source-only CI fallback through `validate_ci_state.py --fullrepo-ref refs/remotes/origin/fullrepo` when agent-only files are not restored. `sync_github_metadata.py --apply` writes configured GitHub descriptions, homepages, and topics. `release_orchestrator.py --apply --push --owner-approved` is the owner-approved automated path for adapter version bumps, commits, numeric tags, GitHub Release waits, root submodule sync, root validation, root commit, and root push.
- Root maintenance skills live in `skills/catalog.json`; generated canonical/projection skill files and runtime discovery bridges under `.claude/skills`, `.agents/skills`, and `.opencode/skills` are validated by `scripts/generate_skill_projection.py --check` and `scripts/validate_skill_runtime_discoverability.py`.
- Adapter skill descriptions share one canonical description shape (russian-first noun lead, 'Используй для:' use-cases, EN triggers) with routing-term coverage proven by the Codex routing suite.
- Root maintenance skill descriptions and adapter invocation metadata are Russian-first with English trigger suffixes so Russian owner prompts activate tools consistently in Claude Code, Codex, OpenCode, Gemini CLI, and MiMoCode.
- Memory-domain bootstrap/check script `scripts/sync_serena_memory_domains.py`.

It does not own adapter implementation source. Make implementation changes in the relevant adapter repository, then update the submodule pin here.

Canonical author metadata across the control plane and adapter manifests is `Danil Silantyev (github:rldyourmnd), CEO NDDev`. The control plane and all first-party adapter repositories use `AGPL-3.0-or-later`.

## Submodules

- `modules/rldyour-claudecode`: Claude Code configuration repo, pinned to `203f30db5454d840c5236add85c0d201416e9189` (`1.5.1`) on `main`.
- `modules/rldyour-codex`: Codex configuration/runtime repo, pinned to `fc4f792e2366858e2ee40d23ec0f2e2ea61d4051` (`1.5.1`) on `main`.
- `modules/rldyour-opencode`: OpenCode configuration repo, pinned to `850ed67775b122779ed0343723820f14352c691a` (`1.5.1`) on `main`.
- `modules/rldyour-antigravity-cli`: Antigravity CLI configuration repo, pinned to `aac43c337caed1762f23209bcdf2c5ed68205b2d` (`1.5.2`) on `main`.
- `modules/rldyour-mimocode`: MiMoCode configuration repo, pinned to `8cf8400bae3ed958e62d528ee028e7721dbfa830` (`1.5.1`) on `main`.

Current owner runtime policy:

- YOLO mode, full-auto mode, and dangerously-skip-permissions mode are the standard posture across adapters.
- Claude records this as `runtime_policy.id = "owner-full-auto-standard"` in its adapter contract.
- Codex default install is `rldyour-yolo` with `approval_policy = "never"` and `sandbox_mode = "danger-full-access"` using the legacy sandbox dialect; it must not write an active `default_permissions` permission-profile field while `sandbox_mode` is present. `--safe-mode` is the explicit conservative override.
- OpenCode top-level, `build`, and `plan` primary permissions intentionally allow the canonical v1.17.6 permission keys, including `read`, `edit`, `bash`, `task`, `external_directory`, and `doom_loop`, for the trusted owner workstation; reviewer subagents remain read-only by role.
- OpenCode `/ry-sync` is mapped as canonical manual sync, not adapter-only behavior.
- Root owner launchers are installed with `scripts/install_yolo_launchers.sh --apply`: `cx` wraps Codex YOLO/full-access, `cl` wraps Claude Code `--dangerously-skip-permissions`, and `oc` wraps OpenCode with runtime `OPENCODE_CONFIG_CONTENT` permission overrides plus `OPENCODE_DISABLE_CLAUDE_CODE=1` so root skill resolution uses `.opencode/skills`.
- MiMoCode is a native adapter with `.mimocode` config, build/plan/compose agents, persistent memory projection, commands, skills, MCP, browser routing, and worker-only cmux integration. Its compose/subagent/background features are not rldyour cmux orchestrator mode.
- `standard` execution mode is the direct-agent default for macOS, Linux, WSL, and Windows. In standard mode, no agent orchestrates other sessions; the owner/user remains the vision and orchestration layer and works directly through the selected Claude Code, Codex, OpenCode, Gemini CLI, or MiMoCode configuration. macOS cmux `orchestrator` mode is opt-in through project policy or `/ry-repair --os macos --mode orchestrator --cmux`; workers report to the orchestrator and must not push, publish fullrepo, delete branches, mutate project policy, run system installs, or run final sync unless explicitly delegated.

Current release policy:

- Public adapter releases are tag-driven. A `VERSION` file or root product-version entry is not enough; each current public adapter product version must have a matching numeric GitHub Release.
- Default version movement is patch: after a public GitHub Release exists, any later adapter source, config, or documentation change prepares `+0.0.1`.
- Minor (`+0.1.0`) and major (`+1.0.0`) bumps are owner-directed decisions only.
- Use `python3 scripts/release_orchestrator.py --only-changed --apply --push --owner-approved --summary "..."` for the owner-approved automated release path. It prepares synchronized adapter version files, commits adapter changes, creates and pushes numeric tags, waits for adapter GitHub Releases, advances root submodule pins, validates the control plane, commits root, and pushes the root branch.

## Claude Code Workflow Notes

This is a control-plane repository, not a Claude Code plugin marketplace itself. The Claude Code adapter implementation lives in `modules/rldyour-claudecode`.

Use the repository docs and Serena memories for context:

- `docs/control-plane.md`
- `docs/submodule-workflow.md`
- `docs/ry-repair-sync.md`
- `docs/os-install-matrix.md`
- `docs/cmux-orchestrator-mode.md`
- `docs/orchestrator-worker-protocol.md`
- `docs/audit-resolution.md`
- `docs/adr/README.md`
- `docs/adr/0001-owner-full-auto-standard.md`
- `docs/adr/0002-clean-atomic-history-standard.md`
- `docs/yolo-launchers.md`
- `.serena/memories/CORE-01-INDEX.md`

Do not reduce this file to an `@AGENTS.md` import. Claude Code should be able to understand the repository purpose, module boundaries, and validation commands directly from this memory.

## Validation

Run:

```bash
python3 scripts/validate_control_plane.py
python3 scripts/validate_public_ci_policy.py
python3 scripts/validate_github_metadata.py
python3 scripts/validate_public_metadata_surfaces.py
python3 scripts/sync_github_metadata.py
python3 scripts/validate_instruction_pin_parity.py
python3 scripts/validate_serena_runtime_markers.py
python3 scripts/validate_contract_parity.py
python3 scripts/validate_runtime_baselines.py
python3 scripts/validate_flow_parity.py
python3 scripts/validate_mcp_parity.py
python3 scripts/validate_mcp_version_parity.py
python3 scripts/validate_adapter_health.py
python3 scripts/validate_skill_catalog.py
python3 scripts/generate_skill_projection.py --check
python3 scripts/validate_skill_runtime_discoverability.py
python3 scripts/validate_templates.py
python3 scripts/validate_surface_adoption_matrix.py
python3 scripts/validate_owner_full_auto_policy.py
python3 scripts/validate_all.py --lane static-only --global-timeout 180 --json dist/gates/static-only.json --stream
python3 scripts/validate_release_version_policy.py
python3 scripts/validate_github_releases.py
python3 scripts/bump_adapter_versions.py --dry-run --level patch --summary "Verified patch release."
python3 scripts/validate_bilingual_descriptions.py
python3 scripts/validate_active_unreleased_claims.py --scope all
python3 scripts/validate_reference_metadata_versions.py --scope all
python3 scripts/validate_memory_taxonomy.py
python3 scripts/validate_memory_evidence.py
python3 scripts/validate_memory_freshness.py
python3 scripts/validate_serena_memory_schema.py
python3 scripts/validate_serena_memory_semantics.py
python3 scripts/validate_policy_contracts.py
python3 scripts/validate_os_install_policy.py
python3 scripts/validate_cmux_orchestrator_config.py --scope templates --strict
python3 scripts/release_orchestrator.py --plan --only-changed --json /tmp/rldyour-release-plan.json
python3 scripts/sync_serena_memory_domains.py --memory-ref fullrepo
python3 scripts/validate_fullrepo_sync.py --scope all --require-adapter-fullrepo --strict --timeout 20
python3 scripts/validate_ci_state.py --fullrepo-ref fullrepo
bash -n scripts/install_yolo_launchers.sh
scripts/build_release_archive.sh
python3 scripts/validate_release_archive.py dist/rldyour-ai-cli-tools.zip
scripts/build_source_audit_archive.sh
python3 scripts/validate_source_archive_hygiene.py --mode source-archive dist/rldyour-ai-cli-tools-source-audit.zip
python3 -m py_compile scripts/*.py
git diff --check && git diff --cached --check
actionlint .github/workflows/validate.yml
git submodule status --recursive
```

Run `validate_ci_state.py` only after normal `HEAD` and local `fullrepo` are synchronized.

If `actionlint` is not installed, report that the workflow lint was unavailable.

The adapter repositories are public and use standard GitHub-hosted runners for
zero paid private-repository Actions minutes. Root CI is private and must stay
lightweight: one Ubuntu job, no dependency installation, no cache, no artifacts,
and no heavy matrix unless the owner explicitly changes the policy.

## Agent-Only And Fullrepo

Root `AGENTS.md`, `.claude/CLAUDE.md`, `.serena/project.yml`, `.serena/memories/`, and `.serena/newproj/` are agent-only context for this repository. Generated root maintenance skill bridges under `.claude/skills`, `.agents/skills`, and `.opencode/skills` are product artifacts and stay in normal history. Normal `main` history should not carry the agent-only files once `fullrepo` is initialized.

Use the installed rldyour-flow fullrepo script:

```bash
python3 ${CODEX_HOME:-$HOME/.codex}/plugins/cache/rldyour-codex/rldyour-flow/local/scripts/fullrepo_sync.py --status-json
python3 ${CODEX_HOME:-$HOME/.codex}/plugins/cache/rldyour-codex/rldyour-flow/local/scripts/fullrepo_sync.py --migrate-main
python3 ${CODEX_HOME:-$HOME/.codex}/plugins/cache/rldyour-codex/rldyour-flow/local/scripts/fullrepo_sync.py --publish
```

Publishing pushes `fullrepo` to `origin` with safe force-with-lease.

Memory domain rules:

- Root required memory domains are the union of `universal_domains`, `control_plane_domains`, and `adapter_domains` from `config/rldyour-system-contract.json`.
- Adapter memory sets require `adapter_required_domains` plus the adapter-specific domain from `adapter_specific_domains`.
- Project-specific domains are proposed only when current code/config evidence proves they are durable.
- Do not create memory domains from chat phrasing alone.
- After adapter fullrepo context is restored locally, run `python3 scripts/sync_serena_memory_domains.py --include-adapters` before publishing memory-domain changes.

## Git History

- Use Conventional Commits.
- Commits and PRs are sole-authored by Danil Silantyev (github:rldyourmnd). Do
  NOT add `Co-Authored-By:` trailers (including Claude) or a "Generated with
  Claude Code" line. Claude Code keeps `includeCoAuthoredBy: false`; this
  overrides any agent default that would add a co-author trailer.
- Keep history logical and inspectable: split unrelated implementation, tests,
  validators, docs/instructions, license/metadata, generated artifacts, and
  Serena/fullrepo sync into separate commits when they are independently
  reviewable.
- Do not rewrite already-pushed history without explicit owner approval; use a
  follow-up commit for published branches.
- Advance submodule gitlinks only after the adapter repository commit is pushed.

## Current Module Tuple

- `rldyour-claudecode` (`modules/rldyour-claudecode`) -- `main` at `203f30db5454d840c5236add85c0d201416e9189` (`1.5.1`)
- `rldyour-codex` (`modules/rldyour-codex`) -- `main` at `fc4f792e2366858e2ee40d23ec0f2e2ea61d4051` (`1.5.1`)
- `rldyour-opencode` (`modules/rldyour-opencode`) -- `main` at `850ed67775b122779ed0343723820f14352c691a` (`1.5.1`)
- `rldyour-antigravity-cli` (`modules/rldyour-antigravity-cli`) -- `main` at `aac43c337caed1762f23209bcdf2c5ed68205b2d` (`1.5.2`)
- `rldyour-mimocode` (`modules/rldyour-mimocode`) -- `main` at `8cf8400bae3ed958e62d528ee028e7721dbfa830` (`1.5.1`)
