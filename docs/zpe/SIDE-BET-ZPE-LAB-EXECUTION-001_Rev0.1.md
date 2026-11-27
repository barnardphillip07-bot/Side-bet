# SIDE-BET ZPE LAB EXECUTION AND INTEGRATION PLAN — Rev 0.1

- **Document ID:** SB-ZPE-LAB-EXEC-001
- **Revision:** 0.1
- **Date:** 2026-11-27
- **Status:** CONTROLLED DERIVED EXECUTION PLAN — PROPOSED / NOT A CANONICAL DINGOOS SPECIFICATION
- **Repository:** `barnardphillip07-bot/Side-bet`
- **Branch:** `zpe/side-bet-lab-integration-001`
- **Parent:** `zpe/sw-zpe-01-consolidation-001`
- **Purpose:** Coordinate the user's Mathematics, Physics, Engineering and Technology laboratory capabilities to advance the Side-bet ZPE programme through independently testable, provenance-preserving work.

## 1. Governing direction

Side-bet is the active project workspace and ZPE is the engineering/research focus. The laboratories are working capabilities that contribute to the project; they are not independent projects whose outputs are disconnected from one another.

Work is to proceed in parallel where dependencies permit. Results flow into the Side-bet ZPE programme only with their source identity, assumptions, conditions, evidence class, uncertainty and limitations intact.

The governing discipline is:

> Recover what existed, establish what is true, derive what follows, and only then claim what is new.

Objective innovation applies throughout: failed, null, contradictory, superseded and numerically unstable outcomes are retained with their exact conditions and failure analysis. Reuse of a failed result's data or method does not change the original result's disposition.

## 2. Scope and boundaries

This plan coordinates the ZPE-focused Side-bet work visible in the currently connected repository and the recovered SW-ZPE-01 source index. It does not assert that the connected public repository contains the complete private/canonical DingoOS or ZPE source universe.

The ZPE focus is broader than the SW-ZPE-01 piezoelectric prototype. It includes the distinct ZPE research streams and historical wireless-transfer / household / vehicle engineering work where recovered source records establish those connections. The current accessible ZPE branch is heavily weighted toward SW-ZPE-01 and ZPE-05; coverage of the remaining programme must be recovered rather than inferred.

### 2.1 Domain firewall

- Quantum-field theory and quantum-vacuum claims require their own recovered mathematical foundations, physical mechanism, discriminating predictions and evidence.
- Classical RF, rectification, piezoelectric transduction, resonance, SECE/SSHI and wireless power transfer remain classical engineering domains unless an independently justified and experimentally supported connection is established.
- A classical prototype, simulation, energy-recovery circuit or wireless-transfer demonstration is not evidence of quantum-vacuum extraction.
- DNG-RES-006 remains a separate diagnostic identifier. It is not QFIE-006 and is not to be merged with it absent authenticated source lineage.
- Protected BIF/IP sources remain private and excluded from this public-safe repository plan. No protected material is reproduced or reconstructed here.

## 3. Laboratory responsibilities and project interfaces

| Laboratory | Primary responsibility | Required outputs into Side-bet ZPE | Does not independently establish |
|---|---|---|---|
| Mathematics Lab | Recover and independently derive governing mathematics; dimensional/type checks; analytical solutions; state-space and energy identities; numerical analysis | Equation/source lineage, derivation records, benchmark vectors, uncertainty/sensitivity analysis, unresolved discrepancies | Physical validity or experimental truth |
| Physics Lab | Test physical assumptions, mechanisms, boundary conditions, conservation, predictions, observability and measurement validity | Physical-domain reviews, independent predictions, benchmark comparisons, measurement plans, calibrated data and uncertainty, contradictions | Device qualification merely from equation consistency |
| Engineering Lab | Implement and reproduce models, testbenches, simulators, parsers, instruments, prototype assemblies and energy ledgers | Versioned code/netlists, execution logs, raw outputs, test reports, integration and failure records | New physical law or field-extraction claim from successful implementation |
| Technology Lab | Evaluate technology alternatives, materials, components, architectures, manufacturability, reliability and integration | Requirements-linked alternatives, BOM/MPN evidence, design revisions, prototype performance envelopes, lifecycle and integration assessments | New physics merely because a technology works |

