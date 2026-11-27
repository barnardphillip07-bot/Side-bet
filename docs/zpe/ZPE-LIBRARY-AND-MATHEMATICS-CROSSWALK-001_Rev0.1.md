# ZPE-LIBRARY-AND-MATHEMATICS-CROSSWALK-001 — Source and Equation Traceability

- **Record ID:** ZPE-LIB-XWALK-001
- **Revision:** Rev0.1
- **Date:** 27 November 2026
- **Repository:** `barnardphillip07-bot/Side-bet`
- **Branch:** `zpe/side-bet-lab-integration-001`
- **Status:** **DERIVED CROSS-LIBRARY INDEX / PARTIAL SOURCE RECONCILIATION / NOT A CANONICAL LAB CHARTER**
- **Companion:** `ZPE-DES-DEST-001 Rev0.1`
- **Purpose:** identify the source records, libraries, equations, software and verification artefacts required to develop the ZPE design destination without conflating workstreams or losing provenance.

---

## 1. Scope and evidence rule

This crosswalk connects the ZPE programme across Mathematics, Physics, Engineering and Technology. It is a navigation and reconciliation instrument, not proof that every historical source has been recovered or authenticated.

The accessible SW-ZPE-01 `SOURCE_REGISTER.csv` contains 27 indexed source records (`SWZ-SRC-001` through `SWZ-SRC-027`). Prior reconciliation work also identified a 146-record indexed collection assembled from that register and a 125-file Library collection. These counts describe discovery/index coverage, not 146 independently authenticated sources or 125 verified engineering results.

The 27-record source register is the controlling discovery lead for the SW-ZPE-01 source set. Preserve its exact file names, Library paths, SHA-256 values, duplicate relationships and audit dispositions. Do not silently normalize conflicting files or overwrite historical revisions.

## 2. Cross-library ownership map

| Library / lab | ZPE responsibilities | Recovered source lead | Current evidence status |
|---|---|---|---|
| Mathematics | Quantum field/Casimir models, analytical derivations, modal mechanics, ODE/FEM, SPICE analogies, numerical methods, energy identities, uncertainty | DINGOOS-MFR-001; DINGOOS-MATH-MARRIAGE-001; ZPE-01-ENC-0001; ZPE-01-ENC-0002; ZPE-04A; ZPE-05 | Substantial working mathematics recovered; canonical full equation ownership and several source records remain unresolved |
| Physics | Physical interpretation, Casimir/Lifshitz theory, test hypotheses, apparatus, calibration, confounders, measurement and replication | PHYSICS-LAB-REFERENCE-AUDIT-001 Rev0.2; independent physics reference PoC; DINGOOS ZPE research blueprint | Partial source recovery; no complete authenticated physical-lab charter, calibration package or physical ZPE measurement dataset located in inspected surfaces |
| Engineering | System requirements, SW-ZPE-01 POC, mechanical/electrical design, BOM, control topology, instrumentation, energy ledger, safety and release gates | SW-ZPE-01 Rev2.1; Rev2.3; SW-ZPE-01-PHY-DES-001; ZPE-04A and ZPE-05 audits | Substantial derived engineering documentation; manufacturing, simulation, physical and integration holds remain |
| Technology | AFM/MEMS, surface/material technologies, sensors, vacuum, precision motion, dynamic-Casimir resonators, acquisition and secure data systems | TECHNOLOGY-LAB-RECOVERY-AND-INTEGRATION-001 Rev0.1; DINGOOS-IDE-001; advanced-systems roadmap | Technology Lab charter/index/ownership and integrated source not authenticated; proposal/navigation records only |
| Programme | ZRI and ZHEP separation, hypotheses, falsification, design destination, gate structure and cross-lab interfaces | DINGOOS ZPE — Continuous-Energy Research & Engineering Blueprint v0.1 | Recovered as Library source; ZRI-01A selected as first research-instrument destination, not a generator |

### 2.1 Repository records

