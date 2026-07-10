<!-- Memory Metadata
Last updated: 2026-07-10
Last verified: 2026-07-10
Last commit: c74adf6766b1fb1c88c019d20f78dab65ae5e932 feat(browser): enforce managed CloakBrowser skill boundary
Scope: MCP runtime transport and pin policy
Area: MCP
-->

# MCP-01-TOOLS

## Purpose
Maintain durable Antigravity CLI adapter knowledge for `MCP-01-TOOLS`.

## Current Facts
- Current facts are recorded in the source-of-truth, facts, and evidence sections below.

## Operational Rules
- Current code, configuration, tests, and live runtime evidence override stale memory text.
- Keep this memory fact-only and update it after verified Antigravity adapter changes.

## Last Verified
2026-07-10


## Scope
MCP runtime transport and pin policy

## Current source of truth
- `path:.gemini/antigravity-cli/mcp_config.json`
- `path:.gemini/settings.json`
- `path:gemini-extension.json`
- `path:config/mcp-runtime-versions.env`
- `path:scripts/gemini_contract.py`

## Last verified
- date: 2026-07-10
- commit: `c74adf6766b1fb1c88c019d20f78dab65ae5e932`
- checked by: Antigravity MCP transport and projection validation

## Facts
- The active inventory contains exactly 11 MCP servers and all three Antigravity MCP projections must remain byte-equivalent after normalization.
- Sequential Thinking is pinned to `@modelcontextprotocol/server-sequential-thinking@2026.7.4`; Context7 is pinned to `@upstash/context7-mcp@3.2.3`.
- npm metadata, stdio `initialize`, `tools/list`, safe-call, and an isolated `0 vulnerabilities` audit provide compatibility evidence for the refreshed pins.
- `chrome-devtools` uses `/bin/sh -c` to execute the bootstrap-owned
  `$HOME/.local/bin/chrome-devtools-mcp` wrapper; no direct package launcher is
  allowed.
- CloakBrowser identity, endpoint, health, and version remain owned by the bootstrap rather than this adapter.

## Evidence
- `commit:c74adf6766b1fb1c88c019d20f78dab65ae5e932`
- `path:.gemini/antigravity-cli/mcp_config.json`
- `path:config/mcp-runtime-versions.env`
- `path:docs/audit-resolution.md`
- `path:config/browser-provider-policy.json`
- `path:scripts/gemini_contract.py`
- `path:tests/test_gemini_mcp_inventory.py`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.
