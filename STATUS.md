# Manualletaren – projektstatus

**Projektversion:** 0.7.0-dev. **Byggmotor:** GPT Byggaren v1.6.19 (PR #5, omergad).

## Verifierat
- Canonical projektmodell och två separata domän-Skills finns kvar.
- Centrala bygg-, lint-, distributions- och Skills-bibliotek är hämtade från GPT Byggarens v1.6.19-tagg.
- GitHub Actions kör lint, domän- och regressionstester samt bygger och validerar sex arkiv.
- CI har passerat på versionsmigreringen; se `docs/MIGRATION-GPT-BYGGAREN-1.6.19.md`.
- `project-status.yaml` är normerande; `project/status.json` hålls synkroniserad för bakåtkompatibilitet.

## Kvarstår
- Installerade hosttester av webbsökning, PDF-innehåll och exakt modell-/variantkoppling.
- Separat beslut om merge och stabil release.

**Releaseklar:** nej. **Aktiverade runtimes:** inga.