- Physics Lab audit: https://github.com/barnardphillip07-bot/Side-bet/blob/research/physics-lab-audit/docs/dingoos/research/PHYSICS-LAB-REFERENCE-AUDIT-001_Rev0.2.md
- Technology Lab recovery: https://github.com/barnardphillip07-bot/Side-bet/blob/research/technology-lab-recovery/docs/dingoos/research/TECHNOLOGY-LAB-RECOVERY-AND-INTEGRATION-001_Rev0.1.md
- Independent physics reference PoC: https://github.com/barnardphillip07-bot/Side-bet/tree/research/independent-physics-reference-poc
- ZPE programme design destination: https://github.com/barnardphillip07-bot/Side-bet/blob/zpe/side-bet-lab-integration-001/docs/zpe/ZPE-DESIGN-DESTINATION-REFERENCE-001_Rev0.1.md

These are derived/public-safe records. They do not authenticate protected BIF material or the private canonical DingoOS repository.

## 3. SW-ZPE-01 source register — 27 indexed records

The following is a compact functional map of the 27 rows in `SOURCE_REGISTER.csv`. The CSV remains the source of exact SHA-256, Library ID, byte size and Library path.

| Register ID | Original file / record | Function | Recorded disposition |
|---|---|---|---|
| SWZ-SRC-001 | `SW-ZPE-01_revised_mechanical_design_v1_2.pdf` | Preliminary mechanical geometry | Preliminary |
| SWZ-SRC-002 | `SW-ZPE-01_Mechanical_Drawings_M001-M005_RevA.pdf` | Mechanical drawings | Preliminary / conflicting |
| SWZ-SRC-003 | `SW-ZPE-01_Complete_POC_Engineering_Blueprint_Rev2.1.docx` | Consolidated POC design and test manual | Preliminary |
| SWZ-SRC-004 | `SW-ZPE-01_Rev2.2_BOM_RECONCILIATION_PRELIMINARY.xlsx` | BOM reconciliation | Preliminary / not purchase release |
| SWZ-SRC-005 | `SW-ZPE-01_Rev2.3_Engineering_Reconciliation_Reference_Report.pdf` | Governing mechanical/electrical reconciliation | Preliminary / not fabrication released |
| SWZ-SRC-006 | `SW-ZPE-01_M001-M005_RevA_PRELIMINARY.pdf` | Revised mechanical drawings | Preliminary / hold |
| SWZ-SRC-007 | `sw_zpe_01_fem_aligned.py` | Interface-aligned stepped-beam FEM | Retrieved and executed; ideal model limitations apply |
| SWZ-SRC-008 | `sw_zpe_01_fem_aligned(1).py` | Duplicate FEM source | Byte-identical to SRC-007 |
| SWZ-SRC-009 | `SW-ZPE-01_HOLD-E07_CM_Sensitivity_Envelope.py` | First-order common-mode sensitivity | Retrieved and executed; not a vendor macromodel |
| SWZ-SRC-010 | `SW-ZPE-01_HOLD-E07_CM_Sensitivity_Envelope(1).py` | Duplicate sensitivity source | Byte-identical to SRC-009 |
| SWZ-SRC-011 | `SW-ZPE-01_HOLD-E07_CM_Sensitivity_Envelope.csv` | Generated sensitivity data | Regenerated numeric columns; header discrepancy |
| SWZ-SRC-012 | `SECE_004A_CaseA_Source_Reconciliation.md` | SECE source/energy-ledger audit | Blocked / not ready for LTspice |
| SWZ-SRC-013 | `SWZ-ENV-001_ClosedLoop_Rev01I_CANDIDATE.cir` | SECE parent candidate netlist | Source retrieved; not simulation verified |
| SWZ-SRC-014 | `SWZ-ENV-001_ClosedLoop_Rev01I_CaseA_VSTORE5V_DERIVATIVE.cir` | 5 V derivative | Blocked / not executed |
| SWZ-SRC-015 | `SWZ-ENV-001_ClosedLoop_Rev01I_CaseA_VSTORE12V_DERIVATIVE.cir` | 12 V derivative | Blocked / not executed |
| SWZ-SRC-016 | `SWZ-ENV-001_Rev01I_ENVREC_A.cir` | Controlled SECE derivative | Blocked / static audit in progress |
| SWZ-SRC-017 | `SWZ-ENV-001_Rev01I_ENVREC_A_CaseA_VSTORE5V.cir` | 5 V ENVREC_A copy | Byte-identical to SRC-016 |
| SWZ-SRC-018 | `SWZ-ENV-001_Rev01I_ENVREC_A_CaseA_VSTORE12V.cir` | 12 V ENVREC_A derivative | Not executed |
| SWZ-SRC-019 | `SWZ-ENV-001_Rev01I_Engineering_Change_Note.md` | Derivative provenance | Source recovered |
| SWZ-SRC-020 | `SW-ZPE-01_Integrated_Virtual_Prototype_Rev0.1.md` | Integrated architecture candidate | Proposed / not frozen |
| SWZ-SRC-021 | `SW-ZPE-01_Integrated_Virtual_Prototype_Rev0.1(1).md` | Duplicate integrated prototype | Byte-identical to SRC-020 |
| SWZ-SRC-022 | `ZPE01-ENC-0001.md` | Original mathematical encyclopaedia Rev0.1 | Historical revision preserved |
| SWZ-SRC-023 | `ZPE01-ENC-0001_Rev0.2.md` | Reciprocal equations and ODE reference | Mathematical foundation reviewed; ODE executed; SPICE not executed |
| SWZ-SRC-024 | `ZPE01_RECIPROCAL.sub` | SPICE mobility-analogy subcircuit | Not simulator verified |
| SWZ-SRC-025 | `ZPE01_ENERGY_TEST.cir` | SPICE energy testbench | Not simulator verified |
| SWZ-SRC-026 | `ZPE01_REFERENCE_TESTS.py` | Independent ODE reference implementation | Reproduced against archived output |
| SWZ-SRC-027 | `ZPE01_REFERENCE_RESULTS.json` | ODE reference results | Reproduced; numerical model output only |

