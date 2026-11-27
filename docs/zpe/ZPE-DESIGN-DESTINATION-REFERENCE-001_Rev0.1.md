# ZPE-DESIGN-DESTINATION-REFERENCE-001 — Programme Design Destination and Cross-Library Engineering Reference

- **Record ID:** ZPE-DES-DEST-001
- **Revision:** Rev0.1
- **Date:** 27 November 2026
- **Repository:** `barnardphillip07-bot/Side-bet`
- **Branch:** `zpe/side-bet-lab-integration-001`
- **Status:** **DERIVED PROGRAMME REFERENCE / PRIMARY RESEARCH-INSTRUMENT DESTINATION SELECTED / NOT A GENERATOR DESIGN / NOT RELEASED FOR FABRICATION**
- **Programme parent:** `DINGOOS ZPE — Continuous-Energy Research & Engineering Blueprint v0.1`
- **Scope:** Cross-library ZPE research and engineering destination, including Mathematics, Physics, Engineering and Technology workstreams; SW-ZPE-01 remains one distinct substream.
- **Authority:** Derived engineering reference. It does not amend authenticated originals, approve protected BIF/IP use, authorize fabrication, or establish a net-energy result.

---

## 1. Purpose and required outcome

This record converts the existing ZPE programme direction into a concrete, traceable engineering destination. The required outcome is at least one design that can be taken through requirements, mathematical modelling, engineering definition, construction planning, calibrated measurement and independent verification.

The primary destination selected for first development is:

**ZRI-01A — Sphere–Plane Casimir Research Instrument**

It is a laboratory research instrument for measuring Casimir-related force/force-gradient behaviour as a function of separation and for testing complete-cycle energy accounting. It is a viable scientific-instrument destination in the sense that its measurement principle, architecture and verification route are established enough to support detailed engineering. It is **not** a demonstrated zero-point-energy generator and must not be represented as one.

The programme retains two independent tracks:

1. **ZPE Research Instrument (ZRI):** measure quantum-vacuum-related interactions and test falsifiable energy-cycle hypotheses.
2. **ZPE Home/Vehicle Energy Platform (ZHEP):** a conventional, independently functional energy-management and charging platform using approved grid, PV, stationary battery, inverter and EVSE interfaces. ZHEP must never depend on an unqualified ZRI output.

No over-unity, vacuum-energy harvesting, gravity modification, autonomy or vehicle self-charging claim is authorized by this record.

## 2. Programme architecture and design candidates

### 2.1 Primary destination — ZRI-01A sphere–plane instrument

A sphere–plane test geometry is selected as the first research-instrument candidate because it reduces the large-area parallelism problem and has a substantial experimental measurement literature, including dynamic AFM-based measurements. The exact sensor, sphere radius, coatings, gap range, vacuum level, bandwidth and environmental specification remain design inputs to be selected from a metrology capability study.

Functional architecture:

- Test cell with a characterized sphere and planar sample.
- Calibrated force-sensitive cantilever / AFM or equivalent force-gradient sensor.
- Precision positioning actuator and independent gap reference.
- Surface characterization: material identity, coating thickness, roughness, contamination and geometry.
- Electrostatic calibration and patch-potential characterization.
- Temperature, pressure, vibration, humidity and electromagnetic-environment monitoring.
- Independently metered actuator, reset, vacuum, thermal-control, controller and data-acquisition supplies.
- Synchronized acquisition with immutable raw data, calibration metadata, configuration hashes and repeatable analysis.
- Reference artefact, sham configuration and blinded control sequence.

The preferred first measurement mode is force-gradient detection with a calibrated dynamic cantilever/AFM. Direct force measurement may be retained as an alternative. Final selection requires an instrument trade study and uncertainty budget.

### 2.2 Retained independent candidates

- **ZRI-01B — Parallel-plate MEMS instrument:** controlled boundary geometry and integrated displacement sensing. Retain as a distinct candidate; alignment, stiction, surface and actuator-reset effects require explicit evaluation.
- **ZRI-01C — Dynamical Casimir research platform:** time-dependent electromagnetic boundary conditions, microwave resonators and parametric modulation. Retain as a separate advanced-technology branch. All modulation and readout energy must be measured; photon generation does not by itself establish net vacuum-energy extraction.

