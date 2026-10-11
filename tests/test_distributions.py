import sys,unittest,zipfile,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from build_distributions import build,TARGETS
class DistributionTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls): cls.results=build('0.5.0-dev-test')
 def test_five_targets(self): self.assertEqual(set(x['runtime'] for x in self.results),set(TARGETS))
 def test_all_are_unverified(self):
  for r in self.results:
   with zipfile.ZipFile(ROOT/'dist'/r['file']) as z:
    manifest=json.loads(z.read('COMPATIBILITY.json'))
    self.assertFalse(manifest['host_verified']);self.assertFalse(manifest['activated'])
 def test_canonical_consistency(self):
  expected=hashlib.sha256((ROOT/'src/canonical/instructions.md').read_bytes()).hexdigest()
  for r in self.results:
   with zipfile.ZipFile(ROOT/'dist'/r['file']) as z:
    self.assertEqual(json.loads(z.read('COMPATIBILITY.json'))['canonical_sha256'],expected)
 def test_no_mcp_json(self):
  for r in self.results:
   with zipfile.ZipFile(ROOT/'dist'/r['file']) as z:self.assertFalse(any(n.endswith('mcp.json') for n in z.namelist()))
 def test_instructions_present(self):
  for r in self.results:
   with zipfile.ZipFile(ROOT/'dist'/r['file']) as z:self.assertTrue(any(n.endswith('SKILL.md') or n in ('instructions.md','PROJECT-INSTRUCTIONS.md') for n in z.namelist()))
if __name__=='__main__': unittest.main()
