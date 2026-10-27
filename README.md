# User Wiki

Personal guidance that helps agents work consistently with the user across projects. It stores confirmed cross-project preferences; project-specific rules stay with the project.

The goal is practical behavior: choosing scope, asking only consequential questions, using evidence, and reporting verified outcomes.

## Start

Agents start at `AGENTS.md`, then follow `graph/index.md` to the smallest set of related pages. There is intentionally no root-level index entrypoint.

The wiki is a default layer below platform, request, and project instructions; `graph/policy.md` defines the priority order.

## Install And Apply

Ask an agent to install, update, or apply this wiki; it follows the procedures in `graph/setup.md`. Installation places or updates this checkout and makes the platform's user-level agent guidance point future sessions to it. Applying the wiki to another workspace adapts that workspace's maintained guidance instead of copying this wiki into it.

## Maintain

From the checkout root, run these checks with Python 3; no extra packages are required:

```sh
python3 scripts/check-wiki.py
python3 -m unittest discover -s scripts -p 'test_*.py' -v
git diff --check
```

The checker prints `WIKI_CHECK_OK` on success, or one diagnostic per line and exits with status 1 on failure. See `graph/commands.md` for maintenance and manual review guidance.

Markdown links, including reference definitions, resolve from the containing document, and their anchors match a heading's GitHub slug or its text. Paths in inline code, whether the whole span or a command argument, use the wiki root for paths under `graph`, `evals`, or `scripts`; bare filenames look beside the document, then at the root. Explicit `./` and `../` paths always start beside the document. References must stay inside the checkout. Fenced examples and HTML comments do not register links or routes.

`scripts/check-wiki.py` locates the checkout and handles CLI output. `scripts/wiki_check.py` owns repository validation; `scripts/wiki_markdown.py` extracts Markdown references and routes. Regression tests in `scripts/test_check_wiki.py` exercise validation and the CLI on temporary wiki fixtures.