The candidates must be compared against common requirements. Do not select a winner using an unweighted narrative or a single idealized formula.

## 3. Design boundary and interfaces

### 3.1 ZRI control volume

The instrument control volume includes the test cell, test bodies, sensor, positioning actuator, reset mechanism, vacuum/environment systems, thermal control, controller, acquisition electronics, calibration apparatus where energized during the run, and all energy-storage elements.

Every boundary crossing must be identified as electrical, mechanical, thermal, optical/RF, chemical, pneumatic or other relevant transfer. Startup, idle, measurement, shutdown and reset are all included.

### 3.2 Interfaces

- **Mechanical:** force, displacement, velocity, actuator work, reset work, vibration and fixture motion.
- **Electrical:** simultaneous voltage/current at each supply and output boundary; real power, not apparent power alone.
- **Thermal:** temperatures, gradients, heat exchange and thermal stabilization energy.
- **Vacuum/environment:** pump power, pressure, gas load, leaks and environmental stability.
- **Optical/metrology:** interferometer or displacement-reference power and calibration.
- **Data/control:** acquisition, timing, processing, communications and controller energy.
- **Evidence:** raw records, calibration IDs, test configuration, software version, hashes, uncertainty and signed review.

ZRI is physically separate from vehicle traction high voltage and household grid wiring. Any household/vehicle integration is conceptual only until a separate certified product programme exists.

## 4. Physics and mathematics reference register

All equations below must be accompanied by symbol definitions, SI units, domain assumptions, boundary conditions, provenance and verification tests in the detailed model records.

### 4.1 Quantized harmonic oscillator ground state — established

`E_n = \hbar\omega(n+1/2),   E_0 = \hbar\omega/2.`

This is the ground-state energy of a quantized mode. It does not identify a controllable reservoir or prove that cyclic net work can be extracted.

### 4.2 Electromagnetic vacuum-mode expression — formal expression

`E_vac = (1/2) Σ_(k,λ) ħω_(k,λ).`

The ideal unbounded mode sum is formally divergent and requires a defined regularization/renormalization treatment. Absolute vacuum energy must not be treated as a directly measurable local fuel tank. Observable Casimir predictions concern changes under specified boundaries, material response and environmental conditions.

### 4.3 Ideal parallel-plate Casimir reference — idealized limit only

For ideal perfectly conducting parallel plates, area `A`, separation `a`, and zero temperature:

`U_C/A = -π² ħc/(720 a³)`

`F_C(a) = -dU_C/da = -π² ħc A/(240 a⁴).`

The sign convention takes increasing separation as positive; negative force is attractive. This equation is a reference limit, not a real-material production prediction.

### 4.4 Sphere–plane proximity-force approximation — initial design estimate only

For a sphere of radius `R` above a plane, with `a << R`, ideal materials and zero temperature:

`F_sp(a) ≈ -π³ ħc R/(360 a³).`

The corresponding idealized interaction energy is:

`U_sp(a) ≈ -π³ ħc R/(720 a²).`

The approximation is a screening/reference equation. Acceptance analysis must use a validated real-material model appropriate to measured dielectric response, coating thickness, finite conductivity, temperature, geometry, roughness and patch potentials. Do not freeze a gap or sphere radius by back-solving an ideal formula alone.

### 4.5 Real-material Lifshitz calculation — required for quantitative comparison

The real-material parallel-plate free energy per unit area is to be evaluated using a validated Lifshitz formulation with frequency-dependent material response and the declared temperature. A standard Matsubara representation is:

`F/A = (k_B T / 2π) Σ'_(n=0..∞) ∫_0^∞ k_perp dk_perp Σ_(p=TE,TM) ln[1 - r_1p r_2p exp(-2 q_n a)]`

where `ξ_n = 2π n k_B T/ħ`, `q_n = sqrt(k_perp² + ξ_n²/c²)`, and `r_1p,r_2p` are the polarization-dependent reflection coefficients for the two material interfaces. The prime denotes the conventional half-weight for the zero-frequency term. Force per area follows from `P = -∂(F/A)/∂a`. The sphere–plane force may then use a justified proximity approximation or a geometry-specific calculation with its validity and error stated.

