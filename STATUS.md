# Manualletaren – projektstatus

**Version:** 0.7.0-dev. **Migrering:** GPT Byggaren v1.6.14 på PR #3.

## Klar i migrationsbranchen
- Canonical modell, projektstatus och två Skills har skapats.
- Originalmotorns åtta källfiler (byggare, installerare, validatorer och delade bibliotek) är **byte-identiska** med Git-taggen `erland/gpt-byggaren@v1.6.14` enligt Git blob-SHA.
- Den gamla ZIP-assemblern har ersatts med en bakåtkompatibel delegator till originalmotorn.
- GitHub Actions använder canonical lint, projekttester, originalmotorns byggning och validering.
- GitHub Actions har passerat kontrollen av sex ZIP-arkiv för projektet och dess fem runtime-distributioner.
- Byggdokumentation och release-workflow är uppdaterade.

## Kvarstående acceptans
- Praktiska installerade hosttester av webbsökning, dokumentåtkomst, PDF-innehåll och exakt modellmatchning.
- Fortsatt verifiering av domänscenarier och installerade värdmiljöer före stabil release.
- `project-status.yaml` är auktoritativ status, medan `project/status.json` används för äldre kontroller och hålls synkroniserad.
- Separat releasebeslut.

**Releaseklar:** nej. **Aktiverade runtimes:** inga.

Se `project-status.yaml`, `project/status.json` och `docs/MIGRATION-GPT-BYGGAREN-1.6.14.md`.
