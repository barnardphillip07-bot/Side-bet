# SW-ZPE-01 Mathematical Reverse-Engineering Record — Rev 0.1

- **Record ID:** SWZ-MATH-RE-001
- **Revision:** 0.1
- **Date:** 2026-11-27
- **Governing engineering reference:** SW-ZPE-01 Rev2.3 Engineering Reconciliation Reference Report
- **Primary mathematical source:** ZPE-01-ENC-0001 Rev0.2
- **Status:** INDEPENDENT NUMERICAL REPRODUCTION PASS FOR ODE/FEM REFERENCES / PARAMETER AUTHENTICATION OPEN / SPICE AND HARDWARE VALIDATION OPEN

## 1. Objective and provenance boundary

This record independently reconstructs and checks the mathematical behaviour of the recovered SW-ZPE-01 models. It is a derived verification record, not a replacement for the original documents or code. Original equations are identified as recovered; independently executed results are identified separately. No protected BIF axioms or source are reproduced or inferred.

## 2. Recovered reciprocal electromechanical model

The recovered ZPE-01-ENC-0001 Rev0.2 defines a single-mode mechanical port and differential electrical PZT port:

```text
m*xddot + c*xdot + k*x - theta*v = Fext
q = C0*v + theta*x
i_into = C0*vdot + theta*xdot + Gp*v
```

Sign conventions:
- `x`: modal displacement, m.
- `v = V(A)-V(B)`: differential PZT voltage, V.
- `i_into`: current entering the transducer at terminal A and leaving terminal B.
- `theta`: signed modal coupling coefficient; same sign in both reciprocal paths.

The stored energy is:

```text
E = 0.5*m*xdot^2 + 0.5*k*x^2 + 0.5*C0*v^2
Pdiss = c*xdot^2 + Gp*v^2
```

The governing power identity is:

```text
Fext*xdot + v*i_into = dE/dt + c*xdot^2 + Gp*v^2
```

This follows by multiplying the mechanical equation by `xdot`, the electrical equation by `v`, and adding. The reciprocal coupling terms cancel. The identity is exact for the stated linear model and sign convention; it does not authenticate the parameter values or establish physical energy-harvesting performance.

## 3. Boundary-condition stiffness and frequencies

For the model's short-circuit stiffness `kSC=k`:

```text
kOC = kSC + theta^2/C0
fSC = (1/(2*pi))*sqrt(kSC/m)
fOC = (1/(2*pi))*sqrt(kOC/m)
```

Do not use an open-circuit measured stiffness as `kSC` and then add `theta^2/C0` again. That would double-count electrical stiffening.

The recovered ODE script uses:
- `m = 1.08864e-3 kg`
- `k = 1190.21 N/m`
- `theta = 450e-6 N/V`
- `C0 = 3.9844e-9 F`
- `Gp = 1e-15 S`
- `c = 0` in the principal reference cases.

These are provisional model inputs, not calibrated physical parameters. The source record identifies historical C0 candidates of 3.9844 nF, 4.10 nF and 15 nF; the discrepancy remains open.

## 4. Independent ODE reproduction

The materialized `ZPE01_REFERENCE_TESTS.py` was executed in the current runtime. Its SHA-256 exactly matched the recovered source-register value:

`8164e36383ba8af5331542680cdd63fec92423f0619be6067eaf4be591459651`.

The generated JSON object matched the archived `ZPE01_REFERENCE_RESULTS.json` exactly.

Selected reproduced outputs:
- Short-circuit analytical frequency: **166.41397150793696 Hz**.
- Ideal open-circuit analytical frequency: **169.92985608883936 Hz**.
- Open-circuit pulse relative energy residual: approximately **1.2761e-14**.
- Finite 100 kΩ load pulse relative energy residual: approximately **1.2228e-14**.
- Lossless initial-energy exchange residual: **0 J** in the stored output.
- One-sided coupling-sign fault relative energy residual: approximately **6.2795%**.

The fault-injection case is important: reversing only one reciprocal coupling path produces a material energy-identity residual, while the correctly signed reference cases close numerically. This verifies the implementation's internal mathematical consistency under its declared assumptions; it is not a physical measurement.

## 5. Independent stepped-beam FEM reproduction

The materialized `sw_zpe_01_fem_aligned.py` was executed. Its SHA-256 matched the source-register value:

`8c3c3ef2d46b6076034ca2d117254b82d2a2052a945d2743aa127a728b6c3f9f`.

The mesh inserts the two material interfaces explicitly at local x = 0.25 mm and 10.25 mm. Refinement results:

| Refinement | M100 frequency (Hz) | M156 frequency (Hz) | Beam modal mass (g) |
|---:|---:|---:|---:|
| 1 | 166.434236093 | 135.243349449 | 0.088643250 |
| 2 | 166.434236087 | 135.243349452 | 0.088643250 |
| 4 | 166.434236268 | 135.243349599 | 0.088643250 |
| 8 | 166.434236300 | 135.243349626 | 0.088643250 |
| 16 | 166.434224601 | 135.243340117 | 0.088643250 |

