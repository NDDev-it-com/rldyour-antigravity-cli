---
name: ry-sync
description: "Синхронизируй Antigravity docs, memories и git. EN: synchronize Antigravity docs, memories, and git."
---

# Purpose

Finalize Antigravity CLI adapter work into synchronized source, docs, memories,
git, and GitHub state.

# Native Antigravity Boundary

Use Antigravity-native docs and runtime surfaces. Durable agent context is
tracked on `main`; runtime-local state stays ignored.

# When To Use

Use at the end of a completed task or when a Stop/post-task sync hook asks for
final synchronization.

# Inputs

- Current git status and upstream state.
- Serena memory freshness state.
- Instruction docs state.
- Repository context policy and branch state.

# Procedure

1. Confirm memories are current before docs/git sync.
2. Inspect uncommitted changes and exclude secrets, runtime markers, caches, and
   browser artifacts.
3. Run scope-matching checks.
4. Commit/push coherent source changes when appropriate.
5. Report advisory branch cleanup when policy allows it.

# Evidence Required

Git status, memory state, validator output, commit/tag IDs, repository context
state, and GitHub sync status.

# Forbidden Actions

Do not delete branches, force-push, or mutate system configs unless policy and
owner authorization allow that exact action.

# Acceptance Checks

Working tree is clean, memories are current, runtime markers are absent, and
repository context state matches policy.

# Failure Reporting

Report exact blockers and the command needed to clear each one.
