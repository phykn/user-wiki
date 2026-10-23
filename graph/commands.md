Commands for inspecting and checking this wiki.

## Read

- `rg --files --hidden -g '!.git'`: List maintained wiki files, including root dotfiles.
- `rg -n '<search term>' graph`: Find duplicate rules, stale wording, and filename references.

## Check

- `python3 scripts/check-wiki.py`: Check the wiki layout, the entrypoint route, index routes and page entries, eval routing, links, anchors, path references, and empty docs.
- `python3 -m unittest discover -s scripts -p 'test_*.py' -v`: Run discoverable regression tests against small fixture repos.
- `evals/behavior.md`: Manual review prompts, not automatic tests. Review only the cases a behavior-changing edit touches.
- `git diff --check`: Check whitespace in the pending changes. It skips untracked files, so run `git add -N` on new files first.
- `git status --short --branch`: Check added, modified, deleted files, and branch sync before finishing.

After every wiki edit, run the checker, the regression tests, and the whitespace check, then inspect status. If commands cannot run, report that the review was static only.
