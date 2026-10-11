import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
from manual_search.evidence import ManualEvidence, evaluate, sort_key

class ManualSearchTest(unittest.TestCase):
    def fixture(self, **changes):
        values = dict(url='https://example.com/manual.pdf',title='Test',source_kind='manufacturer',content_checked=True,link_checked=True,document_type='user_manual',listed_models=('ABC/02',),language='sv',region='SE')
        values.update(changes)
        return ManualEvidence(**values)
    def test_exact_match(self): self.assertEqual(evaluate('ABC/02', self.fixture(), 'SE')['status'], 'Verifierad')
    def test_formatting(self): self.assertEqual(evaluate('abc 02',self.fixture())['status'], 'Verifierad')
    def test_variant_collision(self): self.assertEqual(evaluate('ABC/01',self.fixture())['status'], 'Ej fastställd')
    def test_region(self): self.assertEqual(evaluate('ABC/02',self.fixture(), 'US')['status'], 'Ej fastställd')
    def test_unchecked_link(self): self.assertEqual(evaluate('ABC/02',self.fixture(link_checked=False))['status'], 'Trolig – kontroll krävs')
    def test_unchecked_content(self): self.assertEqual(evaluate('ABC/02',self.fixture(content_checked=False))['status'], 'Trolig – kontroll krävs')
    def test_support_page(self): self.assertEqual(evaluate('ABC/02',self.fixture(document_type='support_page'))['status'], 'Ej fastställd')
    def test_installation_only(self): self.assertEqual(evaluate('ABC/02',self.fixture(document_type='installation'))['status'], 'Ej fastställd')
    def test_missing_model(self): self.assertEqual(evaluate('ABC/02',self.fixture(listed_models=()))['status'], 'Ej fastställd')
    def test_invalid_scheme(self): self.assertEqual(evaluate('ABC/02',self.fixture(url='http://example.com/manual.pdf'))['status'], 'Ej fastställd')
    def test_no_embedded_credentials(self): self.assertEqual(evaluate('ABC/02',self.fixture(url='https://user:pass@example.com/a'))['status'], 'Ej fastställd')
    def test_language_priority(self): self.assertLess(sort_key(self.fixture(language='sv')),sort_key(self.fixture(language='en')))
    def test_official_priority(self): self.assertLess(sort_key(self.fixture(source_kind='manufacturer',language='en')),sort_key(self.fixture(source_kind='third_party',language='sv')))
if __name__=='__main__': unittest.main()
