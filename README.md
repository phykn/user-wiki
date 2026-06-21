# User Wiki

Personal wiki for durable work preferences and user-specific operating rules.

This repository is meant to be read by agents and humans who need the shared defaults that apply across projects. It stores confirmed preferences only; project-specific rules belong in each project's own instructions.

The goal is not tone matching. The goal is to let agents work autonomously in the user's way: choose scope, ask only necessary questions, revise plans, handle evidence, and report outcomes according to confirmed preferences.

## Start Here

- Agents should read `AGENTS.md` first.
- The wiki graph starts at `graph/index.md`.
- There is intentionally no root `index.md`; do not treat its absence as a fallback event.
- Read only the graph pages related to the current task.

## Install Or Update

When this repository is given as a Git URL and the request is "install this" or "set up my user wiki", install it as the local user-wiki checkout for the active user. Use the user's Codex home, usually a `user-wiki` directory under `.codex`, unless the user gives another path.

If the checkout does not exist, clone the repository there. If it already exists, check local git status before updating it. Do not overwrite, reset, or delete local changes without the user's approval.

After installing or updating, verify that `AGENTS.md` and `graph/index.md` are present. Run `scripts/check-wiki.py` when Python is available.

The useful result is not just a cloned repository. Future agents should be able to find this wiki, read `AGENTS.md`, then follow `graph/index.md` for the task at hand.

## Applying This Wiki Elsewhere

Common use: give an AI this repository URL and ask it to reflect the wiki in another workspace, project, repository, or document set.

The AI should not copy these documents into the target surface. It should read the wiki as the user's default work preferences, including `graph/policy.md` and `graph/workflow.md`, inspect the target's own instructions, then create or update only the target files that control repeated behavior, usually `AGENTS.md`, `README.md`, prompts, or project docs.

The result should make future work in that target more natural: clearer entrypoints, sharper document roles, less generic explanation, decisions that follow the user's way, and evidence placed next to the claims it supports.

If the target work reveals a new preference that should apply across projects, the AI should also update this source wiki when it has write access. If it cannot update the wiki, it should say which user-wiki update is pending.

## Priority

This wiki is a default layer. Current user requests, system/developer instructions, and project-local instructions take precedence over it.
