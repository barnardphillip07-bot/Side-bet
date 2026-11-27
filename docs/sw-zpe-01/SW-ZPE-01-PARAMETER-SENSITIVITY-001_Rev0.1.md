# SW-ZPE-01 Parameter Sensitivity — Electromechanical Open-Circuit Frequency — Rev 0.1

- **Record ID:** SWZ-MATH-SENS-001
- **Revision:** 0.1
- **Date:** 2026-11-27
- **Parent / related:** SWZ-MATH-RE-001 Rev0.1; ZPE-01-ENC-0001 Rev0.2; SW-ZPE-01 Rev2.3
- **Status:** INDEPENDENT PARAMETRIC DERIVATION / INPUTS PROVISIONAL / NOT CALIBRATED

## 1. Purpose

Quantify how the recovered single-mode model's ideal open-circuit natural frequency changes across the conflicting candidate values for modal coupling coefficient \(\theta\) and clamped capacitance \(C_0\). This is a sensitivity calculation, not a parameter-selection decision.

## 2. Governing equations

\[
k_{OC}=k_{SC}+\frac{\theta^2}{C_0}
\]

\[
f_{OC}=\frac{1}{2\pi}\sqrt{\frac{k_{OC}}{m}}
\qquad
f_{SC}=\frac{1}{2\pi}\sqrt{\frac{k_{SC}}{m}}
\]

The calculation holds the recovered Rev2.3 independent stiffness reference at \(k_{SC}=1190.21\,\mathrm{N/m}\), and the Rev0.2 model modal masses at:
- M100: \(m=1.08864\times10^{-3}\,\mathrm{kg}\)
- M156: \(m=1.64864\times10^{-3}\,\mathrm{kg}\)

Candidate values swept:
- \(\theta=0.35, 0.45, 0.55\,\mathrm{mN/V}\)
- \(C_0=3.9844, 4.10, 15.0\,\mathrm{nF}\)

The 15 nF value is an earlier historical candidate, not a confirmed value. All three capacitances remain unresolved until the exact PZT part, measurement boundary, frequency, amplitude and fixture corrections are authenticated.

## 3. Results

### 3.1 M100

| \(\theta\) (mN/V) | \(C_0\) (nF) | \(\Delta k=\theta^2/C_0\) (N/m) | Ideal \(f_{OC}\) (Hz) |
|---:|---:|---:|---:|
| 0.35 | 3.9844 | 30.7449 | 168.5496 |
| 0.35 | 4.10 | 29.8780 | 168.4898 |
| 0.35 | 15.0 | 8.1667 | 166.9839 |
| 0.45 | 3.9844 | 50.8232 | 169.9299 |
| 0.45 | 4.10 | 49.3902 | 169.8317 |
| 0.45 | 15.0 | 13.5000 | 167.3551 |
| 0.55 | 3.9844 | 75.9211 | 171.6395 |
| 0.55 | 4.10 | 73.7805 | 171.4944 |
| 0.55 | 15.0 | 20.1667 | 167.8179 |

### 3.2 M156

| \(\theta\) (mN/V) | \(C_0\) (nF) | \(\Delta k=\theta^2/C_0\) (N/m) | Ideal \(f_{OC}\) (Hz) |
|---:|---:|---:|---:|
| 0.35 | 3.9844 | 30.7449 | 136.9642 |
| 0.35 | 4.10 | 29.8780 | 136.9156 |
| 0.35 | 15.0 | 8.1667 | 135.6919 |
| 0.45 | 3.9844 | 50.8232 | 138.0858 |
| 0.45 | 4.10 | 49.3902 | 138.0060 |
| 0.45 | 15.0 | 13.5000 | 135.9935 |
| 0.55 | 3.9844 | 75.9211 | 139.4751 |
| 0.55 | 4.10 | 73.7805 | 139.3571 |
| 0.55 | 15.0 | 20.1667 | 136.3696 |

## 4. Interpretation

Across this candidate grid:
- M100 ideal open-circuit frequency spans approximately **166.984–171.640 Hz**.
- M156 ideal open-circuit frequency spans approximately **135.692–139.475 Hz**.
- At \(\theta=0.45\,\mathrm{mN/V}\), changing \(C_0\) from 3.9844 nF to 15 nF changes the M100 ideal open-circuit result from 169.930 Hz to 167.355 Hz, a difference of approximately 2.575 Hz.
- The coupling contribution is quadratic in \(\theta\) and inversely proportional to \(C_0\). Therefore the unresolved coupling and capacitance values are not minor bookkeeping details; they materially affect the open-circuit stiffness and frequency prediction.

The calculation is an ideal constant-charge open-circuit limit. It does not represent the finite-leakage 50 MΩ candidate testbench, external protection capacitance, TVS leakage, fixture loading or a measured resonance.

## 5. Required parameter closure

Before selecting a model point:
1. Authenticate the exact PZT manufacturer part number, lot, electrode layout and poling direction.
2. Measure \(C_0\) at a declared frequency, amplitude, temperature and mechanical boundary; record fixture and parasitic correction.
3. Establish dielectric loss/leakage over the operating frequency and voltage range.
4. Derive the signed modal \(\theta\) from the piezoelectric constitutive tensor and actual mode shape, or infer \(|\theta|\) from matched short/open-circuit stiffness measurements with consistent modal normalisation.
5. Preserve the sign determination separately; the stiffness relation \(\theta^2=C_0(k_{OC}-k_{SC})\) determines magnitude, not sign.
6. Compare predicted short/open poles with independently executed ODE and simulator models, then with calibrated physical measurements.

## 6. Disposition

No candidate \(C_0\) or \(\theta\) is selected. This page demonstrates sensitivity only. The original Rev2.3 and Rev0.2 inputs remain unchanged, and no physical performance or energy-harvesting claim follows from these calculations.

## 7. Change history

- **Rev0.1 — 2026-11-27:** First independent parameter-sensitivity sweep over the recovered candidate \(\theta\) and \(C_0\) ranges.