Shared tools and datasets may be reused. Each laboratory retains its own method, acceptance criteria and decision authority. Existing DingoOS requirements, execution, challenge, evidence, qualification and knowledge authorities must be recovered and reused where applicable; this plan does not create a competing evidence registry or workflow authority.

## 4. Recovered baseline and evidence state

The following are repository findings, not claims that the full ZPE programme is complete.

| Source / asset | Recovered state | Consequence |
|---|---|---|
| `SW-ZPE-01-CONSOLIDATION-AND-LINEAGE-001 Rev0.1` | 146 unique source-register rows; derived metadata index | Source identity map exists; most Library items still require byte-level verification and content audit |
| `SW-ZPE-01-MATHEMATICAL-REVERSE-ENGINEERING-001 Rev0.1` | Independent ODE/FEM numerical reproduction reported; parameter authentication open | Use as a derived verification record, not as replacement for original source |
| `SW-ZPE-01-PARAMETER-SENSITIVITY-001 Rev0.1` | Candidate sweep over C0 and coupling coefficient | Demonstrates sensitivity only; selects no physical parameter |
| `ZPE-05-REV04-REPRODUCTION-001 Rev0.1` | ZIP integrity 12/12; synthetic tests 55/56 in default environment and 56/56 with low-startup wrapper | Software regression only; simulator/parser and physical qualification remain open |
| `PHYSICS-LAB-REFERENCE-AUDIT-001 Rev0.2` | Partial source recovery; numerical time-grid defect identified; equation links unresolved | Physics Lab is not fully audited; physical apparatus and measurement chain remain unretrieved in inspected surfaces |
| `TECHNOLOGY-LAB-RECOVERY-AND-INTEGRATION-001 Rev0.1` | Partial recovery; canonical charter/index not authenticated | Technology Lab remains a distinct workstream; capability map and exact ownership remain incomplete |
| `DINGOOS-TECHNOLOGY-LAB-OBJECTIVE-INNOVATION-PRINCIPLES-001 Rev0.1` | Proposed operating principles record | Apply its falsifiability, traceability and evidence-led selection principles; reconcile with canonical authorities |

### 4.1 Important unresolved mathematical and physical inputs

- `DNG-MECH-OSC-001` and the four spatial PDE equation references are unresolved or access-restricted in the inspected Knowledge Snowflake stores. They must be recovered from source or remain unresolved; do not synthesize substitute canonical equations.
- PZT identity, lot, electrode/poling configuration, C0, dielectric loss/leakage, coupling coefficient theta and sign, damping, bondline, adhesive and as-built geometry require authentication or measurement.
- The M100 frequency discrepancy (reported 166.434 Hz versus 166.414 Hz from rounded ODE inputs) must be traced to unrounded inputs and modal-mass conventions.
- Historical C0 values 3.9844 nF, 4.10 nF and 15 nF are conflicting candidates, not interchangeable measurements.
- Physical measurement data, instrument inventory, calibration certificates, raw acquisition chain and uncertainty budgets were not located in the inspected Physics Lab surfaces.
- The controlled `TEST-001 Rev1.0`, `ZPE-05-VER-0001 Rev0.1`, original ZPE-01 Rev0.4 testbench and runner bytes remain recovery priorities.

## 5. Parallel execution work packages

### WP-0 — Source recovery, identity and preservation (all labs; blocking)
1. Reconcile the 146-row SW-ZPE-01 source register against original Library bytes, hashes, revisions and duplicate locators.
2. Recover and authenticate the controlled test specifications, original testbench and runner, simulator fixtures and source equation records.
3. Continue full-source coverage beyond the inspected archives and connected public repository; record every inaccessible or uninspected surface.
4. Keep originals immutable. Any correction, reconstruction or new run receives a new identity and explicit parent/source links.
5. Recover the broader ZPE and historical wireless-transfer workstream inventory; do not treat SW-ZPE-01 as the entire ZPE programme.

**Exit:** source coverage and missing-source boundaries are explicit; critical originals are authenticated or remain visibly UNRETRIEVED.

