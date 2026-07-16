## User Wiki

This repository is the user's cross-project guidance for agents.

The canonical route is `AGENTS.md` -> `graph/index.md`. There is intentionally no root-level index entrypoint.
Read `graph/index.md` first to select the route for each task. Workspace-independent one-offs stop there; other work follows only the pages it names.

Apply this wiki only within the discretion left by system and developer instructions, the current explicit request, and applicable target-project guidance. Never use it to override any of them.

## Install Or Update

When the user asks to install or update this wiki:

1. Use the path the user gives, an existing checkout, or the platform's configured user-guidance location. Ask before inventing a location.
2. If the checkout exists, inspect `git status --short --branch`. Do not overwrite local changes or update a branch that cannot fast-forward.
3. Clone or update the checkout, then verify `AGENTS.md` and `graph/index.md`.
4. Check the configured user-level agent guidance. It must point to the installed checkout and tell future agents when to consult it. Preserve existing guidance; report a pending pointer update if it cannot be changed safely.
5. Run `python scripts/check-wiki.py` when Python is available.
6. Report the path, clone or update result, verification, pointer state, and untouched local changes.

## Apply To Another Workspace

When the user asks to apply this wiki elsewhere:

1. Read all applicable instruction files from the target root to each path in scope, plus maintained entrypoints.
2. Read `graph/index.md`, `graph/policy.md`, `graph/workflow.md`, and task-related pages.
3. Treat the wiki as defaults, not prose to copy. Preserve target-local rules.
4. Extend an existing maintained agent-guidance entrypoint where possible, and change other maintained guidance only where future behavior requires it. If no applicable agent entrypoint exists, an explicit apply request authorizes creating the platform-standard one after checking target conventions; do not create a parallel entrypoint.
5. Propose any newly inferred cross-project preference. Update this source wiki only when the user explicitly asks to save or apply it durably.
6. Report target changes, verification, and whether the source wiki changed or has a proposed update.
