---
name: browser-validation
description: "Проверь browser/UI поведение только через управляемые Playwright CLI и Chrome DevTools MCP. EN: validate browser behavior through CloakBrowser."
---

# Purpose

Collect deterministic evidence for browser flows, UI behavior, screenshots,
traces, runtime defects, and responsive states.

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

Use for browser flows, UI regressions, screenshots, traces, console/network
diagnosis, responsive checks, and visual evidence.

# Inputs

URL, preconditions, expected behavior, viewport matrix, and task objective.

# Procedure

Use the managed Playwright CLI for flows, screenshots, snapshots, traces,
responsive matrices, visual evidence, and long-horizon stepwise workflows. Use
the managed Chrome DevTools MCP transport for console, network, runtime,
DOM/layout, performance, Lighthouse, and memory diagnosis.

Run health again immediately before every browser action:

```bash
$HOME/.local/bin/cloakbrowser-cdp-health
$HOME/.local/bin/playwright-cli -s="${RY_PROJECT_SLUG:-rldyour}" open "$URL"
$HOME/.local/bin/cloakbrowser-cdp-health
$HOME/.local/bin/playwright-cli -s="${RY_PROJECT_SLUG:-rldyour}" snapshot
$HOME/.local/bin/cloakbrowser-cdp-health
$HOME/.local/bin/playwright-cli -s="${RY_PROJECT_SLUG:-rldyour}" screenshot
```

# Evidence Required

Report provider, URL/state, viewport matrix, exact artifact paths, findings,
confidence, and `NOT_PROVEN` gaps.

# Forbidden Actions

Do not bypass, weaken, or fall back from the mandatory boundary.

# Acceptance Checks

Run `python3 scripts/validate_gemini_browser_routing.py --strict`.

# Failure Reporting

Separate proven defects from `NOT_PROVEN` provider, health, or auth gaps.
