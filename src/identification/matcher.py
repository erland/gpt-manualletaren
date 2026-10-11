"""Conservative product candidate matching; all candidates must come from evidence."""
from dataclasses import dataclass
import re
import unicodedata


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "").casefold()
    return re.sub(r"[^a-z0-9]+", "", value)


@dataclass(frozen=True)
class Candidate:
    maker: str
    model: str
    source_url: str
    category: str = ""
    region: str = ""
    variant: str = ""
    year_start: int | None = None
    year_end: int | None = None
    # Manually established from retrieved sources, never fabricated.


@dataclass(frozen=True)
class Query:
    maker: str = ""
    model: str = ""
    category: str = ""
    region: str = ""
    variant: str = ""
    approx_year: int | None = None


def evaluate(query: Query, candidates: list[Candidate]) -> list[dict]:
    """Rank sourced candidates without upgrading them to 'verified'."""
    result = []
    for c in candidates:
        if not c.source_url.startswith(("https://", "http://")):
            continue
        qmaker, cmaker = normalize(query.maker), normalize(c.maker)
        qmodel, cmodel = normalize(query.model), normalize(c.model)
        if qmaker and qmaker != cmaker:
            continue
        if query.category and c.category and normalize(query.category) != normalize(c.category):
            continue
        score, evidence, conflicts = 0, [], []
        if qmaker:
            score += 15
            evidence.append("märke")
        if qmodel:
            if qmodel == cmodel:
                score += 70
                evidence.append("exakt modellkod")
            elif len(qmodel) >= 4 and cmodel.startswith(qmodel):
                score += 28
                evidence.append("modellprefix")
            else:
                continue  # never fuzzy-match arbitrary short/ambiguous identifiers
        if query.region:
            if c.region and normalize(query.region) != normalize(c.region):
                conflicts.append("region")
            elif c.region:
                score += 5
                evidence.append("region")
        if query.variant:
            if c.variant and normalize(query.variant) != normalize(c.variant):
                conflicts.append("variant")
            elif c.variant:
                score += 10
                evidence.append("variant")
        if query.approx_year is not None and c.year_start is not None and c.year_end is not None:
            if c.year_start <= query.approx_year <= c.year_end:
                score += 3
                evidence.append("ungefärligt år")
            else:
                conflicts.append("årtal (svag uppgift)")
        # Region/variant mismatches cannot be overridden by a model-family match.
        if any(x in conflicts for x in ("region", "variant")):
            continue
        result.append({"candidate": c, "score": score, "evidence": evidence,
                       "notes": conflicts, "manual_verified": False})
    return sorted(result, key=lambda x: (-x["score"], x["candidate"].maker, x["candidate"].model))[:5]


def next_question(query: Query, candidates: list[Candidate]) -> str | None:
    """Choose one question that maximally distinguishes grounded candidates."""
    if not query.maker:
        return "Vilket märke står på produkten?"
    if not query.model:
        return "Kan du läsa modell- eller produktnumret på typskylten (gärna foto)?"
    if len(candidates) < 2:
        return None
    def choices(field):
        return {normalize(getattr(c, field)) for c in candidates if getattr(c, field)}
    if len(choices("variant")) > 1 and not query.variant:
        return "Vilken fullständig variant eller revision står efter modellbeteckningen?"
    if len(choices("region")) > 1 and not query.region:
        return "Vilket land eller vilken marknad är produkten avsedd för?"
    if len(choices("model")) > 1:
        return "Kan du fotografera typskylten så att hela modell-/produktnumret syns?"
    return None
