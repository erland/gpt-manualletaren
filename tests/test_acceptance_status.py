import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class AcceptanceTests(unittest.TestCase):
 def test_report_present(self):
  report=(ROOT/'docs/ACCEPTANCE-TESTS.md').read_text(encoding='utf-8')
  self.assertIn('906.533.26',report)
  self.assertIn('monteringsanvisning',report.lower())
  self.assertIn('runtime_host_tests_verified',report)
 def test_smoke_test_does_not_activate(self):
  s=json.loads((ROOT/'project/status.json').read_text())
  self.assertTrue(s['live_document_chain_checked'])
  self.assertFalse(s['live_manual_matching_verified'])
  self.assertFalse(s['runtime_host_tests_verified'])
  self.assertFalse(s['release_ready'])
  self.assertTrue(s['live_variant_ambiguity_checked'])
  self.assertEqual(s['runtimes_activated'],[])

