# DINGOOS-HYB-COMP-002 — WLC-001 Architecture Topology Prototype Report

- Revision: Rev0.2
- Date: 27 November 2026
- Workspace: `barnardphillip07-bot/Side-bet`
- Branch: `dingoos/recovery-engine-adopted-requirements`
- Status: **DERIVED EXPERIMENTAL PROTOTYPE — IMPLEMENTED — CI VERIFIED — FT-02 PROTOTYPE SUBSET EXECUTED — NOT ARCHITECTURE ACCEPTANCE — NO WINNER SELECTED**
- Parent work package: `DINGOOS-HYB-COMP-001 Rev0.3`
- Workload: `WLC-001-FROZEN Rev0.2`

## 1. Purpose and disposition

This report records the first executable topology smoke test using the user-approved WLC-001 common workload. It is a derived experimental prototype, not canonical DingoOS runtime code, not a recovered original implementation, and not an architecture selection.

The purpose is narrow: demonstrate that the same frozen analytical/numerical workload can execute through three different orchestration topologies while preserving identical outputs and explicit assurance limits.

**Result:** all three variants returned identical WLC-001 numerical outputs. Four local topology tests passed. GitHub Actions passed the topology tests and emitted/preserved a raw JSON smoke result artifact. No architecture is selected.

## 2. Source and working-baseline reconciliation

The active parallel reverse-engineered DingoOS working baseline remains part of the Library/archive reconstruction. Its controlling source-inspection and continuity record is `DINGOOS-PRE-RESTORATION-INSPECTION-001 Rev0.1`; the reconciled state snapshot is `DINGOOS-RECONCILED-BASELINE-001 Rev0.3`.

These are derived parallel-reconstruction records, distinct from authenticated original private A0 source. The private `phillipbarnard07-cell/DingoOS` source remains `UNRETRIEVED` through the connected GitHub context. A 404/access failure is not proof of deletion or non-existence.

`Pasted text(7).txt` remains a source-bearing historical compilation with multiple generations and fragments. It is not silently promoted to a single authenticated canonical revision. WLC-001's DigitalTwin algorithm is attributed to its exact source-bearing region; the harness and topology variants are separate `DERIVED_RECONSTRUCTION` artifacts.

### 2.1 Side-bet repository inventory at this increment

Repository tree inspection found:
- `main`: README-only starter tree.
- `research/independent-physics-reference-poc`: six-file generic physics-reference benchmark; not a DingoOS architecture implementation.
- `dingoos/recovery-engine-adopted-requirements`: DingoOS workspace mandate, adopted recovery-engine requirements/contracts/schemas/indexer, source-recovery evidence/indexes, WLC-001 specification/harness, and this derived architecture experiment.

No pre-existing centralized, federated or local-first-hybrid DingoOS runtime implementation was found in the inspected Side-bet branch tree. This is a statement about the inspected repository tree, not a claim that no such implementation exists elsewhere in the parallel Library reconstruction or inaccessible private source.

The user's later adopted Side-bet Workspace Mandate supersedes the earlier HYB-ARCH-002 Rev0.2 restriction that this public repository was not a DingoOS development destination. Public-repository confidentiality restrictions remain in force.

## 3. Topology variants implemented

All variants use the same frozen WLC-001 inputs, Alpha A analytical damped-frequency function, Alpha B source-faithful explicit-Euler simulation, and Beta independent characteristic-root calculation.

### A — Centralized modular

- One process.
- Central coordinator invokes Alpha A, Alpha B and Beta directly.
- All computation and result assembly occur in the same process.

### B — Federated process-isolated surrogate

- Three local worker processes: Alpha A, Alpha B and Beta.
- Each worker receives the same frozen input envelope and returns a JSON result.
- The coordinator collects the role outputs.
- This is a **single-host process-isolated surrogate**, not a complete federation: no remote nodes, network partitions, independent persistent domain stores, distributed policy replication or production reconciliation protocol is implemented.

