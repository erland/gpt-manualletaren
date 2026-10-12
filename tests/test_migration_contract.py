"""Migration contract checks; these do not replace engine lint or host tests."""
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "chat": ("chat", "chat_zip"),
    "plugin": ("plugin", "plugin"),
    "claude_project": ("claude", "claude"),
    "claude_skills": ("claude_skills", "claude"),
    "opencode": ("opencode", "opencode"),
}


class MigrationContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = yaml.safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
        cls.status = yaml.safe_load((ROOT / "project-status.yaml").read_text(encoding="utf-8"))

    def test_identity_and_canonical_source(self):
        self.assertEqual(self.model["project"]["id"], "manualletaren")
        self.assertEqual(self.model["project"]["language"], "sv")
        path = self.model["instructions"]["canonical"]
        self.assertTrue((ROOT / path).is_file())

    def test_six_build_targets_and_engine_contract(self):
        build = self.model["build_system"]
        self.assertEqual(set(build["targets"]), {"project", *EXPECTED})
        self.assertEqual(set(build["runtime_targets"]), set(EXPECTED))
        for name, (builder, runtime_key) in EXPECTED.items():
            target = build["runtime_targets"][name]
            self.assertEqual(target["builder"], builder)
            self.assertEqual(target["runtime_key"], runtime_key)
            for key in ("runtime_id", "artifact_type", "filename_pattern"):
                self.assertTrue(target[key], (name, key))
        self.assertFalse(self.model["runtime"]["custom_gpt"]["enabled"])

    def test_project_specific_skill_references_exist(self):
        for skill in self.model["skills"]["definitions"]:
            self.assertTrue((ROOT / "skills" / skill["id"] / "SKILL.md").is_file())
            for ref in skill["references"]:
                self.assertTrue((ROOT / ref).is_file(), ref)

    def test_status_does_not_claim_release_ready(self):
        self.assertFalse(self.status["release_ready"])
        self.assertFalse(self.status["runtime"]["activated"])


if __name__ == "__main__":
    unittest.main()
