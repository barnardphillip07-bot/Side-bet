# ZPE-RBP-01-ENC-0004 — Laboratory-Frame Quantum Covariance Model and RWA Cross-Validation

- **Revision:** 0.1
- **Date:** 2026-11-28
- **Status:** IMPLEMENTED CANDIDATE — 10/10 software/model tests passed; independent review pending; not physically validated
- **Programme:** ZPE-RBP-01 only
- **Implementation:** `experiments/zpe_rbp01_enc0004/zpe_rbp01_labframe.py`
- **Tests:** `experiments/zpe_rbp01_enc0004/test_zpe_rbp01_labframe.py`
- **Runner/results:** adjacent `run_zpe_rbp01_labframe.py` and `zpe_rbp01_labframe_results.json`

## 1. Authority, provenance and scope

This record implements an independent laboratory-frame reference for an isolated, closed, single-mode lumped microwave resonator with externally prescribed time-varying capacitance. The primary propagator retains the full capacitance time dependence and makes no rotating-wave approximation (RWA).

This is a **derived comparison model**, not an authenticated original theory or an owner-approved physical architecture. The archived incident record `DINGOOS-AI-RESEARCH-INCIDENT-002 Rev 0.1` dispositions the assistant-derived ENC-0003 quantum input-output package as an unselected comparison candidate. ENC-0003 is preserved unchanged and used here only to cross-check its declared closed-Hamiltonian RWA convention. This work does not promote ENC-0003 into the selected physical design.

Predecessor records:
- **ENC-0001 Rev 0.1:** derived classical electromechanical and microwave-boundary reference. Its time-varying microwave capacitance law is a derived extension, not a recovered original law.
- **ENC-0002 Rev 0.1:** reported 9/9 equation-level charge, KCL, reciprocal-force and power-pairing checks.
- **ENC-0003 Rev 0.1:** assistant-derived single-mode Gaussian RWA/open-system comparison package; 12/12 reported model-level checks; not selected as physical architecture and not hardware validated.

No SW-ZPE-01-A source, physical design, canonical DingoOS record or protected BIF/IP source is changed. No fabrication, physical performance, vacuum-energy extraction or net-positive-energy claim is made.

## 2. Model boundary

Included:
- one lumped resonator mode with fixed inductance (L_r);
- externally prescribed positive capacitance (C_r(t));
- closed-system dynamics, with no damping, transmission-line port, thermal reservoir or noise;
- zero-mean Gaussian states represented by a symmetrized covariance matrix;
- fixed-reference canonical quadratures.

Excluded:
- mechanical coordinate and PZT dynamics or quantization;
- distributed electromagnetic fields and multimode effects;
- physical actuator, pump supply, measurement chain and apparatus-level energy ledger;
- all losses, baths and output ports.

Do not append phenomenological damping or unpaired noise to this model. Any later open-system extension must derive coupling and noise from an actual port model.

For this isolated test model:
\\[
\bar C(t)=C_r(t)/C_{r0}=1+\epsilon\cos(\Omega_p t+\phi),\quad |\epsilon|<1.
\\]
All sweep values are numerical test inputs, not measured device parameters or selected hardware values.

## 3. Canonical Hamiltonian and exact laboratory-frame equations

Start from
\\[
\hat H_r(t)=\frac{\hat Q_r^2}{2C_r(t)}+
\frac{\hat\Phi_r^2}{2L_r},\qquad
[\hat\Phi_r,\hat Q_r]=i\hbar.
\\]
With
\\[
\omega_0=(L_rC_{r0})^{-1/2},\quad
\hat X=\frac{\hat\Phi_r}{\sqrt{\hbar/(C_{r0}\omega_0)}},\quad
\hat P=\frac{\hat Q_r}{\sqrt{\hbar C_{r0}\omega_0}},
\\]
we have ([X,P]=i). Define
\\[
\alpha(t)=\frac{C_{r0}}{C_r(t)}=\frac{1}{\bar C(t)}.
\\]
Then
\\[
\boxed{\hat H_r(t)=\frac{\hbar\omega_0}{2}
[\hat X^2+\alpha(t)\hat P^2].}
\\]
The canonical Heisenberg equations are
\\[
\boxed{\dot{\mathbf R}=A(t)\mathbf R,\quad
A(t)=\begin{bmatrix}0&\omega_0\alpha(t)\\-\omega_0&0\end{bmatrix},
\quad \mathbf R=[\hat X,\hat P]^T.}
\\]
No expansion of (1/C_r(t)) is made in the laboratory-frame propagator.

