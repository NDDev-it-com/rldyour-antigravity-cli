# AGENTS.md

## Purpose

This repository is the Antigravity CLI-native rldyour adapter. Repository
artifacts are English. Owner-facing conversation in connected agents remains
Russian unless explicitly requested otherwise.

## Source Of Truth

- `VERSION`: adapter product version.
- `GEMINI.md`: Antigravity CLI context file.
- `.gemini/antigravity-cli/settings.json`: Antigravity project settings.
- `.gemini/antigravity-cli/mcp_config.json`: Antigravity MCP server config.
- `gemini-extension.json`: extension manifest and extension MCP inventory.
- `.gemini/commands/`: Antigravity TOML custom commands.
- `.gemini/skills/`: Antigravity Agent Skills.
- `.gemini/agents/`: Antigravity subagent definitions.
- `.gemini/hooks/`: synchronous bounded Antigravity hooks.
- `.gemini/policies/`: policy extension data.
- `config/rldyour-contract.json`: adapter contract consumed by the root control plane.
- `config/gemini-baseline.json`: runtime baseline and source-of-truth policy.
- `references/`: durable native-boundary, browser, release, and auth documentation.
- `.serena/memories/`: fact-only durable adapter memory.

## Native Boundary

Use Antigravity CLI-native surfaces. Do not copy Claude slash commands, Codex plugin
manifests, or OpenCode command JSON as runtime surfaces. Comparison notes are
allowed only in documentation when they clarify boundaries.

## MCP Policy

The active MCP inventory is exactly 11 servers: Serena, Chrome DevTools,
Sequential Thinking, shadcn, Dart/Flutter, Context7, GitHub, DeepWiki, Grep,
Figma, and OpenAI Docs. Aliases are dash-separated and must not contain
underscores. Configure only providers listed in the approved active inventory.
Removed or historical tools must not be reintroduced unless the owner updates
the inventory and release policy.

`config/mcp-runtime-versions.env` owns package pin literals. Sequential
Thinking is `2026.7.4` and Context7 is `3.2.3`; `gemini-extension.json`, both
`.gemini` runtime MCP surfaces, contract claims, docs, and tests must remain in
exact parity.

## Browser Policy

Before every browser action, run exact
`$HOME/.local/bin/cloakbrowser-cdp-health`; missing or nonzero health stops as
`NOT_PROVEN`. Execute only exact `$HOME/.local/bin/playwright-cli` or the exact
managed `$HOME/.local/bin/chrome-devtools-mcp` transport in project
configuration. `run-code` and `--filename` are forbidden.

`webwright-task` is compatibility intent routed to `browser:validate`; the
Webwright runtime is retired fail-closed. Stock/raw/in-app Browser,
`browser_agent`, `node_repl`, computer-use, Playwright MCP, raw Playwright,
direct browser packages, alternate CDP/executable/config paths, and all
fallbacks are forbidden. See `references/browser-provider-routing.md`.

## cmux Boundary

Antigravity may run as a visible cmux worker terminal or, when explicitly selected by
the owner, as a visible cmux orchestrator terminal. Antigravity subagents and
headless `antigravity-cli -p` smoke prompts are not cmux orchestration and must not become
background, headless, daemon, or detached orchestrator processes.

## Validation

Run repository-local validators for changed scope. Do not fake green checks.
Installed-runtime checks are optional and require explicit local authentication.

## CI runner selection

Every workflow run is evidence and must finish. Use a concurrency group unique
to `github.run_id` and `cancel-in-progress: false`; never discard a queued or
running check as superseded.

This repository is public, so `pull_request` executes untrusted fork code.
Every caller of a `NDDev-OpenNetwork/ci-workflows` reusable that exposes a `runner`
input passes `runner: ubuntu-latest` explicitly, and must keep it. Several of
those reusables default `runner` to the estate's self-hosted `amsterdam`
label, and a default is a property of the **pinned commit**, not of this
repository — so dropping the explicit value would let a routine pin bump route
fork PRs onto trusted private infrastructure with no diff here to review. On
any ci-workflows pin bump, diff `inputs.runner.default` between the old and
new commit before merging.
