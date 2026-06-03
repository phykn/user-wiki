Repeated shell commands for checking and maintaining this wiki.

## Read

- `rg --files graph`: List wiki documents.
- `rg -n '<search term>' graph`: Find duplicate rules, stale wording, and filename references.

## Check

- `rg -n '^# ' graph`: Find top-level headings that may duplicate filenames.
- `rg -n '\[\[' graph`: Inspect wikilinks before or after renaming documents.
- `git diff --check -- graph`: Check whitespace issues in wiki changes.
- `git status --short`: Check added, modified, or deleted files before finishing.
