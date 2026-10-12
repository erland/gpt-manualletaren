# Manualletaren

En svenskspråkig GPT som hjälper användare att identifiera produkter och hitta rätt användarmanual med verifierbara källor, även utan exakt modellbeteckning.

**Aktuell projektversion:** v0.7.0-dev. **Byggmotor:** GPT Byggaren v1.6.19 på PR #5. Canonical lint, tester och sex distributionsarkiv har verifierats i GitHub Actions; installerade hosttester och stabil release återstår.

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
- Canonical projektmodell: `gpt-project.yaml`
- Canonical projektstatus: `project-status.yaml` (historisk status i `project/status.json`)
- Runtimebegränsningar: `docs/RUNTIME-PARITY.md`
- Distributionsbeskrivning: `docs/DISTRIBUTIONS.md`
- Acceptanstester: `docs/ACCEPTANCE-TESTS.md`

## Utveckling och tester

```bash
python3 -m pip install PyYAML jsonschema
python3 scripts/lint_gpt_project.py --project-root .
python3 scripts/validate_project.py
python3 -m unittest discover -s tests -v
python3 scripts/build_distributions.py --project-root . --version 0.7.0-dev
python3 scripts/validate_distributions.py --project-root .
```

GitHub Actions kör validering och tester vid pull requests. Release-workflow kör vid taggar `v*` och använder taggversionen vid byggning. Verifiera alltid det publicerade paketet innan det kallas en stabil release.

## Distributioner

Projektet bygger kandidater för ChatGPT Chat, OpenAI Plugin, Claude Projects, Claude Skills och OpenCode. GPT Byggarens originalmotor v1.6.19 bygger projekt-ZIP plus de fem runtime-arkiven från samma canonical instruktion. **Att en ZIP byggs innebär inte att dess runtimefunktioner är verifierade.** Installations- och funktionskontroller ska göras separat för varje miljö.

## Praktiskt test, 11 oktober 2026

Användaren har rapporterat att en ChatGPT-konversation med Manualletaren ställde relevanta frågor och ledde fram till korrekt manual. Detta dokumenteras som ett **användarrapporterat godkänt end-to-end-test**, inte som oberoende verifierad PDF-/modellmatchning; transcript och exakta belägg kunde inte granskas direkt.

Se `docs/ACCEPTANCE-TESTS.md` för övriga källkontroller och kvarstående releasekrav.
