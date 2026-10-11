import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from scripts import build_distributions

ROOT = Path(__file__).resolve().parents[1]


class LiveEvidenceTests(unittest.TestCase):
    def test_bosch_variants_are_documented(self):
        report = (ROOT / 'docs/ACCEPTANCE-TESTS.md').read_text(encoding='utf-8')
        for suffix in ('/01', '/27', '/28', '/41'):
            self.assertIn(suffix, report)
        self.assertIn('runtime_host_tests_verified=false', report)

    def test_chat_distribution_has_core_rules(self):
        # Build a fresh test distribution rather than relying on ZIPs checked into Git.
        with tempfile.TemporaryDirectory() as temporary:
            with patch.object(build_distributions, 'OUT', Path(temporary)):
                build_distributions.build('test')
                archive = Path(temporary) / 'manualletaren-chatgpt-chat-vtest.zip'
                with zipfile.ZipFile(archive) as z:
                    self.assertIsNone(z.testzip())
                    instructions = z.read('instructions.md').decode('utf-8')
                    self.assertIn('E-Nr', instructions)
                    self.assertIn('Verifierad', instructions)
