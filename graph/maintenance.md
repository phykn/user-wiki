How this wiki is laid out, written, and checked.

## Structure

- The root holds one Markdown file, `README.md`. There is intentionally no root-level index or entry file.
- Pages sit directly in `graph/`, with no subfolders. The `Route` section of `graph/index.md` links every page from a bullet.
- Each page opens with one sentence that states its responsibility. Read those opening lines to decide which page owns a rule.

## Syntax

The checker understands only this subset of Markdown, so keep links and paths within it.

- Write each paragraph and list item on one line. The checker reads one line at a time, so it misses a wrapped link, path, or route.
- Write headings as plain text, without emphasis or links.
- Link a page with `[[page]]`, a section with `[[page#Heading]]`, and a section of the same page with `[[#Heading]]`. The heading text must match, ignoring case.
- Name a wiki file in inline code by its path from the wiki root, such as `graph/setup.md`.
- Use Markdown links only for external `http`, `https`, or `mailto` addresses.
- Put examples that contain links or paths in fenced code blocks, which the checker skips.

## Check

After every edit to this wiki, run these from the wiki root and fix what they report, then inspect the status:

- `python3 scripts/check-wiki.py`: prints `WIKI_CHECK_OK`, or one problem per line and exits with status 1.
- `python3 -m unittest discover -s scripts -p 'test_*.py' -v`: only after a change under `scripts/`.
- `git diff --check`: skips untracked files, so run `git add -N` on new files first.
- `git status --short --branch`

After adding, moving, or rewording a rule, check that no rule on another page conflicts with it.
