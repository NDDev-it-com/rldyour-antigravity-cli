# Antigravity Runtime Transition

## Current Fact

Antigravity CLI adapter `1.7.11` targets Antigravity CLI `1.0.13` through the
`agy` command. Gemini CLI is retired as a supported runtime for this adapter.

## Migration Status: MIGRATED

Google transitioned unpaid and Google One users from Gemini CLI to Antigravity
CLI on `2026-06-18`. That historical product transition is recorded here only
as migration evidence; this adapter no longer installs, validates, or supports
Gemini CLI as an active runtime.

## Antigravity CLI Details

- Binary: `agy` (alias of `antigravity`)
- Install: `curl -fsSL https://antigravity.google/cli/install.sh | bash`
- Config path: `~/.gemini/antigravity-cli/settings.json`
- MCP config: `~/.gemini/antigravity-cli/mcp_config.json`
- Hooks: `.gemini/hooks/hooks.json` projected into the Antigravity native namespace
- GitHub: `https://github.com/google-antigravity/antigravity-cli`
- Latest version: `1.0.13`

## Supported Access Targets

- Enterprise (Gemini Code Assist Standard/Enterprise)
- Paid API-key
- Vertex AI
- Google Cloud
- Owner-approved authenticated environments

## Evidence

- `config/gemini-baseline.json`
- `references/authentication.md`
- Google developer update: `https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli`
- Antigravity CLI GitHub: `https://github.com/google-antigravity/antigravity-cli`
