# Migreringsanalys – GPT Byggaren v1.6.14

**Projekt:** Manualletaren (`v0.7.0-dev`)  
**Mål:** Beteendebevarande migrering till originalmotorn från GPT Byggaren v1.6.14  
**Tillstånd:** Originalmotorn installerad och CI-verifierad; hostacceptans och releasebeslut återstår.

## Verifierade utgångspunkter

| Källa | Observation | Åtgärd |
| --- | --- | --- |
| `src/canonical/instructions.md` | En svensk canonical instruktion med tydliga krav på modell-, region- och manualverifiering | Behåll som källa för domänbeteende, anpassa projektmodellens referenser |
| `scripts/build_distributions.py` | Egen paketerare producerar fem distributionsarkiv utan GPT Byggarens originalmotor | Ersätt **först efter** fullständig projektmodell och verifierad originalmotor |
| `project/status.json` | `release_ready: false`, inga aktiverade runtimes, hosttester saknas | Bevara blockerad release-status |
| `docs/PROJECT-PLAN.md` | Domänsteg och releasegates definierade | Utöka med migrationsgates |
| `README.md` | Beskriver de fem distributionerna och begränsningarna | Uppdatera bygginstruktioner efter verifierad installation |

## Domänkontrakt som inte får gå förlorat

1. Följdfråga om en särskiljande egenskap åt gången när produktidentifieringen är osäker.
2. Använd endast belagda modellkandidater, normalt högst fem.
3. Skilj på modell, revision, produktnummer och marknadsregion.
4. Presentera aldrig en sökträff eller supportsida som en verifierad användarmanual.
5. Kräv verklig tillgång till och granskning av dokumentet för statusen **Verifierad**.
6. Behåll statuserna **Verifierad**, **Trolig – kontroll krävs** och **Ej fastställd**.
7. Hitta aldrig på länkar, dokumentcitat, sidnummer eller modellkoder.
8. Redovisa begränsningar när webbsökning, bildtolkning eller PDF-läsning saknas.

## Målarkitektur

- **Canonical källa:** projektunik instruktion, kompletterande manual- och identifieringskunskap samt tydliga capability-/verktygskontrakt.
- **Projektmodell:** `gpt-project.yaml` och `project-status.yaml` enligt den versionerade originalmotorns kontrakt; fem explicita `build_system.runtime_targets` samt `runtime.chat_zip`, `runtime.plugin`, `runtime.claude`, `runtime.opencode` och inaktiverad `runtime.custom_gpt`.
- **Skills:** lämplig uppdelning i produktidentifiering och manualsökning/dokumentverifiering, med delade principer för samtliga runtime-mål. Skills får inte hävda tillgång till verktyg som saknas.
- **Byggsystem:** originalmotorns verifierade skript och mallar från Git-taggen v1.6.14; upstream-installationsskriptet medföljer. Inga egenutvecklade ersättningsbyggare.
- **Utdata:** separat projekt-ZIP och de fem runtime-arkiven ChatGPT Chat, OpenAI Plugin, Claude Projects, Claude Skills och OpenCode.
- **CI:** GitHub Actions ska köra originalmotorns lint, tester och byggvalidering på PR och release; `dist/` ska inte versionshanteras.

## Säker migrationsordning

1. Inventera kvarvarande `src/`, `project/`, `scripts/`, `tests/`, `docs/` och `.github/workflows/`; spara källor och verifiera gamla tester.
2. Skapa projektunik `gpt-project.yaml`, kontrakt, status och Skills med bevarat domänbeteende. Kontrollera att inga GPT Byggaren-specifika innehållsfiler råkat kopieras.
3. Installera originalmotor v1.6.14 från bifogad runtime-distribution. Om den inte är tillgänglig: avbryt motorbyte, redovisa beroendet.
4. Kör originalmotorns projektsjälvtest, lint, distributionsbyggare och validatorer. Bekräfta sex artefakter och innehållsintegritet.
5. Jämför gamla och nya domänscenarier, särskilt icke-verifierade manualer, fel region/revision, ofullständiga modelluppgifter, bildbegränsningar och otillgängliga PDF:er.
6. Uppdatera README, distributions-, runtime- och acceptanstestdokumentationen; ta bort gamla byggskript **endast när** den nya CI-kedjan är grön.
7. Redovisa kvarvarande verkliga hosttester. Markera inte stabil release eller runtimeparitet baserat enbart på ZIP-validering.

## Nuvarande blockerare

Installerade hosttester för webbsökning, dokumentläsning och modellkoppling återstår. Canonical lint, tester och sex distributioner är redan CI-verifierade; ingen runtime är aktiverad och stabil release är inte godkänd.

## Genomförande och verifiering, 12 oktober 2026

- Installerade den ursprungliga distributonsmotorns åtta källfiler från den versionslåsta Git-taggen `erland/gpt-byggaren@v1.6.14`. Alla åtta jämfördes separat med Git blob-SHA och var identiska.
- Kompletterade projektmodellen med Knowledge-källa, runtime-mallar, Skills-kontrakt och de schemafiler som krävs för lint.
- Uppdaterade tester som använde den gamla, interna `build()`-funktionen till originalmotorns CLI, och anpassade testernas versionsnamn så att exakt sex arkiv genereras.
- Anpassade PR-CI och release-workflow till `scripts/lint_gpt_project.py`, `scripts/build_distributions.py` och `scripts/validate_distributions.py`.
- GitHub Actions genomförde godkänd lint, projektets unittest-svit, byggning, distributionvalidering, och ZIP-/leveransmanifestkontroll för sex arkiv (bl.a. commit `75e5b53a` och `2df87fdf`).
- `scripts/build.py` är nu endast en delegator, utan separat ZIP-assembler. Dokumentationen beskriver canonical kommandon.

**Verifieringsgräns:** Godkänt CI och sex giltiga ZIP betyder inte att den installerade assistenten har verifierad åtkomst till produktwebb, PDF-innehåll eller exakt manual/variant. Därför kvarstår release-gaten; `release_ready: false` och inga aktiverade runtimes.

**Nästa steg:** manuell domän- och hostacceptans, städa historiska filer med avgränsad påverkan, och besluta först därefter om merge/release.