## 4. Fundamental matrix, covariance and physicality

Propagate the fundamental matrix independently:
\\[
\dot S=A(t)S,\qquad S(0)=I.
\\]
For the symmetrized covariance
\\[
V_{ij}=\tfrac12\langle\hat R_i\hat R_j+\hat R_j\hat R_i\rangle,
\\]
and zero mean:
\\[
\boxed{\dot V=A(t)V+VA(t)^T.}
\\]
With
\\[
\Omega=\begin{bmatrix}0&1\\-1&0\end{bmatrix},
\\]
closed evolution must preserve
\\[
S^T\Omega S=\Omega,
\\]
which preserves the canonical commutator. Quantum covariance physicality is
\\[
V+\frac{i}{2}\Omega\succeq0,
\\]
equivalent for one mode to (det V\ge1/4).

The implementation propagates both (V) and (S V(0)S^T) and checks their agreement. The default initial state is the fixed-mode vacuum (V(0)=I/2). Alternate initial covariance is accepted only when symmetric and uncertainty-admissible.

## 5. Boundary-work identity and energy closure

For a zero-mean state:
\\[
E(t)=\langle H_r(t)\rangle=
\frac{\hbar\omega_0}{2}
[V_{XX}(t)+\alpha(t)V_{PP}(t)].
\\]
Since (dot\alpha=d(1/\bar C)/dt):
\\[
\frac{dW_{boundary}}{dt}
=\left\langle\frac{\partial\hat H_r}{\partial t}\right\rangle
=\frac{\hbar\omega_0}{2}\dot\alpha V_{PP}
=-\frac{\dot C_r(t)}{2}\langle\hat V_r^2\rangle,
\quad \hat V_r=\hat Q_r/C_r(t).
\\]
The work is integrated as a separate state variable and compared with the energy change. For this closed prescribed-boundary model:
\\[
\boxed{E(t)-E(0)=W_{boundary}(0\to t).}
\\]
This identity traces resonator energy change to work performed by the time-varying boundary; it is not an independent vacuum-energy source.

## 6. RWA comparison

The comparison uses only the **closed Hamiltonian drift** from the ENC-0003 convention—not its damping, baths, output ports or noise model. In the frame rotating at (Omega_p/2):
\\[
\Delta=\omega_0-\frac{\Omega_p}{2},\qquad
\lambda=-i\frac{\epsilon\omega_0}{4}e^{-i\phi}.
\\]
The RWA quadrature drift is
\\[
A_{RWA}=\begin{bmatrix}
\operatorname{Re}\lambda&\Delta+\operatorname{Im}\lambda\\
-\Delta+\operatorname{Im}\lambda&-\operatorname{Re}\lambda
\end{bmatrix}.
\\]
The exact laboratory covariance is transformed into the same rotating quadrature frame. Maximum error is the maximum relative Frobenius covariance error over the full sampled time series, including within-cycle micromotion. Final error is the endpoint comparison after an integer number of pump cycles. The RWA is a first-order weak-modulation approximation; this finite sweep does not establish a universal validity boundary.

## 7. Implementation and reproduction

- Integrator: SciPy `solve_ivp`, method `DOP853`.
- Solver tolerances: `rtol=2e-11`, `atol=2e-13`.
- Environment: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0.
- The propagator integrates (S), (V) and explicit boundary work.
- The runner performs a 3-by-3 modulation/detuning comparison and fixed-endpoint numerical refinement.

From `experiments/zpe_rbp01_enc0004/`:
```bash
python -m unittest -v test_zpe_rbp01_labframe.py
python run_zpe_rbp01_labframe.py
```
The second command regenerates the JSON results.

## 8. Results — software/model verification only

**10/10 tests passed** in the recorded environment. Tests cover:
- constant-capacitance analytic rotation and stationary vacuum;
- symplectic preservation and covariance reconstruction;
- uncertainty-matrix positivity and determinant bound;
- explicit boundary-work/energy closure;
- invalid capacitance and unphysical initial-covariance rejection;
- ENC-0003 RWA drift convention and detuning;
- finite execution of an exact-vs-RWA comparison.

