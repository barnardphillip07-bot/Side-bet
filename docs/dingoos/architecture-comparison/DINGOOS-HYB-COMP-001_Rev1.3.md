# DINGOOS-HYB-COMP-001 — Comparative Architecture Acceptance Plan

- Revision: Rev1.3
- Date: 27 November 2026
- Workspace: `barnardphillip07-bot/Side-bet`
- Branch: `dingoos/recovery-engine-adopted-requirements`
- Status: **ACTIVE COMPARISON WORK PACKAGE — WLC-001 WORKLOAD FROZEN — THREE-TOPOLOGY SMOKE PROTOTYPE IMPLEMENTED AND CI VERIFIED — FT-02 PROTOTYPE SUBSET EXECUTED — FT-03 MODEL SUBSET EXECUTED — FUNCTIONAL SMOKE PROTOCOL FROZEN — PERFORMANCE PROTOCOL OPEN — NO ARCHITECTURE SELECTED**
- Supersedes: Rev0.1 for current execution status; Rev0.1 remains preserved as the prior revision.

## 1. Continuity and authority

This work continues the prior Side-bet DingoOS engineering direction. It does not restart architecture design, select a winner, or adopt `DINGOOS-HYB-ARCH-002 Rev0.2` as canonical.

Recovered prior direction:
- `DINGOOS-HYB-ARCH-002 Rev0.2` identifies local-first modular DingoOS with a hybrid logical architecture as the preferred hypothesis.
- Centralized modular architecture remains the reference baseline and fallback.
- Federation is deferred until measured requirements justify it.
- The current POC direction is one local deployable with strict module, authority, data and trust boundaries; later extraction of specialist domains is conditional on measured need.
- `DINGOOS-HYB-FAULT-001` defines five hard gates A–E and maps existing FT scenarios to them.
- Numerical performance thresholds remain undefined and must be set by project owners after baseline measurements. No thresholds are invented here.

The user's workspace directive makes Side-bet the primary DingoOS engineering and construction workspace. This supersedes the older HYB-ARCH-002 §4.5 restriction that DingoOS-specific architecture should remain outside Side-bet. Protected BIF/IP, credentials and private original source remain protected; workspace scope is not permission to publish confidential material.

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
- Specialist domains can later be selectively extracted when measurements justify it.
- Shared project identity, requirements lineage, provenance and governance semantics remain coherent.
- Disconnection permits bounded local research but not consequential actions requiring current global authority.

The local-first hybrid is the prior preferred hypothesis, not a measured winner or approved canonical architecture. The comparison must be capable of falsifying it.

## 3. Frozen common workload — WLC-001

**Decision: APPROVED BY USER — FROZEN WORKLOAD DEFINITION.**

WLC-001 — CSRE1/CSRE2 resonance-analysis and verification vertical slice — is the common workload for all three architectures.

Frozen workload artifacts:
- Specification: [`WLC-001-FROZEN-Rev0.2.json`](workloads/WLC-001-FROZEN-Rev0.2.json)
- Derived harness: [`benchmarks/dingoos/wlc_001.py`](../../../../benchmarks/dingoos/wlc_001.py)
- Harness tests: [`tests/dingoos/test_wlc_001.py`](../../../../tests/dingoos/test_wlc_001.py)
- Topology prototype and FT-02 subset report: [`DINGOOS-HYB-COMP-002 Rev0.4`](DINGOOS-HYB-COMP-002_Rev0.4.md)
- FT-03 bounded partition model report: [`DINGOOS-HYB-COMP-004 Rev0.3`](DINGOOS-HYB-COMP-004_Rev0.3.md)
- Functional topology smoke protocol: [`DINGOOS-HYB-COMP-003 Rev0.2`](DINGOOS-HYB-COMP-003_Rev0.1.md)

### 3.1 Source provenance

Source artifact: Library `Pasted text(7).txt`, 133,685 bytes, 2,778 lines, whole-file SHA-256:

`548a7a5595bd5d81863fbc8815e45e0b0423c51712883b585135cfea3d369752`

| Component | Lines | Byte range | Region SHA-256 |
|---|---:|---:|---|
| C3PO proposer / C4PO verifier | 98–123 | `[9456:11166]` | `ba4d793d8dcbe48d49013a6ff6d7823843c9a42d9f7bd18dbe5b4ec6cd66cdae` |
| DigitalTwin transient simulation | 135–166 | `[12090:13403]` | `1cb95d3cbb612aa5c31b94588e8accaf84511be427ec44235212e3cebad77556` |
| SensorHardwareGateway | 167–195 | `[13403:14517]` | `086b4eb8a84a38adcb4c7367689e58976350e54836e03711dc37c76602205317` |
| Main orchestration excerpt | 1659–1685 | `[92743:93802]` | `35aa9263150b129cef76d1a9d5c5cb30aa82404d67ef45900bdc24fb1bb96ad3` |

The source is a mixed prose/source **HISTORICAL_COMPILATION**, not an authenticated canonical source tree or verified executable. The harness is a separate **DERIVED_RECONSTRUCTION** and does not modify or authenticate that compilation.

### 3.2 Frozen inputs

| Input | Frozen value |
|---|---:|
| Mass | 5.0 kg |
| Stiffness | 500.0 N/m |
| Viscous damping coefficient | 0.05 N·s/m |
| Duration | 2.0 s |
| Time step | 0.001 s |
| Integration steps | 2,000 |
| Initial displacement | 1.0 m |
| Initial velocity | 0 m/s |

### 3.3 Corrected analytical/numerical comparison

The numerical simulation includes non-zero viscous damping. Therefore the primary analytical oracle is the **damped natural frequency**, not the undamped formula.

[
f_d = \frac{1}{2\pi}\sqrt{\frac{k}{m}-\left(\frac{c}{2m}\right)^2}
]

| Result | Frequency |
|---|---:|
| Analytical damped reference | 1.591549231975262 Hz |
| Analytical undamped boundary reference | 1.5915494309189535 Hz |
| Source-faithful numerical estimate | 1.5923566878980893 Hz |
| Absolute numerical difference vs damped reference | 0.0008074559228272715 Hz |

Numerical zero crossings: 0.157, 0.471, 0.785, 1.099, 1.413 and 1.727 seconds. Mean half-period: 0.314 seconds.

This comparison uses the historical DigitalTwin update sequence and zero-crossing estimator. The difference is a result for this fixed numerical method, step size and estimator; it is not an architecture-performance threshold.

### 3.4 Deterministic harness and local verification

The derived harness:
- uses Python standard library only;
- fixes all core inputs;
- excludes wall-clock-derived IDs, random identifiers, sensor noise, network access and external services from the deterministic core;
- reproduces the historical DigitalTwin state-update and zero-crossing sequence;
- reports both damped and undamped analytical values;
- implements β verification through a separate characteristic-root calculation, not by reusing α's analytical function;
- labels the epistemic limit explicitly.

Local test result: **7/7 unittest cases passed** for analytical references, independent β characteristic-root verification, numerical reference, repeatability, epistemic-limit labeling, input validation and underdamped-domain validation.

This is a local harness test result only. It is not a GitHub Actions result, architecture comparison, integration test, or physical validation.

### 3.5 Explicit source/integration limitations

- The historical main orchestration hardcodes a simulated measurement of approximately 1.59155 Hz and does not call the separate DigitalTwin implementation. The harness composes the methods explicitly; this is new derived benchmark code, not a recovered original call-site.
- Historical C3PO/C4PO IDs use wall-clock-derived values. The deterministic numerical core excludes these agent IDs; any later architecture integration must use declared fixed IDs or a deterministic ID generator in the run manifest.
- The SensorHardwareGateway uses Gaussian noise without a source-recorded seed. It is excluded from the frozen deterministic core. Any noisy-sensor extension must be separately versioned with a declared RNG algorithm and seed.
- The source compilation contains mixed prose/source and conflicting gateway variants. Preserve it byte-for-byte and do not promote it to authenticated canonical source.
- The workload contains no production γ authority or consequential target operation. Authority/fencing acceptance remains covered by existing test ownership and actual target-source verification.