### WP-1 — Mathematical foundations and independent derivation (Mathematics Lab)
1. Recover equation definitions and derivation lineage before reproducing them.
2. Independently derive the SW-ZPE-01 reciprocal electromechanical model and signed port convention from the authenticated source.
3. Re-derive the complete energy identity and storage/dissipation terms; retain the known T2.2 double-counting defect and T2.3 correction lineage.
4. Reconcile modal mass, stiffness, frequency, geometry and coordinate definitions, including unrounded input values.
5. Correct the oscillator fixed-endpoint convergence test in a new run while preserving the original failed artifact.
6. Resolve the 1-D spatial benchmark equations and boundary conditions from their exact source records before mesh/time convergence work.
7. Keep QFT/ZPE-01 mathematics as a separate derivation branch; no classical electromechanical equations are substituted for quantum-field foundations.

**Exit:** derivations are independently reproducible, assumptions and units are explicit, source lineage is pinned, and unresolved equation identities remain unresolved.

### WP-2 — Physical mechanisms and metrology (Physics Lab)
1. Recover the Physics Lab charter, experiment register, apparatus/instrument register, calibration chain, raw data and review history.
2. For each ZPE research stream, state the physical system, boundary conditions, mechanism, observable, competing conventional explanation and discriminating prediction.
3. Review the SW-ZPE-01 physical model independently: clamp/bond assumptions, PZT constitutive parameters, mode shape, losses, parasitics, temperature and environmental sensitivity.
4. Define traceable measurement chains and uncertainty budgets for force, displacement/velocity, voltage/current, RF forward/reflected power, temperature and timebase.
5. Preregister controls, sample plan, stopping criteria, safety limits and failure conditions before physical testing.
6. Preserve null, contradictory and failed outcomes with raw data and complete conditions.

**Exit:** physical predictions and measurement procedures are independently reviewable; measurement uncertainty is fit for the intended discrimination; no quantum claim is made without quantum-specific evidence.

### WP-3 — Simulation, testbench and reproducibility (Engineering Lab)
1. Repair the oscillator time-grid defect in a separately reviewed patch; verify final state and energy timestamps agree and convergence compares identical terminal times.
2. Recover original ZPE-01 Rev0.4 testbench and runner bytes; implement the nine audit corrections in a new revision without overwriting historical source.
3. Execute LTspice/ngspice with pinned versions and retain commands, netlists, logs, RAW waveforms, exports, environment and hashes.
4. Qualify native RAW parsing against simulator-produced fixtures, not only synthetic parser objects.
5. Verify energy-ledger signs, storage deltas, boundary terms, parasitic elements and residual uncertainty.
6. Separate electrical excitation surrogates from fully coupled electromechanical models.
7. Maintain reproducible regression suites and record environment-sensitive failures rather than relaxing limits without justification.

**Exit:** source, simulator, parser, numerical and ledger evidence each have separate qualification status; no static audit or synthetic regression is called simulator or hardware validation.

### WP-4 — Technology and prototype engineering (Technology Lab)
1. Freeze measurable requirements and compare materially different candidate architectures at comparable fidelity.
2. Close exact PZT, adhesive, beam, clamp, tip-mass, RF, rectifier, driver, recovery and instrumentation part identities against datasheets and measured operating envelopes.
3. Resolve the RF input and accepted-power boundary; characterize nonlinear rectifier loading rather than treating the ideal L-match as final.
4. Complete the physical assembly, safety, thermal and electrical interface definitions only after mathematical and physical inputs are closed.
5. Build a modular prototype only after design holds are cleared; do not authorize procurement/fabrication from candidate values alone.
6. Compare conventional baseline, passive recovery and active recovery variants with matched measurement boundaries.
7. Evaluate historical household/vehicle wireless-transfer concepts as a distinct technology stream with their own safety, coupling, efficiency, interoperability and installation requirements.

**Exit:** requirements-linked design is buildable, safe and traceable; measured performance and reliability are qualified only within the demonstrated envelope.

### WP-5 — ZPE-specific physical research and cross-stream synthesis
1. Recover the original ZPE-01/QFIE/QIT source definitions, equations, textbook references and revision lineage.
2. Maintain the distinct 12-stream ZPE research architecture only to the extent supported by recovered authoritative records; reconcile exact names and ownership before canonising it.
3. For each stream, map source equations, physical mechanism, observables, conventional baselines, numerical tools, experiments, uncertainty and unresolved hypotheses.
4. Transfer methods, calibration data, error signatures and negative results only through explicit source-to-recipient links.
5. Require recipient-stream validation; source conclusions never transfer automatically.
6. Keep QFIE-006 and DNG-RES-006 strictly distinct pending authenticated evidence of any relationship.

