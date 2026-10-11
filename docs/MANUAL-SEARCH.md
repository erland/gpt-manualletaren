# Manualsökning – steg 3

## Sökning

1. Identifiera modell/variant enligt `docs/IDENTIFICATION.md`. Skilj modell, produktnummer, serie/individnummer och region.
2. Sök tillverkarens officiella manualsida med exakt identifierare. Om bara partiell modell finns: sök identifierbara kandidater och ställ en särskiljande fråga.
3. Sök därefter auktoriserad support, och först därefter tredjepartsarkiv. En oberoende manualhost är inte automatiskt falsk men kräver extra belägg.
4. Dokumentera originalkällan och direktdokument-URL var för sig. En supportsida med sökfält är en **hitta-manual-ingång**, inte ett bevis för en viss manual.
5. Kontrollera att länken leder till rätt dokumenttyp, att innehåll kan granskas och att modellförteckningen täcker exakt modell/variant. Konstatera tydligt om webbläsare/PDF-läsare inte kan verifiera detta.
6. Hantera olika regioner och varianter separat. Svenska prioriteras framför engelska när källkvalitet och matchning är likvärdiga. En svensk felmodell är aldrig bättre än korrekt engelsk modell.
7. Källhänvisa till kontrollerade uppgifter; ange besökt åtkomstdatum i livefall. Påstå inte att nätverkskontroller har körts när bara deterministiska offline-tester körts.

## Statusdefinitioner

- **Verifierad:** Faktisk användarmanual öppnad/granskad, fungerande mål-länk kontrollerad och exakt modell eller uttrycklig modellvariant återfinns i dokumentet, utan regionkonflikt.
- **Trolig – kontroll krävs:** Modellkoppling finns i källmaterial men dokumentet eller direktlänken kan inte kontrolleras fullständigt. Kräver identifierad produktmodell; aldrig enbart liknande namn.
- **Ej fastställd:** Endast ingångssida eller sökträff, fel dokumenttyp, avvikande region/variant, saknade dokumentuppgifter eller inget resultat.

## Tillverkarspecifika ingångar (verifierade webbsidor, 2026-10-11)

- Bosch Sverige: https://www.bosch-home.se/service/om-du-behover-hjalp/bruksanvisningar – stödjer sökning på E-nummer inklusive variant `/xx`.
- Electrolux Sverige: https://www.electrolux.se/support/user-manuals/ – stödjer modell eller produktnummer (PNC), även foto på produktdekal.
- IKEA Sverige: https://www.ikea.com/se/sv/customer-service/product-support/ – support och anvisningar; produktsidorna kan visa monteringsanvisningar. För IKEA-vitvaror kan artikel- och servicenummer behövas.

Dessa källor verifierar **sökingångar**, inte specifika manualmatchningar.

## Kontrollerat manualexempel

IKEA:s officiella dokument `https://www.ikea.com/se/sv/manuals/framtid-mw-mikrovagsugn__AA-486210-2.pdf` påträffades i webbsökning. Detta belägger att officiella dokument kan ha PDF-direktlänkar, **inte** att en viss användares mikro matchar just denna manual. Dokumentet får bara erbjudas som verifierad modellträff efter faktisk matchning av produktens artikel-/modellbeteckning med manualens innehåll.

## Automatisk kontroll

`src/manual_search/evidence.py` är en deterministisk bedömare för **redan inhämtade, uppgivna** evidensuppgifter. Den laddar inte ned manualer och verifierar inte själv källornas äkthet. Flaggan `content_checked` måste sättas först efter dokumentgranskning; `link_checked` först efter separat länkgranskning. URL-domän och källkategori är indata, inte automatiskt verifierade. Reglerna testas med syntetiska fixtures utan att låtsas vara livedata.
