import math
import unittest

from physics_reference import (
    OscillatorParameters, critical_angle_rad, fresnel_power,
    rk4_free_response, snell_angle_rad,
)


class OscillatorTests(unittest.TestCase):
    def test_frequency_and_undamped_quality_limit(self):
        model = OscillatorParameters(1, 100, 0)
        self.assertAlmostEqual(model.natural_angular_frequency, 10)
        self.assertAlmostEqual(model.natural_frequency_hz, 10/(2*math.pi))
        self.assertTrue(math.isinf(model.quality_factor))
        self.assertEqual(model.regime, "underdamped")

    def test_damping_ratio_and_quality_factor(self):
        model = OscillatorParameters(1.0, 100.0, 2.0)
        self.assertAlmostEqual(model.damping_ratio, 0.1)
        self.assertAlmostEqual(model.quality_factor, 5.0)

    def test_rk4_zero_duration_returns_initial_displacement(self):
        result = rk4_free_response(OscillatorParameters(1, 4, 0.2), 0.0, 0.01, 3.2, -1.0)
        self.assertEqual(result, 3.2)

    def test_three_damping_regimes(self):
        self.assertEqual(OscillatorParameters(1, 9, 2).regime, "underdamped")
        self.assertEqual(OscillatorParameters(1, 9, 6).regime, "critically_damped")
        self.assertEqual(OscillatorParameters(1, 9, 8).regime, "overdamped")

    def test_undamped_exact_response(self):
        self.assertAlmostEqual(OscillatorParameters(2, 18).free_response(0.37), math.cos(3*0.37), places=12)

    def test_initial_condition_and_energy(self):
        model = OscillatorParameters(1, 4, 0.4)
        self.assertAlmostEqual(model.free_response(0, 2.5, -0.7), 2.5)
        self.assertGreaterEqual(model.stored_energy_j(-0.4, 1.2), 0)

    def test_rk4_cross_check_refines_toward_analytic_response(self):
        model = OscillatorParameters(1, 25, 1.2)
        exact = model.free_response(1.25, 0.8, -0.15)
        errors = [abs(rk4_free_response(model, 1.25, h, 0.8, -0.15)-exact) for h in (0.04, 0.02, 0.01)]
        self.assertGreater(errors[0], errors[1])
        self.assertGreater(errors[1], errors[2])
        self.assertLess(errors[2], 1e-7)

    def test_invalid_oscillator_inputs(self):
        for args in ((0, 1, 0), (1, 0, 0), (1, 1, -1), (float("nan"), 1, 0), (True, 1, 0)):
            with self.subTest(args=args), self.assertRaises((TypeError, ValueError)):
                OscillatorParameters(*args)
        with self.assertRaises(ValueError):
            OscillatorParameters(1, 1).free_response(-0.1)
        with self.assertRaises(ValueError):
            rk4_free_response(OscillatorParameters(1, 1), 1, 0)


class OpticsTests(unittest.TestCase):
    def test_snell_known_case(self):
        angle = snell_angle_rad(1.5, 1.33, math.radians(45))
        self.assertAlmostEqual(math.degrees(angle), 52.89096995918989, places=10)

    def test_critical_angle(self):
        self.assertAlmostEqual(critical_angle_rad(1.5, 1), math.asin(2/3))
        self.assertIsNone(critical_angle_rad(1, 1.5))

    def test_total_internal_reflection(self):
        result = fresnel_power(1.5, 1, math.radians(70))
        self.assertTrue(result.total_internal_reflection)
        self.assertEqual(result.reflected_s, 1)
        self.assertEqual(result.reflected_p, 1)
        self.assertEqual(result.transmitted_unpolarized, 0)

    def test_normal_incidence(self):
        result = fresnel_power(1, 1.5, 0)
        expected = ((1-1.5)/(1+1.5))**2
        self.assertAlmostEqual(result.reflected_s, expected)
        self.assertAlmostEqual(result.reflected_p, expected)
        self.assertAlmostEqual(result.reflected_unpolarized+result.transmitted_unpolarized, 1)

    def test_energy_closure(self):
        for degrees in (0, 10, 30, 50, 60):
            result = fresnel_power(1, 1.5, math.radians(degrees))
            self.assertAlmostEqual(result.reflected_s+result.transmitted_s, 1)
            self.assertAlmostEqual(result.reflected_p+result.transmitted_p, 1)
            self.assertAlmostEqual(result.reflected_unpolarized+result.transmitted_unpolarized, 1)

    def test_brewster_angle(self):
        result = fresnel_power(1, 1.5, math.atan(1.5))
        self.assertAlmostEqual(result.reflected_p, 0, places=14)
        self.assertGreater(result.reflected_s, 0)

    def test_invalid_optics_domains(self):
        with self.assertRaises(ValueError):
            snell_angle_rad(0, 1.5, 0.1)
        with self.assertRaises(ValueError):
            fresnel_power(1, 1.5, math.pi/2)
        with self.assertRaises(TypeError):
            critical_angle_rad(True, 1)


if __name__ == "__main__":
    unittest.main()
