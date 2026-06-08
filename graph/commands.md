Repeated shell commands for checking and maintaining this wiki.

## Read

- `rg --files graph`: List wiki documents.
- `rg --files evals`: List regression prompts for agent behavior.
- `rg --files scripts`: List wiki maintenance scripts.
- `rg -n '<search term>' graph`: Find duplicate rules, stale wording, and filename references.

## Check

- `rg -n '^# ' graph`: Find top-level headings that may duplicate filenames.
- `rg -n '\[\[' graph`: Inspect wikilinks before or after renaming documents.
- `python scripts/check-wiki.py`: Check empty docs and broken wikilinks.
- `git diff --check`: Check whitespace issues across root files and graph documents.
- `git status --short --branch`: Check added, modified, deleted files, and branch sync before finishing.

## Wiki Maintenance Check

For structural wiki edits, usually run:

1. `rg --files graph evals scripts`
2. `rg -n '\[\[' graph`
3. `python scripts/check-wiki.py`
4. `git diff --check`
5. `git status --short --branch`

Use static review instead when the repository is not checked out locally, and report that command verification did not run.