The exact CSV Library ID is `libfile_bd8a51df90188191b82becf769f1c94c`; retrieved file identity is `file_00000000a14882118ab66b1762f52ddc`. The register records the exact SHA-256 values and paths. Examples of material conflicts that must remain visible include the PZT leading-edge/bondline geometry disagreement between SRC-002 and SRC-006, and the controller sensitivity CSV header discrepancy in SRC-011.

## 4. Supplementary ZPE Library records beyond the 27-row source register

The 27-row CSV is the historical SW-ZPE-01 source register, not the full later ZPE verification and design archive. The following additional records were found in Library searches and must be included in the next consolidated source manifest.

| Record / file | Contribution | Current status / limitation |
|---|---|---|
| `RESEARCH_AND_ENGINEERING_BLUEPRINT_v0.1.md` | Programme-level ZRI/ZHEP architecture, Casimir mathematics, hypotheses, energy ledger and gates | Research blueprint; not generator validation |
| `ZPE-01-ENC-0001 Rev0.3` | Reciprocal electromechanical model, FEM-to-SDOF mapping, ODE and SPICE audit | Equations reviewed; ODE reproduced; SPICE unexecuted; parameters unauthenticated |
| `ZPE-01-ENC-0002 Rev0.1–Rev0.4` | Testbench and runner review lineage | Candidate review; Rev0.4 contains blocking execution/readiness findings; not validated |
| `ZPE-04A-ENC-0002 Rev0.1–Rev0.5` | SECE topology, recovery and energy-ledger derivatives | Rev0.5 static/reduced-order screen only; no SPICE run; topology not selected/validated |
| `ZPE-05-DEV-AUDIT-0001 Rev0.2–Rev0.4` | Postprocessor, batch runner, governance and regression audits | Synthetic regression only; qualification remains open |
| `ZPE-05-RAW-ADAPTER-QUAL-0001 Rev0.1–Rev0.2` | Native simulator RAW fixture/adapter qualification | Three fixture byte-integrity checks pass; real Spicelib parser not executed/qualified |
| `ZPE-05-GOV-0001 Rev0.1` | Proposed governance overlay | Proposed, not authenticated/controlled |
| `postproc_zpe05(8).py`, `postproc_zpe05(9).py` | Processor candidates | Must be revision-pinned and reconciled with their audit bundles |
| `ZPE-05-RAW-001_Recovery_Audit_Package_Rev0.1_CANDIDATE.zip.sha256` | Candidate recovery package identity | Hash file only; retrieve package and verify manifest before use |
| `RESEARCH_SPECIFICATION_v0.2.md`, `RESEARCH_SPECIFICATION_v0.3.md` | Research specification lineage | Reconcile exact source and authority before treating as controlled |
| `ZPE01_RECIPROCAL_Rev0.3_DRAFT.sub`, `ZPE01_ENERGY_TEST_Rev0.3_DRAFT.cir` | Corrected SPICE candidate files | Drafts; simulator execution remains unverified |
| `SW-ZPE-01_Physical_Prototype_Engineering_Design_Rev0.1.docx` | Coordinated physical prototype definition | Derived design candidate; not fabrication released |

