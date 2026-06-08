Repeated shell commands for checking and maintaining this wiki.

## Read

- `rg --files graph`: List wiki documents.
- `rg --files evals`: List regression prompts for agent behavior.
- `rg -n '<search term>' graph`: Find duplicate rules, stale wording, and filename references.

## Check

- `rg -n '^# ' graph`: Find top-level headings that may duplicate filenames.
- `rg -n '\[\[' graph`: Inspect wikilinks before or after renaming documents.
- `git diff --check`: Check whitespace issues across root files and graph documents.
- `git status --short --branch`: Check added, modified, deleted files, and branch sync before finishing.

## Wiki Maintenance Check

For structural wiki edits, usually run:

1. `rg --files graph evals`
2. `rg -n '\[\[' graph`
3. Broken wikilink check command below
4. `git diff --check`
5. `git status --short --branch`

Use static review instead when the repository is not checked out locally, and report that command verification did not run.

- Broken wikilink check:

```text
python -c "from pathlib import Path; import re, sys; files=list(Path('graph').glob('*.md')); names={p.stem for p in files}; missing=[]; [missing.append(f'{p}: {target}') for p in files for target in re.findall(r'\[\[([^\]|#]+)', p.read_text(encoding='utf-8')) if target not in names]; print('\n'.join(sorted(set(missing))) if missing else 'NO_BROKEN_WIKILINKS'); sys.exit(1 if missing else 0)"
```
