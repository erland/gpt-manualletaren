# Acceptanstest – faktisk webbsökning, 2026-10-11

## Testmiljö och omfattning
Testoperatör: ChatGPT med tillgängligt webbläsningsverktyg, inte en separat installerad Manualletaren-distribution. Följande resultat är en manuellt observerad kontroll av källor och dokument; den ger **inte** godkänd hostteststatus för ChatGPT Chat-distributionen eller någon annan runtime.

### A1 – Känd produkt, officiell PDF: GODKÄND för källkedjan
- Fråga: ”Hitta monteringsanvisningen till IKEA KALLAX, artikelnummer 906.533.26.”
- Produktkälla: https://www.ikea.com/se/sv/p/kallax-hylla-brun-valnoetsmoenstrad-90653326/
- Identifiering: IKEA KALLAX, hylla 77 × 147 cm, brun valnötsmönstrad, artikelnummer 906.533.26. På officiell produktsida anges dokument under ”Montering och dokument” med artikelnumret.
- Direkt PDF från samma produktsida: https://www.ikea.com/se/sv/assembly_instructions/kallax-hylla-brun-valnoetsmoenstrad__AA-2703433-1-2.pdf
- PDF öppnades i verktyget, identifierades som `application/pdf`, 36 sidor; första sidan visar KALLAX och svenskt varningstextavsnitt finns på PDF:s sida 3 (nollbaserat index 2).
- Utfallet verifierar länkkedjan och dokumenttyp `installation`/monteringsanvisning. Det är **inte** en generell användarmanual. Källsidans artikelnummer är belagt, men PDF-omslaget visar bara KALLAX, varför kopplingen baseras på tillverkarens produktlänk, inte på att artikelnumret står på omslaget.
- Förväntat användarsvar: presentera dokumentet som **monteringsanvisning** från officiell IKEA-sida, inte etiketten ”användarmanual”.

### A2 – Saknad exakt modell: DELVIS GENOMFÖRD
- Fall: ”Jag behöver manualen till en Bosch diskmaskin från omkring 2018.”
- Kontrollerat beteende i canonical instruktion: fråga efter E-Nr/typskylt, gissa inte en modell baserat på ungefärligt år.
- Inga faktiska kandidatmodeller eller riktiga manual-PDF:er har verifierats i detta test. Scenariot är inte godkänt som praktiskt end-to-end-hosttest.

### A3 – Närliggande variant och fel dokumentslag: EJ PRAKTISKT GENOMFÖRD
- Krav: Förväxla inte suffix, region eller installationsanvisning med användarmanual. Offline-regeltester finns; separat interaktivt hosttest återstår.

## Beslut
- `real_world_source_entrypoints_checked`: true
- `live_document_chain_checked`: true, begränsat till ett offentligt IKEA-exempel
- `live_user_manual_matching_verified`: false (kontrollerat dokument är monteringsanvisning)
- `runtime_host_tests_verified`: false
- `runtimes_activated`: []
- `release_ready`: false

## Nästa acceptansgate
Kör den installerade ChatGPT Chat-distributionen med T1–T5 från `docs/RUNTIME-PARITY.md`. Dokumentera prompt, svar, datum, källa, PDF-innehåll, korrekt/fel och pass/fail. Välj en användarmanual med exakt variant och en verkligt tvetydig produkt. Först därefter kan dess hoststatus uppdateras; andra runtimes kräver egna separata tester.


## A4 – Verkligt tvetydig Bosch-modell, 2026-10-11: DELVIS GODKÄND
- Ingång: ”Jag har en Bosch SMS46MI08E diskmaskin, manual?”
- Officiell Bosch-sökning visar minst följande revisionsvarianter: `SMS46MI08E/01`, `/27`, `/28`, `/41`. Belägg: https://www.bosch-home.com/it/support/list/SMS46MI08E
- Officiell supportsida för `/01` listar uttryckligen `User Manual`, `Short Instructions`, `Installation Instruction` som olika dokumenttyper: https://www.bosch-home.com/us/en/productservice/SMS46MI08E-01
- Förväntad uppföljning: ”Kan du läsa hela E-numret från typskylten, även siffrorna efter snedstrecket? På diskmaskiner finns den ofta vid luckans kant.”
- Utfall: riktig revisions-tvetydighet belagd och ett korrekt nästa dialogsteg definierat. Ingen PDF-innehållsgranskning och ingen faktiskt installerad ChatGPT-session.
- Bedömning: **godkänt som realvärldsunderlag till testfallet**, **ej godkänt som installerat hosttest eller verifierad användarmanual**.

## Status efter steg 6 – faktiskt ChatGPT Chat-paket granskat
- ZIP `dist/manualletaren-chatgpt-chat-v0.6.0-dev.zip` innehåller `instructions.md`, `references/IDENTIFICATION.md`, `references/MANUAL-SEARCH.md`, `references/RUNTIME-PARITY.md` och `COMPATIBILITY.json`.
- Instruktionen förbjuder fabricerade PDF-länkar och kräver matchande revision och dokumenttyp.
- Paketets filer är granskade lokalt, men paketet har **inte** aktiverats som en ny separat ChatGPT-session.
- `runtime_host_tests_verified=false`, `live_manual_matching_verified=false`, `release_ready=false`.
- Nästa gate: Kör en faktisk session med ChatGPT Chat-ZIP och få ett manuellt bedömt transcript för (1) exakt modell+öppnad användarmanual och (2) ofullständig Bosch-revision med följdfråga.


## A5 – Användarrapporterat fullständigt ChatGPT-test, 2026-10-11
- Testaren uppger att Manualletaren användes i en separat ChatGPT-konversation.
- Rapport: GPT:n ställde relevanta identifieringsfrågor och gav korrekt manual.
- Delad konversation: https://chatgpt.com/share/6acb1a90-b8d8-83ed-ab70-f30f7ae60a47
- Resultat: **GODKÄNT enligt användarens bedömning** för identifieringsdialog och manualresultat.
- Begränsning: samtalsinnehåll, exakt modellkod, manual-URL och PDF-innehåll har inte kunnat granskas oberoende. Äldre A1–A4-utfall ändras inte retroaktivt.
- Releasebeslut: en stark positiv signal för ChatGPT Chat, men `runtime_host_tests_verified` och `release_ready` i strukturerad status förblir `false` tills dokumenterade belägg och tillämpliga gates finns.
