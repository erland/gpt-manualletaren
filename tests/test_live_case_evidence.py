import subprocess
import sys
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class LiveEvidenceTests(unittest.TestCase):
    def test_bosch_variants_are_documented(self):
        report = (ROOT / 'docs/ACCEPTANCE-TESTS.md').read_text(encoding='utf-8')
        for suffix in ('/01', '/27', '/28', '/41'):
            self.assertIn(suffix, report)
        self.assertIn('runtime_host_tests_verified=false', report)

    def test_chat_distribution_has_core_rules(self):
        # Build a fresh test distribution rather than relying on ZIPs checked into Git.
        subprocess.run(
            [sys.executable, str(ROOT / 'scripts/build_distributions.py'),
             '--project-root', str(ROOT), '--version', 'ci-test'],
            check=True, cwd=ROOT)
        archive = ROOT / 'dist' / 'manualletaren-chat-ci-test.zip'
        with zipfile.ZipFile(archive) as z:
            self.assertIsNone(z.testzip())
            instructions = z.read('assistant/instructions.md').decode('utf-8')
            self.assertIn('E-Nr', instructions)
            self.assertIn('Verifierad', instructions)
