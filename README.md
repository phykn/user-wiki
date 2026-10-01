# User Wiki

Personal guidance that helps agents work consistently with the user across projects. It stores confirmed cross-project preferences; project-specific rules stay with the project.

The goal is practical behavior: choosing scope, asking only consequential questions, using evidence, and reporting verified outcomes.

## Start

Agents start at `AGENTS.md`, then follow `graph/index.md` to the smallest set of related pages. There is intentionally no root-level index entrypoint.

## Install And Apply

Installation places or updates this checkout and ensures the platform's user-level agent guidance points future sessions to it. Applying the wiki to another workspace means adapting that workspace's maintained guidance, not copying this wiki into it.

See `AGENTS.md` for the authoritative install and application procedures.

## Priority

This wiki is a default layer. Follow the platform's instruction hierarchy and use the wiki only within the discretion left by the current request and applicable target-local guidance.

## Maintain

From the checkout root, run these checks with Python 3; no extra packages are required:

```sh
python scripts/check-wiki.py
python -m unittest discover -s scripts -p 'test_*.py' -v
git diff --check
```

The checker prints `WIKI_CHECK_OK` on success, or one diagnostic per line and exits with status 1 on failure. See `graph/commands.md` for maintenance and manual review guidance.

`scripts/check-wiki.py` locates the checkout and handles CLI output. `scripts/wiki_check.py` owns repository validation; `scripts/wiki_markdown.py` extracts Markdown references and routes. Regression tests in `scripts/test_check_wiki.py` exercise validation on temporary wiki fixtures and check CLI output and exit status separately.
