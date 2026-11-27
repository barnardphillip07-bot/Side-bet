# DINGOOS-HYB-COMP-001 — Comparative Architecture Acceptance Plan

- Revision: Rev0.1
- Date: 27 November 2026
- Workspace: `barnardphillip07-bot/Side-bet`
- Branch: `dingoos/recovery-engine-adopted-requirements`
- Status: **ACTIVE COMPARISON WORK PACKAGE — WORKLOAD NOT YET FROZEN — NO ARCHITECTURE SELECTED**
- Purpose: Continue the previously agreed measurable comparison of centralized modular, federated and local-first hybrid DingoOS architectures.

## 1. Continuity and authority

This work continues the prior Side-bet DingoOS engineering direction. It does not restart architecture design, select a winner, or adopt `DINGOOS-HYB-ARCH-002 Rev0.2` as canonical.

Recovered prior direction:
- `DINGOOS-HYB-ARCH-002 Rev0.2` identifies local-first modular DingoOS with a hybrid logical architecture as the preferred hypothesis.
- Centralized modular architecture remains the reference baseline and fallback.
- Federation is deferred until measured requirements justify it.
- The current POC direction is one local deployable with strict module, authority, data and trust boundaries; later extraction of specialist domains is conditional on measured need.
- `DINGOOS-HYB-FAULT-001` defines five hard gates A–E and maps existing FT scenarios to them.
- Its numerical performance thresholds are explicitly undefined and must be set by project owners after baseline measurements. No thresholds are invented here.

The user's subsequent workspace directive makes Side-bet the primary DingoOS engineering and construction workspace. This supersedes the older HYB-ARCH-002 §4.5 restriction that DingoOS-specific architecture should remain outside Side-bet. Protected BIF/IP, credentials and private original source remain protected; workspace scope is not permission to publish confidential material.

## 2. Three architectures under comparison

All three variants must implement the same logical workflow, requirements and fault scenarios at comparable fidelity.

### A — Centralized modular baseline/fallback

- One central deployable and common coordination/persistence boundary.
- Domain functions remain separated as modules with explicit interfaces.
- Central scheduler/governance controls workflow progression.
- Baseline for measuring simplicity, integration cost and central bottleneck/single-failure exposure.

### B — Federated architecture

- Autonomous domain nodes own local execution and domain state.
- Nodes exchange versioned, provenance-linked messages asynchronously.
- Common identity, policy and evidence semantics remain shared; no domain may invent global authority.
- Reconciliation handles duplicate, conflicting, stale and disconnected work.
- Federation is an experimental candidate, not the assumed destination.

### C — Local-first hybrid hypothesis

- One local deployable initially, with strict logical module, authority, data and trust boundaries.
- Local analytical loops avoid synchronous coordinator calls for every internal computation.
- Specialist domains can later be selectively extracted when measurements justify distribution.
- Shared project identity, requirements lineage, provenance and governance semantics remain coherent.
- Disconnection permits bounded local research but not consequential actions requiring current global authority.

The local-first hybrid is the prior preferred hypothesis, not a measured winner or approved canonical architecture. The comparison must be capable of falsifying it.

## 3. Common frozen workload — selection still open

No exact workload was frozen in the recovered prior decision. The fault-model record gives an illustrative toy engineering workflow requiring two distinct solution approaches, α generation, β verification and a decision gate; it does not identify a selected problem, exact inputs or an accepted workload SHA.

A concrete source-derived candidate has now been identified:

**WLC-001 — CSRE1/CSRE2 resonance analysis and verification vertical slice**

Source artifact: `Pasted text(7).txt`, 133,685 bytes, 2,778 lines, whole-file SHA-256:

`548a7a5595bd5d81863fbc8815e45e0b0423c51712883b585135cfea3d369752`

Relevant byte-accurate source regions:

