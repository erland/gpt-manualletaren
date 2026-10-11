# Distributioner v0.5.0-dev

Fem installationskandidater genereras från `src/canonical/instructions.md`: ChatGPT Chat, OpenAI Plugin (skills-first), Claude Projects, Claude Skills och OpenCode. ChatGPT Custom är endast historiskt och byggs inte.

`python3 scripts/build_distributions.py --version 0.5.0-dev` skapar ZIP-filer och SHA-256-manifest i dist/.

**Status:** Strukturellt paketerade, ej installerade och ej hostverifierade. `COMPATIBILITY.json` anger explicit `host_verified: false`.

## Öppna gates inför aktivering
1. Webbsökning med riktig produkt.
2. Öppning av rätt supportsida och dokumentlänk.
3. Läsning av faktisk manual inklusive variant/region.
4. Sex hosttestscenarier i docs/RUNTIME-PARITY.md.

Om hosten saknar obligatoriska verktyg används textbaserat identifieringsstöd och en verifierad sökingång, aldrig påstådd verifiering.
