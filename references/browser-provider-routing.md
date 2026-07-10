# Fail-Closed Browser Provider Routing

Antigravity inherits the bootstrap-owned CloakBrowser trust boundary. Every
browser action starts with exact `$HOME/.local/bin/cloakbrowser-cdp-health`.
Missing or nonzero health produces `NOT_PROVEN` and stops the workflow; no
fallback is allowed.

Exactly two execution providers are active:

- `$HOME/.local/bin/playwright-cli` `0.1.17` handles flows, screenshots,
  snapshots, traces, responsive matrices, visual evidence, and long-horizon
  stepwise workflows. `run-code`, `--filename`, raw Playwright, package-runner
  invocation, alternate executables, and alternate configs are forbidden.
- Chrome DevTools MCP `1.5.0` handles console, network, runtime, DOM/layout,
  performance, Lighthouse, and memory through the exact managed
  `$HOME/.local/bin/chrome-devtools-mcp` transport in Antigravity configuration.

`webwright-task` remains compatibility intent only. It routes through
`browser:validate`; Webwright runtime is never installed, imported, or run. Stock/raw/
in-app Browser, Antigravity `browser_agent`, `node_repl`, computer-use,
Playwright MCP, raw Playwright, direct browser packages, alternate CDP,
executables/configs, and all fallback paths remain forbidden.

`config/browser-provider-policy.json` is the machine-readable authority. The
source policy in `policies/rldyour-browser-routing.toml` is projected
byte-for-byte to `.gemini/policies/`. Browser skills, agents, and commands each
carry the exact mandatory boundary and are also projected byte-for-byte.