| Component | Lines | Byte range | Region SHA-256 |
|---|---:|---:|---|
| C3PO proposer / C4PO verifier | 98–123 | `[9456:11166]` | `ba4d793d8dcbe48d49013a6ff6d7823843c9a42d9f7bd18dbe5b4ec6cd66cdae` |
| DigitalTwin transient simulation | 135–166 | `[12090:13403]` | `1cb95d3cbb612aa5c31b94588e8accaf84511be427ec44235212e3cebad77556` |
| SensorHardwareGateway | 167–195 | `[13403:14517]` | `086b4eb8a84a38adcb4c7367689e58976350e54836e03711dc37c76602205317` |
| Main orchestration excerpt | 1659–1685 | `[92743:93802]` | `35aa9263150b129cef76d1a9d5c5cb30aa82404d67ef45900bdc24fb1bb96ad3` |

Historical workload parameters visible in the compilation:
- mass (m = 5.0\,kg);
- stiffness (k = 500\,N/m);
- DigitalTwin default damping (c = 0.05);
- simulation duration (2.0\,s);
- time step (0.001\,s);
- initial displacement (1.0\,m);
- initial velocity (0);
- main orchestration's simulated measurement (1.59155\,Hz);
- C4PO default comparison tolerance (0.05\,Hz).

The undamped analytical reference is:

[
f_n = \frac{1}{2\pi}\sqrt{\frac{k}{m}}
= 1.5915494309\,Hz
]

This source-derived workload is a **candidate only**. It is not yet frozen or approved.

### 3.1 Important source limitations before freezing WLC-001

- The main orchestration excerpt hardcodes the simulated measurement; it does not call the separate DigitalTwin implementation. Connecting the analytic and numerical paths would require a derived benchmark harness.
- The C3PO/C4PO IDs use wall-clock-derived values, and the sensor gateway uses random Gaussian noise without a recorded seed. A reproducible harness would need fixed identity/time inputs and a declared RNG seed; it must not silently alter the recovered source.
- The C4PO fragment sets an epistemic status to `VALIDATED` when a simulated value falls within tolerance. Simulation agreement is not physical validation. The benchmark must keep analytical agreement, simulation, measurement and physical validation distinct.
- The compilation is mixed prose/source with conflicting gateway variants. It is a historical source-bearing compilation, not an authenticated canonical source tree or a verified executable.
- No target-side consequential operation or production γ authority is established by this workload.

If WLC-001 is selected, the comparison harness must explicitly version its derived composition, fixed inputs, seeds, IDs, environment, oracle and source attribution. The original source compilation remains byte-preserved.

## 4. Frozen-workload contract required before execution

Before any architecture is benchmarked, freeze and hash:
1. Problem statement and intended engineering outcome.
2. Exact input data and source revisions.
3. Candidate solution methods and expected outputs/oracle.
4. α candidate-generation inputs, agent/tool/model identities and versions.
5. β verification method, independence boundary, inputs and access restrictions.
6. γ policy/authority test fixture and explicit limits of any simulated authority.
7. Σ synthesis inputs and projection rules.
8. Resource envelope and execution environment.
9. Concurrency/load schedule and fault-injection schedule.
10. Determinism controls: clock, IDs, random seeds, ordering and retry inputs.
11. Measurement definitions and evidence capture.
12. Pre-registered repetition count and stopping rule.

No architecture may receive an easier workload, fewer faults or looser acceptance criteria than another.

## 5. Measurement protocol

Record raw observations and exact run provenance for every architecture. At minimum:

| Metric | Measurement definition |
|---|---|
| End-to-end latency | Time from accepted workflow request to terminal workflow outcome; report distribution, not only mean |
| Throughput | Completed valid workflows divided by measured wall-clock interval |
| Recovery time | Time from injected fault to restored consistent, usable state |
| Event loss | Count of committed events absent after recovery |
| Duplicate delivery/effect | Count of duplicate event acceptances and duplicate consequential effects, reported separately |
| Verification backlog | Pending β assessments and age of oldest pending assessment |
| Resource use | CPU time, peak memory, persistent bytes and network bytes per completed workflow |
| Fault containment | Number of unrelated domains/workflows affected by a scoped domain failure |
| Reconciliation burden | Conflicts, unresolved items and manual interventions required after reconnect/restart |
| Evidence integrity | Injected tampering detected, missed tampering, and false rejection |
| Independence | Recorded separation of producer/verifier identities, workspaces, methods, tools and data access |
| Authority safety | Unauthorized consequential actions accepted; target-side rejection evidence and receipt evidence |

