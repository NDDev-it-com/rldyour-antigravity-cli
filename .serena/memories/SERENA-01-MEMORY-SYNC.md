<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: f031b9ecb437c92579b84aa967cc6d0d7b0cfe8c chore(release): antigravity 1.6.1
Scope: Antigravity CLI Serena memory rules
Area: SERENA
-->

# SERENA-01-MEMORY-SYNC

## Purpose

Record Serena memory maintenance rules.

## Current Facts

- Antigravity CLI memories use the standard Memory Metadata block plus durable
  fact sections such as Purpose, Current Facts, Evidence, Operational Rules,
  and Last Verified.
- Memories store durable facts only.

## Evidence

- `.serena/project.yml`
- `.serena/memories/CORE-01-INDEX.md`
- `.gemini/skills/serena-memory-sync/SKILL.md`

## Operational Rules

- Do not store chat logs, speculation, secrets, raw tokens, cookies, or
  credentials.
- Cite file or upstream evidence for each current fact.

## Last Verified

2026-06-11


## Last verified
- date: 2026-06-25
- commit: `f031b9ecb437c92579b84aa967cc6d0d7b0cfe8c`
- checked by: antigravity 1.7.0 tracked-context migration