**Exit:** each stream has an independently testable research dossier; cross-stream connections are explicit, justified and falsifiable.

## 6. Energy and evidence rules

For every experiment, declare the system boundary before calculating efficiency or net energy.

For the electrical/mechanical boundary, retain signed power:
`p_e(t)=v(t)i(t)`, `p_m(t)=F(t)u(t)`.

For stored energy, use final-minus-initial changes, including all relevant capacitors, inductors, mechanical modes and thermal stores. Internal recovery is not a new external energy source. Driver-supplied energy must remain counted as external input even if it is later recovered. Do not count stored energy and delivered load energy twice. Report unexplained residuals and uncertainty rather than assigning them to a preferred mechanism.

Every result must identify:
- source record and immutable revision;
- stream/lab and work package;
- claim class (measured, derived, simulated, inferred, proposed);
- raw-data and code/model hashes;
- exact initial/boundary/environment/instrument/solver conditions;
- calibration, corrections, uncertainty and covariance assumptions;
- acceptance criteria and actual disposition;
- failure mode, limitations and unresolved causes;
- related, contradicting, superseding and recipient records.

Use the existing DingoOS evidence/provenance authorities once their ownership and interfaces are recovered. This document does not establish a new registry or alter the 10-tier retention vocabulary.

## 7. Release gates

| Gate | Requirement | Release effect |
|---|---|---|
| G0 — Source integrity | Critical originals recovered or explicitly bounded as missing; protected IP boundary enforced | No derived claim presented as original |
| G1 — Mathematical closure | Equations, units, assumptions, boundary conditions and derivations independently checked | No physical prediction promoted from unresolved mathematics |
| G2 — Numerical verification | Code/solver correctness, fixed-endpoint convergence, benchmark and sensitivity evidence | No simulation claim beyond verified numerical scope |
| G3 — Physical validation | Discriminating measurements, traceability, uncertainty, controls and repeatability | No physical-mechanism claim without adequate evidence |
| G4 — Engineering qualification | Requirements, safety, components, prototype and lifecycle evidence | No fabrication/release or performance qualification before closure |
| G5 — ZPE claim review | Quantum-field-specific theory, predicted observable, exclusion of conventional inputs and independent replication | No vacuum-extraction claim from classical RF/piezoelectric or wireless-transfer results |

A candidate can be returned to an earlier gate, retained for research, rejected or placed on hold. Passing one gate does not automatically pass the next.

## 8. Immediate priority order

1. **P0:** Recover and authenticate `TEST-001 Rev1.0`, `ZPE-05-VER-0001 Rev0.1`, original ZPE-01 Rev0.4 testbench and runner; reconcile the 146-row source index against source bytes.
2. **P0:** Recover the original ZPE/QFIE/QIT mathematical sources and broader ZPE/historical wireless-transfer programme inventory.
3. **P1:** Mathematics Lab closes equation lineage, oscillator endpoint correction and reciprocal energy identity.
4. **P1:** Physics Lab recovers physical measurement chain and defines discriminating predictions/uncertainty.
5. **P1:** Engineering Lab qualifies simulator execution and RAW parser with native fixtures.
6. **P2:** Technology Lab closes component identities, design holds and comparative prototype plan.
7. **P3:** Integrate only qualified outputs into the wider ZPE stream map and household/vehicle technology work.

## 9. Explicit non-claims

At this revision:
- No quantum-vacuum energy extraction is demonstrated.
- No physical prototype measurement or net-positive/autonomous energy result is established.
- LTspice/ngspice execution and native RAW parser qualification are not established by the recovered records.
- The Physics Lab and Technology Lab canonical charters and complete inventories are not authenticated.
- The 146-row source register is a derived metadata index; it is not proof that all 146 underlying files have been rehashed or content-audited.
- No manufacturing release is authorized.
- No protected BIF/IP source is included, altered or reconstructed.
- This plan is a derived public-safe coordination artifact, not a canonical DingoOS or QFIE specification.

## 10. Change history

- **Rev 0.1 — 2026-11-27:** Established a Side-bet ZPE-focused cross-laboratory execution plan from the accessible ZPE consolidation, Physics Lab audit, Technology Lab recovery, objective-innovation principles and independent physics-reference PoC. Added parallel work packages, domain firewalls, evidence gates and immediate recovery priorities. No original project source was modified; no physical experiment, simulator run or hardware qualification is claimed.