### 3.6 Scope of the freeze

Frozen now:
- workload identity and purpose;
- exact deterministic core inputs;
- analytical damped oracle and undamped boundary reference;
- source-faithful numerical algorithm and reference outputs;
- deterministic harness and its source attribution;
- epistemic limits and explicit exclusions.

Not frozen yet:
- architecture implementation commits and fidelity-equivalence assessment;
- common host/runtime resource envelope and isolation conditions;
- architecture invocation and concurrency/load schedule;
- fault-injection schedule and repetition count;
- raw observation schema, metric calculations and stopping rule;
- owner-defined architecture performance thresholds.

Do not describe the entire benchmark campaign as frozen. The **workload definition** is frozen; the **execution protocol** remains open.

## 4. Measurement protocol

Record raw observations and exact run provenance for every architecture. At minimum:

| Metric | Measurement definition |
|---|---|
| End-to-end latency | Time from accepted workflow request to terminal workflow outcome; report distribution, not only mean |
| Throughput | Completed valid workflows divided by measured wall-clock interval |
| Recovery time | Time from injected fault to restored consistent, usable state |
| Event loss | Count of committed events absent after recovery |
| Duplicate delivery/effect | Count of duplicate event acceptances and duplicate consequential effects, separately |
| Verification backlog | Pending β assessments and age of oldest pending assessment |
| Resource use | CPU time, peak memory, persistent bytes and network bytes per completed workflow |
| Fault containment | Number of unrelated domains/workflows affected by a scoped domain failure |
| Reconciliation burden | Conflicts, unresolved items and manual interventions after reconnect/restart |
| Evidence integrity | Injected tampering detected, missed tampering and false rejection |
| Independence | Separation of producer/verifier identities, workspaces, methods, tools and data access |
| Authority safety | Unauthorized consequential actions accepted; target-side rejection and receipt evidence |

Do not turn measurements into pass thresholds until baseline runs are complete and the project owner sets the required limits.

## 5. Hard acceptance gates — retain existing A–E

The five gates from the recovered fault model remain mandatory:

- **Gate A — Authority integrity:** current scope and permission must be enforced at the target boundary for consequential actions. FT-06 and FT-08 are directly relevant. A valid signature or old approval alone is insufficient.
- **Gate B — Continuity/recovery:** crashes, partitions, duplicate delivery and reopening must not lose committed work, duplicate effects or corrupt lineage. Preserve existing FT recovery cases.
- **Gate C — Evidence integrity:** corruption, tampering, stale trust anchors and provenance defects must be detected. Retain FT-07/FT-08/FT-09 and the existing PROV-FI family.
- **Gate D — Independent verification:** β must be meaningfully independent and able to dispute α. Retain FT-10/FT-11.
- **Gate E — Scalability/resilience:** domain failures, partitions, overload and remote evidence access must be contained without cascading failure or uncontrolled retries. Retain FT-02/FT-03/FT-12/FT-13 as described in the existing fault record.

Hard categorical outcomes already present in the fault model remain hard: no unauthorized action, no lost committed work, no duplicate side effect, no undetected injected corruption, no false independence claim, no uncontrolled retry storm and no unrelated-domain collapse. These are not invented performance thresholds.

## 6. Existing test ownership — no parallel test family

Preserve and reuse:
- `FT-01…FT-16` — existing hybrid architecture fault scenarios.
- `SEARM-FI-01…SEARM-FI-18` — lifecycle persistence and recovery.
- `PROV-FI-01…PROV-FI-10` — provenance/evidence integrity.
- `AD-01…AD-12` — DDEP authority/fencing/revocation/idempotency/receipt/recovery ownership where applicable.
- `C-01…C-19` — cross-track qualification/correction/reopening ownership where applicable.