Important exact Library IDs found during this pass:
- Programme blueprint: `libfile_50250cb5dcfc8191b091c82d9df2abd0`.
- SW-ZPE-01 Rev2.1 blueprint: `libfile_44b439cbd9188191b6f7e8769f11be18`.
- ZPE-01-ENC-0002 Rev0.1: `libfile_d6e9fa2718888191b433f4e8a684afca`.
- ZPE-01-ENC-0002 Rev0.2: `libfile_5af4a3698c988191891e1ba78eba4764`.
- ZPE-01-ENC-0002 Rev0.3: `libfile_ddecfec89f78819186f7a84560550101`.
- ZPE-01-ENC-0002 Rev0.4: `libfile_22d0d34cc9708191b398a2af3c19ac50`.
- ZPE-04A-ENC-0002 Rev0.5: `libfile_281ef95577d08191a3f813e6d5c5fe3c`.
- ZPE-05-DEV-AUDIT-0001 Rev0.4: `libfile_416dc43543748191bb958d254dee20d4`.
- ZPE-05 RAW adapter qualification Rev0.1: `libfile_c112f1ed25e08191968d03bf0605af09`.
- ZPE-05 RAW adapter qualification Rev0.2: `libfile_0fa9e059fe0c819193866b03eef7367e`.
- Proposed ZPE-05 governance overlay: `libfile_342254978570819185dd513577ed2b7e`.
- Physical prototype design Rev0.1: `libfile_3138d24144b08191a57d4322f2d5e95f`.

Library IDs are navigation identifiers, not cryptographic identities. The source register's SHA-256 and exact source bytes remain the integrity reference where available.

## 5. Mathematics ownership and equation traceability

### 5.1 ZPE programme mathematics (ZRI/Casimir)

| Equation family | Required owner | Status |
|---|---|---|
| Quantum harmonic oscillator `E_n=ħω(n+1/2)` | Mathematics + Physics | Established mathematical model; not an extraction mechanism |
| Vacuum mode sum `E_vac=(1/2)Σħω` | Mathematics + Physics | Formal divergent expression; requires regularization/renormalization |
| Ideal parallel-plate Casimir energy/force | Mathematics + Physics | Established idealized limit |
| Sphere–plane proximity-force approximation | Mathematics + Physics | Approximation; validity and corrections required |
| Lifshitz real-material force | Mathematics + Physics | Required quantitative comparison; material response and temperature data required |
| Dynamic Casimir mode/circuit equations | Mathematics + Physics + Technology | Separate advanced branch; modulation input energy must be included |
| Closed-cycle work `∮F dq` | Mathematics + Physics | Conservative reference cycle gives zero net reversible work when all states restore |
| Net energy balance | Engineering + Mathematics + Physics | Mandatory system-level accounting identity |
| Uncertainty propagation/covariance | Mathematics + Engineering + Physics | Required before acceptance |

### 5.2 SW-ZPE-01 mathematics (classical electromechanical substream)

Governing reciprocal single-mode equations:

`m x¨ + c x˙ + k_sc x - θv = F_ext`

`q = C0 v + θx`

`i_into = C0 v˙ + θx˙ + Gp v`

Stored energy:

`E = 1/2 m x˙² + 1/2 k_sc x² + 1/2 C0 v²`

Dissipation:

`P_diss = c x˙² + Gp v²`

Power identity:

`F_ext x˙ + v i_into = dE/dt + c x˙² + Gp v².`

Open-circuit stiffening:

`k_oc = k_sc + θ²/C0.`

Modal frequency:

