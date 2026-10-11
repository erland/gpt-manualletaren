"""Pure evaluation of supplied manual evidence. No fetch, browsing or PDF decoding."""
from dataclasses import dataclass
from urllib.parse import urlparse
import re

@dataclass(frozen=True)
class ManualEvidence:
    url: str
    title: str
    source_kind: str  # manufacturer | authorized | third_party
    content_checked: bool
    document_type: str  # user_manual | installation | quick_start | support_page | unknown
    listed_models: tuple[str, ...] = ()
    language: str = 'unknown'
    region: str = ''
    source_page: str = ''
    link_checked: bool = False


def normalize(value: str) -> str:
    return re.sub(r'[^A-Z0-9]', '', value.upper())


def evaluate(product_model: str, evidence: ManualEvidence, product_region: str = '') -> dict:
    """Never certify a match without the model *and* document being checked.

    Caller must supply checked evidence from actual documents; this function never
    infers checking from a URL's appearance or tests reachability on its own.
    """
    parsed = urlparse(evidence.url)
    if parsed.scheme != 'https' or not parsed.netloc or parsed.username or parsed.password:
        return {'status': 'Ej fastställd', 'reason': 'Ingen giltig HTTPS-källa', 'verified': False}
    if evidence.document_type != 'user_manual':
        return {'status': 'Ej fastställd', 'reason': 'Inte verifierad som användarmanual', 'verified': False}
    if not product_model or not evidence.listed_models:
        return {'status': 'Ej fastställd', 'reason': 'Saknar produkt- eller dokumentmodell', 'verified': False}
    exact = normalize(product_model) in {normalize(x) for x in evidence.listed_models}
    if not exact:
        return {'status': 'Ej fastställd', 'reason': 'Exakt modell/variant saknas i manualens modellförteckning', 'verified': False}
    if product_region and evidence.region and product_region.casefold() != evidence.region.casefold():
        return {'status': 'Ej fastställd', 'reason': 'Regionkonflikt', 'verified': False}
    if not evidence.content_checked or not evidence.link_checked:
        return {'status': 'Trolig – kontroll krävs', 'reason': 'Modelluppgift finns men dokument/länk har inte kontrollerats', 'verified': False}
    return {'status': 'Verifierad', 'reason': 'Exakt modell återfinns i kontrollerad användarmanual och länken är kontrollerad', 'verified': True}


def sort_key(evidence: ManualEvidence) -> tuple:
    """Source quality first; Swedish, then English; never manufacture matches."""
    source_rank = {'manufacturer': 0, 'authorized': 1, 'third_party': 2}
    language_rank = {'sv': 0, 'svenska': 0, 'en': 1, 'english': 1}
    return (source_rank.get(evidence.source_kind, 3), language_rank.get(evidence.language.casefold(), 2))
