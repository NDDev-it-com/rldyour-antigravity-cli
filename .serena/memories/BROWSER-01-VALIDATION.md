<!-- Memory Metadata
Last updated: 2026-07-10
Last verified: 2026-07-10
Last commit: eaed204f9dac5b022f62bb673e36a0b96d915cdc feat(browser): enforce managed Cloak routing
Scope: browser-visible validation and debugging workflows
Area: BROWSER
-->

# BROWSER-01-VALIDATION

## Purpose
Maintain durable Antigravity CLI adapter knowledge for `BROWSER-01-VALIDATION`.

## Current Facts
- Current facts are recorded in the source-of-truth, facts, and evidence sections below.

## Operational Rules
- Current code, configuration, tests, and live runtime evidence override stale memory text.
- Keep this memory fact-only and update it after verified Antigravity adapter changes.

## Last Verified
2026-07-10


## Scope
browser-visible validation and debugging workflows

## Current source of truth
- `path:README.md`
- `path:config/browser-provider-policy.json`
- `path:references/browser-provider-routing.md`
- `path:scripts/gemini_contract.py`

## Last verified
- date: 2026-07-10
- commit: `eaed204f9dac5b022f62bb673e36a0b96d915cdc`
- checked by: Antigravity browser transport release validation

## Facts
- Webwright, Playwright CLI, and Chrome DevTools MCP must attach to the bootstrap-owned CloakBrowser backend.
- The only configured browser MCP transport is `/bin/sh -c` executing `~/.local/bin/chrome-devtools-mcp` with the managed privacy flags.
- Direct `bunx`/`npx` Chrome DevTools package transport and raw, stock, or in-app browser fallback are forbidden.

## Evidence
- `commit:eaed204f9dac5b022f62bb673e36a0b96d915cdc`
- `path:README.md`
- `path:config/browser-provider-policy.json`
- `path:references/browser-provider-routing.md`
- `path:tests/test_gemini_browser_routing.py`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.
