# Migrering till GPT Byggaren v1.6.19

## Utgångsläge
Manualletaren är baserad på GPT Byggaren v1.6.14; tidigare PR #3 är mergad.
Den befintliga canonical instruktionen och de två domän-Skills som hanterar produktidentifiering respektive manualverifiering ska bevaras.

## Migrationsmål
- Använd den oförändrade originalmotorn från den bifogade GPT Byggaren Chat v1.6.19 som källa för bygg-, lint- och distributionsskript, deras beroenden och kontrakt.
- Säkerställ att alla motorkomponenter installeras samstämmigt; blanda inte v1.6.14- och v1.6.19-filer.
- Jämför projektets gpt-project.yaml mot v1.6.19-kontrakten och komplettera enbart nödvändiga fält.
- Behåll två semantiskt separata domän-Skills. Placera gemensamma beteenderegler i canonical kärnan och undvik duplicering.
- Behåll GitHub-arbetsflödet och sex arkiv (projekt + fem distributioner).
- Verifiera projektlint, projekttester, samtliga distributionsbyggnader, ZIP-integritet, checksumme- och manifestparitet samt GitHub-CI.
- Testa modell- och regionidentifiering, korrekta manualbelägg, riktade följdfrågor och oförändrat beteende utan hittad dokumentlänk.

## Utförandestatus
Originalmotorns centrala bygg-, validerings- och Skills-bibliotek från GPT Byggaren v1.6.19 är installerade från originaltaggen `erland/gpt-byggaren@v1.6.19`. GitHub Actions har passerat med denna motor i [run 38299824420](https://github.com/erland/gpt-manualletaren/actions/runs/38299824420). Projektets status anger nu byggarversion 1.6.19. Den första CI-körningen upptäckte ett saknat biblioteksberoende som åtgärdades före godkänd körning.

Installerade hosttester för sökning, faktisk manual-PDF och modell-/regionkoppling återstår. Releaseklar är fortfarande false.

## Kvalitetsgrindar före release
1. Installera fullständig originalmotor v1.6.19 utan handmodifiering.
2. Kör `python3 scripts/lint_gpt_project.py --project-root .`.
3. Kör `python3 scripts/validate_project.py` och `python3 -m unittest discover -s tests -v`.
4. Kör `python3 scripts/build_distributions.py --project-root . --version 0.7.0-dev`.
5. Kör `python3 scripts/validate_distributions.py --project-root .` och kontrollera samtliga sex ZIP samt manifest och SHA256SUMS.
6. Granska att testerna lyckats på GitHub Actions och uppdatera sedan versionsfält och projektstatus.
7. Låt host-acceptanstester och releasebeslut ligga kvar som öppna grindar tills de verkligen är utförda.

**Ingen merge eller release ingår i denna ändring.**
