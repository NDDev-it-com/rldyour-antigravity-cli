<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: 56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c chore(release): prepare antigravity 1.7.2 tracked context
Scope: Antigravity CLI SDLC flow rules
Area: FLOW
-->

# FLOW-01-SDLC

## Purpose

Record Antigravity adapter SDLC flow rules.

## Current Facts

- `/ry:repair`, `/ry:start`, `/flow:post-task-sync`, browser, release, Serena,
  and security command surfaces are TOML Gemini commands.
- Post-task sync updates docs and Serena memories only from verified facts.

## Evidence

- `.gemini/commands/ry/repair.toml`
- `.gemini/commands/ry/start.toml`
- `.gemini/commands/flow/post-task-sync.toml`
- `.gemini/skills/flow-post-task-sync/SKILL.md`

## Operational Rules

- Do not add background orchestrators or hidden worker jobs.
- In standard mode the owner remains the orchestration layer.

## Last Verified

2026-06-11


## Last verified
- date: 2026-06-25
- commit: `56af1bd1d5c2f14c3417a8bd8c7737d6beba3f1c`
- checked by: antigravity 1.7.2 tracked-context migration
