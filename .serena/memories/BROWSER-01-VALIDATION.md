<!-- Memory Metadata
Last updated: 2026-07-10
Last verified: 2026-07-10
Last commit: c74adf6766b1fb1c88c019d20f78dab65ae5e932 feat(browser): enforce managed CloakBrowser skill boundary
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
- commit: `c74adf6766b1fb1c88c019d20f78dab65ae5e932`
- checked by: Antigravity fail-closed browser policy validation

## Facts
- Every browser action first runs exact
  `$HOME/.local/bin/cloakbrowser-cdp-health`; missing or nonzero health stops as
  `NOT_PROVEN` with no fallback.
- Active browser execution is limited to exact managed Playwright CLI and the
  exact managed Chrome DevTools MCP transport. `run-code` and `--filename` are
  forbidden.
- `webwright-task` is compatibility intent routed through `browser:validate`.
  Webwright runtime, built-in/raw browser surfaces, direct packages, alternate
  CDP/executable/config paths, and fallbacks are forbidden.
- Both browser skills, both browser-aware agents, and both browser commands
  carry the exact mandatory boundary and match their `.gemini` projections.

## Evidence
- `commit:c74adf6766b1fb1c88c019d20f78dab65ae5e932`
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
