# PHYSICS-LAB-REFERENCE-AUDIT-001 — Archive Recovery and Numerical-Integrity Review

- Revision: Rev0.2
- Date: 27 November 2026
- Status: **PARTIAL SOURCE RECOVERY — NUMERICAL EXPERIMENT DEFECT IDENTIFIED — EQUATION LINKS UNRESOLVED — FULL PHYSICAL LAB AUDIT NOT COMPLETE**
- Repository: `barnardphillip07-bot/Side-bet`
- Branch: `research/physics-lab-audit`
- Parent audit: [Rev0.1](https://github.com/barnardphillip07-bot/Side-bet/blob/research/physics-lab-audit/docs/dingoos/research/PHYSICS-LAB-REFERENCE-AUDIT-001_Rev0.1.md)
- Authority: Derived, public-safe research audit. Not an Owner Decision, not an authenticated Physics Lab master specification, not a canonical equation release, not a source reconstruction of protected BIF material, and not a physical experiment report.

## 1. Executive disposition

The recovery pass has inspected three source-bearing Knowledge Snowflake archives from the reverse-engineered DingoOS working baseline: v0.8.0, v0.10.0 and v0.11.0. The archives contain substantial mathematical-research and numerical-simulation material. They do **not**, within the inspected contents, provide a dedicated Physics Lab charter/index, physical apparatus register, calibration-certificate package, raw physical-measurement dataset, or complete physical experiment history.

The most consequential new finding is a time-grid defect in the archived damped-oscillator example. The model sets its step size to (T/(N-1)), consistent with (N) samples including both endpoints, but performs (N) integration steps. Its final displacement and velocity therefore correspond to (T+Delta t), while its final stored-energy sample corresponds to (T). At the archived 2,001-sample baseline, the nominal 10-second calculation advances to 10.005 seconds. This makes the recorded state and energy outputs refer to different times, and it compromises the existing convergence study because each resolution is evaluated at a different terminal time.

A corrected independent calculation using (N-1) steps for (N) endpoint-inclusive samples gives approximately fourth-order RK4 convergence for the one archived oscillator case. That is a diagnostic calculation performed for this audit; it is not a source patch, an execution of the full DingoOS package test suite, or evidence of physical validity.

**Overall disposition:** the numerical-reference and simulation records are now materially better understood, but the Physics Lab as a physical measurement and validation capability remains **NOT FULLY AUDITED**. The authenticated lab-specific governing records and the actual physical-measurement chain remain UNRETRIEVED in the inspected surfaces. Broader existence is not established.

## 2. Source identity, archive provenance and comparison

### 2.1 Exact archives inspected

| Archive | Bytes | SHA-256 |
|---|---:|---|
| `dingoos_knowledge_snowflake_v0.8.0.zip` | 887,216 | `544bb9e080ac7d98f6dc88989c8ebde0dd166e74f8a578f42b90369bb482cb05` |
| `dingoos_knowledge_snowflake_v0.10.0.zip` | 824,807 | `605c63cc402386841882a710dca7408c43dd467a30d20f77aa2f069c9dabae1d` |
| `dingoos_knowledge_snowflake_v0.11.0.zip` | 835,439 | `6672810b3874d1822a213ee838954566197808241212078473e79a1645bb4c58` |

The v0.11.0 ZIP contains 198 entries (147 files). Its README title still identifies the package as “v0.8.0” while later sections describe v0.9.0 and v0.11.0 additions. This is a version-label/provenance discrepancy to reconcile before treating the ZIP filename as a fully authoritative software release identifier.

### 2.2 Cross-archive preservation finding

The following four files are byte-identical in all three inspected archives:

| Relative path | SHA-256 |
|---|---|
| `snowflake-data/records.jsonl` | `8a9f5e0628d7dbc002f6ddcc743f38c6afdb10ddce404d30b30b48d07a0f8512` |
| `numerical-artifacts/086ca9d6-6f60-4f5a-b198-f9223acc8adc.json` | `b21d66d0b099d3e31894b867ae135652c1176fdc7c6ae233f9495d734cbb4b0f` |
| `examples/numerical_resonance.py` | `c699024244ea578157a0c8485b62a72206f359ef336aba6efa34521806afe519` |
| `dingoos-integrated-data/knowledge-store/records.jsonl` | `9aa7340ba8e293a7e03e19c63a248ed3948cb190df63bf10144c1935d6d171e7` |

Accordingly, the damped-oscillator example, its failed convergence artifact, and the linked research-record snapshots were not corrected between these three supplied archive snapshots. This observation is limited to the inspected ZIP contents; it does not establish the state of other working-baseline files outside those archives.

### 2.3 Object-store integrity and contents

The v0.11.0 integrated SQLite object store contains 21 indexed `object_versions`:

| Kind | Count |
|---|---:|
| `COUPLED_MULTIPHYSICS_EXPERIMENT` | 4 |
| `COUPLING_STRATEGY_COMPARISON` | 4 |
| `MULTIPHYSICS_ARCHITECTURE` | 1 |
| `SPATIAL_MULTIPHYSICS_EXPERIMENT` | 12 |
| `MATHEMATICAL_EQUATION` | **0** |

All 21 stored blobs were decompressed and checked against both their stored-byte SHA-256 and the plaintext SHA-256/length declared in the SQLite metadata. No mismatch was found. This is an integrity check of the recovered bundle, not proof of authorship, canonical authority, or scientific truth.

## 3. Numerical experiment engine and equation linkage

The v0.11.0 package contains a model-agnostic numerical experiment engine supporting deterministic model calls, parameter sweeps, seeded uncertainty propagation, resolution comparisons, JSON artifacts and SHA-256 artifact checks. Its own documentation correctly cautions that numerical verification does not establish physical validation; a convergence result depends on the selected resolution parameter and metric; and the engine does not itself infer units, certify solver stability or validate constitutive laws.

The stored `snowflake-data/records.jsonl` snapshot contains four linked numerical artifacts:

1. `NUMERICAL_EXPERIMENT` — damped oscillator baseline;
2. `PARAMETER_SWEEP` — five damping-coefficient values;
3. `UNCERTAINTY_ANALYSIS` — 500 seeded samples;
4. `CONVERGENCE_TEST` — failed endpoint-displacement convergence record.

The baseline declares:
- model: `damped-oscillator-rk4`, version `1.0`;
- parameters: (m=1), (c=0.08), (k=4), (x_0=1), (v_0=0), duration (T=10) s;
- resolution: (N=2001), seed `20261122`;
- assumptions: linear viscous damping and one degree of freedom;
- equation reference: `DNG-MECH-OSC-001`.

The archive contains the equation ID in the example and experiment/sweep/uncertainty artifacts, but no corresponding equation-registry object in `snowflake-data/records.jsonl` or the 21-object integrated object-store snapshot. The reference therefore remains **UNRESOLVED IN THESE ARCHIVES**. It must not be recreated from the example code and then represented as a recovered canonical equation.

The source does contain an equation-storage capability: `ResearchMemory.store_equation` writes a `MATHEMATICAL_EQUATION` object, and the dependency resolver can pin exact parent versions or preserve references as unresolved/access-restricted. Tests for this prototype capability are present in the source tree. That capability is distinct from the evidence question: no equation object for `DNG-MECH-OSC-001` was present in the inspected bundled store. No full package test run was performed as part of this archive audit.

## 4. Critical numerical finding — oscillator time-step count

### 4.1 Source-level cause

The archived example computes:

```python
dt = duration / (resolution - 1)
...
for i in range(resolution):
    energy.append(0.5*m*v*v + 0.5*k*x*x)
    ...
    x += dt * (...)
    v += dt * (...)
```

The step size corresponds to (N-1) intervals between (N) samples. The loop nevertheless advances the state (N) times. Consequently:

```text
number of state advances = N
dt                         = T / (N - 1)
actual state end time     = N*T / (N - 1) = T + dt
last energy sample time   = (N - 1)*dt = T
```

The energy trace is recorded before each step. Its last entry is at (T); the final (x) and (v) returned by the function are after the last, extra advance at (T+Delta t).

### 4.2 Reproduction at the stored baseline

For (N=2001), (T=10) s and (Delta t=0.005) s:

| Quantity | Archived/reproduced value |
|---|---:|
| State advances | 2,001 |
| Actual state endpoint | 10.005 s |
| Returned final displacement | 0.282088299401168 m |
| Returned final velocity | -1.22719025450812 m/s |
| Last stored energy-trace value (at 10 s) | 0.9127454308214699 J |
| Energy computed from the returned final (x,v) | 0.9121455776979381 J |
| Endpoint energy mismatch | 0.0005998531235317 J |

An independent analytic solution of the declared damped oscillator gives, at (t=10) s, (x=0.2882112685142683) m, (v=-1.221977053718388) m/s and (E=0.9127454305043434) J. At (t=10.005) s it gives (x=0.28208829834822313) m, (v=-1.2271902552171408) m/s and (E=0.9121455773799478) J. The archived state agrees with the latter endpoint to the expected numerical precision, while its recorded energy agrees with the former. This independently confirms the endpoint mismatch.

### 4.3 Consequence for the archived convergence test

The archived convergence test uses resolutions 251, 501, 1001 and 2001 with the same (dt=T/(N-1)) and the same (N)-step loop. Its actual state endpoints are therefore 10.04, 10.02, 10.01 and 10.005 s, respectively. It compares different terminal physical times rather than measuring resolution error at one fixed terminal time.

The stored artifact remains:

- tolerance: (2	imes10^{-4});
- final relative change: (0.021797106163725315);
- recorded result: `passed: false`.

**The FAILED record must remain FAILED and immutable.** However, its result is not a valid fixed-terminal-time convergence assessment because the compared outputs have different end times. It neither establishes that the corrected RK4 implementation fails convergence nor establishes physical validity.

### 4.4 Independent fixed-endpoint diagnostic

For this audit only, the same RK4 scheme was independently evaluated with (N) endpoint-inclusive samples and (N-1) state advances, so each resolution ends at exactly (T=10) s. Displacement errors against the independent analytic solution were:

| Samples (N) | Step size (s) | Absolute final-displacement error (m) |
|---:|---:|---:|
| 251 | 0.040 | (4.2011	imes10^{-6}) |
| 501 | 0.020 | (2.6607	imes10^{-7}) |
| 1001 | 0.010 | (1.6732	imes10^{-8}) |
| 2001 | 0.005 | (1.0488	imes10^{-9}) |

The corresponding observed orders between successive refinements are approximately 3.981, 3.991 and 3.996. This is consistent with fourth-order convergence for this one linear oscillator case under the corrected fixed-endpoint diagnostic.

This diagnostic is **not** a committed code change, not a project-wide test pass, not an independent physical experiment and not a replacement for the original failed artifact.

### 4.5 Required code-review correction

A future separately reviewed patch should choose and document one consistent API meaning:
- if `resolution` means sample count including both endpoints, execute exactly `resolution - 1` advances and store energy after the final advance; or
- if it means step count, calculate `dt = duration / resolution` and define the output sampling contract accordingly.

The correction should add regression checks that:
1. returned final state time equals the declared duration;
2. the final energy is calculated from the returned final state;
3. energy trace length and sample timestamps match the declared grid;
4. convergence compares the same terminal time and same observable at each resolution;
5. observed order is estimated over a declared asymptotic refinement range;
6. the old failed artifact remains available as an immutable historical result, explicitly superseded only by a new run.

No source code was changed in this audit branch.

## 5. Multiphysics models and unresolved equation references

The package contains two distinct simulation levels.

### 5.1 Reduced-order five-domain demonstrator

`MULTIPHYSICS_SOLVER.md` describes a lumped/reduced-order model coupling mechanical, effective-fluid, lumped RLC/electromagnetic and thermal states, with a global energy ledger. It states the continuous energy balance and uses RK4 to integrate work/heat accounting. It explicitly excludes general 3-D CFD, full Maxwell field solutions, finite-element solid mechanics and general continuum simulation. Its coefficients and constitutive assumptions are illustrative; its own documentation says physical validation requires calibrated data and uncertainty-aware comparison.

The three stored coupled-multiphysics experiment records are labelled `PROPOSED_REDUCED_ORDER_MODEL` and have empty equation-ID lists. They are derived computational demonstrations, not measurements of a physical apparatus.

### 5.2 Periodic one-dimensional spatial benchmark

The spatial solver is explicitly a bounded one-dimensional periodic demonstrator: a linear elastic bar, linear viscous fluid momentum, transverse one-dimensional Maxwell fields and heat conduction. The records identify `DNG-MP-SPATIAL-1D-001`, use 64 cells, (Delta t=10^{-4}) s and duration (0.01) s, and record Python 3.13.5 / NumPy 2.3.5 environments. Stored energy residuals are very small for the selected numerical cases, but the solver itself correctly says that the discrete energy residual is a numerical diagnostic, not proof, and that physical validation requires measured data.

The 12 spatial experiment objects carry references to:
- `DNG-MECH-PDE-001`;
- `DNG-FLD-PDE-001`;
- `DNG-EM-PDE-001`;
- `DNG-THM-PDE-001`.

For all 12 objects, the object-store provenance metadata records these references as `UNRESOLVED_OR_ACCESS_RESTRICTED`. No matching equation objects appear in the 21-object store snapshot. Some experiment-to-experiment dependencies are correctly pinned; those dependencies do not resolve the missing equation identities.

The spatial artifacts are classified `PROPOSED_DISTRIBUTED_1D_BENCHMARK` and report `NUMERICALLY_TESTED_ONLY`. Their energy-identity results must not be promoted to a physical validation claim or interpreted as proof of the referenced canonical PDEs.

## 6. Actual Physics Lab artefacts not located

Across the inspected Library search/list surfaces, the three recovered Knowledge Snowflake ZIPs, the DingoOS mathematical/engineering records and the historical project compilation, the following Physics Lab master artefacts were **not located**:

- dedicated Physics Lab charter, governing scope and canonical index;
- authoritative lab experiment register and protocol catalogue;
- physical apparatus and instrument inventory;
- current calibration certificates and measurement-standard chain;
- raw physical measurement datasets, acquisition metadata and calibration corrections;
- processed datasets tied to raw-data hashes;
- full measurement uncertainty budgets and covariance assumptions;
- physical test reports, controls, repeatability and independent replication records;
- a complete lab change/review history and disposition of null, failed or contradictory runs.

This is a bounded “not located in the inspected surfaces” result, not a claim that these records do not exist elsewhere.

### 6.1 Historical project-board navigation leads

The public DingoOS Project Board is a sanitized, read-only status source, not the private canonical implementation. Its current README snapshot identifies Laboratory as one intended logical workstream; it does not establish a separate Laboratory repository or a complete Physics Lab implementation.

That historical board snapshot points to:
- PR #128, “Section #007 Experiment Protocol”: preregistration/protocol completeness structures for variables, controls, sample size, randomization/blinding, stopping criteria and safety gates;
- PR #129, “Section #008 Evidence Ledger”: append-only evidence ledger and a proposed raw → calibrated → derived → analysed → reported path;
- PR #130, replay integrity: reuse of existing research execution, ledger, evidence and knowledge services, with raw-observation identity binding instrument, calibration, environment and context.

The same snapshot says the changes were draft/unmerged at that recorded checkpoint, tests had been authored but not run on the exact branches, and governed execution/evidence integration remained open. Those historical PR links are navigation leads only; the current private PR source and branch state were not retrieved in this pass.

The linked GitHub connection returned HTTP 404 for `phillipbarnard07-cell/DingoOS` and `phillipbarnard07-cell/V1`. The public Project Board and `dingoos-horizon` were readable with pull-only permissions. The Horizon tree had no lab/physics/experiment/calibration paths. A 404 is an access limitation; it is not evidence that a repository or source has been deleted. The reverse-engineered Library working baseline remains a distinct evidence source and is not invalidated by this GitHub access limitation.

## 7. External verification and metrology method

This audit uses external standards as method references, not as DingoOS-authority substitutes:

1. **NASA-STD-7009B, Standard for Models and Simulations** — active NASA standard; it places model acceptance criteria within the project/program and delegated technical-authority context. [NASA standard record](https://standards.nasa.gov/node/263)
2. **NASA-HDBK-7009B, Implementation Guide** — active handbook published 3 February 2026 and companion to NASA-STD-7009B; it provides technical implementation guidance for model/simulation practices. [NASA handbook record](https://standards.nasa.gov/standard/nasa/nasa-hdbk-7009)
3. NASA verification guidance distinguishes implementation/code verification and calculation/solution verification from validation against physical referents. Quantitative solution-verification and error estimates are needed to detect non-convergent calculations. [NASA verification assessment](https://www.grc.nasa.gov/www/wind/valid/tutorial/verassess.html) · [NASA procedures for calculation verification](https://www.nas.nasa.gov/assets/nas/pdf/papers/NASA-TP-2016-219422_and_JANNAF-GL-2016-0001.pdf)
4. **NIST metrological traceability policy** defines traceability as a property of a measurement result linked through a documented unbroken calibration chain, each step contributing to uncertainty. Calibration of an instrument alone does not make every result traceable, and traceability alone does not establish fitness for purpose. [NIST policy](https://www.nist.gov/calibrations/traceability)
5. **NIST Technical Note 1297** provides methods for Type A and Type B uncertainty evaluation, combining standard uncertainty components with covariance where appropriate, and reporting expanded uncertainty and its coverage factor. [NIST TN 1297](https://www.nist.gov/pml/nist-technical-note-1297)
6. **NISTIR 8250** collects calibration procedures for weights-and-measures laboratories, including time/frequency, electricity, force, dimensional, thermodynamic and pressure measurements. [NISTIR 8250](https://doi.org/10.6028/NIST.IR.8250)

Practical consequence: the lab audit needs a traceable measurement result chain, not merely a list of calibrated devices. Each result needs a defined measurand, method, instrument/setup identity, calibration references and corrections, uncertainty components, raw observations, transformations, software versions and purpose-specific acceptance criteria.

## 8. Findings and dispositions

| ID | Finding | Disposition |
|---|---|---|
| PLA-01 | v0.8.0, v0.10.0 and v0.11.0 research archives recovered and compared by exact bytes | SOURCE-RECOVERED / DERIVED ARCHIVE CLASS |
| PLA-02 | Numerical experiment and multiphysics simulation records recovered | COMPUTATIONAL EVIDENCE ONLY |
| PLA-03 | 21 integrated object-store blobs match stored and plaintext digests | BUNDLE-INTEGRITY-CHECKED |
| PLA-04 | `DNG-MECH-OSC-001` referenced but not represented by a mathematical-equation object in inspected stores | UNRESOLVED IN RECOVERED ARCHIVES |
| PLA-05 | 12 spatial records preserve four PDE refs as unresolved/access-restricted | UNRESOLVED EQUATION LINEAGE |
| PLA-06 | Oscillator example advances one step beyond its declared end time; final energy/state mismatch quantified | SOURCE DEFECT IDENTIFIED / PATCH NOT APPLIED |
| PLA-07 | Historical fixed-resolution convergence test compares different end times and remains failed | FAILED RECORD PRESERVED / TEST DESIGN INVALID FOR FIXED-ENDPOINT CLAIM |
| PLA-08 | Corrected fixed-endpoint RK4 diagnostic shows approximately fourth-order behaviour for one case | INDEPENDENT BENCHMARK DIAGNOSTIC ONLY |
| PLA-09 | Reduced-order and spatial multiphysics examples are explicitly proposed/numerically tested model classes | PHYSICAL VALIDATION NOT ESTABLISHED |
| PLA-10 | Dedicated Physics Lab charter, apparatus, instrument, calibration and raw physical-measurement package not located | NOT LOCATED IN INSPECTED SURFACES / BROADER EXISTENCE NOT ESTABLISHED |
| PLA-11 | Private canonical GitHub source could not be retrieved through the linked connection | INACCESSIBLE VIA THIS CONNECTION / NOT A DELETION CLAIM |
| PLA-12 | README package-version label is inconsistent with later internal version sections | PROVENANCE/VERSION RECONCILIATION OPEN |

## 9. Required continuation

1. Continue recovery against the full reverse-engineered canonical working baseline, not just this Knowledge Snowflake subpackage. Locate the lab charter/index, actual experiment catalogue, measurement object and calibration path, physical instrument register, raw data storage, lab execution/controller path and review history. Reconcile exact revision and ownership before calling these items canonical.
2. Resolve `DNG-MECH-OSC-001` and the four PDE references from their immutable source records, or keep them explicitly UNRESOLVED/ACCESS-RESTRICTED. Do not synthesize substitute equation objects.
3. Prepare a separately reviewed correction for the oscillator endpoint/time-step defect; preserve all existing archives and the failed convergence record byte-for-byte. Generate a new run with a fixed physical endpoint and report raw convergence values and observed order.
4. For the spatial model, recover the exact equation records and derivation lineage, independently verify discrete operators and boundary conditions, and run fixed-domain mesh/time refinement against independent benchmark solutions. Small energy residuals alone do not establish solution accuracy or physical validity.
5. Recover or design controlled physical experiments only after the intended physical predictions and authorized equations are available. Preregister the measurands, controls, domain, sample plan, stopping/safety criteria and discrimination against standard alternatives. Use traceable calibration chains and uncertainty budgets, retain raw data, and arrange independent replication proportionate to consequence.
6. Keep the numerical reference PoC, reduced-order model and proposed spatial benchmark separate from protected canonical mathematics and from DingoOS production integration until their provenance, interfaces, evidence and authorization are reviewed.
7. Preserve null, failed, contradictory and inconclusive outcomes. No result is to be promoted from simulation to physical observation or from numerical verification to scientific validation.

## 10. Change history

- Rev0.1 — 27 November 2026: Initial static source audit of the independent physics-reference PoC and available SW-ZPE-01 laboratory-method records.
- Rev0.2 — 27 November 2026: Recovered and compared the v0.8.0/v0.10.0/v0.11.0 Knowledge Snowflake archives; verified 21 stored-object blobs; traced oscillator and multiphysics equation references; identified the oscillator's extra RK4 step and fixed-endpoint inconsistency; performed an independent analytic/fixed-endpoint diagnostic; updated Physics Lab recovery scope and external V&V/metrology references. No project source code was changed; no canonical BIF equation authenticated; no physical experiment or full package test suite run; full Physics Lab audit remains incomplete.
