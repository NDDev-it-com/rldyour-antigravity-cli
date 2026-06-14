# Gemini Antigravity Transition

## Current Fact

Gemini adapter `1.4.0` has migrated primary runtime to Antigravity CLI `1.0.8`.
The adapter now targets Antigravity CLI as the primary runtime while maintaining
backward compatibility with Antigravity CLI `0.46.0` for enterprise users.

## Migration Status: MIGRATED

Google transitioned unpaid and Google One Antigravity CLI users to Antigravity CLI
on `2026-06-18`. Enterprise Standard/Enterprise license holders retain access
to Antigravity CLI.

## Antigravity CLI Details

- Binary: `antigravity-cli`
- Install: `curl -fsSL https://antigravity.google/cli/install.sh | bash`
- Config path: `~/.gemini/antigravity-cli/settings.json`
- MCP config: `~/.gemini/antigravity-cli/mcp_config.json`
- Hooks: `~/.gemini/config/hooks.json` (shared with Antigravity CLI)
- GitHub: `https://github.com/google-antigravity/antigravity-cli`
- Latest version: `1.0.8`

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
