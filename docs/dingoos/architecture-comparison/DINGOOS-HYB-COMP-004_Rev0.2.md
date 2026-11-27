# DINGOOS-HYB-COMP-004 — FT-03 Network Partition Model Experiment

- Revision: Rev0.2
- Date: 27 November 2026
- Workspace: `barnardphillip07-bot/Side-bet`
- Branch: `dingoos/recovery-engine-adopted-requirements`
- Status: **BOUNDED FT-03 MODEL-LEVEL SUBSET IMPLEMENTED AND CI-VERIFIED — REAL NETWORK PARTITION / DURABLE RECONCILIATION NOT TESTED — FULL FT-03 NOT ESTABLISHED**
- Related: `DINGOOS-HYB-COMP-001 Rev1.0`; `DINGOOS-HYB-COMP-002 Rev0.4`; `DINGOOS-HYB-COMP-003 Rev0.2`.

## 1. Purpose and recovered requirement

The recovered Library source `Fault model and acceptance criteria for DingoOS hybrid architecture` defines FT-03 (Network Partition) as:
- loss of connectivity between the core and a domain;
- local tasks may proceed in read-only or offline mode;
- global coordination pauses;
- global state must not be corrupted;
- after reconnection, conflicting updates (for example, two domains changing the same object differently) must be detected;
- version vectors are identified as a possible conflict-detection control;
- the original scenario proposes disabling the network link between modules.

This report records a **derived deterministic model experiment**, not execution against an existing DingoOS network/runtime. The current three-topology code is a smoke prototype; it has no actual network links, durable replica stores, production event bus, DDEP enforcement or conflict-resolution service. This boundary is mandatory when interpreting the result.

## 2. Implemented model

Source:
- `experiments/dingoos_architecture_comparison/ft03_partition_model.py`
- Test: `tests/architecture_comparison/test_ft03_partition_model.py`
- Runner integration: `experiments/dingoos_architecture_comparison/runner.py`

The model runs the same bounded partition/conflict scenario under the three architecture labels:
- `CENTRALIZED_MODULAR`
- `FEDERATED_PROCESS_ISOLATED_SURROGATE`
- `LOCAL_FIRST_HYBRID`

All three are evaluated using the same abstract state-machine rules. This is not proof that the current topology prototypes implement these rules.

### 2.1 Scenario

1. A core object exists at a common base state: `WLC-001/design-parameter = design-baseline-v1`, vector `{core: 1}`.
2. Connectivity between core and domain is lost.
3. Global coordination is marked `PAUSED`.
4. Two domains create distinct speculative offline branch updates from the same base:
   - domain-a: `design-branch-alpha`, vector `{core: 1, domain-a: 1}`;
   - domain-b: `design-branch-beta`, vector `{core: 1, domain-b: 1}`.
5. Neither branch is globally committed while partitioned.
6. On reconnection, vector-clock comparison identifies the updates as concurrent.
7. Reconciliation returns `CONFLICT`; automatic merge is prohibited; global state remains unchanged and pending explicit review.

### 2.2 Formal vector relation

For vector clocks (V_a) and (V_b), missing components are zero.

- (V_a leq V_b) componentwise and (V_a 
eq V_b): (V_a) is BEFORE.
- (V_b leq V_a) componentwise and (V_a 
eq V_b): (V_a) is AFTER.
- Both equal: EQUAL.
- Neither dominates: CONCURRENT.

The experiment's updates are concurrent because domain-a and domain-b each advance a different component from the same base. A concurrent update pair cannot be safely resolved by simple last-write-wins without a separately approved domain-specific merge policy.

### 2.3 Expected invariants

| Invariant | Model outcome |
|---|---|
| Global coordination pauses during partition | PASS |
| Local speculative work remains separately represented | PASS |
| Offline updates are not silently globally committed | PASS |
| Concurrent updates are detected after reconnect | PASS |
| Global baseline is not overwritten by unresolved branches | PASS |
| Automatic merge is prohibited | PASS |
| Explicit conflict resolution remains required | PASS |

These are model assertions, not runtime acceptance evidence.

## 3. Test and CI evidence

