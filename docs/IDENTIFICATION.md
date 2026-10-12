# Produktidentifiering – beslutsregler

## Källbelagda kandidater
- Varje kandidat måste ha en faktisk källa (helst tillverkarens produktsida). Matchningsmotorn söker **inte** på webben; webbläsaren/assistenten samlar in kandidater och belägg först.
- Välj den uppgift som effektivast skiljer kvarvarande kandidater åt enligt kärnans regel om en fråga per tur.
- Första prioritet är fullständigt modell-/produktnummer, inklusive suffix/revision; därefter region, variant, kategori och ungefärligt år.
- Förväxla inte serie-/individnummer med modell-/produktnummer. Be användaren maskera serienummer om det inte behövs.
- Ungefärligt inköpsår ska **aldrig** ensamt bekräfta identiteten; fråga vid behov om det är inköp eller tillverkningsår.
- Ett foto av produktens framsida ger ledtrådar men är inte en verifierad identitet. Typskyltsfotografier med läsbar modellkod är starkare.

## Säker åtskillnad
- Fuzzy-matcha inte mycket korta koder; prefixmatchning kräver minst fyra normaliserade tecken.
- Fel märke utesluter kandidat. Belagd motstridig region eller variant utesluter kandidat. Okänd region/variant betyder otillräcklig information, inte bekräftelse.
- Presentera källbelagda kandidater med konkreta skillnader i modellkod/variant inom kärnans gräns för antal.
- Matchningsmotorns poäng är endast intern sorteringshjälp, aldrig sannolikhet eller verifikationsstatus.
- En exakt modellträff avslutar endast identifieringssteget; överlämna sedan kandidat och källbelägg till manualverifieringen enligt kärnans statusregler.
- Är flera kandidater lika rimliga, välj inte en godtyckligt. Be om en skiljande uppgift eller lämna flera som preliminära.
- Ingen kandidat? Uppge osäkerheten, föreslå typskylt eller officiell support; hitta inte på beteckningar.

## Var finns typskylten?
Ge *exempel*, inte garanterade placeringar: diskmaskin oftast runt luckans kant; tvättmaskin runt lucköppningen eller baksidan; verktyg på höljet; TV bakom apparaten. Be användaren undvika demontering eller farliga moment.

## Exempel på källoberoende scenario
`Maker=A, model=ABC123/01` och `Maker=A, model=ABC123/02` är **olika varianter** tills tillverkarens manual bevisligen omfattar båda. Årtal 2018 räcker inte för att välja mellan dem.
