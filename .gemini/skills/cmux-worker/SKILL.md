---
name: cmux-worker
description: "Воркер cmux v3 для Antigravity CLI: cmux worker role, typed task envelope, heartbeat, scoped JSON report, no push/final sync. Используй для: cmux worker, worker report. EN triggers: cmux v3 worker. EN: cmux v3 worker."
---

# Purpose

Generated from root `config/cmux-adapter-projections.json`. Do not edit manually.

Perform a scoped visible cmux worker task for Antigravity CLI using the root-owned cmux orchestration protocol `3.0.0`.

# Native Antigravity Boundary

## Native Adapter Notes

- Antigravity CLI is worker-only until a native head orchestration contract is proven.
- The active runtime binary is agy; Gemini namespace paths are native compatibility surfaces, not Gemini CLI runtime support.

Antigravity native subagents and Gemini namespace compatibility paths are not rldyour cmux workers. The active runtime binary remains `agy`.

# When To Use

Use only when the visible head assigns this terminal a schema-valid task envelope and worker identity. Antigravity CLI is worker-only until head orchestration is proven and implemented.

# Inputs

- Explicit run and task identifiers.
- Root-owned immutable task envelope and task-local instructions file.
- `RLDYOUR_EXECUTION_MODE=orchestrator`, `RLDYOUR_AGENT_ROLE=worker`, and matching `RLDYOUR_WORKER_ID`.
- `CMUX_WORKSPACE_ID` and `CMUX_SURFACE_ID`, when present, matching the task assignment.

# Procedure

## Current Implementation Status

- `typed-task-report-protocol`: `IMPLEMENTED`.
- `live-start-fail-closed`: `IMPLEMENTED`.
- `compact-template`: `IMPLEMENTED`.
- `workspace-group-topology`: `PLANNED`.
- `delegation-command`: `PLANNED`.
- `worktree-scheduler`: `PLANNED`.
- `adapter-native-projections`: `IMPLEMENTED`.
- `stop-finalization-receipt`: `PLANNED`.

Treat `PLANNED` and `NOT_PROVEN` entries as unavailable in production.

1. Accept only the assigned run/task through the worker helper.
2. Work only inside the assigned repository/worktree and scope.
3. Treat allowed paths as JSON task-envelope data, never shell text.
4. Stop and report `blocked` or `not_proven` when scope, identity, or evidence is ambiguous.
5. Record commands and checks in the report.

# Evidence Required

Completion authority is a schema-valid report at `$(git rev-parse --git-common-dir)/rldyour/cmux/<run-id>/tasks/<task-id>/report.json` with `report_digest`. Report changed paths, out-of-scope paths, diff digest, commands, checks, findings, risks, and needed head actions. Notifications are UI hints only.

# Forbidden Actions

- Do not push, force-push, tag, delete branches, mutate project policy, run system install, or run final sync.
- Do not delegate nested visible workers.
- Do not create hidden or daemon-style orchestration processes.
- Do not treat native subagents, Gemini namespace compatibility, hooks, or background tasks as rldyour cmux workers.
- Do not claim success when the report was not written and validated.

# Acceptance Checks

Run only the scoped checks from the task envelope. Mark unavailable checks `NOT_PROVEN` with an exact reason.

# Failure Reporting

Write a schema-valid failed, blocked, cancelled, or not_proven report with bounded evidence and no secrets.