A numerical implementation must be checked against published limits, convergence in Matsubara frequency and transverse wavevector, material-data provenance and independent reference cases.

### 4.6 Conservative closed-cycle work — derived

For a one-coordinate conservative force:

`W_cycle = ∮ F(a) da = 0`

when the system returns to the same separation and all relevant internal, material, thermal, electrical and stored states are restored. A one-way attractive stroke is not a complete engine cycle. Real actuator, reset, control and dissipation costs must be measured.

### 4.7 Force-gradient sensor model

For a calibrated cantilever sensor:

`m_s x¨ + c_s x˙ + k_s x = F_C(a) + F_parasitic(a,V,T,...) + F_drive(t).`

The undamped natural frequency is `f_0 = (1/2π)sqrt(k_s/m_s)`. For small oscillation amplitude and a conservative force gradient, the approximate frequency shift is:

`Δf ≈ -(f_0/(2 k_s)) (∂F/∂a).`

The exact dynamic-AFM estimator, finite-amplitude correction, transfer function and calibration method must be specified for the selected instrument. The force-gradient approximation is not to be applied outside its assumptions.

### 4.8 Electrostatic calibration and patch-potential control

A voltage sweep around the contact-potential compensation point is required to characterize electrostatic contributions and determine the effective potential offset. The chosen calibration model must include actual geometry, dielectric layers, wiring and patch-potential uncertainty. A fitted offset does not prove that all patch forces are removed.

### 4.9 Complete system energy identity — mandatory

For a declared control volume and interval:

`E_net = E_useful,out - Σ E_all,in + ΔE_stored`

where `ΔE_stored = E_stored,final - E_stored,initial`. Include actuator and reset work, pumps, thermal control, controller, data acquisition, shielding, cooling, standby and any other energy crossing the boundary. A fall in stored energy is not generation.

The time-domain estimator is:

`P_net_hat = (E_useful,out - Σ E_all,in + ΔE_stored)/T.`

For a proposed positive-net result, use a preregistered conservative lower confidence bound:

`P_LCB = P_net_hat - k u_c(P_net_hat).`

An initial `k=3` may be used as a proposed engineering gate only after the uncertainty model and coverage interpretation are approved. Require `P_LCB > 0`, repeated complete cycles, restored state variables, independent channels and independent replication. A positive point estimate alone is not a pass.

### 4.10 Measurement and uncertainty mathematics

For each channel, preserve calibration, resolution, bandwidth, drift, linearity, cross-sensitivity, timebase, phase/deskew and loading information. Combine uncertainty with covariance:

`u_c²(y) = J Σ Jᵀ`

where `J` is the sensitivity/Jacobian vector and `Σ` is the covariance matrix of input quantities. Include Type A repeatability and Type B calibration/specification contributions. Correlated channels and common timing errors must not be treated as independent by default.

### 4.11 SW-ZPE-01 reciprocal piezoelectric model — separate substream

The existing SW-ZPE-01 mathematical model is a classical reciprocal electromechanical transducer model. It is valuable for measuring driven piezoelectric behaviour and energy recovery, but it does not model extraction of vacuum energy.

For one mechanical modal coordinate and one differential PZT port:

`m x¨ + c x˙ + k_sc x - θv = F_ext`

`q = C0 v + θx`

`i_into = C0 v˙ + θ x˙ + Gp v.`

Stored energy:

`E = 1/2 m x˙² + 1/2 k_sc x² + 1/2 C0 v².`

Dissipation:

`P_diss = c x˙² + Gp v².`

Power identity:

`F_ext x˙ + v i_into = dE/dt + c x˙² + Gp v².`

Open-circuit stiffness and frequency:

`k_oc = k_sc + θ²/C0`

`f_sc = (1/2π)sqrt(k_sc/m)`

`f_oc = (1/2π)sqrt((k_sc + θ²/C0)/m).`

The same signed `θ` must appear in both reciprocal coupling paths. `k_sc` is short-circuit modal stiffness; do not add the coupling increment to an open-circuit stiffness a second time. Modal mass and stiffness must come from a consistent mode normalization/eigenpair, not silently substitute static tip stiffness.

