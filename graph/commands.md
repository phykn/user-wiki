Commands for inspecting and checking this wiki.

## Read

- `rg --files --hidden -g '!.git'`: List maintained wiki files, including root dotfiles.
- `rg -n '<search term>' graph`: Find duplicate rules, stale wording, and filename references.

## Check

- `rg -n '\[\[' graph`: Inspect wikilinks before or after renaming documents.
- `python scripts/check-wiki.py`: Check the canonical entrypoint route, intentionally absent root index, routed graph pages, maintained path references, empty docs, and broken wikilinks.
- `python -m unittest discover -s scripts -p 'test_*.py' -v`: Run discoverable regression tests against small fixture repos.
- `evals/personal-agent.md`: Review only cases related to behavior-changing guidance edits; these are manual evidence, not automatic tests.
- `git diff --check`: Check whitespace issues across root files and graph documents.
- `git status --short --branch`: Check added, modified, deleted files, and branch sync before finishing.

After wiki edits, run the wiki checker and whitespace check, then inspect status. Run the regression suite when checker behavior changes. Review relevant manual cases when guidance changes; these do not establish model performance. If execution is unavailable, report static review only.