`f = (1/2π)sqrt(k_modal/m_modal).`

The exact same signed `θ` must appear in the reciprocal mechanical and electrical paths. `k_sc` is short-circuit modal stiffness. Static tip stiffness and modal stiffness are different quantities; use a consistent FEM eigenpair/mode normalization for SDOF reduction.

### 5.3 Structural and material equations

For a stepped Euler–Bernoulli beam:

`C_tip = ∫_0^L (L-s)²/[EI(s)] ds,  k_tip=1/C_tip.`

For mode shape `φ(s)`:

`m_eff = ∫ρAφ² ds + Σ M_j φ(s_j)² + attached distributed contributions.`

`k_eff = ∫EI(s)[φ''(s)]² ds.`

For a simple capacitance geometry check:

`C0 ≈ ε0 εr A/t.`

This is a plausibility check, not an authenticated PZT capacitance. Historical candidate values 3.9844 nF, 4.10 nF and 15 nF conflict and must remain unresolved until exact part identity and measurement conditions are recovered.

For a simplified dielectric-loss model:

`Gp = ω C0 tan(δ).`

For a measured quality factor under a specified boundary:

`c ≈ m_modal ω_n/Q.`

These are model relations; frequency, temperature, amplitude and boundary conditions must be stated.

### 5.4 Energy and measurement equations

Electrical and mechanical boundary power:

`P_e = v i,  P_m = F v_m.`

Stored energy:

`E_C=1/2 C V²,  E_L=1/2 L I².`

RF accepted power:

`P_RF,accepted = P_incident - P_reflected.`

System net-energy accounting:

`E_net = E_useful,out - ΣE_all,in + ΔE_stored.`

Proposed conservative lower confidence bound:

`P_LCB = P_net_hat - k u_c(P_net_hat).`

For correlated inputs:

`u_c²(y)=JΣJᵀ.`

No subsystem's recovered energy may be counted twice. A piezoelectric recovery stage transfers energy from an externally driven/mechanically excited system; it is not an independent energy source.

## 6. Software, solver and verification traceability

| Asset / audit | Evidence established | Still not established |
|---|---|---|
| ZPE-01 independent SciPy ODE reference | Rev0.2 archived JSON hash reproduced; Rev0.3 FEM-reduced parameter mapping and ODE cases recorded | Physical parameter calibration; SPICE equivalence |
| FEM aligned beam script | Source retrieved and executed; ideal Euler–Bernoulli mesh results | Adhesive, clamp, rotary inertia, sensor/lead effects, electromechanical coupling and physical validation |
| ZPE-01 SPICE drafts | Static KCL/source review and corrected draft strategy | Actual LTspice/ngspice run, syntax compatibility, convergence, native RAW/log |
| ZPE-04A Rev0.5 | Parent hashes, static topology/ledger review and reduced-order model reproduced | Device-level MOSFET model, SPICE run, physical topology and integration |
| ZPE-05 Rev0.5 candidate | 161 synthetic tests recorded as passing | Locked verification schema, trusted authority, native RAW parsing, simulator and hardware qualification |
| ZPE-05 Rev0.4 reproduction | 12/12 bundle hashes and 56/56 synthetic tests under low-startup wrapper; default environment timeout sensitivity recorded | Native parser/simulator/hardware qualification |
| RAW adapter qualification Rev0.1/0.2 | Three real simulator-generated fixture byte-integrity checks, parser API source audit | Actual Spicelib parser execution; real fixture ingestion qualification |
| Physics Lab reference PoC | Standard-library oscillator and optics reference models/tests | Full physical validation, unit/dimensional engine, uncertainty and experimental acquisition |

A software `PASS`, synthetic fixture `PASS`, file hash match, static audit `PASS` or ODE energy residual does not mean the hardware, simulator, parser or energy-generation hypothesis has passed.

## 7. Contradictions and unresolved source authority

The following remain open and must not be silently normalized:

