<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: 56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c chore(release): prepare antigravity 1.7.5 tracked context
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
- commit: `56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c`
- checked by: antigravity 1.7.5 tracked-context migration
