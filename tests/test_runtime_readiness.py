import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.runtime.readiness import evaluate_runtime, all_runtime_readiness, REQUIREMENTS

class RuntimeReadinessTests(unittest.TestCase):
    def test_missing_evidence_blocks(self):
        for name in REQUIREMENTS['runtimes']:
            if name != 'chatgpt_custom':
                self.assertEqual(evaluate_runtime(name, {})['status'], 'blocked_pending_host_tests')
    def test_partial_pass_blocks(self):
        result = evaluate_runtime('chatgpt_chat', {'web_search': 'passed', 'source_access':'passed'})
        self.assertIn('manual_content_read', result['missing'])
    def test_packaged_is_not_verified(self):
        self.assertEqual(evaluate_runtime('openai_plugin', {'web_search':'packaged', 'source_access':'declared', 'manual_content_read':'passed'})['status'], 'blocked_pending_host_tests')
    def test_optional_image_does_not_block(self):
        evidence = {key:'passed' for key in REQUIREMENTS['required_for_functional_activation']}
        result = evaluate_runtime('claude_projects', evidence)
        self.assertEqual(result['status'], 'eligible_for_activation')
        self.assertIn('image_input', result['optional_unverified'])
    def test_all_reported(self):
        self.assertEqual(len(all_runtime_readiness({})), 6)
    def test_historical_not_activated(self):
        self.assertEqual(evaluate_runtime('chatgpt_custom', {})['status'], 'historical_inactive')
    def test_unknown_raises(self):
        with self.assertRaises(ValueError): evaluate_runtime('unknown', {})

if __name__ == '__main__': unittest.main()