The model's reported relative frequency changes between refinements are approximately 7e-6 percent. This is strong numerical mesh stability for this particular discretised model.

Limitations remain: ideal bonded Euler–Bernoulli beam; no adhesive compliance, clamp compliance, tip rotary inertia, nonlinear effects or electromechanical coupling. Mesh convergence does not prove the material inputs, boundary conditions or as-built geometry are correct.

## 6. Discrepancies requiring mathematical closure

1. Rev2.3 reports 166.434 Hz (M100) and 135.243 Hz (M156). The independent ODE arithmetic using rounded `m=1.08864 g` and `k=1190.21 N/m` gives 166.414 Hz for M100. The FEM script gives 166.434236 Hz and 135.243349 Hz. The approximately 0.012% M100 difference is small but must be traced to unrounded inputs and modal-mass conventions, not silently harmonised.
2. The ODE model uses `C0=3.9844 nF`; another testbench audit uses `4.10 nF`; an earlier historical candidate mentions `15 nF`. These are not interchangeable.
3. `theta=450 µN/V` is a provisional midpoint of a 0.35–0.55 mN/V range. Its sign and physical derivation remain unauthenticated.
4. Perfect bonding, rigid clamp and translational-only tip mass are modelling assumptions requiring physical evidence.
5. Rev2.3 source values and the preliminary drawing revisions contain geometry/bondline differences; the exact controlled as-built definition is not available.

## 7. SECE energy-ledger reconstruction

The general boundary balance is:

```text
E_external,in - E_external,out
  = delta(E_stored) + sum(E_dissipated) + E_residual
```

Every storage element must use a consistent final-minus-initial change. The recovered ZPE-04A-ENC-0002 Rev0.5 record identifies that T2.2 added initial capacitor energies to the input side while also including final-minus-initial energy changes on the output side. This double-counted initial stored energy.

T2.3 corrects the residual to use consistent deltas for CSTORE, L1, parasitic capacitors, COSS and gate capacitance. The Rev0.5 package's 11 internal file hashes were verified in this pass; its static audit reproduced:

`PASS_STATIC_LEDGER_AND_REQUIREMENTS_STRUCTURE_NOT_SPICE`.

The same audit explicitly states:
- S_VL implementation: ideal switch placeholder, not a physical MOSFET pair.
- SPICE execution: NOT RUN.
- Hardware validation: NOT PERFORMED.
- Part selection: NONE.
- All 22 component-neutral requirements remain open.

## 8. ZPE-05 software verification boundary

The recovered ZPE-05 Rev0.4 batch bundle passed its 12-member SHA-256 manifest. Its archived regression log records 56 tests passing. An independent rerun in this runtime produced 55 passes and one environment-sensitive failure in the 1.5-second child-process timeout-retention test. The Python child interpreter took approximately 4.24 seconds to start in this environment, so the test's fixed 1.5-second limit expired before the stub began and before it could write its marker. The test is not counted as passed in this reproduction.

The remaining 55 tests passed. Even the recorded 56-test result is software regression only: the README explicitly leaves the locked ZPE-05 verification specification, production topology signer, simulator qualification and native RAW parser qualification open.

## 9. Verification classification

| Evidence | Current disposition |
|---|---|
| ODE reference script | Executed; archived JSON exact match |
| Stepped-beam FEM script | Executed; mesh convergence reproduced |
| SECE-004A Rev0.5 package hashes | 11/11 verified |
| SECE-004A Rev0.5 static audit | Pass, limited to static/source assertions |
| ZPE-05 Rev0.4 bundle hashes | 12/12 verified |
| ZPE-05 Rev0.4 regression | 55/56 reproduced; one timeout test environment-limited |
| LTspice/ngspice execution | Not established by this work |
| Native Spicelib RAW parser | Not qualified |
| Physical prototype measurement | Not established |
| Energy autonomy / net-positive result | Not established |
| Manufacturing release | Not authorized |

## 10. Next mathematical and engineering sequence

1. Recover exact controlled `TEST-001 Rev1.0` and `ZPE-05-VER-0001 Rev0.1` sources.
2. Reconcile C0, theta, damping, modal mass, material data, geometry and coordinate definitions.
3. Reconstruct the full state-space model and independently derive a symbolic energy identity with explicit port directions.
4. Extend the model to distributed/multi-mode electromechanical behaviour only after validating the single-mode basis.
5. Verify the ZPE-01 testbench and runner source bytes; correct the audit findings before execution.
6. Execute LTspice/ngspice with exact versions and retain netlists, logs, raw waveforms, exports, run commands and SHA-256 hashes.
7. Qualify the native raw-data adapter against real simulator-produced fixtures.
8. Only then revisit the ZPE-01/SECE integration gates and physical prototype requirements.

## 11. Change history

- **Rev0.1 — 2026-11-27:** Independent ODE and FEM source execution, archived ODE JSON comparison, SECE-004A Rev0.5 manifest/static-audit verification, and ZPE-05 Rev0.4 bundle/regression recheck. No original source modified.
