# Manualletaren

## Syfte

Manualletaren är en svensk GPT för att identifiera produkter och hitta rätt användarmanual från verifierbara källor. Den ska kunna arbeta från partiella produktuppgifter utan att överdriva säkerheten i modell- och dokumentmatchningar.

## Canonical källor

- `src/canonical/instructions.md` — gemensamma beteenderegelverket
- `docs/IDENTIFICATION.md` — produktidentifiering
- `docs/MANUAL-SEARCH.md` — manualsökning och dokumentkontroll
- `docs/RUNTIME-PARITY.md` — hostbegränsningar
- `gpt-project.yaml` — projektets maskinläsbara distributionskontrakt

## Build och distribution

Originalmotorn från GPT Byggaren v1.6.19 är avsedd att bygga projekt-ZIP och fem separata runtime-arkiv. GitHub Actions har verifierat lint, projekttester och distributionsbyggen. Praktiska hosttester återstår före stabil release.

## Kvalitetsgränser

- Produktidentifiering med källstöd och en bästa särskiljande fråga åt gången
- Ingen bekräftad modell eller manual utan bevis för rätt modell, variant och region
- Verklig åtkomst till manualinnehåll krävs för verifierad dokumentkoppling
- Ingen fabricerad länk, sidangivelse eller påstådd runtimekapacitet

Se `STATUS.md` och `docs/MIGRATION-GPT-BYGGAREN-1.6.19.md` för migrationsstatus.
