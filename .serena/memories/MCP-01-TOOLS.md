<!-- Memory Metadata
Last updated: 2026-07-10
Last verified: 2026-07-10
Last commit: eaed204f9dac5b022f62bb673e36a0b96d915cdc feat(browser): enforce managed Cloak routing
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
- `path:scripts/gemini_contract.py`

## Last verified
- date: 2026-07-10
- commit: `eaed204f9dac5b022f62bb673e36a0b96d915cdc`
- checked by: Antigravity MCP projection and transport validation

## Facts
- The active inventory contains exactly 11 MCP servers and all three Antigravity MCP projections must remain byte-equivalent after normalization.
- `chrome-devtools` uses `/bin/sh -c` to execute the bootstrap-owned `~/.local/bin/chrome-devtools-mcp` wrapper; no direct package launcher is allowed.
- CloakBrowser identity, endpoint, health, and version remain owned by the bootstrap rather than this adapter.

## Evidence
- `commit:eaed204f9dac5b022f62bb673e36a0b96d915cdc`
- `path:.gemini/antigravity-cli/mcp_config.json`
- `path:config/browser-provider-policy.json`
- `path:scripts/gemini_contract.py`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.