Parameter status remains conditional: `C0` candidates 3.9844 nF / 4.10 nF / 15 nF conflict; `θ` candidate range 0.35–0.55 mN/V is provisional; exact PZT MPN, poling, electrode orientation, leakage, loss, damping and physical calibration remain open.

### 4.12 SW-ZPE-01 structural and electrical equations

For a stepped composite cantilever, preserve piecewise rigidity and the established coordinate convention. Static tip compliance:

`C_tip = ∫_0^L (L-s)²/[EI(s)] ds,   k_tip = 1/C_tip.`

For a mode shape `φ(s)` normalized to unit tip displacement:

`m_eff = ∫ ρAφ² ds + Σ M_j φ(s_j)² + attached distributed contributions.`

`k_eff = ∫ EI(s)[φ''(s)]² ds.`

A distributed load and point loads map to generalized force through the mode shape; base acceleration uses a modal participation factor and is not automatically equal to modal mass. Material, adhesive, clamp, sensor, leads and higher-mode contributions must be evaluated.

Electrical energy and power use simultaneous measurements:

`P_e(t)=v(t)i(t),   E_e=∫v(t)i(t)dt.`

Mechanical boundary power:

`P_m(t)=F(t)v_m(t),   E_m=∫F(t)v_m(t)dt.`

Capacitor and inductor storage:

`E_C=1/2 C V²,   E_L=1/2 L I².`

Accepted RF power at the declared reference plane:

`P_RF,accepted = P_incident - P_reflected.`

The 10 MHz RF subsystem is a separately measured input path; it is not the cantilever mechanical resonance and is not a vacuum-energy source.

## 5. Cross-library ownership and information map

The ZPE destination is cross-disciplinary. The following work areas must remain separately owned but linked by stable record IDs and revision-pinned interfaces.

### 5.1 Mathematics Library / Mathematics Lab

Responsibilities:
- quantum harmonic oscillator and field-mode definitions;
- Casimir energy/force and Lifshitz calculations;
- sphere–plane approximations and validity limits;
- coupled differential equations, modal reduction and FEM mapping;
- numerical integration, solver convergence and sensitivity;
- uncertainty propagation, covariance and statistical acceptance;
- energy-ledger identities and independent mathematical oracles.

Known source leads:
- `DINGOOS-MATH-MARRIAGE-001 Rev0.1`;
- `DINGOOS-MFR-001 Rev0.2`;
- `ZPE-01-ENC-0001 Rev0.2 / Rev0.3`;
- `ZPE-01-ENC-0002 Rev0.3 / Rev0.4`;
- `ZPE-04A-ENC-0002 Rev0.1`;
- `RESEARCH_AND_ENGINEERING_BLUEPRINT_v0.1.md`;
- `ZPE01_REFERENCE_TESTS.py`, `ZPE01_REFERENCE_RESULTS.json` and Rev0.3 derivatives;
- `sw_zpe_01_fem_aligned.py` and its pinned outputs.

Open mathematics conditions:
- The exact canonical Mathematics Lab charter/index and complete authoritative equation ownership map are not authenticated in this record.
- The recovered Physics Lab audit identifies unresolved equation-object links and a historical damped-oscillator time-grid defect. Preserve the failed historic artifact; any correction must be a new, separately reviewed run.
- Do not infer missing canonical equations from simulation code.
- Protected BIF axioms, notation, action, field equations and frequency-selection law remain outside this public-safe record and must not be reconstructed or exposed.

### 5.2 Physics Library / Physics Lab

Responsibilities:
- establish the physical interpretation and assumptions of each model;
- distinguish established quantum theory, idealized limits, derived results and hypotheses;
- select measurable quantities and controls;
- identify conventional electromagnetic, electrostatic, thermal, mechanical and environmental confounders;
- define experiment protocol, calibration and independent replication.

Known source leads:
- `PHYSICS-LAB-REFERENCE-AUDIT-001 Rev0.2`, branch `research/physics-lab-audit`;
- independent physics reference PoC, branch `research/independent-physics-reference-poc`;
- the Casimir and dynamic-Casimir literature listed in Section 8.

