# Manualsökning – steg 3

## Sökning

1. Ta emot identifierad eller preliminär modellkandidat med dess belägg från produktidentifieringen. Vid olöst tvetydighet: återgå till identifierings-Skill.
2. Sök tillverkarens officiella manualsida med belagd exakt identifierare. Om endast partiell modell finns: begär precisering via identifierings-Skill.
3. Sök därefter auktoriserad support, och först därefter tredjepartsarkiv. En oberoende manualhost är inte automatiskt falsk men kräver extra belägg.
4. Dokumentera originalkällan och direktdokument-URL var för sig. En supportsida med sökfält är en **hitta-manual-ingång**, inte ett bevis för en viss manual.
5. Kontrollera att länken leder till rätt dokumenttyp, att innehåll kan granskas och att modellförteckningen täcker exakt modell/variant. Konstatera tydligt om webbläsare/PDF-läsare inte kan verifiera detta.
6. Hantera olika regioner och varianter separat. Svenska prioriteras framför engelska när källkvalitet och matchning är likvärdiga. En svensk felmodell är aldrig bättre än korrekt engelsk modell.
7. Källhänvisa till kontrollerade uppgifter; ange besökt åtkomstdatum i livefall. Påstå inte att nätverkskontroller har körts när bara deterministiska offline-tester körts.

## Statusbedömning

Tillämpa exakt de tre normerande statusdefinitionerna i `src/canonical/instructions.md`. Denna Skill ansvarar för att samla belägg (länkgranskning, dokumenttyp, dokumentinnehåll, modell- och regionkoppling), inte för en egen alternativ klassificering. Vid endast supportsida eller otillgänglig PDF ska status inte höjas till `Verifierad`.

## Tillverkarspecifika ingångar (verifierade webbsidor, 2026-10-11)

- Bosch Sverige: https://www.bosch-home.se/service/om-du-behover-hjalp/bruksanvisningar – stödjer sökning på E-nummer inklusive variant `/xx`.
- Electrolux Sverige: https://www.electrolux.se/support/user-manuals/ – stödjer modell eller produktnummer (PNC), även foto på produktdekal.
- IKEA Sverige: https://www.ikea.com/se/sv/customer-service/product-support/ – support och anvisningar; produktsidorna kan visa monteringsanvisningar. För IKEA-vitvaror kan artikel- och servicenummer behövas.

Dessa källor verifierar **sökingångar**, inte specifika manualmatchningar.

## Kontrollerat manualexempel

IKEA:s officiella dokument `https://www.ikea.com/se/sv/manuals/framtid-mw-mikrovagsugn__AA-486210-2.pdf` påträffades i webbsökning. Detta belägger att officiella dokument kan ha PDF-direktlänkar, **inte** att en viss användares mikro matchar just denna manual. Dokumentet får bara erbjudas som verifierad modellträff efter faktisk matchning av produktens artikel-/modellbeteckning med manualens innehåll.

## Automatisk kontroll

`src/manual_search/evidence.py` är en deterministisk bedömare för **redan inhämtade, uppgivna** evidensuppgifter. Den laddar inte ned manualer och verifierar inte själv källornas äkthet. Flaggan `content_checked` måste sättas först efter dokumentgranskning; `link_checked` först efter separat länkgranskning. URL-domän och källkategori är indata, inte automatiskt verifierade. Reglerna testas med syntetiska fixtures utan att låtsas vara livedata.
