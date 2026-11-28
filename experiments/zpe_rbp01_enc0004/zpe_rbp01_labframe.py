"""ZPE-RBP-01 laboratory-frame closed resonator reference, ENC-0004 candidate.

Independent single-mode, closed-system covariance propagator for an externally
prescribed time-varying capacitance. No damping, bath, port, mechanical
quantization, or PZT is included. SI units except dimensionless quadratures.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from scipy.integrate import solve_ivp
from scipy.constants import hbar

Array = np.ndarray

@dataclass(frozen=True)
class LabFrameParams:
    omega0: float = 2*np.pi*5e9
    epsilon: float = 3e-4
    omega_p: float | None = None
    phase: float = 0.0

    def validate(self):
        op = 2*self.omega0 if self.omega_p is None else self.omega_p
        if not np.isfinite(self.omega0) or self.omega0 <= 0:
            raise ValueError("omega0 must be finite and positive")
        if not np.isfinite(self.epsilon) or abs(self.epsilon) >= 1:
            raise ValueError("epsilon must be finite with abs(epsilon) < 1")
        if not np.isfinite(op) or op <= 0:
            raise ValueError("omega_p must be finite and positive")
        if not np.isfinite(self.phase):
            raise ValueError("phase must be finite")

    @property
    def pump_angular_frequency(self):
        return 2*self.omega0 if self.omega_p is None else self.omega_p

    @property
    def detuning(self):
        return self.omega0 - 0.5*self.pump_angular_frequency


def capacitance(t, p):
    p.validate()
    return 1 + p.epsilon*np.cos(p.pump_angular_frequency*t+p.phase)


def capacitance_rate(t, p):
    return -p.epsilon*p.pump_angular_frequency*np.sin(
        p.pump_angular_frequency*t+p.phase)


def drift_matrix(t, p):
    alpha = 1/capacitance(t,p)
    return np.array([[0.,p.omega0*alpha],[-p.omega0,0.]])


def rotation(angle):
    c,s=np.cos(angle),np.sin(angle)
    return np.array([[c,s],[-s,c]])


def _pack(S,V,W):
    return np.concatenate((S.reshape(4),V.reshape(4),[W]))


def propagate(p, t_span, t_eval=None, V0=None, rtol=2e-11,
              atol=2e-13, max_step=None):
    """Integrate Sdot=A S, Vdot=A V+V A^T and explicit boundary work."""
    p.validate()
    t0,tf=map(float,t_span)
    if not np.isfinite(t0+tf) or tf<=t0:
        raise ValueError("t_span must be finite and increasing")
    V0=.5*np.eye(2) if V0 is None else np.asarray(V0,dtype=float)
    if V0.shape!=(2,2) or not np.all(np.isfinite(V0)):
        raise ValueError("V0 must be a finite 2x2 matrix")
    if not np.allclose(V0,V0.T,rtol=0,atol=1e-13):
        raise ValueError("V0 must be symmetric")
    J=np.array([[0.,1.],[-1.,0.]])
    if np.linalg.eigvalsh(V0+.5j*J).min() < -1e-12:
        raise ValueError("V0 violates quantum uncertainty")
    h0=.5*hbar*p.omega0*(V0[0,0]+V0[1,1]/capacitance(t0,p))

    def rhs(t,y):
        S=y[:4].reshape(2,2); V=y[4:8].reshape(2,2)
        A=drift_matrix(t,p)
        dS=A@S
        dV=A@V+V@A.T
        cb=capacitance(t,p)
        alphadot=-capacitance_rate(t,p)/(cb*cb)
        dW=.5*hbar*p.omega0*alphadot*V[1,1]
        return _pack(dS,dV,dW)

    if max_step is None: max_step=(tf-t0)/4000
    if not np.isfinite(max_step) or max_step<=0:
        raise ValueError("max_step must be finite and positive")
    sol=solve_ivp(rhs,(t0,tf),_pack(np.eye(2),V0,0.),method="DOP853",
                  t_eval=t_eval,rtol=rtol,atol=atol,max_step=max_step)
    if not sol.success: raise RuntimeError(sol.message)
    S=sol.y[:4].T.reshape(-1,2,2)
    V=sol.y[4:8].T.reshape(-1,2,2)
    W=sol.y[8]
    alpha=np.array([1/capacitance(t,p) for t in sol.t])
    E=.5*hbar*p.omega0*(V[:,0,0]+alpha*V[:,1,1])
    V_from_S=np.einsum('nij,jk,nlk->nil',S,V0,S)
    symp=np.einsum('nji,jk,nkl->nil',S,J,S)-J
    umin=np.array([np.linalg.eigvalsh(v+.5j*J).min().real for v in V])
    return {"solution":sol,"S":S,"V":V,"V_from_S":V_from_S,
            "boundary_work_J":W,"energy_J":E,
            "energy_residual_J":(E-E[0])-W,
            "symplectic_residual":symp,
            "uncertainty_min_eigenvalue":umin,
            "detV":np.linalg.det(V),"initial_energy_J":h0,"params":p}


def rwa_drift(p):
    """ENC-0003 closed Hamiltonian RWA drift, in the pump/2 rotating frame."""
    p.validate()
    lam=-1j*(p.epsilon*p.omega0/4)*np.exp(-1j*p.phase)
    d=p.detuning
    return np.array([[lam.real,d+lam.imag],[-d+lam.imag,-lam.real]])


def compare_rwa(p, cycles=100, points_per_cycle=256):
    """Compare exact lab covariance with closed RWA in the rotating frame."""
    p.validate()
    if cycles<1 or points_per_cycle<32:
        raise ValueError("cycles >= 1 and points_per_cycle >= 32 required")
    period=2*np.pi/p.pump_angular_frequency
    t=np.linspace(0,cycles*period,cycles*points_per_cycle+1)
    exact=propagate(p,(0.,float(t[-1])),t_eval=t,
                    max_step=period/points_per_cycle/4)
    A=rwa_drift(p); V0=.5*np.eye(2)
    def rhs(_,v):
        V=v.reshape(2,2)
        return (A@V+V@A.T).reshape(4)
    rwa=solve_ivp(rhs,(0.,float(t[-1])),V0.reshape(4),method="DOP853",
                  t_eval=t,rtol=2e-11,atol=2e-13,
                  max_step=period/points_per_cycle/4)
    if not rwa.success: raise RuntimeError(rwa.message)
    Vrwa=rwa.y.T.reshape(-1,2,2)
    Vrot=np.asarray([rotation(-.5*p.pump_angular_frequency*ti)@vi@
                     rotation(-.5*p.pump_angular_frequency*ti).T
                     for ti,vi in zip(t,exact["V"])])
    scale=np.maximum(np.linalg.norm(Vrwa,axis=(1,2)),1e-30)
    err=np.linalg.norm(Vrot-Vrwa,axis=(1,2))/scale
    return {"time_s":t,"V_exact_rotating":Vrot,"V_rwa":Vrwa,
            "relative_frobenius_error":err,
            "max_relative_error":float(np.max(err)),
            "final_relative_error":float(err[-1]),
            "detuning_rad_s":p.detuning,"epsilon":p.epsilon,
            "cycles":cycles,"points_per_cycle":points_per_cycle}