Six new tests cover:
1. concurrent vector updates are detected;
2. dominating versions are ordered;
3. same-version/different-content records are treated as a conflict;
4. all three architecture-labelled model runs pause global coordination and detect conflict;
5. offline branches do not modify global state;
6. unknown architecture labels are rejected.

The existing seven topology tests remain unchanged. The architecture workflow discovers both test files, for 13 topology/FT-03 tests total.

GitHub Actions evidence for branch `dingoos/recovery-engine-adopted-requirements`:
- Architecture comparison run: [45932047519](https://github.com/barnardphillip07-bot/Side-bet/actions/runs/45932047519) — **SUCCESS**.
- WLC-001 workload run: [45932047449](https://github.com/barnardphillip07-bot/Side-bet/actions/runs/45932047449) — **SUCCESS**.
- Recovery-engine contract run: [45932047490](https://github.com/barnardphillip07-bot/Side-bet/actions/runs/45932047490) — **SUCCESS**.
- Exact tested commit including FT-03 runner integration and this report: `35e39a534b43918951382bb7a77cb9e90cbc804b`.
- Preserved architecture smoke artifact: `wlc001-architecture-smoke`, artifact ID `15169076080`, 2,772 bytes, not expired at inspection; downloaded and inspected. It contains both `FT-02` and `FT-03` experiment outputs for all three architecture labels.
- The earlier Rev0.1 artifact pointer (`15168429842`) was an earlier run before FT-03 was wired into the runner. It is superseded by this corrected artifact pointer; Rev0.1 is retained unchanged as historical record.

The Actions job completed the topology tests, evidence-emission step and artifact-upload step successfully. The WLC-001 and recovery-engine contract jobs also completed successfully on the same commit. CI success confirms the configured suites ran without failure; it does not establish full FT-03 acceptance.

## 4. Assurance limitations

The following remain **NOT TESTED / NOT ESTABLISHED**:
- actual network partition, packet loss, link flapping or partial connectivity;
- multiple physical or independently hosted domain nodes;
- durable local replica persistence and crash/restart recovery;
- synchronization ordering, retries, duplicate/reordered delivery and concurrent reconnect races;
- version-vector persistence, compaction, node identity lifecycle or malicious vector manipulation;
- production conflict resolution, merge authorization or human/domain-owner approval;
- global lineage integration, provenance receipts and exact DingoOS object schemas;
- real centralized/federated/hybrid implementation behavior;
- Gate A authority integrity, Gate B complete recovery, Gate C evidence integrity, Gate D independent verification, Gate E resilience;
- complete FT-03 acceptance.

The current model uses a deterministic abstract vector-clock function. It does not prove that the DingoOS runtime stores, transports or enforces these vectors. The model's offline updates are speculative branch values only; no persistent state mutation occurs.

## 5. Disposition

**Bounded FT-03 model subset: PASS for the asserted abstract state-machine properties.**

**Full FT-03: NOT ESTABLISHED.** No claim of a real network partition test or architecture acceptance is made.

**Architecture selection: NOT MADE.** The centralized modular baseline, local-first hybrid hypothesis and federated candidate remain under evaluation. Consequential dispatch remains **HOLD / NO-GO**.

## 6. Next engineering work

1. Recover and map existing DingoOS state/version/provenance types before adapting the model to runtime code. Do not invent canonical schemas.
2. Inspect the existing reverse-engineered working baseline for any already implemented version vectors, branch lineage, offline queues or conflict reconciliation. Do not build a parallel engine if an authoritative mechanism exists.
3. Define a real network fault harness only after the target node/process boundaries and persistence owners are established.
4. Extend FT-03 from the model to process/network-level partition injection, with persistent branch state and restart/reconnect testing.
5. Then continue the existing fault sequence: FT-01 coordinator crash/recovery, FT-04 duplicate result delivery/idempotent ingestion, and FT-12 overload/backpressure. FT-01 remains blocked until authoritative persistence/commit semantics are recovered.
6. Preserve FT-01…FT-16 and SEARM-FI/PROV-FI/AD/C ownership. No parallel permanent fault IDs or test suite.

No numerical performance threshold is introduced. No production mechanism is claimed implemented.
