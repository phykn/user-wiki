How this wiki is laid out, written, and checked.

## Layout

- The root holds one Markdown file, `README.md`. There is intentionally no root-level index or entry file.
- Pages sit directly in `graph/`, with no subfolders. The `Route` section of `graph/index.md` links every page.
- Each page opens with one sentence that states its responsibility. Read those opening lines to decide which page owns a rule.

## Syntax

The checker reads one line at a time and understands only what is listed here. Anything else it reports as a broken link, or misses.

- Write each paragraph and list item on one line, so no link or path wraps.
- Link a page with `[[page]]`, the page's filename without `.md`. There are no section links or aliases.
- Name a wiki file in inline code by its path from the wiki root, such as `graph/setup.md`.
- Use Markdown links only for external `http`, `https`, or `mailto` addresses.
- Put examples that contain links or paths in single-backtick inline code or in a block fenced by three backticks. The checker skips both.

## Check

After every edit to this wiki, run these from the wiki root and fix what they report:

- `python3 scripts/check.py`: prints `WIKI_CHECK_OK`, or one problem per line and exits with status 1.
- `python3 -m unittest discover -s scripts -p 'test_*.py'`: only after a change under `scripts/`.

After adding, moving, or rewording a rule, check that no rule on another page conflicts with it.
