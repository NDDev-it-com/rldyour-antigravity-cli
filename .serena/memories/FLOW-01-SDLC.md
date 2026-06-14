# FLOW-01-SDLC

## Purpose

Record Gemini adapter SDLC flow rules.

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
- date: 2026-06-15
- commit: `834e12d1320b0f9d966ac746385d404dcd34a4bd`
- checked by: flow-memory-sync post-task sync
