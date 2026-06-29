# Security Policy

## Supported Versions

Only the current exact numeric product release tag receives security fixes. The
`1.7.x` line label tracks only the latest released patch, not every historical
patch in the line. Development snapshots and older tags are not supported unless
the root control plane explicitly pins them.

| Version | Supported |
| --- | --- |
| Current exact tag `1.7.9` | yes |
| Older minor / major lines | no |

## Secrets

Do not commit Antigravity API keys, Google API keys, OAuth material, service-account
JSON, Google Cloud ADC files, cookies, browser profile state, or MCP provider
tokens. `.env.example` documents accepted local variable names; real values must
remain local and ignored.

## Runtime Posture

Committed Antigravity project settings use the `auto_edit` approval mode: the maximal
owner-autonomy posture that Antigravity CLI accepts in committed config (it
auto-approves edits without prompting). Full shell-command YOLO flags are
`NOT_PROVEN` until the installed-runtime lane verifies the current `agy --help`
contract, so launchers must not claim unverified legacy approval semantics.
Unverified `yolo` values must never be written into committed settings.

## Reporting

Report security issues privately through GitHub security advisories for
`NDDev-it-com/rldyour-antigravity-cli`.
