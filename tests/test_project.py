import sys,unittest,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ProjectTests(unittest.TestCase):
 def test_canonical_source_exists(self): self.assertTrue((ROOT/'src/canonical/instructions.md').exists())
 def test_unverified_link_not_claimed(self):
  s=(ROOT/'src/canonical/instructions.md').read_text();self.assertIn('inte kan granskas',s)
 def test_not_released(self):
  s=json.loads((ROOT/'project/status.json').read_text());self.assertFalse(s['release_ready']);self.assertEqual(s['completed_steps'],[1,2,3,4,5])
 def test_runtime_parity_explicit(self):
  s=(ROOT/'docs/RUNTIME-PARITY.md').read_text();self.assertIn('OpenAI Plugin',s);self.assertIn('OpenCode',s)
if __name__=='__main__': unittest.main()
