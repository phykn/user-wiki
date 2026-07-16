Repeated shell commands for checking and maintaining this wiki.

## Read

- `rg --files --hidden -g '!.git'`: List maintained wiki files, including root dotfiles.
- `rg --files graph`: List wiki documents.
- `rg --files evals`: List regression prompts for agent behavior.
- `rg --files scripts`: List wiki maintenance scripts.
- `rg -n '<search term>' graph`: Find duplicate rules, stale wording, and filename references.

## Check

- `rg -n '^# ' graph`: Find top-level headings that may duplicate filenames.
- `rg -n '\[\[' graph`: Inspect wikilinks before or after renaming documents.
- `python scripts/check-wiki.py`: Check the canonical entrypoint route, intentionally absent root index, routed graph pages, maintained path references, empty docs, and broken wikilinks.
- `python -m unittest discover -s scripts -p 'test_*.py' -v`: Run discoverable regression tests against small fixture repos.
- `evals/personal-agent.md`: Review only cases related to behavior-changing guidance edits; these are manual evidence, not automatic tests.
- `git diff --check`: Check whitespace issues across root files and graph documents.
- `git status --short --branch`: Check added, modified, deleted files, and branch sync before finishing.

## Wiki Maintenance Check

For structural wiki edits, usually run:

1. `rg --files --hidden -g '!.git'`
2. `rg -n '\[\[' graph`
3. `python scripts/check-wiki.py`
4. `python -m unittest discover -s scripts -p 'test_*.py' -v`
5. Review the relevant cases in `evals/personal-agent.md` when behavior guidance changed.
6. `git diff --check`
7. `git status --short --branch`

Use static review instead when the repository is not checked out locally, and report that command verification did not run.
