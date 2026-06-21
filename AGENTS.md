## User Wiki

This project is the user's personal wiki.

The canonical route is `AGENTS.md` -> `graph/index.md`.
There is intentionally no root `index.md` entrypoint in this repo.
Do not report those root files as missing unless their absence actually blocks the task.

For non-trivial work, first read `graph/index.md` and follow its reading order.
Read only the related user-wiki pages beyond that.

Apply confirmed user-wiki documents as project-common default preferences.
Current user requests, system/developer instructions, and project-local `AGENTS.md` files take precedence over the user wiki.

## Installing This Wiki

When the user gives this repository as a Git URL, local checkout, or attached source and asks to "install this", "set up my user wiki", or similar:

1. Treat the task as installing or updating the user's local user-wiki checkout, not as applying the wiki to the current target project.
2. Use `C:\Users\KN\.codex\user-wiki` as the default install path when that path is available. If it is not available, use the nearest equivalent under the user's Codex home and report the actual path.
3. If the install path does not exist, clone the repository there.
4. If the install path already exists, inspect `git status --short --branch` before changing it.
5. Do not overwrite, reset, or delete local changes. If the checkout is dirty or the update cannot fast-forward, report the concrete state and ask before proceeding.
6. After cloning or updating, verify that `AGENTS.md` and `graph/index.md` exist, then run `python scripts/check-wiki.py` when Python is available.
7. Report the installed path, whether this was a clone or update, the verification result, and any local changes left untouched.

## Applying This Wiki Elsewhere

When the user gives this wiki as a URL, local checkout, attached document set, or other source and asks to "reflect" or "apply" it to another workspace, repository, or document set:

1. Treat this wiki as a default preference layer, not as content to copy wholesale.
2. The goal is autonomous work in the user's way, not tone matching or copying wiki prose.
3. Read `graph/index.md` and the related pages for the target task. For this cross-workspace task, `graph/policy.md` and `graph/workflow.md` are required related pages.
4. Inspect the target's own instructions, front page, and relevant docs before editing.
5. Create or update the target's agent-facing or front-page guidance only where it changes future behavior.
6. Preserve target-local instructions when they conflict with this wiki.
7. If the work reveals a new or corrected project-common preference, update this source user-wiki too when it is writable.
8. If this source user-wiki is not writable or not checked out, report the pending user-wiki update explicitly instead of silently dropping it.
9. Report which target files changed, whether this source wiki changed, and which wiki preferences drove the change.
