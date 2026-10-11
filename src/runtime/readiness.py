"""Conservative host-evidence gate; never assumes functionality from packaging."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REQUIREMENTS = json.loads((ROOT / 'src/contracts/runtime-requirements.json').read_text(encoding='utf-8'))


def evaluate_runtime(runtime, evidence):
    if runtime not in REQUIREMENTS['runtimes']:
        raise ValueError('Unknown runtime')
    if REQUIREMENTS['runtimes'][runtime].get('historical'):
        return {'runtime': runtime, 'status': 'historical_inactive', 'missing': [], 'optional_unverified': []}
    required = REQUIREMENTS['required_for_functional_activation']
    optional = REQUIREMENTS['optional']
    # Only explicit successful real-host tests count; a declaration alone doesn't.
    missing = [cap for cap in required if evidence.get(cap) != 'passed']
    optional_unverified = [cap for cap in optional if evidence.get(cap) != 'passed']
    return {'runtime': runtime, 'status': 'eligible_for_activation' if not missing else 'blocked_pending_host_tests', 'missing': missing, 'optional_unverified': optional_unverified}


def all_runtime_readiness(evidence_by_runtime):
    return {name: evaluate_runtime(name, evidence_by_runtime.get(name, {})) for name in REQUIREMENTS['runtimes']}
