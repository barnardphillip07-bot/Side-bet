import unittest

from experiments.dingoos_architecture_comparison.runner import (
    run_centralized,
    run_federated_process_surrogate,
    run_local_first_hybrid,
)


class ArchitectureTopologySmokeTests(unittest.TestCase):
    def test_all_variants_produce_same_wlc001_results(self):
        variants = [run_centralized(), run_federated_process_surrogate(), run_local_first_hybrid()]
        reference = variants[0]["results"]
        for variant in variants[1:]:
            self.assertEqual(variant["results"], reference)

    def test_federated_variant_is_explicitly_a_surrogate(self):
        result = run_federated_process_surrogate()
        self.assertEqual(result["architecture_id"], "FEDERATED_PROCESS_ISOLATED_SURROGATE")
        self.assertIn("single_host_process_surrogate", result["topology"]["federation_limit"])

    def test_beta_isolated_but_gate_d_not_established(self):
        for variant in (run_centralized(), run_federated_process_surrogate(), run_local_first_hybrid()):
            assurance = variant["assurance"]
            self.assertTrue(assurance["beta_receives_only_frozen_inputs"])
            self.assertFalse(assurance["beta_receives_alpha_outputs"])
            self.assertFalse(assurance["independent_codebase"])
            self.assertEqual(assurance["gate_d_independence"], "NOT_ESTABLISHED")

    def test_no_gamma_authority_or_consequential_effect_is_claimed(self):
        for variant in (run_centralized(), run_federated_process_surrogate(), run_local_first_hybrid()):
            assurance = variant["assurance"]
            self.assertEqual(assurance["gamma_authority"], "NOT_IN_SCOPE")
            self.assertFalse(assurance["consequential_effects"])
            self.assertEqual(assurance["target_side_enforcement"], "NOT_TESTED")
            self.assertEqual(assurance["fault_gates_a_to_e"], "NOT_RUN")


if __name__ == "__main__":
    unittest.main()
