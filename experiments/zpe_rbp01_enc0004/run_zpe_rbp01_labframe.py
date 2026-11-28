"""Reproducible ENC-0004 candidate RWA sweep and numerical refinement."""
import json
import platform
from pathlib import Path
import numpy as np
import scipy
from zpe_rbp01_labframe import LabFrameParams, compare_rwa, propagate


def main():
    # Computationally scaled reference, not a device parameter selection.
    omega=2*np.pi*5e6
    sweep=[]
    for eps in (1e-5,1e-4,1e-3):
        g=eps*omega/4
        for ratio in (0.,.5,1.):
            delta=ratio*g
            p=LabFrameParams(omega0=omega,epsilon=eps,
                             omega_p=2*(omega-delta),phase=0.)
            c=compare_rwa(p,cycles=5,points_per_cycle=32)
            sweep.append({
                "epsilon":eps,"detuning_over_g":ratio,
                "detuning_rad_s":delta,
                "max_relative_covariance_error":c["max_relative_error"],
                "final_stroboscopic_relative_covariance_error":c["final_relative_error"],
                "cycles":5,"points_per_cycle":32})
    p=LabFrameParams(omega0=omega,epsilon=3e-4)
    refinement=[]
    for divisions in (32,64,128):
        period=2*np.pi/p.pump_angular_frequency
        r=propagate(p,(0,5*period),
                    t_eval=np.linspace(0,5*period,161),
                    max_step=period/divisions)
        refinement.append({
            "maximum_steps_per_pump_period":divisions,
            "max_symplectic_residual":float(np.max(np.abs(r["symplectic_residual"]))),
            "max_relative_energy_closure_residual":float(
                np.max(np.abs(r["energy_residual_J"]))/np.max(np.abs(r["energy_J"]))),
            "minimum_detV":float(np.min(r["detV"])),
            "max_covariance_reconstruction_error":float(
                np.max(np.abs(r["V"]-r["V_from_S"])))})
    result={
        "status":"candidate numerical results; software/model verification only",
        "scope":"closed, isolated, single-mode, prescribed-capacitance laboratory-frame model",
        "environment":{"python":platform.python_version(),
                       "numpy":np.__version__,"scipy":scipy.__version__},
        "rwa_sweep_frequency_Hz":omega/(2*np.pi),
        "rwa_sweep_frequency_note":"computationally scaled reference; not hardware selection",
        "rwa_sweep":sweep,"numerical_refinement":refinement}
    Path(__file__).with_name("zpe_rbp01_labframe_results.json").write_text(
        json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