### C — Local-first hybrid

- Alpha A and Alpha B execute as local modules.
- Beta executes in a separate worker process and receives only the frozen workload inputs.
- This models local analytical execution with a selectively isolated verifier.
- No remote specialist domain is deployed in this increment.

### 3.1 Independence and authority limits

Beta does not receive Alpha outputs in any variant. It computes the characteristic-root frequency from the frozen inputs. This establishes input separation within the prototype, but not independent codebase, toolchain, model provider, credentials, operator or organization.

Therefore:
- Gate D independence: **NOT ESTABLISHED**.
- γ authority: **NOT IN SCOPE**.
- Consequential effects: **NONE**.
- Target-side enforcement: **NOT TESTED**.
- Fault gates A–E: **NOT RUN**.
- Physical/experimental validation: **NOT ESTABLISHED**.

The prototype does not implement or claim DDEP fencing, γ revocation, durable receipts, idempotent external effects, persistence/recovery guarantees, or any production security boundary.

## 4. Reproducible result

All three variants produced the same result:

| Quantity | Result |
|---|---:|
| Alpha A analytical damped reference | 1.591549231975262 Hz |
| Alpha B numerical estimate | 1.5923566878980893 Hz |
| Beta independent characteristic-root result | 1.591549231975262 Hz |
| Absolute numerical/Beta difference | 0.0008074559228272715 Hz |

This is internal analytical/numerical consistency for the declared model and integration step. It is not empirical measurement, experimental validation or physical validation.

## 5. Test and CI evidence

### 5.1 Local test

Environment:
- Python 3.13.5
- Linux 6.18.57 x86_64
- Reported CPU count: 3
- No CPU affinity, processor model, memory reservation or isolation guarantee was established.

Command:
`python -m unittest discover -s tests -v`

Result: **7/7 topology tests passed**:
1. All variants produce identical WLC-001 outputs.
2. Federated topology is explicitly labelled a single-host surrogate.
3. Beta receives only frozen inputs; Gate D is not overstated.
4. Three FT-02 prototype-subset cases verify failure handling in each topology; no full FT-02 or Gate A–E pass is claimed.
5. No γ authority, consequential effect or target enforcement is claimed.

The WLC-001 harness separately has **7/7 tests passing**.

### 5.2 GitHub Actions

Commit: `0a6e6e6120a8be04b5bf15e67a5f48b0fc33e68b`

- Architecture topology workflow: **SUCCESS**.
- WLC-001 deterministic workload workflow: **SUCCESS**.
- Recovery-engine contract workflow: **SUCCESS**.

Architecture workflow run:
https://github.com/barnardphillip07-bot/Side-bet/actions/runs/45929466583

The architecture workflow ran the seven topology tests, emitted the JSON comparison and FT-02 subset results, and uploaded them as the `wlc001-architecture-smoke` artifact. The CI runner is a correctness/functional environment, not a controlled performance benchmark platform.

### 5.3 Single local timing observation — diagnostic only

One local smoke invocation produced:

| Variant | Observed elapsed wall time |
|---|---:|
| Centralized modular | 0.493 ms |
| Federated process-isolated surrogate | 1,255.1 ms |
| Local-first hybrid | 715.3 ms |

These are single observations on an uncontrolled container. Process startup and scheduling dominate the isolated-process variants. They are not steady-state measurements, have no statistical confidence, do not establish an architecture ranking, and must not be used to set performance thresholds.

### 5.3 FT-02 domain-failure prototype subset

The existing FT-02 owner scenario is domain failure: a specialist node fails, unrelated domains continue, and Σ records the missing contribution. This prototype executes only a bounded WLC-001 subset of that scenario.

