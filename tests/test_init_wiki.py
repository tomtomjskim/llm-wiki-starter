import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "init-wiki.sh"


class InitWikiTest(unittest.TestCase):
    def test_life_os_option_creates_optional_profile_directories(self):
        with tempfile.TemporaryDirectory() as tmp:
            wiki_root = Path(tmp) / "wiki"
            result = subprocess.run(
                ["bash", str(SCRIPT), "--life-os", str(wiki_root)],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)

            expected_dirs = [
                "raw/life-os",
                "personal/life-os/inbox",
                "personal/life-os/reviewed",
                "personal/life-os/canonical",
                "compiled/life-os/generated",
                "compiled/life-os/hubs",
                "compiled/life-os/context-packs",
            ]
            for relative in expected_dirs:
                self.assertTrue((wiki_root / relative).is_dir(), relative)
                self.assertTrue((wiki_root / relative / ".gitkeep").exists(), relative)

            self.assertIn("Life OS profile", result.stdout)


if __name__ == "__main__":
    unittest.main()
