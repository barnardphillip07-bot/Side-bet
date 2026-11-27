import unittest

from experiments.dingoos_architecture_comparison.ft03_partition_model import (
    Relation,
    ReconciliationStatus,
    ReplicaUpdate,
    compare_versions,
    reconcile_updates,
    run_all_ft03,
    simulate_ft03_partition,
)


class FT03PartitionModelTests(unittest.TestCase):
    def test_concurrent_vector_updates_are_detected(self):
        self.assertEqual(
            compare_versions({"core": 1, "a": 1}, {"core": 1, "b": 1}),
            Relation.CONCURRENT,
        )

    def test_dominating_version_is_ordered(self):
        self.assertEqual(compare_versions({"core": 2}, {"core": 1}), Relation.AFTER)

    def test_same_version_different_content_is_conflict(self):
        left = ReplicaUpdate("object-1", "A", {"core": 1}, "a")
        right = ReplicaUpdate("object-1", "B", {"core": 1}, "b")
        self.assertEqual(reconcile_updates(left, right), ReconciliationStatus.CONFLICT)

    def test_all_three_topology_models_pause_global_and_detect_conflict(self):
        results = run_all_ft03()
        self.assertEqual(len(results), 3)
        for result in results:
            self.assertEqual(result["partition"]["global_coordination"], "PAUSED")
            self.assertEqual(result["reconnection"]["version_relation"], "CONCURRENT")
            self.assertEqual(result["reconnection"]["reconciliation_status"], "CONFLICT")
            self.assertFalse(result["reconnection"]["automatic_merge"])
            self.assertEqual(result["reconnection"]["global_state_after_reconnection"], "UNCHANGED_PENDING_REVIEW")
            self.assertTrue(result["safety_assertions"]["offline_updates_not_silently_committed"])
            self.assertEqual(result["assurance_limits"]["full_FT_03_acceptance"], "NOT_ESTABLISHED")

    def test_global_state_is_not_modified_by_offline_branches(self):
        for result in run_all_ft03():
            self.assertEqual(
                result["partition"]["base_object"]["value"],
                "design-baseline-v1",
            )
            self.assertTrue(
                all(not update["globally_committed"] for update in result["offline_updates"])
            )

    def test_rejects_unknown_architecture(self):
        with self.assertRaises(ValueError):
            simulate_ft03_partition("UNKNOWN")


if __name__ == "__main__":
    unittest.main()
