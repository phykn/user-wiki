## User Wiki

This project is the user's personal wiki.

The canonical route is `AGENTS.md` -> `graph/index.md`.
There is intentionally no root `index.md` or `CORE.md` entrypoint in this repo.
Do not report those root files as missing unless their absence actually blocks the task.

For non-trivial work, first read `graph/index.md` and follow its reading order.
Read only the related user-wiki pages beyond that.

Apply confirmed user-wiki documents as project-common default preferences.
Current user requests, system/developer instructions, and project-local `AGENTS.md` files take precedence over the user wiki.

## Applying This Wiki to Another Repository

When the user gives this wiki as a Git repository URL and asks to "reflect" or "apply" it to another repository:

1. Treat this wiki as a default preference layer, not as content to copy wholesale.
2. The goal is autonomous work in the user's way, not tone matching or copying wiki prose.
3. Read `graph/index.md` and the related pages for the target task. For this cross-repository task, `graph/policy.md` and `graph/workflow.md` are required related pages.
4. Inspect the target repository's own `AGENTS.md`, `README.md`, and relevant docs before editing.
5. Create or update the target repository's agent-facing or front-page guidance only where it changes future behavior.
6. Preserve target-repository instructions when they conflict with this wiki.
7. If the work reveals a new or corrected project-common preference, update this source user-wiki too when it is writable.
8. If this source user-wiki is not writable or not checked out, report the pending user-wiki update explicitly instead of silently dropping it.
9. Report which target files changed, whether this source wiki changed, and which wiki preferences drove the change.