1. Exact controlled `TEST-001 Rev1.0` source is `UNRETRIEVED`.
2. Exact locked `ZPE-05-VER-0001 Rev0.1`, including Section 8.6 and P0–P9, remains `UNRETRIEVED`.
3. `ZPE-05-GOV-0001` is a proposed overlay, not authenticated production authority.
4. Production topology signer/authority root and physical Rev01I pin/current/trace mapping are not authenticated.
5. Native Spicelib parser and LTspice/ngspice execution are not qualified.
6. Exact PZT MPN, poling/electrode orientation, capacitance, signed coupling, damping, leakage and material properties remain unauthenticated.
7. Mechanical drawing/bondline/PZT-position discrepancies remain in the source register.
8. Rev01I source omissions and energy-ledger defects remain in the controlled audit lineage; derivative repairs must not be transplanted into parent source without a new revision and provenance.
9. Canonical Mathematics, Physics and Technology Lab charters/indices/ownership maps are not all authenticated in the inspected surfaces.
10. Protected BIF/IP source and exact original mathematical foundations remain private and must not be reconstructed or published.

## 8. External reference register

- Real-material Casimir force review: Klimchitskaya, Mohideen & Mostepanenko, *Rev. Mod. Phys.* 81, 1827 (2009), https://doi.org/10.1103/RevModPhys.81.1827.
- Casimir MEMS materials/geometries/metrology review (2024), https://doi.org/10.3390/ma17143393.
- Precision Casimir force measurement review (2024), https://doi.org/10.3390/physics6020055.
- Dynamical Casimir Effect: 55 Years Later (2025), https://doi.org/10.3390/physics7020010.
- NIST TN 1297 measurement uncertainty guidance, https://www.nist.gov/pml/nist-technical-note-1297.
- Spicelib RawRead documentation, https://spicelib.readthedocs.io/en/stable/classes/raw_read.html.
- ngspice batch output manual, https://nmg.gitlab.io/ngspice-manual/analysesandoutputcontrol_batchmode.html.

External references support scientific/methodological claims only; they do not authenticate DingoOS or prove a ZPE generator.

## 9. Required completion actions

1. Materialize/reconcile the complete 146-record index and 125-file collection against the 27-row source register; record exact Library paths, IDs, revisions, hashes, duplicates and dispositions.
2. Recover the complete `RESEARCH_AND_ENGINEERING_BLUEPRINT_v0.1` model bundle and source `src/zpe_model.py`; inspect and execute only after exact source/environment recovery.
3. Complete the Mathematics source-to-equation register for Casimir/Lifshitz, sphere–plane, dynamic Casimir, SW-ZPE-01, ZPE-04A and ZPE-05.
4. Recover the canonical Physics and Technology Lab charters/indexes or preserve the authority gaps as unresolved.
5. Continue SW-ZPE-01 PZT parameter and source authentication, TEST-001/ZPE-05-VER recovery, simulator installation/execution and native RAW parser qualification.
6. Complete the ZRI-01A instrument trade study, requirements, metrology plan, real-material mathematical oracle and safety review.
7. Keep the ZRI and SW-ZPE-01 test boundaries distinct; link only through justified shared measurement and assurance methods.
8. Preserve every failed, superseded and null result. Do not promote a hypothesis by changing the acceptance criteria after observing data.

## 10. Disposition

**Cross-library navigation:** established for the inspected sources.

**SW-ZPE-01 source register:** 27 records identified; exact source metadata remains in `SOURCE_REGISTER.csv`.

**Broader ZPE Library collection:** 146 indexed records and 125-file collection referenced by prior reconciliation; exhaustive byte-level verification and final crosswalk remain open.

**Mathematical foundation:** reciprocal PZT model equations and energy identity reviewed; ideal Casimir references and programme-level net-energy equations recovered; real-material Casimir implementation and full cross-lab equation ownership remain to be completed.

**Primary destination:** ZRI-01A sphere–plane Casimir Research Instrument, as defined in `ZPE-DES-DEST-001 Rev0.1`.

**Generator qualification:** not established. No positive net-energy ZPE generator is demonstrated by the current library, simulations or prototypes.

## 11. Change history

- **Rev0.1 — 27 November 2026:** first cross-library source and mathematics crosswalk, based on the recovered 27-row SW-ZPE-01 source register, supplementary ZPE Library searches, Mathematics/Physics/Technology recovery records and the ZPE programme blueprint. No original source modified; no simulation or physical qualification claimed.
