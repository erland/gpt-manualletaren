from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=['README.md','src/canonical/instructions.md','src/contracts/capabilities.yaml','src/contracts/artifacts.md','src/contracts/workspace-and-tools.md','docs/PROJECT-PLAN.md','docs/RUNTIME-PARITY.md','project/status.json','docs/IDENTIFICATION.md','src/identification/matcher.py','docs/MANUAL-SEARCH.md','src/contracts/runtime-requirements.json','src/runtime/readiness.py','tests/test_runtime_readiness.py','src/manual_search/evidence.py','tests/test_manual_search.py','scripts/build_distributions.py','tests/test_distributions.py','docs/DISTRIBUTIONS.md','.github/workflows/ci.yml','.github/workflows/release.yml']
def main():
 errors=[f'Missing: {f}' for f in REQUIRED if not (ROOT/f).is_file()]
 s=json.loads((ROOT/'project/status.json').read_text(encoding='utf-8'))
 if s.get('release_ready') or s.get('runtimes_activated'): errors.append('Runtime/release claimed without validation')
 instructions=(ROOT/'src/canonical/instructions.md').read_text(encoding='utf-8')
 for word in ['Verifierad','Trolig','Ej fastställd','aldrig','tillverkare']:
  if word.casefold() not in instructions.casefold(): errors.append(f'Missing critical behavior {word}')
 print('VALIDATION FAILED: '+', '.join(errors) if errors else 'VALIDATION PASSED')
 return bool(errors)
if __name__=='__main__': sys.exit(main())
