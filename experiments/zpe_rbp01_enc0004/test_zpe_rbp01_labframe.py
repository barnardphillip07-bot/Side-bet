import unittest
import numpy as np
from zpe_rbp01_labframe import (LabFrameParams, capacitance, propagate,
                                compare_rwa, rwa_drift)

class LabFrameTests(unittest.TestCase):
    def test_constant_capacitance_is_symplectic_and_stationary_vacuum(self):
        p=LabFrameParams(epsilon=0.)
        r=propagate(p,(0,2e-9),t_eval=np.linspace(0,2e-9,101))
        self.assertLess(np.max(np.abs(r["symplectic_residual"])),2e-10)
        self.assertLess(np.max(np.abs(r["V"]-.5*np.eye(2))),2e-10)
        self.assertLess(np.max(np.abs(r["energy_residual_J"])),1e-30)
        self.assertTrue(np.all(r["detV"]>=.25-2e-10))

    def test_constant_capacitance_fundamental_matrix_matches_rotation(self):
        p=LabFrameParams(epsilon=0.)
        r=propagate(p,(0,1e-9),t_eval=np.linspace(0,1e-9,51))
        expected=np.array([[[np.cos(p.omega0*t),np.sin(p.omega0*t)],
                            [-np.sin(p.omega0*t),np.cos(p.omega0*t)]]
                           for t in r["solution"].t])
        self.assertLess(np.max(np.abs(r["S"]-expected)),2e-9)

    def test_fundamental_matrix_reconstructs_covariance(self):
        p=LabFrameParams(epsilon=1e-4)
        r=propagate(p,(0,1e-9),t_eval=np.linspace(0,1e-9,301))
        self.assertLess(np.max(np.abs(r["V"]-r["V_from_S"])),2e-9)

    def test_uncertainty_matrix_is_positive(self):
        p=LabFrameParams(epsilon=3e-4)
        r=propagate(p,(0,2e-9),t_eval=np.linspace(0,2e-9,401))
        self.assertGreaterEqual(np.min(r["uncertainty_min_eigenvalue"]),-2e-9)

    def test_boundary_work_closes_energy(self):
        p=LabFrameParams(epsilon=2e-4)
        r=propagate(p,(0,4e-9),t_eval=np.linspace(0,4e-9,1001))
        scale=max(np.max(np.abs(r["energy_J"])),1e-300)
        self.assertLess(np.max(np.abs(r["energy_residual_J"]))/scale,2e-8)

    def test_positive_capacitance_domain(self):
        self.assertGreater(capacitance(0,LabFrameParams(epsilon=.9)),0)
        with self.assertRaises(ValueError): LabFrameParams(epsilon=1.).validate()

    def test_bad_initial_covariance_rejected(self):
        with self.assertRaises(ValueError):
            propagate(LabFrameParams(),(0,1e-9),V0=np.zeros((2,2)))

    def test_rwa_drift_matches_declared_enc0003_convention(self):
        p=LabFrameParams(epsilon=4e-4,phase=.2)
        A=rwa_drift(p)
        lam=-1j*p.epsilon*p.omega0/4*np.exp(-1j*p.phase)
        expected=np.array([[lam.real,lam.imag],[lam.imag,-lam.real]])
        self.assertTrue(np.allclose(A,expected,rtol=0,atol=1e-12))

    def test_off_resonant_detuning_enters_rwa_drift(self):
        p=LabFrameParams(omega_p=2*(2*np.pi*5e9-2*np.pi*1e6),epsilon=1e-4)
        A=rwa_drift(p)
        self.assertAlmostEqual(A[0,1]-A[1,0],2*p.detuning,delta=1e-6)

    def test_rwa_comparison_is_finite(self):
        p=LabFrameParams(omega0=2*np.pi*5e6,epsilon=1e-4)
        c=compare_rwa(p,cycles=8,points_per_cycle=64)
        self.assertTrue(np.all(np.isfinite(c["relative_frobenius_error"])))
        self.assertGreaterEqual(c["max_relative_error"],0.)

if __name__=="__main__":
    unittest.main(verbosity=2)
