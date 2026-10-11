# Manualletaren

En svenskspråkig GPT som identifierar produkter och hittar rätt användarmanual med verifierbara källor.

**Status:** v0.4.0-dev, steg 4 (runtimegranskning). Detta är ett utvecklingsprojekt, inte en validerad release.

## Så fungerar det
1. Tolka användarens produktuppgifter, även osäkra.
2. Sök först officiella tillverkarkällor och modellbeteckningar.
3. Hitta kandidater och ställ en riktad följdfråga när modellen inte kan särskiljas.
4. Kontrollera att manualen gäller den identifierade modellen.
5. Leverera källhänvisad länk med språk och matchningsstatus.

Se `docs/MANUAL-SEARCH.md` för källhierarki, manualverifiering och verkliga sökingångar. Se `docs/IDENTIFICATION.md` för beslutsregler och `src/identification/matcher.py` för den konservativa, deterministiska kandidatenheten. Dessa ersätter inte verklig webbsökning eller granskning av manualinnehåll.

## Kom igång
- Börja i `src/canonical/instructions.md` (auktoritativa beteenderegler).
- Läs `docs/PROJECT-PLAN.md`, `project/status.json` och `docs/RUNTIME-PARITY.md`.
- Kör `python3 scripts/validate_project.py` och `python3 -m unittest discover -s tests -v`.
- Bygg paket: `python3 scripts/build.py --version 0.4.0-dev`.

Distributioner är ännu inte aktiverade: steg 3 omfattar manualsökningsregler och verifierade sökingångar, men inte automatiserad live-PDF-granskning, inte en påstått verifierad runtime.

## Runtimebeslut steg 4
Se `docs/RUNTIME-PARITY.md` och `src/contracts/runtime-requirements.json`. Inga runtimes är aktiverade: riktiga hosttester krävs för webbåtkomst, källöppning och läsning av specifik manual. Offlinekontroller är inte funktionella hosttester.

## Distributioner v0.5.0-dev
Se `docs/DISTRIBUTIONS.md`; bygg `python3 scripts/build_distributions.py --version 0.5.0-dev`. Dessa paket kräver hosttester före aktivering.

## Praktisk acceptanskontroll
Se `docs/ACCEPTANCE-TESTS.md` för ett test med en verklig IKEA-PDF samt kvarstående hosttester.

## v0.7.0-dev – Verklighetsbaserat revisionsfall
Bosch SMS46MI08E har flera officiellt listade revisioner. Acceptansrapporten dokumenterar detta samt begränsningen att inget installerat hosttest ännu genomförts.