Open Physics Lab conditions:
- The inspected audit did not locate a dedicated authenticated Physics Lab charter/index, full apparatus register, calibration-certificate set, raw physical-measurement dataset or independent physical replication record.
- The damped-oscillator historical example has a time-grid mismatch: endpoint-inclusive sampling used `T/(N-1)` but integrated `N` steps, so state and stored-energy outputs refer to different terminal times. Preserve the failed historical artifact and use a separately identified correction.
- A numerical simulation or energy residual does not establish physical validity.

### 5.3 Engineering Library / Engineering Lab

Responsibilities:
- system requirements, architecture, trade studies and design decisions;
- test-cell, fixture, actuator, sensor, vacuum and thermal engineering;
- electrical isolation, low-voltage control, interlocks and fail-safe states;
- calibration, metrology, energy accounting and safety case;
- CAD, drawings, BOM, manufacturing process and release gates.

Known source leads:
- `SW-ZPE-01 Complete POC Engineering Blueprint Rev2.1`;
- `SW-ZPE-01 Rev2.3 Engineering Reconciliation & Reference Report`;
- `SW-ZPE-01-PHY-DES-001 Rev0.1`;
- `ZPE-01-ENC-0001 Rev0.3`;
- `ZPE-05-DEV-AUDIT-0001 Rev0.4`.

SW-ZPE-01 remains a separate classical RF/PZT electromechanical testbed with 01A RF/DC, 01B transducer and 01C recovery branches. It is not the ZRI-01A Casimir test cell and must not be represented as a ZPE generator. Reuse its proven methods for synchronized measurements, energy ledgers, uncertainty and test discipline only where interfaces are justified.

### 5.4 Technology Library / Technology Lab

Responsibilities:
- advanced sensor and actuator technologies;
- AFM/MEMS, interferometric displacement sensing and low-noise acquisition;
- vacuum-compatible materials, coatings and surface preparation;
- dynamic-Casimir microwave/circuit-QED alternatives;
- data acquisition, immutable evidence storage, automation and secure interfaces;
- technology readiness, supplier capability and manufacturing route.

Known source lead:
- `TECHNOLOGY-LAB-RECOVERY-AND-INTEGRATION-001 Rev0.1`, branch `research/technology-lab-recovery`.

Open Technology Lab conditions:
- Dedicated canonical Technology Lab charter, index, ownership map, full programme register and integrated implementation source were not authenticated in the inspected surfaces. The recovered integration proposal remains a proposal.
- Do not treat proposed lab layers or repositories as canonical implementation.
- Each technology choice requires supplier/source provenance, physical limits, compatibility, uncertainty and test evidence.

### 5.5 Shared programme and security records

- `DINGOOS ZPE — Continuous-Energy Research & Engineering Blueprint v0.1` is the programme-level source lead.
- The 146-record SW-ZPE-01 index and 125-file Library collection are discovery/reconciliation inventories, not proof that every record is source-authenticated or verified.
- Protected BIF/IP and private DingoOS source remain protected. Public Side-bet records may contain only authorized public-safe derived material.
- Preserve originals byte-for-byte; new interpretations and derivatives receive new IDs and revisions.
- A hash proves byte identity against a known digest, not authorship, authority or scientific correctness.

## 6. SW-ZPE-01 current engineering disposition

The existing design remains useful and should continue as a parallel substream.

### 6.1 Recovered baseline

- Rev2.1 engineering blueprint: substantive POC working manual, not released manufacturing drawings.
- Rev2.3 reconciliation: refined mechanical coordinate convention, M100/M156 modal branches and P1–P6 evidence gates.
- ZPE-01 reciprocal model Rev0.3: equations and energy identity reviewed; ODE reference reproduced/extended; physical parameters remain unauthenticated; SPICE drafts unexecuted.
- SW-ZPE-01-PHY-DES-001 Rev0.1: coordinated candidate physical prototype definition, not released for fabrication.
- ZPE-05 Rev0.5 candidate: synthetic software regression has been exercised, but simulator/parser and engineering qualification remain open.

### 6.2 Non-negotiable open items

