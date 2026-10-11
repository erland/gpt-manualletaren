# Runtimekompatibilitet – granskning v0.4.0-dev

## Beslut
**Ingen runtime är aktiverad eller liveverifierad.** Projektet kan beskriva sitt arbetsflöde portabelt, men funktionell aktivering kräver verifierade hostverktyg. Webbåtkomst och verklig läsning av en specifik manual är obligatoriska för full funktion. Bildanalys är önskvärd men inte obligatorisk.

| Runtime | Trolig distributionsform | Kritisk hostkontroll | Status |
|---|---|---|---|
| ChatGPT Chat | Instruktioner/projekt-ZIP | Webbresultat, länkåtkomst och faktisk manualtext/PDF; mobil/webb | Kandidat, ej testad |
| OpenAI Plugin | Skills-first med instruktion/resurser | Plugin-skill ger inte automatiskt webb-/PDF-verktyg; testa på installerad host | Kandidat, ej testad |
| Claude Projects | Projektinstruktioner + knowledge | Kontrollera att webbsökning och dokumentsläsning fungerar i projektet | Kandidat, ej testad |
| Claude Skills | Skill + resurser | Kontrollera verktyg i aktuell körmiljö och skill-anrop | Kandidat, ej testad |
| OpenCode | Agent/skill + verktygsinställningar | websearch/webfetch, åtkomst till dokument/PDF samt behörigheter | Kandidat, ej testad |
| ChatGPT Custom | Historisk, ej aktiv | Kräver separat beslut | Ej distributionsmål |

## Funktionsgates
1. `web_search`: kan söka efter manual på tillverkarens sida och ge en faktisk URL.
2. `source_access`: kan öppna den relevanta länken och urskilja supportsida från manual.
3. `manual_content_read`: kan faktiskt läsa relevanta delar i manualen och jämföra modell/variant.
4. `image_input` är valfritt: foto av typskylt ska kunna användas, men får inte ensam verifiera produkten.
5. `code_execution` är valfritt under användarsessionen: deterministiska utvecklingsscript körs vid build/CI.

`src/runtime/readiness.py` godkänner bara explicit `passed` från verkliga hosttester. Tom/okänd evidens blockerar aktivering. Testmodulen demonstrerar spärren offline, den utför **inte** hosttesterna. Automatisk övergång till aktivering är förbjuden; mänskligt reproducerbar testlogg krävs.

## Hosttestscenarier
- **T1:** Ange exakt modell och revision, få träff hos officiell tillverkare; verifiera dokumentets modellkoppling och faktisk text.
- **T2:** Ange märke, kategori och ungefärligt år; få källbelagda kandidater och en träffsäker följdfråga.
- **T3:** Ange närliggande modell med fel region/suffix; systemet får inte hävda `Verifierad`.
- **T4:** Källa ger endast supportportal/otillgänglig PDF; status får inte uppgraderas till `Verifierad`.
- **T5:** Stäng av webbåtkomst; resultatet ska tydligt ange begränsning och inte hitta på en URL.
- **T6 (valfri):** Fotografera typskylt; identifiera enbart modelluppgifter utan att begära individserienummer.

## Källor granskade 2026-10-11
- OpenAI: https://help.openai.com/en/articles/20001256-plugins-in-chatgpt
- OpenAI: https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt
- Anthropic: https://support.claude.com/en/articles/10684626-enable-and-use-web-search
- Anthropic: https://support.claude.com/en/articles/9517075-what-are-projects
- OpenCode: https://docs.opencode.ai/docs/tools/

Dokumentationen visar möjliga värdfunktioner, inte att dessa är aktiverade i användarens konto eller fungerar med varje manual.
