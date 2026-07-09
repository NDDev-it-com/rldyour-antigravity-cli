# Browser Provider Routing

Use the shared rldyour provider model:

- Webwright: high-level long-horizon web workflows, reusable scripts,
  screenshots/logs/evidence, and final-script reproduction.
- Playwright CLI + Skills: deterministic UI automation, screenshots, snapshots,
  traces, responsive matrices, and visual evidence.
- Chrome DevTools MCP: console, network, performance, Lighthouse, memory, heap,
  and live Chrome debugging. Every Antigravity MCP surface invokes the exact
  `~/.local/bin/chrome-devtools-mcp` wrapper; the bootstrap owns CloakBrowser
  identity, the fixed endpoint, and its health gate. No stock-browser fallback
  is supported.

Gemini built-in `browser_agent` is disabled for this release. It is not a silent
replacement for any provider above and must be added as a separately validated
provider before use.

Current provider boundary:

- Configure only providers listed in the approved active inventory.
- Webwright remains a non-MCP provider/harness.
- Removed or historical tools require an explicit inventory and release-policy
  update before they can become active.
