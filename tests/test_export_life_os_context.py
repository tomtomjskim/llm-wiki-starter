import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "export-life-os-context.py"


def write_note(path: Path, title: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        textwrap.dedent(
            f"""\
            ---
            name: {path.stem}
            description: {title}
            type: guide
            updated: 2026-07-06
            status: active
            ---

            # {title}

            {body}
            """
        ),
        encoding="utf-8",
    )


class ExportLifeOsContextTest(unittest.TestCase):
    def test_quick_profile_exports_reviewed_and_canonical_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            wiki = Path(tmp) / "wiki"
            write_note(
                wiki / "personal/life-os/canonical/policy.md",
                "Policy",
                "CANONICAL_CONTENT",
            )
            write_note(
                wiki / "personal/life-os/reviewed/note.md",
                "Reviewed Note",
                "REVIEWED_CONTENT",
            )
            write_note(
                wiki / "personal/life-os/inbox/private.md",
                "Inbox Note",
                "INBOX_CONTENT_SHOULD_NOT_BE_IN_BUNDLE",
            )
            write_note(
                wiki / "compiled/life-os/generated/draft.md",
                "Generated Draft",
                "GENERATED_CONTENT_SHOULD_NOT_BE_IN_BUNDLE",
            )
            write_note(
                wiki / "raw/life-os/raw-note.md",
                "Raw Note",
                "RAW_CONTENT_SHOULD_NOT_BE_IN_BUNDLE",
            )

            result = subprocess.run(
                [
                    "python3",
                    str(SCRIPT),
                    "--wiki-root",
                    str(wiki),
                    "--profile",
                    "quick",
                    "--date",
                    "2026-07-06",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)

            out_dir = wiki / "compiled/life-os/context-packs/2026-07-06-quick"
            self.assertTrue(out_dir.is_dir())

            expected_files = {
                "AI_HANDOFF.md",
                "MANIFEST.md",
                "CANONICAL_REVIEWED_BUNDLE.md",
                "RAW_INDEX.md",
                "SOURCE_FILES.txt",
            }
            self.assertEqual(
                expected_files,
                {path.name for path in out_dir.iterdir() if path.is_file()},
            )

            bundle = (out_dir / "CANONICAL_REVIEWED_BUNDLE.md").read_text(encoding="utf-8")
            self.assertIn("CANONICAL_CONTENT", bundle)
            self.assertIn("REVIEWED_CONTENT", bundle)
            self.assertNotIn("INBOX_CONTENT_SHOULD_NOT_BE_IN_BUNDLE", bundle)
            self.assertNotIn("GENERATED_CONTENT_SHOULD_NOT_BE_IN_BUNDLE", bundle)
            self.assertNotIn("RAW_CONTENT_SHOULD_NOT_BE_IN_BUNDLE", bundle)

            raw_index = (out_dir / "RAW_INDEX.md").read_text(encoding="utf-8")
            self.assertIn("raw/life-os/raw-note.md", raw_index)
            self.assertIn("personal/life-os/inbox/private.md", raw_index)
            self.assertIn("compiled/life-os/generated/draft.md", raw_index)
            self.assertNotIn("RAW_CONTENT_SHOULD_NOT_BE_IN_BUNDLE", raw_index)

            source_files = (out_dir / "SOURCE_FILES.txt").read_text(encoding="utf-8")
            self.assertIn("personal/life-os/canonical/policy.md", source_files)
            self.assertIn("personal/life-os/reviewed/note.md", source_files)


if __name__ == "__main__":
    unittest.main()
