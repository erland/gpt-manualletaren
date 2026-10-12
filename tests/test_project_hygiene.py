"""Hygiene regression checks for the v1.6.14 migration."""
import json
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]


class HygieneTests(unittest.TestCase):
    def test_project_status_mirror(self):
        canonical = yaml.safe_load((ROOT / "project-status.yaml").read_text(encoding="utf-8"))
        legacy = json.loads((ROOT / "project/status.json").read_text(encoding="utf-8"))
        self.assertEqual(legacy["project"], canonical["project"]["id"])
        self.assertEqual(legacy["version"], canonical["project"]["version"])
        self.assertEqual(legacy["builder_version"], canonical["project"]["builder_version"])
        self.assertEqual(legacy["workflow_state"], canonical["workflow"]["state"])
        self.assertEqual(legacy["next_step"], canonical["next_step"]["id"])
        self.assertEqual(legacy["runtimes_activated"], canonical["runtime"]["activated"])
        self.assertIs(legacy["release_ready"], canonical["release_ready"])

    def test_optional_engine_paths_are_documented(self):
        project = yaml.safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
        for key in ("conversation_starters", "runtime_policy"):
            configured = project["structure"][key]
            self.assertFalse(configured["required"])
            readme = ROOT / configured["path"] / "README.md"
            self.assertTrue(readme.is_file())
            self.assertIn("canonical", readme.read_text(encoding="utf-8"))

    def test_build_output_is_gitignored(self):
        ignore = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
        for entry in ("build/", "dist/"):
            self.assertIn(entry, ignore)


if __name__ == "__main__":
    unittest.main()