Do not turn measurements into pass thresholds until the workload and baseline have been run and the project owner sets the required limits.

## 6. Hard acceptance gates — retain existing A–E

The five gates from the recovered fault model remain mandatory:

- **Gate A — Authority integrity:** current scope and permission must be enforced at the target boundary for consequential actions. FT-06 and FT-08 are directly relevant. A valid signature or old approval alone is insufficient.
- **Gate B — Continuity/recovery:** crashes, partitions, duplicate delivery and reopening must not lose committed work, duplicate effects or corrupt lineage. Preserve the existing FT recovery cases.
- **Gate C — Evidence integrity:** corruption, tampering, stale trust anchors and provenance defects must be detected. Retain FT-07/FT-08/FT-09 and the existing PROV-FI family.
- **Gate D — Independent verification:** β must be meaningfully independent and able to dispute α. Retain FT-10/FT-11.
- **Gate E — Scalability/resilience:** domain failures, partitions, overload and remote evidence access must be contained without cascading failure or uncontrolled retries. Retain FT-02/FT-03/FT-12/FT-13 as described in the existing fault record.

Hard categorical outcomes already present in the fault model remain hard: no unauthorized action, no lost committed work, no duplicate side effect, no undetected injected corruption, no false independence claim, no uncontrolled retry storm and no unrelated-domain collapse. These are not invented performance thresholds.

## 7. Existing test ownership — no parallel test family

Preserve and reuse:
- `FT-01…FT-16` — existing hybrid architecture fault scenarios.
- `SEARM-FI-01…SEARM-FI-18` — lifecycle persistence and recovery.
- `PROV-FI-01…PROV-FI-10` — provenance/evidence integrity.
- `AD-01…AD-12` — separate DDEP authority/fencing/revocation/idempotency/receipt/recovery ownership where applicable.
- `C-01…C-19` — cross-track qualification/correction/reopening ownership where applicable.

The recovered fault-model record explicitly describes FT-01, FT-02, FT-03, FT-04, FT-06, FT-07, FT-08, FT-09, FT-10, FT-11, FT-12 and FT-15. It references FT-13 as remote evidence access and FT-14 as state transitions. The exact definitions of FT-05 and FT-16 are not established in that record. Preserve those identifiers and retrieve their authoritative definitions; do not invent or renumber them.

The fault-model record identifies gaps around trust-anchor replacement, chain-of-custody/canonicalization bypass and common verification data. Keep these as documented gaps until reconciled with the existing test owners; do not create new permanent test IDs or a parallel suite.

## 8. Fair comparison and decision rule

- Pin the same workload SHA, requirements, test set, resource budget and measurement harness across all three variants.
- Bring variants to comparable fidelity; document any feature or maturity asymmetry.
- Capture exact source SHA, environment, commands, raw logs, metrics and artifacts for every run.
- Run each existing fault scenario against each architecture where the scenario applies; mark non-applicable only with a reason and owner review.
- Preserve failures, retries, conflicts, manual interventions and negative results.
- Compare both steady-state performance and fault/recovery behavior.
- No architecture is accepted merely because it is faster or simpler.
- Any failure of a hard gate blocks acceptance, regardless of performance.
- No winner is declared until workload, metrics, test mapping and owner-defined thresholds are frozen and the evidence is independently reviewed.

## 9. Current disposition and next action

- Architecture comparison task: **ACTIVE**.
- Candidate architectures: **identified**.
- Prior preferred hypothesis: **local-first hybrid**, not selected.
- Centralized modular: **reference baseline/fallback**.
- Federation: **candidate under test; expansion deferred pending measured need**.
- Workload: **NOT FROZEN**.
- Numerical performance thresholds: **NOT DEFINED — intentionally not invented**.
- FT/SEARM/PROV tests: **NOT RUN in this comparison**.
- Canonical DingoOS source and authenticated engineering manual: **UNRETRIEVED**.
- Consequential dispatch: **HOLD / NO-GO**.

**Immediate decision required to freeze the benchmark:** whether to use the source-derived WLC-001 resonance-analysis workflow as the common workload, with a deterministic derived harness and explicit separation of simulation agreement from physical validation. Until that decision is made, no comparative architecture implementation or performance run should claim to use a frozen workload.