The recovered fault-model record explicitly describes FT-01, FT-02, FT-03, FT-04, FT-06, FT-07, FT-08, FT-09, FT-10, FT-11, FT-12 and FT-15. It references FT-13 as remote evidence access and FT-14 as state transitions. Exact definitions of FT-05 and FT-16 remain unestablished in that record. Preserve those identifiers and retrieve authoritative definitions; do not invent or renumber them.

The fault-model record identifies gaps around trust-anchor replacement, chain-of-custody/canonicalization bypass and common verification data. Keep these as documented gaps until reconciled with existing test owners; do not create new permanent test IDs or a parallel suite.

The seven WLC-001 harness unit tests validate the deterministic workload implementation only. They do not replace, satisfy or rename any FT/SEARM/PROV/AD/C test.

## 7. Fair comparison and decision rule

- Pin the same WLC-001 frozen specification SHA, workload inputs, requirements, test set, resource budget and measurement harness across all three variants.
- Bring variants to comparable fidelity; document any feature or maturity asymmetry.
- Capture exact source SHA, environment, commands, raw logs, metrics and artifacts for every run.
- Run each existing fault scenario against each architecture where applicable; mark non-applicable only with a reason and owner review.
- Preserve failures, retries, conflicts, manual interventions and negative results.
- Compare steady-state performance and fault/recovery behavior.
- No architecture is accepted merely because it is faster or simpler.
- Any failure of a hard gate blocks acceptance, regardless of performance.
- No winner is declared until execution protocol, metrics, test mapping and owner-defined thresholds are frozen and evidence is independently reviewed.

## 8. Current disposition and next actions

- Architecture comparison task: **ACTIVE**.
- Candidate architectures: **identified**.
- Prior preferred hypothesis: **local-first hybrid**, not selected.
- Centralized modular: **reference baseline/fallback**.
- Federation: **candidate under test; expansion deferred pending measured need**.
- WLC-001 workload definition: **FROZEN BY USER APPROVAL**.
- Deterministic derived harness: **IMPLEMENTED**.
- WLC-001 local unit tests: **7/7 PASS**.
- Three-topology smoke prototype: **IMPLEMENTED; 7/7 local tests PASS; GitHub Actions SUCCESS**.
- FT-02 domain-failure prototype subset: **EXECUTED; federated and hybrid preserve unaffected role results and mark Σ INCOMPLETE; centralized sequential baseline stops before Beta**.
- FT-03 bounded vector-clock partition model subset: **IMPLEMENTED; 6 additional model tests; CI SUCCESS**. Six new model tests (13 total topology/FT-03 tests) passed in the configured workflow. The emitted artifact was downloaded and inspected; it contains FT-02 and FT-03 outputs for all three topology labels. Global coordination pauses, speculative offline branches remain uncommitted, concurrent updates are detected and automatic merge is prohibited. This is a deterministic abstract model, not a real network partition or runtime reconciliation test.
- Full FT-02 acceptance: **NOT ESTABLISHED**; full FT-03 acceptance: **NOT ESTABLISHED**; Gates A–E: **NOT PASSED / NOT RUN AS A FULL CAMPAIGN**.
- Federated variant: **single-host process-isolated surrogate only; not full federation**.
- Gate D independence: **NOT ESTABLISHED**; fault gates A–E: **NOT RUN**.
- Functional topology smoke protocol: **FROZEN**.
- Controlled performance/architecture acceptance protocol: **OPEN / NOT FROZEN**.
- Comparative architecture performance acceptance: **NOT PERFORMED**; one local timing sample is diagnostic only.
- Numerical architecture performance thresholds: **NOT DEFINED — intentionally not invented**.
- FT/SEARM/PROV/AD/C architecture fault campaigns: **NOT RUN except the bounded FT-02 prototype subset and FT-03 abstract model subset**.
- Canonical DingoOS source and authenticated engineering manual: **UNRETRIEVED**.
- Consequential dispatch: **HOLD / NO-GO**.

