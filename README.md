# rldyour-antigravity-cli

`rldyour-antigravity-cli` is the Antigravity CLI-native configuration adapter for the rldyour AI CLI control plane. It provides a public, source-validated Antigravity CLI configuration using native surfaces: `GEMINI.md`, `.gemini/antigravity-cli/settings.json`, `.gemini/antigravity-cli/mcp_config.json`, `gemini-extension.json`, TOML commands, skills, subagents, hooks, policies, MCP servers, browser-provider routing, Serena memory, and release validation.

## Current Baseline

| Surface | Value |
| --- | ---: |
| Adapter version | `1.7.33` |
| Runtime baseline | Antigravity CLI `1.1.1` |
| Runtime channel | bootstrap-owned generation-pinned artifact |
| GitHub release tag | `1.7.33` |

Antigravity CLI freshness uses `agy --version` as the primary
source of truth, with the GitHub release tag as release provenance.
The pinned commit and product version are governed by the root control plane
`config/repositories.json`.

## What This Repository Provides

This repository is a configuration package for Antigravity CLI, not a fork or
copy of the upstream runtime. It wires together
the native Antigravity CLI configuration surfaces - context files, project
settings, MCP config, extension manifest, TOML commands, Agent Skills,
subagents, hooks, policies, and MCP servers - into a coherent,
version-controlled, owner-validated setup. The upstream Antigravity CLI binary
is installed separately via the official installer and is not modified here.
All changes in this repository are configuration and adapter logic; runtime
behavior is governed by the installed `agy` binary version.

## Native Boundaries

Antigravity runtime configuration is represented through Antigravity native
files only; `.gemini/`, `GEMINI.md`, and `gemini-extension.json` are native
namespace filenames retained for Antigravity compatibility.
Claude Code slash-command files, Codex plugin manifests, and OpenCode command
JSON are not Antigravity runtime surfaces and are not present here.

Active native surfaces:

- `GEMINI.md` - repository context injected at session start.
- `.gemini/settings.json` - project settings, hook wiring, and MCP server
  declarations.
- `gemini-extension.json` - extension metadata and extension MCP wiring.
- `.gemini/commands/**/*.toml` - custom commands (13 TOML files across browser,
  flow, release, ry, security, and serena groups).
- `.gemini/skills/*/SKILL.md` - Agent Skills (14 skills).
- `.gemini/agents/*.md` - Antigravity subagents (7 agents: browser-reviewer,
  codebase-investigator, design-reviewer, antigravity-cli-specialist,
  release-reviewer, security-reviewer, serena-curator).
- `.gemini/hooks/` - native hook scripts for SessionStart, BeforeTool,
  AfterAgent, and SessionEnd events.
- `.gemini/policies/*.toml` - policy extension data.

Hooks use the native event-keyed schema: read JSON from stdin, write exactly
one JSON object to stdout, and send diagnostics to stderr. Antigravity subagents
are internal Antigravity CLI delegation and are not cmux worker terminals.
Headless `agy -p` is allowed for smoke, doctor, and CI checks only.

## Install / Update / ry-repair

Install the runtime through the parent bootstrap's verified artifact channel:

```bash
bash scripts/bootstrap.sh --platform <macos|ubuntu> --profile <desktop|server> --apply
agy --version
```

The bootstrap verifies the platform artifact digest, verifies the macOS signer
where applicable, disables self-update, and publishes a tamper-evident
`~/.local/bin/agy` launcher. This adapter never executes a streamed remote
installer.

Clone or update this adapter:

```bash
# First time
git clone https://github.com/NDDev-it-com/rldyour-antigravity-cli.git
cd rldyour-antigravity-cli

# Update to latest
git pull origin main
```

Run `/ry-repair` convergence from within a Antigravity CLI session to normalize
adapter configuration, validate surface adoption, and sync Serena memories.
For offline or check-only mode, run the static validation lane (see
`## Validation`). Runtime doctor:

```bash
agy --version
agy -p 'Return exactly READY.' --output-format json
```

The installed-runtime smoke checks require a deliberately configured owner
machine with valid authentication.

## Active Catalog

| Surface | Count |
| --- | ---: |
| Agent Skills (`.gemini/skills/*/SKILL.md`) | 14 |
| TOML commands (`.gemini/commands/**/*.toml`) | 13 |
| Antigravity subagents (`.gemini/agents/*.md`) | 7 |
| Hook scripts (`.gemini/hooks/`) | 4 |
| MCP servers (`.gemini/settings.json`) | 11 |