| Variant | Injected failure | Observed role outcome | Σ disposition |
|---|---|---|---|
| Centralized modular | Alpha-B module failure during sequential in-process execution | Alpha-A completed; Alpha-B failed; Beta was not reached | `INCOMPLETE`; missing Alpha-B and Beta |
| Federated process-isolated surrogate | Alpha-B worker process exits non-zero | Alpha-A and Beta completed; Alpha-B failed | `INCOMPLETE`; missing Alpha-B |
| Local-first hybrid | Alpha-B local module raises at its module boundary | Alpha-A and isolated Beta completed; Alpha-B failed | `INCOMPLETE`; missing Alpha-B |

The federated and hybrid variants demonstrate bounded continuation of unaffected roles and explicit incomplete synthesis. The centralized variant demonstrates the sequential baseline's larger failure propagation in this prototype. All variants refuse to promote the result to complete when Alpha-B is missing.

**Disposition:** `FT-02 PROTOTYPE SUBSET — PASS FOR THE ASSERTED LOCAL BEHAVIOUR`; **full FT-02 acceptance remains NOT ESTABLISHED**. This does not test actual remote domain nodes, persistent domain state, network partitions, recovery/restart, production messaging, target authority or unrelated real DingoOS services. It is not a pass of Gate E or the complete FT-01–FT-16 suite.

## 6. What this experiment establishes — and does not establish

Established:
- The WLC-001 frozen workload can be called through three distinct orchestration topologies.
- The variants return identical reference outputs.
- The federated surrogate and hybrid isolate Beta in a separate process.
- The bounded FT-02 prototype subset records incomplete state and preserves unaffected role results without false completion.
- The test and result-emission workflow is repeatable in GitHub Actions.

Not established:
- Full centralized, federated or hybrid DingoOS architecture implementations.
- Comparable production fidelity.
- Multi-host federation, domain-owned persistent state, remote evidence access or network-partition recovery.
- Full FT-02 acceptance or the wider FT-01–FT-16 fault suite.
- Gate A authority integrity or target-side fencing.
- Gate B continuity, persistence and crash recovery.
- Gate C end-to-end evidence integrity and trust-anchor enforcement.
- Gate D organizational/method/tool independence.
- Gate E load resilience, backpressure or fault containment.
- Performance acceptance, Pareto dominance or architecture selection.
- DingoOS integration with the inaccessible private canonical source.

WLC-001 is a bounded first vertical slice. It does not cover the whole DingoOS lifecycle, provenance, governance, persistence or consequential dispatch.

## 7. Next engineering work

1. Preserve this topology prototype as a derived experimental branch; do not merge it into `main` or label it production.
2. Reconcile the prototype interfaces against the recovered parallel working baseline and existing DingoOS ownership boundaries before adding persistence, registries, event stores or governance mechanisms.
3. Define a versioned execution/run protocol: exact resource envelope, invocation schedule, concurrency, repetition count, fault-injection schedule, raw observation schema and stopping rule. Leave owner-defined performance thresholds open until controlled baseline measurements exist.
4. Map existing FT/SEARM/PROV/AD/C owners to applicable topology experiments. Reuse their identifiers; do not create a parallel permanent fault suite.
5. Extend the variants only where the common workload can discriminate architecture behavior. Keep unimplemented fault gates explicitly NOT_RUN.
6. Retain centralized modular as baseline/fallback, local-first hybrid as a preferred hypothesis, and federation as a conditional candidate. Do not select a winner from this smoke test.

## 8. Change history

- Rev0.1 — 27 November 2026: first WLC-001 topology smoke prototype across centralized modular, federated process-isolated surrogate and local-first hybrid. Four local tests and GitHub Actions passed. Outputs matched. No architecture selected; no fault gates or performance acceptance claimed.
- Rev0.2 — 27 November 2026: added a bounded FT-02 domain-failure subset across all three topologies. Seven local topology tests and GitHub Actions passed. Federated and hybrid variants preserved unaffected role outputs and marked Σ incomplete; centralized sequential execution stopped before Beta. Full FT-02 and Gate E remain NOT_ESTABLISHED.