- Controlled `TEST-001 Rev1.0` and `ZPE-05-VER-0001 Rev0.1` remain unretrieved in the cited audit.
- Production topology authority root/signer and physical Rev01I pin/current/trace mapping are not authenticated.
- Native LTspice/ngspice RAW parsing and actual simulator execution have not been demonstrated.
- The ODE reference is not a SPICE run or a physical measurement.
- Exact PZT MPN, poling, electrode map, C0, signed θ, damping, dielectric loss, adhesive and clamp properties require evidence.
- RF matching, component ratings, pin-level schematic, PCB, CAD, instrumentation and full energy ledger remain subject to their design holds.
- The ZPE-05 audit's 161/161 result is a synthetic software-regression result, not simulator or hardware qualification. The separate Rev0.4 reproduction recorded 56/56 under a low-startup wrapper, with default-environment timeout sensitivity.

## 7. Design requirements and acceptance gates for ZRI-01A

### Gate ZRI-G0 — requirements and metrology feasibility

Required:
- select candidate geometry and measurement mode;
- define target separation/force-gradient range from instrument capability;
- obtain sensor stiffness, resonance, Q, bandwidth and noise data;
- define surface material, coating, roughness and characterization method;
- define gap calibration and contact-potential method;
- freeze control-volume and all energy interfaces;
- complete initial hazard analysis and independent review.

Pass condition: requirements, measurands, uncertainty targets and a credible instrument route are reviewed. No fabrication release yet.

### Gate ZRI-G1 — reference interaction

Required:
- calibrated gap sweep;
- force/force-gradient measurement;
- electrostatic bias sweep and patch-potential controls;
- surface and environmental records;
- comparison with an appropriate real-material Lifshitz model;
- blinded sham and reference runs;
- raw-data and analysis reproducibility.

Pass condition: reproduce a known reference force/gradient curve within a pre-registered uncertainty budget and disclose residual discrepancies.

### Gate ZRI-G2 — complete-cycle energy audit

Required:
- complete approach, hold, separation and reset cycles;
- all actuator, pump, thermal, controller, DAQ and standby inputs measured;
- useful output independently measured;
- initial/final stored states reconciled;
- repeated randomized sham/reference/normal runs;
- uncertainty and covariance propagation.

Expected baseline: no positive net energy from a closed conservative Casimir cycle after reset and losses. An apparent anomaly is not accepted as ZPE extraction.

### Gate ZRI-G3 — anomalous-result challenge

If a positive residual appears:
- stop generator/product claims;
- investigate calibration drift, electrostatic patches, contact potential, RF pickup, vibration, thermal gradients, clock/phase errors, hidden power paths, chemical changes, pressure changes and stored-energy depletion;
- repeat with independent sensors and a separately assembled apparatus;
- preserve null and failed trials.

### Gate ZRI-G4 — independent replication

Required:
- preregistered protocol and analysis;
- independent laboratory and instrument chain;
- raw data and full uncertainty budget;
- complete energy balance and state restoration;
- repeatable positive lower confidence bound.

Only a successful independent result may justify a separate generator-conversion design programme.

### Gate ZRI-G5 — product engineering

Only after G4:
- generator architecture and conversion;
- FMEA, reliability, thermal, EMC and environmental qualification;
- manufacturing package, regulatory analysis and certification;
- separate household and vehicle integration review.

ZHEP remains a conventional energy platform until then.

## 8. External technical source register

The following references support the scientific and engineering basis; they do not prove a ZPE generator.

