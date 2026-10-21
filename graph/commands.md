Commands for inspecting and checking this wiki.

## Read

- `rg --files --hidden -g '!.git'`: List maintained wiki files, including root dotfiles.
- `rg -n '<search term>' graph`: Find duplicate rules, stale wording, and filename references.

## Check

- `python scripts/check-wiki.py`: Check the canonical entrypoint route, intentionally absent root index, routed graph pages, maintained path references, empty docs, and broken wikilinks.
- `python -m unittest discover -s scripts -p 'test_*.py' -v`: Run discoverable regression tests against small fixture repos.
- `evals/behavior.md`: Manual review prompts, not automatic tests. Review only the cases a behavior-changing edit touches.
- `git diff --check`: Check whitespace in the pending changes.
- `git status --short --branch`: Check added, modified, deleted files, and branch sync before finishing.

After every wiki edit, run the checker and the whitespace check, then inspect status. Run the regression tests when checker code changes. If commands cannot run, report that the review was static only.
