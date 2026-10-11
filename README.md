# Manualletaren

En svenskspråkig GPT som hjälper användare att identifiera produkter och hitta rätt användarmanual med verifierbara källor, även utan exakt modellbeteckning.

**Aktuell projektversion:** v0.7.0-dev. **Status:** utvecklingsprojekt med godkänd GitHub-CI och användarrapporterat lyckat ChatGPT-test. Ingen stabil release eller verifierad runtimeparitet ännu.

## Så fungerar det

1. Tolka användarens uppgifter, även ofullständiga eller osäkra.
2. Sök produktkandidater hos tillverkare och andra kontrollerbara källor.
3. Ställ en riktad följdfråga när flera modeller eller revisioner återstår.
4. Kontrollera manualens dokumenttyp, källa och uttryckliga modell-/variantstöd.
5. Presentera relevant länk med språk och tydlig matchningsstatus.

## Projektets källor och status

- Canonical instruktion: `src/canonical/instructions.md`
- Produktidentifiering: `docs/IDENTIFICATION.md`
- Manualsökning och beläggskrav: `docs/MANUAL-SEARCH.md`
- Utvecklingsplan: `docs/PROJECT-PLAN.md`
- Strukturerad projektstatus: `project/status.json`
- Runtimebegränsningar: `docs/RUNTIME-PARITY.md`
- Distributionsbeskrivning: `docs/DISTRIBUTIONS.md`
- Acceptanstester: `docs/ACCEPTANCE-TESTS.md`

## Utveckling och tester

```bash
python3 scripts/validate_project.py
python3 -m unittest discover -s tests -v
python3 scripts/build_distributions.py --version 0.7.0-dev
```

GitHub Actions kör validering och tester vid pull requests. Release-workflow kör vid taggar `v*` och använder taggversionen vid byggning. Verifiera alltid det publicerade paketet innan det kallas en stabil release.

## Distributioner

Projektet bygger kandidater för ChatGPT Chat, OpenAI Plugin, Claude Projects, Claude Skills och OpenCode. Samma canonical instruktion ligger till grund för paketeringen. **Att en ZIP byggs innebär inte att dess runtimefunktioner är verifierade.** Installations- och funktionskontroller ska göras separat för varje miljö.

## Praktiskt test, 11 oktober 2026

Användaren har rapporterat att en ChatGPT-konversation med Manualletaren ställde relevanta frågor och ledde fram till korrekt manual. Detta dokumenteras som ett **användarrapporterat godkänt end-to-end-test**, inte som oberoende verifierad PDF-/modellmatchning; transcript och exakta belägg kunde inte granskas direkt.

Se `docs/ACCEPTANCE-TESTS.md` för övriga källkontroller och kvarstående releasekrav.
