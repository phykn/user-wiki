Procedures for installing, updating, and applying this wiki.

## Install Or Update

When the user asks to install or update this wiki:

1. Use the path the user gives, an existing checkout, or the platform's configured user-guidance location. Ask before inventing a location.
2. If the checkout exists, inspect `git status --short --branch`. Do not overwrite local changes or update a branch that cannot fast-forward.
3. Clone or update the checkout, then verify `AGENTS.md` and `graph/index.md`.
4. Check the configured user-level agent guidance. It must point to the installed checkout and tell future agents when to consult it. Preserve existing guidance; report a pending pointer update if it cannot be changed safely.
5. Run `python3 scripts/check-wiki.py` when Python 3 is available.
6. Report the path, clone or update result, verification, pointer state, and untouched local changes.

## Apply To Another Workspace

When the user asks to apply this wiki elsewhere:

1. Read all applicable instruction files from the target root to each path in scope, plus maintained entrypoints.
2. Treat the wiki as defaults, not prose to copy. Preserve target-local rules.
3. Extend an existing maintained agent-guidance entrypoint where possible, and change other maintained guidance only where future behavior requires it. If no applicable agent entrypoint exists, an explicit apply request authorizes creating the platform-standard one after checking target conventions; do not create a parallel entrypoint.
4. Propose any newly inferred cross-project preference instead of editing this source wiki, unless the user also asked to save it.
5. Report target changes, verification, and whether the source wiki changed or has a proposed update.
