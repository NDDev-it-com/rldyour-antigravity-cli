<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: 56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c chore(release): prepare antigravity 1.7.1 tracked context
Scope: Antigravity CLI browser-provider routing
Area: BROWSER
-->

# BROWSER-01-VALIDATION

## Purpose

Record browser-provider routing for Gemini workflows.

## Current Facts

- Webwright handles high-level long-horizon browser workflows.
- Playwright CLI handles low-level UI automation, screenshots, snapshots,
  traces, and visual evidence.
- Chrome DevTools MCP handles console, network, performance, Lighthouse,
  memory, and live debugging.

## Evidence

- `config/browser-provider-policy.json`
- `references/browser-provider-routing.md`
- `.gemini/skills/browser-validation/SKILL.md`

## Operational Rules

- Configure only browser providers listed in the approved active inventory.
- Do not represent Webwright as an MCP server.

## Last Verified

2026-06-13

## Last verified
- date: 2026-06-25
- commit: `56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c`
- checked by: antigravity 1.7.1 tracked-context migration
