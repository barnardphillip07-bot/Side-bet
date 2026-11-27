import unittest

from benchmarks.dingoos.wlc_001 import (
    WLC001Inputs,
    analytical_damped_frequency_hz,
    analytical_undamped_frequency_hz,
    run_workload,
    source_faithful_explicit_euler,
)


class WLC001Tests(unittest.TestCase):
    def test_analytical_references(self):
        inputs = WLC001Inputs()
        self.assertAlmostEqual(analytical_undamped_frequency_hz(inputs), 1.5915494309189535, places=12)
        self.assertAlmostEqual(analytical_damped_frequency_hz(inputs), 1.591549231975262, places=12)

    def test_source_faithful_numerical_reference(self):
        result = source_faithful_explicit_euler(WLC001Inputs())
        self.assertEqual(result["step_count"], 2000)
        self.assertEqual(result["zero_crossing_times_s"], [0.157, 0.47100000000000003, 0.785, 1.099, 1.413, 1.727])
        self.assertAlmostEqual(result["estimated_frequency_hz"], 1.5923566878980893, places=12)

    def test_run_is_deterministic(self):
        self.assertEqual(run_workload(), run_workload())

    def test_analytical_comparison_is_not_physical_validation(self):
        self.assertIn("not empirical", run_workload()["epistemic_limit"])

    def test_rejects_non_integral_step_count(self):
        with self.assertRaises(ValueError):
            source_faithful_explicit_euler(WLC001Inputs(duration_s=2.0, time_step_s=0.0015))

    def test_rejects_non_underdamped_frequency_reference(self):
        with self.assertRaises(ValueError):
            analytical_damped_frequency_hz(WLC001Inputs(damping_n_s_per_m=100.0))


if __name__ == "__main__":
    unittest.main()
