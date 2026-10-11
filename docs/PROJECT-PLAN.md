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
Fem distributioner byggda och strukturellt testade i v0.5.0-dev. Faktiska hosttester är nästa blockerande gate före releaseklar status.

## Steg 6 – praktisk källkontroll
Officiell IKEA KALLAX-produktlänk följdes till en faktisk 36-sidig monterings-PDF. Se `docs/ACCEPTANCE-TESTS.md`. Inte en verifierad användarmanual och inte ett installerat hosttest. Fortsatt blockerare: T1–T5 i verklig installerad runtime.
