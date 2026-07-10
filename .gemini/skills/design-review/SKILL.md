---
name: design-review
description: "Проведи дизайн/visual review через управляемый CloakBrowser boundary. EN: review design implementation with managed browser evidence."
---

# Purpose

Evaluate visual implementation against Figma, screenshots, reference images,
or written specifications.

# Native Antigravity Boundary

## Mandatory CloakBrowser Boundary

This boundary applies before every browser action:

1. Run exactly:

   ```bash
   $HOME/.local/bin/cloakbrowser-cdp-health
   ```

   If the command is missing or exits nonzero, stop immediately and report `NOT_PROVEN`.
2. Browser execution is permitted only through:
   - the exact `$HOME/.local/bin/playwright-cli` executable; `run-code` and `--filename` are forbidden;
   - the approved Chrome DevTools MCP transport, exactly `/bin/sh -c 'exec "$HOME/.local/bin/chrome-devtools-mcp" --headless --isolated --no-usage-statistics --no-performance-crux'`.
3. Never execute the Webwright Python runtime, stock/raw/in-app Browser, `browser_agent`, `node_repl`, computer-use, Playwright MCP, raw Playwright, `bunx`, `npx`, direct package invocations, alternate CDP endpoints, alternate browser executables, alternate browser configs, or any fallback. No fallback is allowed.

`webwright-task` is compatibility intent routed to `browser:validate`; it never
authorizes Webwright runtime execution.

# When To Use

Use for Figma-to-code review, responsive visual checks, typography, color/token,
layout, and accessibility deviations.

# Inputs

Expected source, target URL, viewport matrix, dynamic masks, and thresholds.

# Procedure

Use Figma MCP for the expected source, managed Playwright CLI for actual
screenshots and responsive evidence, and managed Chrome DevTools MCP for
DOM/runtime diagnosis. Rerun health immediately before each browser action.

# Evidence Required

Report expected source, exact artifact paths, masks, thresholds, pixel/layout,
typography/token/accessibility deviations, confidence, and `NOT_PROVEN` gaps.

# Forbidden Actions

Do not approve visual quality without artifacts or bypass the browser boundary.

# Acceptance Checks

Run `python3 scripts/validate_gemini_browser_routing.py --strict`.

# Failure Reporting

Report each mismatch with source, viewport, severity, evidence, and any
`NOT_PROVEN` state.
