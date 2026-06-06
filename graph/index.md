Shared user work guidance for multiple projects.

This document set is the user's personal wiki / user wiki.

The root `AGENTS.md` is the entrypoint for agents, and this `graph/` folder contains the actual wiki nodes.
This wiki starts from a minimal document set and accumulates only preferences that apply across multiple projects.

Canonical route: `AGENTS.md` -> `graph/index.md`.
Do not search for or narrate missing root `index.md` / `CORE.md` files unless a user request explicitly depends on them.

The central aim is autonomous work in the user's way. The wiki should change how an agent chooses scope, asks questions, handles evidence, revises plans, and reports results; it should not only change tone.

## Usage

For non-trivial work:

1. Read [[intuition]] first to frame what matters and the judgment criteria for the work.
2. Read [[policy]] to check update rules and document boundaries.
3. Read only the pages related to the current task.
4. Apply confirmed preferences as defaults.
5. If the current user request, system/developer instructions, or project instructions conflict with this wiki, they take precedence over this wiki.

When applying this wiki to another repository, [[workflow]] is a required related page because it owns the target-repository application path and source-wiki update reporting.

## Documents

Current documents:

- [[intuition]]: Higher-level judgment criteria for autonomous work in the user's way, preserving what matters, and making ambiguous work concrete enough to judge.
- [[policy]]: Operating contract for wiki updates, boundaries, and priority.
- [[workflow]]: Confirmed defaults for responses, questions, collaboration, and applying this wiki to another repository.
- [[code]]: Confirmed principles for code edits, refactoring, and tests.
- [[docs]]: Confirmed structure and wording standards for documents, wikis, prompts, and work instructions.
- [[theory]]: Current interpretation used to better align answers with the user.
- [[commands]]: Repeated commands for checking and maintaining the wiki.
- [[changelog]]: Wiki change record.

Document creation and update rules follow [[policy]].