Next engineering sequence:
1. Preserve the Library parallel reverse-engineered working baseline and its provenance; do not equate it with authenticated private A0 source or the historical `Pasted text(7).txt` compilation.
2. Reconcile the inspected Side-bet tree and current derived topology prototype against existing DingoOS ownership boundaries; no pre-existing architecture runtime was found in the inspected branch.
3. Execute the frozen functional smoke protocol on each controlled code revision. Separately define the performance/architecture acceptance protocol: resource envelope, invocation/load schedule, concurrency, repetitions, raw observation schema and stopping rule.
4. Map existing FT/SEARM/PROV/AD/C owners to applicable experiments; preserve all existing identifiers and ownership.
5. Extend the three variants only to comparable, evidence-backed fidelity. Keep target authority, persistence/recovery and independence claims blocked until their actual mechanisms and tests exist.
6. Run the remaining applicable fault scenarios under their existing owners; preserve raw evidence. FT-02 prototype subset does not close the full FT-02 scenario.
7. Run controlled baselines and applicable fault campaigns; preserve raw evidence. Set owner-defined performance thresholds only after measurements.
8. Continue with FT-01 only after recovering the actual coordinator/persistence/commit boundaries; then FT-04 duplicate result delivery and FT-12 overload/backpressure, preserving each original test owner.

## 9. Change history

- Rev0.1 — 27 November 2026: initial comparative acceptance plan; WLC-001 candidate identified but not frozen.
- Rev0.2 — 27 November 2026: WLC-001 workload definition frozen by user approval; deterministic derived harness implemented; primary oracle corrected to damped natural frequency; execution protocol kept open.
- Rev0.3 — 27 November 2026: β verification separated from α's analytical implementation by independently calculating the damped-system characteristic roots; harness test count increased to 7; frozen workload specification versioned as Rev0.2. No architecture selection made.

- Rev0.4 — 27 November 2026: recorded the derived three-topology WLC-001 smoke prototype, four local tests, successful GitHub Actions verification, and explicit single-host federation/assurance limitations. No architecture selected.
- Rev0.5 — 27 November 2026: added a bounded FT-02 domain-failure subset and its seven-test/CI evidence; recorded incomplete synthesis rather than false completion; retained full FT-02 and Gates A–E as unestablished.
- Rev0.6 — 27 November 2026: pinned the FT-02 prototype report to the exact successful CI commit and uploaded artifact. No architecture selected.
- Rev0.7 — 27 November 2026: corrected the report's current test-count summary and section numbering; retained the same exact CI evidence and disposition.
- Rev0.8 — 27 November 2026: corrected the frozen-specification link label and linked the current topology/FT-02 prototype report.
- Rev0.9 — 27 November 2026: froze the functional topology smoke protocol and run-manifest requirements; kept controlled performance and full architecture acceptance protocol open.
- Rev1.0 — 27 November 2026: pinned the frozen-protocol execution to exact commit `9b1235edef6d114c668e51fb00a6e4dc4bd081a4` and successful CI runs/artifact. Performance acceptance remains open; no architecture selected.
- Rev1.1 — 27 November 2026: added the bounded FT-03 vector-clock partition model, six tests, runner evidence output, successful CI verification at commit `35e39a534b43918951382bb7a77cb9e90cbc804b`, and report `DINGOOS-HYB-COMP-004 Rev0.2`. Architecture workflow run `45932229705` succeeded; artifact `15169076080` was downloaded and inspected, confirming FT-02 and FT-03 outputs. Full network/runtime FT-03 remains NOT_ESTABLISHED. No architecture selected.

**No architecture selection is made by this revision.**
