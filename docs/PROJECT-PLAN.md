# Utvecklingsplan – Manualletaren

## Mål
Hitta en korrekt användarmanual även med ofullständiga produktuppgifter, med källstöd och transparent osäkerhet.

## Steg och gates
1. **Projektgrund** – canonical instruktion, kontrakt, status, README, CI, teststruktur och komplett ZIP. Gate: projektvalidering + tester + ZIP integritet.
2. **Produktidentifiering** – definiera och testa modellkandidater, följdfrågor, typskyltsanalys och falska positiva. Gate: scenario- och gränsfallstester.
3. **Manualsökning** – sökstrategier, källhierarki, modellkoppling, språk och länkkvalitet. Gate: riktiga tillverkares sökingångar granskade + offline-kontroller av käll- och modellmatchning; live-verifiering av specifik manual markeras separat.
4. **Runtimekontroll** – bedöm host-stöd för ChatGPT Chat, OpenAI Plugin, Claude och OpenCode; dokumentera funktionella skillnader och testgates. **Genomförd som statisk granskning; verkliga hosttester väntar.**
5. **Distribution och release** – bygg aktiverade distributioner via canonical source, kör runtime-specifik validering och release-readiness.

## Provfall att utöka
- Exakt Bosch E-Nr med revision
- Ofullständig diskmaskinsbeskrivning, cirka 2018
- Samma modellfamilj men olika regioner
- Typskylt med både serie- och modellnummer
- Produkt som saknar offentlig manual
- Träff från inofficiell PDF-host som inte går att verifiera
- Fråga om innehåll i en ännu inte läst manual

## Avgränsningar
Ingen egen crawlingplattform, PDF-hosting, persistent användarprofil eller leverantörsspecifik integration i första versionen.

## Steg 5 – distributioner
GPT Byggarens originalmotor v1.6.14 har i GitHub Actions byggt och validerat sex ZIP-filer (projektet och fem runtime-distributioner). Nästa releaseblockerare är praktiska installerade hosttester. Canonical status finns i `project-status.yaml`; `project/status.json` är en kompatibilitetsspegel för äldre domäntester.

## Steg 6 – praktisk källkontroll
Officiell IKEA KALLAX-produktlänk följdes till en faktisk 36-sidig monterings-PDF. Se `docs/ACCEPTANCE-TESTS.md`. Inte en verifierad användarmanual och inte ett installerat hosttest. Fortsatt blockerare: T1–T5 i verklig installerad runtime.

## Steg 7 – migrering och projekthygien (2026-10-12)
Originalmotor, canonical lint, CI och distributionsvalidering är införda. Två strukturella resurspunkter för konversationsstartare och runtime-policy behålls enligt originalmotorns kontrakt, men dokumenterar nu tydligt att inga separata regler har definierats. Domänimplementationerna och deras tester behålls. Stabil release och runtimeparitet kräver installerade hosttester.
