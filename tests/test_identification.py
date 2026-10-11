import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from identification.matcher import Candidate, Query, evaluate, next_question, normalize

def c(model, **kwargs): return Candidate("Bosch",model,"https://example.org/model/"+model,category="dishwasher",**kwargs)

class IdentificationTests(unittest.TestCase):
    def test_normalization(self): self.assertEqual(normalize("ABC-123 / 01"),"abc12301")
    def test_exact_model_beats_prefix(self):
        r=evaluate(Query(maker="Bosch",model="ABC12301"),[c("ABC123/02"),c("ABC123/01")])
        self.assertEqual(r[0]["candidate"].model,"ABC123/01")
    def test_wrong_brand_excluded(self):
        self.assertFalse(evaluate(Query(maker="Electrolux"),[c("ABC123/01")]))
    def test_region_conflict_excluded(self):
        self.assertFalse(evaluate(Query(maker="Bosch",region="SE"),[c("ABC123/01",region="US")]))
    def test_variant_conflict_excluded(self):
        self.assertFalse(evaluate(Query(maker="Bosch",variant="02"),[c("ABC123",variant="01")]))
    def test_year_is_not_confirmation(self):
        r=evaluate(Query(maker="Bosch",approx_year=2018),[c("ABC123",year_start=2016,year_end=2020)])
        self.assertFalse(r[0]["manual_verified"])
    def test_unverified_source_excluded(self):
        self.assertFalse(evaluate(Query(maker="Bosch"),[Candidate("Bosch","AB12","invented-path")]))
    def test_short_model_not_fuzzy(self):
        self.assertFalse(evaluate(Query(maker="Bosch",model="AB"),[c("AB123")]))
    def test_one_question_model_first(self):
        self.assertIn("modell-", next_question(Query(maker="Bosch"),[c("AB123")]))
    def test_variant_question(self):
        q=next_question(Query(maker="Bosch",model="ABC123"),[c("ABC123",variant="01"),c("ABC123",variant="02")])
        self.assertIn("variant",q)
    def test_region_question(self):
        q=next_question(Query(maker="Bosch",model="ABC123"),[c("ABC123",region="SE"),c("ABC123",region="US")])
        self.assertIn("land",q)
    def test_no_question_single_candidate(self):
        self.assertIsNone(next_question(Query(maker="Bosch",model="ABC123"),[c("ABC123")]))
    def test_max_five(self):
        self.assertEqual(len(evaluate(Query(maker="Bosch"),[c(f"A{i}") for i in range(8)])),5)

if __name__=="__main__": unittest.main()
