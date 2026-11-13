import contextlib
import io
import tempfile
import unittest
from pathlib import Path

import check

FIXTURE = {
    "README.md": "# README\n\nRun `python3 scripts/check.py` and read `graph/index.md`.\n",
    "graph/index.md": "Entry page.\n\n## Route\n\n- Maintenance: [[maintenance]].\n",
    "graph/maintenance.md": "How the wiki is checked.\n\n## Check\n\nSee [the site](https://example.com).\n",
    "scripts/check.py": "",
}


class CheckWikiTests(unittest.TestCase):
    def run_check(self, files, remove=()):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for path, text in {**FIXTURE, **files}.items():
                (root / path).parent.mkdir(parents=True, exist_ok=True)
                (root / path).write_text(text, encoding="utf-8")
            for path in remove:
                (root / path).unlink()
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                status = check.check_wiki(root)
            return status, out.getvalue().splitlines()

    def test_valid_wiki(self):
        self.assertEqual(self.run_check({}), (0, ["WIKI_CHECK_OK"]))

    def test_code_is_not_read(self):
        readme = "Examples: `[[missing]]` and `[x](y.md)`.\n\n```text\n[[missing]]\n[x](y.md)\n```\n"
        self.assertEqual(self.run_check({"README.md": readme}), (0, ["WIKI_CHECK_OK"]))

    def test_every_problem(self):
        status, lines = self.run_check(
            {
                "CLAUDE.md": "Second entry.\n",
                "graph/old/page.md": "Old page.\n",
                "graph/extra.md": "## Extra\n\nLinked outside Route: [[maintenance]].\n",
                "graph/index.md": "Entry page.\n\n## Route\n\n- [[maintenance]]\n\n## Pages\n\n- [[extra]]\n",
                "graph/maintenance.md": "How the wiki is checked.\n\n"
                "[Setup](graph/index.md), `python3 scripts/absent.py --strict`, a literal ` and [[gone]].\n",
            },
            remove=["README.md"],
        )
        self.assertEqual(status, 1)
        self.assertEqual(
            lines,
            [
                "MISSING_DOC README.md",
                "UNEXPECTED_DOC CLAUDE.md",
                "UNEXPECTED_DOC graph/old/page.md",
                "MISSING_SUMMARY graph/extra.md",
                "UNSUPPORTED_SYNTAX graph/maintenance.md -> [Setup](graph/index.md)",
                "BROKEN_PATH graph/maintenance.md -> scripts/absent.py",
                "BROKEN_LINK graph/maintenance.md -> gone",
                "UNROUTED_PAGE graph/extra.md",
            ],
        )


if __name__ == "__main__":
    unittest.main()
