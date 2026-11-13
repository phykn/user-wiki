Procedures for installing, updating, and applying this wiki.

## Install Or Update

When the user asks to install or update this wiki:

1. Use the path the user gives, an existing checkout, or the platform's configured user-guidance location. Ask before inventing a location.
2. If the checkout exists, inspect `git status --short --branch`. Do not overwrite local changes or update a branch that cannot fast-forward.
3. Clone the checkout or fast-forward it. Run `python3 scripts/check.py` in it when Python 3 is available; otherwise confirm that `graph/index.md` exists.
4. Make the platform's user-level agent guidance contain the pointer below, with `<checkout>` replaced by the checkout path. Replace an older wiki pointer and preserve all other guidance. If the file cannot be changed safely, report the pending pointer update.
5. Report the pointer state and any local changes left untouched.

```markdown
# User Wiki

My cross-project guidance lives in `<checkout>` (https://github.com/phykn/user-wiki).

At the start of every task, read `<checkout>/graph/index.md` and follow only the routes that match the task. Paths in the wiki resolve from `<checkout>`.

Treat the wiki as a default layer: system and developer instructions, the current request, and project-local guidance take precedence.
```

## Apply To Another Workspace

When the user asks to apply this wiki elsewhere:

1. Read all applicable instruction files from the target root to each path in scope, plus maintained entrypoints.
2. Treat the wiki as defaults, not prose to copy. Preserve target-local rules.
3. Extend an existing maintained agent-guidance entrypoint where possible, and change other maintained guidance only where future behavior requires it. If no applicable agent entrypoint exists, an explicit apply request authorizes creating the platform-standard one after checking target conventions; do not create a parallel entrypoint.
4. Report whether the source wiki changed or has a proposed update.