### Numerical refinement

At (omega_0/2\pi=5) MHz, (epsilon=3\times10^{-4}), five pump cycles and a fixed terminal time:

| Max steps per pump period | Max symplectic residual | Max relative energy-closure residual | Minimum det(V) | Max covariance reconstruction error |
|---:|---:|---:|---:|---:|
| 32 | 2.276e-14 | 6.577e-16 | 0.24999999999999972 | 1.438e-14 |
| 64 | 1.776e-15 | 7.964e-16 | 0.24999999999999983 | 1.554e-15 |
| 128 | 2.442e-15 | 6.667e-16 | 0.24999999999999972 | 1.554e-15 |

Residuals are at or near floating-point precision for these conditions. Last-digit variation is roundoff-level, not evidence of a systematic convergence order. Broader tolerance/error study remains required.

### RWA comparison sweep

Computational reference frequency: 5 MHz (scaled test value, not device selection). Five pump cycles, 32 sample intervals per pump cycle. Detuning is expressed as a fraction of (g=\epsilon\omega_0/4).

| Epsilon | Detuning / g | Max time-resolved relative covariance error | Final stroboscopic relative error |
|---:|---:|---:|---:|
| 1e-5 | 0.0 | 2.5003e-6 | 3.234e-14 |
| 1e-5 | 0.5 | 2.5003e-6 | 4.909e-11 |
| 1e-5 | 1.0 | 2.5003e-6 | 9.818e-11 |
| 1e-4 | 0.0 | 2.5031e-5 | 3.318e-11 |
| 1e-4 | 0.5 | 2.5031e-5 | 4.913e-9 |
| 1e-4 | 1.0 | 2.5031e-5 | 9.821e-9 |
| 1e-3 | 0.0 | 2.5306e-4 | 3.317e-8 |
| 1e-3 | 0.5 | 2.5307e-4 | 4.962e-7 |
| 1e-3 | 1.0 | 2.5309e-4 | 9.858e-7 |

The time-resolved maximum includes micromotion omitted by the RWA; endpoint stroboscopic error is smaller in this short sweep. This is consistent with improved agreement at smaller modulation depth for the tested conditions. It does not establish accuracy for long integrations, near-instability boundaries, strong modulation, non-sinusoidal boundary motion or any physical device.

## 9. Limitations and unresolved work

1. Independent review of derivation, code and results is pending.
2. Single lumped mode only; no distributed transmission-line or multimode field model.
3. No open-system bath, loss, damping or output field.
4. No mechanical or PZT quantization; no joint quantum electromechanical model.
5. No authenticated physical parameter set, component identity, calibrated measurement or hardware topology.
6. RWA sweep is small and short; extend parameter, duration, phase and solver-convergence coverage before broader validity claims.
7. Prescribed-boundary work is not a complete physical actuator supply/loss ledger.
8. No evidence of photon detection, vacuum-energy extraction, net-positive energy or experimental confirmation.

## 10. Gate disposition

| Requirement | Disposition |
|---|---|
| Independent laboratory-frame implementation | IMPLEMENTED — candidate |
| Symplectic / commutator preservation | PASS for tested cases |
| Covariance uncertainty | PASS for tested cases |
| Boundary-work energy identity | PASS for tested cases |
| RWA comparison | EXECUTED — limited sweep; broader domain unresolved |
| Independent reviewer reproduction | PENDING |
| Open-system port derivation | NOT IN SCOPE — later gate |
| Joint mechanical/PZT quantization | NOT IN SCOPE — later gate |
| Physical measurement / hardware validation | NOT PERFORMED |

**Overall:** ENC-0004 candidate implementation and initial software/model checks are complete. Issue #6 remains open pending independent review, broader convergence/sensitivity work and an explicit decision on subsequent gates.

## 11. Change history

- **Rev 0.1 — 2026-11-28:** First independent laboratory-frame covariance implementation, symplectic and uncertainty checks, explicit boundary-work integration, limited closed-Hamiltonian RWA comparison and reproducible test results. No original ENC-0001/0002/0003 source was modified; no physical validation is claimed.
