import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class LiveEvidenceTests(unittest.TestCase):
 def test_bosch_variants_are_documented(self):
  report=(ROOT/'docs/ACCEPTANCE-TESTS.md').read_text()
  for suffix in ('/01','/27','/28','/41'):
   self.assertIn(suffix,report)
  self.assertIn('runtime_host_tests_verified=false', report)
 def test_chat_distribution_has_core_rules(self):
  import zipfile
  d=ROOT/'dist/manualletaren-chatgpt-chat-v0.7.0-dev.zip'
  with zipfile.ZipFile(d) as z:
   s=z.read('instructions.md').decode()
   self.assertIn('E-Nr',s)
   self.assertIn('Verifierad',s)