Active MCP inventory: `serena`, `chrome-devtools`, `sequential-thinking`,
`shadcn`, `dart-flutter`, `context7`, `github`, `deepwiki`, `grep`, `figma`,
and `openai-docs`.

Commands are grouped into: `browser`, `flow`, `release`, `ry`, `security`, and
`serena`. Hooks cover `SessionStart`, `BeforeTool`, `AfterAgent`, and
`SessionEnd` events.

## Browser / Design / DevTools Routing

Browser work has exactly two execution providers behind the bootstrap-owned
CloakBrowser boundary. Every browser action first runs exact
`$HOME/.local/bin/cloakbrowser-cdp-health`; missing or nonzero health stops as
`NOT_PROVEN`, with no fallback:

- **Managed Playwright CLI** (`$HOME/.local/bin/playwright-cli`, runtime
  `0.1.17`) - flows, screenshots, snapshots, traces, responsive matrices,
  visual evidence, and long-horizon stepwise workflows. `run-code` and
  `--filename` are forbidden.
- **Managed Chrome DevTools MCP** (`chrome-devtools`, runtime `1.5.0`) -
  console, network, runtime, DOM/layout, performance, Lighthouse, and memory
  through the exact configured wrapper.

`webwright-task` is compatibility intent routed to `browser:validate`; it never
authorizes Webwright runtime execution. Stock/raw/in-app Browser,
`browser_agent`, `node_repl`, computer-use, Playwright MCP, raw Playwright,
direct browser packages, alternate CDP/executable/config paths, and every
fallback are forbidden.

### MCP Inventory Detail

The active MCP inventory matches the root positive inventory. All 11 servers are
declared in `.gemini/settings.json` under `mcpServers`:

| Server | Transport | Role |
| --- | --- | --- |
| `serena` | stdio (`uvx`) | LSP-based code intelligence and Serena memory |
| `chrome-devtools` | stdio (managed `$HOME/.local/bin/chrome-devtools-mcp` wrapper) | CloakBrowser live debugging and DevTools |
| `sequential-thinking` | stdio (`bunx`) | Structured reasoning chains |
| `shadcn` | stdio (`bunx`) | shadcn/ui component registry |
| `dart-flutter` | stdio (`dart`) | Dart/Flutter LSP and pub tools |
| `context7` | stdio (`bunx`) | Library documentation lookup |
| `github` | HTTP/SSE | GitHub repos, issues, pull requests |
| `deepwiki` | HTTP/SSE | AI-powered repository documentation |
| `grep` | HTTP/SSE | Cross-repository code search |
| `figma` | HTTP (local) | Figma design context and code connect |
| `openai-docs` | HTTP/SSE | OpenAI API documentation |

Current refreshed package pins are
`@modelcontextprotocol/server-sequential-thinking@2026.7.4` and
`@upstash/context7-mcp@3.2.3`. `config/mcp-runtime-versions.env` owns their
version literals; all three active Antigravity MCP surfaces and
`config/rldyour-contract.json` must remain exact projections of those pins.

## Repository Context / Serena Memory

Normal `main` history carries source-controlled configuration artifacts:
`.gemini/` surfaces, `config/`, `references/`, `scripts/`, tests, and
`CHANGELOG.md`. Durable agent context files - `AGENTS.md`, `GEMINI.md`,
`.serena/project.yml`, and `.serena/memories/` - are tracked on `main` as
normal source. Runtime-local Serena cache, review scratch files, diagnostics,
markers, local state, tokens, cookies, and credentials stay ignored.

Serena memory domains active for this adapter:

- `CORE-01-INDEX` - durable memory index.
- `GEMINI-01-ADAPTER-SURFACE` - native surface facts.
- `RUNTIME-01-BASELINE` - pinned runtime version evidence.
- `MCP-01-TOOLS` - MCP inventory facts.
- `BROWSER-01-VALIDATION` - browser provider routing rules.
- `FLOW-01-SDLC` - SDLC flow rules.
- `SECURITY-01-POSTURE` - security posture facts.
- `RELEASE-01-VALIDATION` - release validation rules.
- `SERENA-01-MEMORY-SYNC` - memory maintenance rules.
- `ANTIGRAVITY-01-TRANSITION` - Antigravity transition notice.

Memories store durable facts only (Purpose, Current Facts, Evidence, Operational
Rules, Last Verified). Chat logs, speculation, secrets, tokens, cookies, and
credentials must not be stored.

