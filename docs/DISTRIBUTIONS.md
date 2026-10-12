# Distributioner – GPT Byggaren v1.6.19

Projektet använder originalmotorns `scripts/build_distributions.py` från den versionslåsta källtaggen `erland/gpt-byggaren@v1.6.19`. De ursprungliga byggfilerna behåller sina Git blob-hashar.

## Sex leveransarkiv

- `manualletaren-project-<version>.zip` – fullständigt projekt
- `manualletaren-chat-<version>.zip` – ChatGPT Chat
- `manualletaren-plugin-<version>.zip` – OpenAI Plugin, skills-first
- `manualletaren-claude-project-<version>.zip` – Claude Projects
- `manualletaren-claude-skills-<version>.zip` – Claude Skills
- `manualletaren-opencode-<version>.zip` – OpenCode

Paketen skapas från samma canonical instruktion och kompletterande kunskap, med runtime-specifika strukturer. Custom GPT är uttryckligen inaktiverad.

## Bygg och kontroll

```bash
python3 -m pip install PyYAML jsonschema
python3 scripts/lint_gpt_project.py --project-root .
python3 scripts/validate_project.py
python3 -m unittest discover -s tests -v
rm -rf build dist
python3 scripts/build_distributions.py --project-root . --version 0.7.0-dev
python3 scripts/validate_distributions.py --project-root .
```

Kontrollera `dist/DELIVERY-MANIFEST.json`, tillhörande SHA256-checksummor och sex intakta ZIP-filer. GitHub Actions utför motsvarande verifiering på PR och vid taggade releaser. `scripts/build.py` är en bakåtkompatibel delegator; den innehåller inte längre egen ZIP-assembler.

## Host-verifiering

Ett genererat och strukturellt godkänt arkiv innebär **inte** att webbsökning, faktisk manualåtkomst, PDF-läsning och produktmatchning fungerar i installerad runtime. Dokumentera och testa dessa för varje använd målmiljö innan en stabil release. `project-status.yaml` behåller `release_ready: false` och `runtime.activated: []` tills separat verifiering genomförts.
