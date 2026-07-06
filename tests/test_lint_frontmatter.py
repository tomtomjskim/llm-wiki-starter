import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "lint-frontmatter.py"


class LintFrontmatterTest(unittest.TestCase):
    def test_linter_runs_with_default_python3(self):
        result = subprocess.run(
            ["python3", str(SCRIPT), "--help"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("frontmatter", result.stdout)

    def test_template_placeholder_dates_do_not_warn(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "templates" / "example.md"
            target.parent.mkdir(parents=True)
            target.write_text(
                textwrap.dedent(
                    """\
                    ---
                    name: example-template
                    description: Example template
                    type: guide
                    updated: YYYY-MM-DD
                    status: active
                    ---

                    # Example
                    """
                ),
                encoding="utf-8",
            )

            result = subprocess.run(
                ["python3", str(SCRIPT), str(target.parent)],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("WARNING: 0건", result.stdout)

    def test_template_placeholder_dates_with_inline_comments_do_not_warn(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "templates" / "example.md"
            target.parent.mkdir(parents=True)
            target.write_text(
                textwrap.dedent(
                    """\
                    ---
                    name: example-template
                    description: Example template
                    type: guide
                    updated: YYYY-MM-DD              # fill in when copied
                    status: active
                    ---

                    # Example
                    """
                ),
                encoding="utf-8",
            )

            result = subprocess.run(
                ["python3", str(SCRIPT), str(target.parent)],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("WARNING: 0건", result.stdout)


if __name__ == "__main__":
    unittest.main()
