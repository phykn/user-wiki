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

When this repository is given as a Git URL and the request is "install this" or "set up my user wiki", install it as the local user-wiki checkout. The default path for this user is:

```text
C:\Users\KN\.codex\user-wiki
```

If the directory does not exist, clone the repository there:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.codex" | Out-Null
git clone <repo-url> "$env:USERPROFILE\.codex\user-wiki"
```

If the directory already exists, update it only after checking local changes:

```powershell
git -C "$env:USERPROFILE\.codex\user-wiki" status --short --branch
git -C "$env:USERPROFILE\.codex\user-wiki" pull --ff-only
```

Do not overwrite a dirty checkout. If local changes exist, report them and ask before changing files.

After installing or updating, verify the route:

```powershell
Test-Path "$env:USERPROFILE\.codex\user-wiki\AGENTS.md"
Test-Path "$env:USERPROFILE\.codex\user-wiki\graph\index.md"
Set-Location "$env:USERPROFILE\.codex\user-wiki"
python scripts\check-wiki.py
```

The useful result is not just a cloned repository. Future agents should be able to find this wiki, read `AGENTS.md`, then follow `graph/index.md` for the task at hand.

## Applying This Wiki Elsewhere

Common use: give an AI this repository URL and ask it to reflect the wiki in another workspace, project, repository, or document set.

The AI should not copy these documents into the target surface. It should read the wiki as the user's default work preferences, including `graph/policy.md` and `graph/workflow.md`, inspect the target's own instructions, then create or update only the target files that control repeated behavior, usually `AGENTS.md`, `README.md`, prompts, or project docs.

The result should make future work in that target more natural: clearer entrypoints, sharper document roles, less generic explanation, decisions that follow the user's way, and evidence placed next to the claims it supports.

If the target work reveals a new preference that should apply across projects, the AI should also update this source wiki when it has write access. If it cannot update the wiki, it should say which user-wiki update is pending.

## Structure

- `AGENTS.md`: Bootstrap instructions for agents.
- `graph/`: Wiki nodes for confirmed preferences, workflow rules, code rules, document rules, and current user understanding.
- `evals/`: Regression prompts for checking whether future agent behavior matches the wiki.
- `scripts/`: Portable maintenance checks for this wiki.
- `.gitignore`: Keeps local Obsidian state and OS/editor noise out of the repository.

## Priority

This wiki is a default layer. Current user requests, system/developer instructions, and project-local instructions take precedence over it.
