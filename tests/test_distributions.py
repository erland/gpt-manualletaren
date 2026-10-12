import json
import subprocess
import sys
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DistributionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        command = [sys.executable, str(ROOT / "scripts/build_distributions.py"), "--project-root", str(ROOT), "--version", "ci-test"]
        subprocess.run(command, check=True, cwd=ROOT)
        cls.archives = sorted((ROOT / "dist").glob("*.zip"))

    def test_six_archives_and_manifest(self):
        self.assertEqual(len(self.archives), 6)
        self.assertTrue((ROOT / "dist" / "DELIVERY-MANIFEST.json").is_file())

    def test_zip_integrity(self):
        for archive in self.archives:
            with self.subTest(archive=archive.name), zipfile.ZipFile(archive) as zf:
                self.assertIsNone(zf.testzip())
                self.assertTrue(zf.namelist())

    def test_runtime_formats_are_distinct(self):
        runtime = [p for p in self.archives if "-project-" not in p.name]
        self.assertEqual(len(runtime), 5)
        with_archives = []
        for archive in runtime:
            with zipfile.ZipFile(archive) as zf:
                with_archives.append(frozenset(zf.namelist()))
        self.assertGreater(len(set(with_archives)), 1)


if __name__ == "__main__":
    unittest.main()
