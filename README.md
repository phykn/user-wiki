# User Wiki

Personal guidance that helps coding agents work the same way with the user across projects. It holds confirmed cross-project preferences: when to ask and when to proceed, when to answer and when to edit, how to stay inside the workspace and scope, and how the user wants code and documents written. Agents treat it as a default layer under the platform's instructions, the user's request, and each project's own guidance, and project-specific rules stay with each project.

## How Agents Use It

An installed checkout is named in the platform's user-level agent guidance, which tells agents to read `graph/index.md` at the start of every task. That page holds the rules every task follows and routes each kind of task to the few pages it needs. Agents working inside this repository start at `AGENTS.md`, which leads to the same page.

## Install, Update, Or Apply

Ask an agent to install or update this wiki, or to apply it to another workspace. It follows `graph/setup.md`, which also holds the pointer text for the user-level guidance. Applying the wiki adapts the target workspace's own guidance instead of copying this wiki into it.

## Check

From the checkout root, with Python 3 and no extra packages:

```sh
python3 scripts/check-wiki.py
python3 -m unittest discover -s scripts -p 'test_*.py' -v
git diff --check
```

The checker prints `WIKI_CHECK_OK`, or one problem per line and exits with status 1. `graph/maintenance.md` describes the layout, the Markdown subset the checker reads, and what to run and review after an edit.