Freshness contract: re-verify memories after each adapter release and after any
upstream Antigravity CLI version change. Memory updates are committed with the
source change that makes their facts true.

## Security Boundary

### Approval Mode and YOLO

Committed `.gemini/settings.json` sets `general.defaultApprovalMode =
"auto_edit"` - the maximal owner-autonomy posture that Antigravity CLI accepts in
committed configuration. `auto_edit` auto-approves file edits without prompting.
`security.disableYoloMode = false` and `security.toolSandboxing = false` are set
explicitly to preserve the maximal committed owner-autonomy posture currently
proven for Antigravity CLI.

Full shell-command YOLO flags for Antigravity CLI are `NOT_PROVEN` until the
installed-runtime lane verifies the current `agy --help` contract. Do not copy
retired legacy runtime `--approval-mode=yolo` semantics into Antigravity
launchers or docs. Writing an unverified `yolo` value into committed settings
has no effect and must not be done.

Permissions are not a sandbox. This adapter is designed for an owner workstation
with owner-trusted tools and reviewed MCP servers. It is not suitable as-is for
untrusted multi-user or production environments.

### Secrets

Do not commit Antigravity, Google model, or Google API keys, OAuth material,
service-account JSON, Google Cloud ADC files, cookies, browser profile state, or
MCP provider tokens. `.env.example` documents accepted local variable names;
real values must remain local and git-ignored.

### MCP Trust Boundary

All 11 active MCP servers are owner-reviewed. HTTP/SSE servers (`github`,
`deepwiki`, `grep`, `openai-docs`) use remote endpoints with env-var tokens
where required. The `figma` server runs locally at `127.0.0.1:3845`. No
unapproved third-party MCP server may be added without an explicit inventory and
release-policy update.

### Access and Antigravity Notice

Antigravity CLI adapter `1.7.33` targets enterprise, paid API-key, Vertex AI, Google
Cloud, and explicitly owner-approved authenticated environments. Consumer OAuth
availability after June 18, 2026 is `NOT_PROVEN` for this adapter because
legacy runtime support is retired for active use in this adapter. See
`references/gemini-antigravity-transition.md`.

## Validation

Static validation (no runtime required):

```bash
python3 scripts/validate_gemini_config.py --strict
python3 scripts/validate_gemini_extension_manifest.py --strict
python3 scripts/validate_gemini_commands.py --strict
python3 scripts/validate_gemini_skills.py --strict
python3 scripts/validate_gemini_subagents.py --strict
python3 scripts/validate_gemini_hooks.py --strict
python3 scripts/validate_gemini_mcp_inventory.py --strict
python3 scripts/validate_gemini_browser_routing.py --strict
python3 scripts/validate_gemini_runtime_baseline.py --strict
python3 scripts/validate_instruction_docs.py --strict
python3 scripts/validate_serena_memory_schema.py --strict
python3 scripts/validate_serena_memory_semantics.py --strict
python3 -m pytest -q
```

Installed-runtime smoke checks (optional; require a deliberately configured
owner machine with valid authentication):

```bash
agy --version
agy -p 'Return exactly READY.' --output-format json
```

The `NOT_PROVEN` policy applies to any validation result that cannot be
confirmed through local static analysis alone (e.g., live MCP connectivity,
consumer OAuth availability after June 18, 2026).

## Release / Rollback

Releases follow the root control plane numeric tag policy. A `VERSION` file
alone is not a release: the GitHub Release and the numeric tag must point to the
same commit that the root pins in `config/repositories.json`.

- Default version movement is patch (`+0.0.1`) after any source, config, or
  documentation change post-release.
- Minor (`+0.1.0`) and major (`+1.0.0`) bumps are owner-directed decisions only.
- `CHANGELOG.md` documents all notable changes per release.
- `SECURITY.md` lists the currently supported version.
- Only the current exact numeric tag receives security fixes.

To roll back: check out the prior numeric tag, verify the root control plane
pins it in `expected_head`, and run the static validation lane.

## Support / License

License: `AGPL-3.0-or-later`.

Author: Danil Silantyev (github:rldyourmnd), CEO NDDev.

Repository: <https://github.com/NDDev-it-com/rldyour-antigravity-cli>

Report security issues privately through GitHub Security Advisories for
`NDDev-it-com/rldyour-antigravity-cli`. Do not open public issues for security
vulnerabilities.