1. Klimchitskaya, Mohideen and Mostepanenko, “The Casimir force between real materials: Experiment and theory,” *Reviews of Modern Physics* 81, 1827 (2009), DOI: https://doi.org/10.1103/RevModPhys.81.1827 — real-material Lifshitz theory and experiment/theory comparison.
2. Elsaka et al., “Casimir Effect in MEMS: Materials, Geometries, and Metrologies—A Review,” *Materials* 17(14), 3393 (2024), DOI: https://doi.org/10.3390/ma17143393 — materials, geometries, metrology, MEMS/NEMS and corrections.
3. Dhital and Mohideen, “A Brief Review of Some Recent Precision Casimir Force Measurements,” *Physics* 6(2), 891–904 (2024), DOI: https://doi.org/10.3390/physics6020055 — precision sphere–plane and other force measurements.
4. Dodonov, “Dynamical Casimir Effect: 55 Years Later,” *Physics* 7(2), 10 (2025), DOI: https://doi.org/10.3390/physics7020010 — dynamic boundary, resonator and photon-generation research.
5. Juárez Aubry and Weder, “A short review of the Casimir effect with emphasis on dynamical boundary conditions,” DOI: https://doi.org/10.31349/SuplRevMexFis.3.020714 — static and dynamic boundary-condition background.
6. NIST Technical Note 1297, https://www.nist.gov/pml/nist-technical-note-1297 — measurement uncertainty framework.
7. Spicelib RAW reader documentation, https://spicelib.readthedocs.io/en/stable/classes/raw_read.html — candidate waveform parser documentation; actual native fixture qualification remains required.
8. ngspice batch-mode documentation, https://nmg.gitlab.io/ngspice-manual/analysesandoutputcontrol_batchmode.html — simulator execution and raw-output method; exact target-version execution remains required.
9. Energy Safe Victoria battery-system guidance, https://www.energysafe.vic.gov.au/industry-guidance/electrical/electrical-technical-information/battery-energy-storage-systems — licensed installation and local safety context for any later conventional ZHEP deployment.
10. Standards Australia, AS/NZS 4777 updates, https://www.standards.org.au/blog/as-nzs-4777-updates — inverter energy-system standards context; current editions and applicability must be checked at design freeze.

## 9. Required source and evidence register fields

Every linked source or result must carry:

- stable record ID, title, revision, date and status;
- owning library/lab and accountable authority;
- original/derived/proposed classification;
- source location, branch, commit SHA or Library identity;
- SHA-256 where a file is available;
- parent and superseding record links;
- equations, symbols, SI units, assumptions and domains;
- data/model/software version and execution environment;
- calibration and instrument metadata;
- verification method, raw evidence and reproducibility instructions;
- uncertainty, limitations, contradictions and unresolved findings;
- release/acceptance gate and decision authority.

Missing records remain `UNRETRIEVED`, `NOT LOCATED IN INSPECTED SURFACES` or `NOT AUTHENTICATED` as appropriate. Do not silently replace them with summaries or reconstructed source.

## 10. Immediate development sequence

1. Reconcile the complete ZPE Library inventory, including the 146-record SW-ZPE-01 index and the 125-file collection, into a source-to-design crosswalk. Preserve all originals.
2. Recover and inspect the complete `RESEARCH_AND_ENGINEERING_BLUEPRINT_v0.1` source/model bundle, including the cited `src/zpe_model.py`, before treating the simulation as executed evidence.
3. Build the ZRI-01A requirements and instrument trade study; compare AFM force-gradient and direct-force modes.
4. Establish the sphere–plane real-material mathematical model, numerical reference cases and uncertainty propagation.
5. Create a metrology chain, test protocol, calibration register and raw-data schema.
6. Keep SW-ZPE-01 parameter authentication, simulator execution, native RAW parsing and physical qualification moving independently.
7. Reconcile the Mathematics, Physics, Engineering and Technology Lab authority/index gaps before declaring cross-library completeness.
8. Complete security/IP review before public integration of any further material.

## 11. Disposition

**Primary design destination:** ZRI-01A sphere–plane Casimir Research Instrument.

**Design status:** selected as the first research-instrument candidate; architecture and verification path defined at programme-reference level; detailed instrument selection, dimensions, procurement and fabrication remain open.

**Generator status:** no viable net-positive ZPE generator has been demonstrated or accepted. The design programme is required to investigate this question rigorously, not assume its answer.

**SW-ZPE-01 status:** retained as a separate classical RF/piezoelectric transducer and recovery testbed. Its equations and measurement methods inform the programme where appropriate but do not establish vacuum-energy extraction.

**Library completeness:** cross-library navigation map established; canonical Mathematics, Physics and Technology Lab authorities and several original verification sources remain unresolved. This document is not a declaration that all sources have been recovered.

## 12. Change history

- **Rev0.1 — 27 November 2026:** establishes the first ZPE design destination, three-candidate research architecture, mathematical reference register, cross-library ownership map, SW-ZPE-01 separation, acceptance gates and source/evidence requirements. Derived from recovered Library records and public-safe Side-bet research records. No original source modified; no fabrication, simulator execution or physical validation claimed.
