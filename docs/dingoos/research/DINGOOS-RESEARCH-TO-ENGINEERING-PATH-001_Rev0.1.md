# DINGOOS-RESEARCH-TO-ENGINEERING-PATH-001 — Research Assessment and Evidence-Led Engineering Path

- Revision: Rev0.1
- Date: 27 November 2026
- Workspace: `barnardphillip07-bot/Side-bet`
- Branch: `dingoos/recovery-engine-adopted-requirements`
- Status: **DERIVED RESEARCH ASSESSMENT — WORKING ENGINEERING PATH — NOT AN OWNER-RATIFIED ARCHITECTURE OR IMPLEMENTATION AUTHORIZATION**
- Authority: Derived from recovered Library records, the current Side-bet comparison work package, and cited public engineering references. It does not authenticate private A0 source, select a persistence architecture, authorize protected-IP publication, or establish runtime conformance.

## 1. Purpose and governing rule

This record converts the available engineering research into a sequenced path for DingoOS work in Side-bet. It continues the reverse-engineered canonical working baseline held in the in-bot Library/archive. That baseline is a valid working reference for reconciliation and further engineering; it is not the same thing as authenticated original private source. A0 remains UNRETRIEVED, and its prior access failure is not evidence of deletion.

Governing method:

**Recover → Reconcile → Research → Prepare remediation → Verify and preserve.**

The governing principle remains: **Recover what existed, establish what is true, derive what follows, and only then claim what is new.**

This document is a research-to-engineering plan, not permission to bypass source recovery or implement a speculative architecture.

## 2. Current verified programme position

### 2.1 Workspace and governance

- Side-bet is the designated primary DingoOS engineering workspace under the adopted workspace mandate.
- This repository is public. Only public-safe derived engineering material may be committed. Protected original IP, confidential BIF material, credentials, secrets and private source must not be published.
- The working branch is `dingoos/recovery-engine-adopted-requirements`. This record does not merge it to `main`.
- Adopted Recovery Engine requirements RE-001 through RE-005 remain requirements/adoption status only; adoption is not implementation or verification.
- Consequential dispatch remains **HOLD / NO-GO** until actual target-side enforcement and the required evidence are established.

### 2.2 Architecture comparison

- WLC-001 is frozen as the common deterministic workload.
- Centralized modular, federated process-isolated surrogate, and local-first hybrid remain comparison candidates; no architecture is selected.
- The federated prototype is a single-host process-isolated surrogate, not a production distributed system.
- FT-02 has a bounded prototype subset; FT-03 has a bounded abstract partition-model subset.
- The FT-03 model's six tests and the existing seven topology tests were CI-verified in the documented run. This does not establish actual network partition, durable replicas, restart recovery or full FT-03 acceptance.
- Gates A–E remain unestablished. FT-01, FT-04 and FT-12 remain unrun in the relevant full acceptance sense. Performance acceptance remains open; thresholds must not be invented.

Controlling current comparison records:
- `DINGOOS-HYB-COMP-001 Rev1.3`
- `DINGOOS-HYB-COMP-002 Rev0.4`
- `DINGOOS-HYB-COMP-003 Rev0.2`
- `DINGOOS-HYB-COMP-004 Rev0.3`
- `WLC-001-FROZEN-Rev0.2.json`

### 2.3 Recovered lifecycle and provenance boundary

Historical and reconstructed records describe a multi-record research lifecycle spanning resource allocation/reservation, experiment creation, raw observations, analysis, evidence, EPC transitions and EvidenceGraph relationships. Individual atomic appends do not establish lifecycle-wide atomicity. The historical finding is a recovery lead and requirements input, not proof of a defect in the current private branch.

The following source and ownership details remain to be recovered from the reverse-engineered working baseline and reconciled:
- coordinator/orchestrator state transitions and durable checkpoints;
- DDEP command, prepare, dispatch, effect, receipt and recovery paths;
- ResearchLedger event/record append and retrieval paths;
- EPC transition persistence and validation;
- EvidenceGraph relationship writes;
- SEARM lifecycle orchestration and restart/replay behavior;
- provenance envelope, digest, predecessor and receipt-binding call sites;
- transaction scopes, retry keys, idempotency constraints, lock/fence consumption, and recovery semantics.

Do not create a new ledger, coordinator, event store, authority registry, invalidation engine or parallel test suite where an existing owner is authoritative.

## 3. External research findings and engineering consequences

### 3.1 Target-side fencing

A lease or coordinator belief is not sufficient to stop a paused stale worker. A protected resource must enforce an ordering token or equivalent conditional-write rule at the effect boundary. The resource must preserve the accepted high-water mark across restart/restore; an in-memory-only check is not adequate.

**DingoOS consequence:** recover the exact effecting target(s), target mutation functions and fence-consumption points. Map existing AD-01, AD-06 and AD-12 ownership. Verify that revocation and effect commitment have a defined order (AD-02/03). If a target cannot enforce fencing, record the gap and retain HOLD / NO-GO rather than describing coordinator-side checking as target enforcement.

Reference: Rutgers distributed-systems lecture notes on fencing tokens, and NIST SP 800-207's policy-enforcement-point distinction:
- https://people.cs.rutgers.edu/~pxk/assets/files/classes-417-notes/06a-coordination-slides.pdf
- https://csrc.nist.gov/pubs/sp/800/207/final

### 3.2 Idempotent effects and ambiguous outcomes

At-least-once delivery can cause duplicates. A stable operation identity, immutable intent binding, durable outcome record, adequate deduplication retention and downstream propagation are needed. Transport-level duplicate filtering alone is insufficient.

**DingoOS consequence:** preserve AD-04/05/07/08 and exact target receipt ownership. Same identity plus same intent must not create a second effect; same identity plus changed intent must conflict. A timeout after a possible effect must yield UNKNOWN/HOLD and trigger target receipt/state reconciliation—not blind replay.

Reference:
- https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer

### 3.3 Transactional outbox and cross-boundary publication

A transactional outbox can atomically commit a local state change and its publication record when both share one database transaction. Delivery can still be duplicated, so consumers remain idempotent. The outbox does not create a transaction spanning independent services or stores.

**DingoOS consequence:** consider this only if source recovery demonstrates an existing local dual-write boundary. Do not prescribe an outbox before locating the exact database, write owner and publication path. It cannot by itself close the entire SEARM lifecycle consistency gap.

Reference:
- https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html

### 3.4 Saga/orchestration and lifecycle recovery

A saga sequences local transactions and may use forward recovery or compensating actions. It entails intermediate states and consistency anomalies; compensation is not equivalent to erasing an irreversible external effect.

**DingoOS consequence:** classify every lifecycle step as (a) reversible/compensable, (b) safely retryable/idempotent, (c) irreversible, or (d) outcome-ambiguous. Define the recovery action and evidence for each before choosing a saga, durable journal or database transaction strategy. Keep the existing coordinator and SEARM ownership; do not add a competing orchestrator.

References:
- https://learn.microsoft.com/en-us/azure/architecture/patterns/saga
- https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga-patterns.html

### 3.5 Event sourcing and append-only provenance

An append-only event history can support audit, reconstruction and projections. Full event sourcing adds material trade-offs in concurrency, event schema evolution, replay, snapshots, retention, ordering and external side effects.

**DingoOS consequence:** do not adopt event sourcing wholesale or create another event store. First recover ResearchLedger, ProvenanceEvent/ProvenanceRecord and EvidenceGraph semantics and determine which existing component is authoritative for each fact. Distinguish event history from current projection, evidence qualification, authorization and external-effect receipt.

References:
- https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
- https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/event-sourcing-pattern.html

### 3.6 Systems engineering traceability

Requirements management should retain source/owner, bidirectional traceability, change control and verification/validation evidence. Derived requirements must be labelled as derived rather than silently promoted to owner requirements.

**DingoOS consequence:** retain RE-001…RE-005, NCP-03 integration and the existing FT/SEARM/PROV/AD/C test ownership. Each implementation change must trace to a recovered source or an explicitly derived requirement, an existing owner, a test method and recorded evidence.

References:
- https://science.nasa.gov/wp-content/uploads/2023/04/nasa_systems_engineering_handbook_0.pdf
- https://www.nasa.gov/reference/system-engineering-handbook-appendix/

## 4. Recommended engineering path

### Phase 0 — Preserve the current baseline and evidence

1. Keep the current branch and commits traceable; do not merge or overwrite historical records.
2. Preserve the WLC-001, FT-02 and FT-03 evidence artifacts and their exact tested source commit.
3. Maintain the current distinction between reverse-engineered working baseline, historical compilation, generated code, derived reconstruction and authenticated original.
4. Continue public-release review for every Side-bet addition.

**Exit evidence:** exact branch/head, artifact inventory, provenance labels and CI evidence are recorded.

### Phase 1 — Recover and reconcile existing lifecycle source (immediate next phase)

1. Search the in-bot Library for the reverse-engineered canonical working baseline, lifecycle source maps, DDEP records, provenance records and coordinator/persistence implementations.
2. Inventory the actual modules, symbols, schemas, mutation functions and call sites for coordinator, DDEP, ResearchLedger, EPC, EvidenceGraph, SEARM and provenance.
3. Map every write boundary: initiating command, owner, transaction scope, durable commit point, event/receipt, retry identity, recovery path and downstream consumers.
4. Reconcile historical source-bearing compilations and PR/commit leads against the working baseline without silently merging mixed revisions.
5. Record missing source as UNRETRIEVED and preserve contradictions rather than filling gaps by inference.

**Exit evidence:** a source-boundary and ownership matrix with file/symbol/call-site references, lineage, confidence, unresolved contradictions and explicit negative-search coverage.

### Phase 2 — Derive lifecycle invariants and crash matrix

1. Map each lifecycle step to the existing owner and state object.
2. Identify crash points before write, during write, after durable write but before acknowledgement, after acknowledgement but before downstream publication, and during replay/restart.
3. Classify each operation as retryable, idempotent, compensable, irreversible or ambiguous.
4. Define required recovery outcomes: resume, deduplicate, compensate, quarantine, reconcile, or UNKNOWN/HOLD.
5. Link each case to existing SEARM-FI-01…18, PROV-FI-01…10, AD-01…12, FT-01…16 and C-01…19. Preserve ownership; do not invent replacement IDs.

**Exit evidence:** source-backed crash-point matrix and traceability review; no persistence mechanism selected without owner and transaction evidence.

### Phase 3 — Execute FT-01 against the recovered seam

Only after Phases 1–2:
1. Use the existing coordinator and persistence owners.
2. Inject process termination at recovered durable boundaries.
3. Restart and replay using actual state and receipts.
4. Assert no committed work loss, no duplicate effect, no fabricated success, and preserved provenance/lineage.
5. Capture exact source SHA, environment, command, raw logs, artifacts and independent review.

**Exit evidence:** FT-01 result is bounded to the actual tested implementation and exact revision. If source or target boundaries remain unverified, FT-01 remains blocked.

### Phase 4 — Continue existing fault sequence

- **FT-04:** duplicate result delivery and idempotent ingestion, after source identity and ingestion owner are known.
- **FT-12:** overload/backpressure, after retry, queue, admission and resource ownership are recovered.
- **FT-03 extension:** replace the abstract model with actual process/network partition, durable branch state, restart/reconnect and conflict-reconciliation tests only after canonical version/lineage types are found.
- Continue applicable AD, PROV-FI, SEARM-FI and cross-track C cases under their existing owners.

### Phase 5 — Architecture and persistence decision

Compare centralized modular, local-first hybrid and federated variants only at comparable implementation fidelity. Use the same frozen workload, fault suite, resource envelope and measurement method. Measure latency distributions, throughput, recovery time, event loss, duplicate effects, resource use, reconciliation burden, fault containment, evidence integrity and authority safety.

Do not choose an architecture based on preference, benchmark speed alone, or the abstract FT-03 model. Do not invent numerical thresholds. Hard gates A–E remain mandatory.

### Phase 6 — Controlled implementation and preservation

Only after source reconciliation, explicit owner decision and acceptance criteria:
- modify the existing mechanism at the smallest responsible boundary;
- preserve prior source and revisions;
- add tests under existing IDs/owners;
- run CI against an exact pinned commit;
- inspect raw logs and artifacts;
- update the architecture and engineering records with measured results and remaining limits.

## 5. Immediate work package and status

| Work item | Current disposition | Next action |
|---|---|---|
| Reverse-engineered canonical working baseline | Exists in Library; working reference | Continue retrieval and source mapping |
| Authenticated private A0 source | UNRETRIEVED | Await changed access or authorized export; not a blocker to parallel reconstruction |
| Coordinator/persistence write map | INCOMPLETE / UNRETRIEVED | Recover source, symbols and call sites |
| DDEP target-side fence and receipts | Requirements/research exist; implementation not established | Recover actual effecting targets and fence/receipt consumption |
| Lifecycle-wide persistence semantics | Historical gap recovered; current implementation not verified | Map all writes and transaction boundaries |
| FT-01 | BLOCKED / NOT RUN | Wait for source-boundary map and crash matrix |
| FT-04 | NOT RUN | Follow FT-01 and recover ingestion idempotency owner |
| FT-12 | NOT RUN | Recover admission/backpressure/retry boundaries |
| FT-03 | Bounded model subset CI-verified; full acceptance NOT ESTABLISHED | Plan real process/network and durable-recovery extension |
| Architecture selection | NOT MADE | Compare only after equivalent implementation and evidence |
| Consequential dispatch | HOLD / NO-GO | Maintain until target-side enforcement and verification pass |

## 6. Existing test and requirement ownership

Preserve, do not duplicate:
- RE-001…RE-005 — recovery-engine requirements.
- NCP-03 — existing dependency and invalidation semantics; reconcile revisions before integration.
- FT-01…FT-16 — architecture fault scenarios.
- SEARM-FI-01…SEARM-FI-18 — lifecycle persistence/recovery.
- PROV-FI-01…PROV-FI-10 — provenance/evidence integrity.
- AD-01…AD-12 — authority, fencing, revocation, idempotency, receipts and recovery.
- C-01…C-19 — cross-track qualification, correction and reopening.

## 7. Conversation and archive traceability

This record consolidates the relevant engineering decisions and evidence available to this turn. It is not a verbatim export of the complete ChatGPT account history. The following recovered project records provide the traceable continuity spine:

- `DINGOOS-PRE-RESTORATION-INSPECTION-001 Rev0.1` — in-bot Library as persistent working home; reverse-engineered reconstruction; source/provenance controls; recovery sequence.
- `DINGOOS-RECONCILED-BASELINE-001 Rev0.3` — reconciliation snapshot and source-incomplete status.
- `DINGOOS-GOV-RECON-001 Rev0.5` — lifecycle persistence alternatives and SEARM-FI ownership.
- `DINGOOS-PROVENANCE-RECON-002 Rev0.4` — lifecycle-wide non-atomicity finding, historical source leads and provenance boundary.
- `DINGOOS-SEARM-RECOVERY-ANALYSIS-001 Rev0.1` — derived lifecycle recovery invariants and source-inspection questions.
- `DINGOOS-TEST-FAMILY-RECON-001 Rev0.1` — existing test-family ownership.
- `DINGOOS-CROSS-TRACK-HANDOFF-001 Rev0.1` — Track A/B/C responsibility boundaries.
- `ADOPTED-RECOVERY-ENGINE-REQUIREMENTS.md` — RE-001…RE-005.
- `GOVERNING-WORKSPACE-MANDATE.md` — Side-bet programme scope and public-source boundary.
- `DINGOOS-HYB-COMP-001 Rev1.3` and `DINGOOS-HYB-COMP-004 Rev0.3` — current comparison plan and bounded FT-03 evidence.

Earlier conversation turns, source artifacts and Library records not represented in this list remain subject to recovery and reconciliation. This document does not claim exhaustive chat-history capture.

## 8. Risks and decision controls

1. **False canonicalization:** prevent mixed historical snippets from being promoted to one canonical revision.
2. **False atomicity:** do not infer lifecycle atomicity from local append atomicity.
3. **Coordinator-only fencing:** do not claim target enforcement unless the effecting resource consumes and persists the fence.
4. **Blind retry:** UNKNOWN after possible effect must be reconciled against target evidence.
5. **Duplicate architecture:** complete existing mechanisms and ownership before proposing new components.
6. **Overclaiming tests:** distinguish unit/model/CI evidence from integration, distributed-runtime and physical validation.
7. **Public disclosure:** do not publish protected BIF/IP, secrets, private source or private conversation content.

## 9. Change history

- **Rev0.1 — 27 November 2026:** Initial research synthesis and evidence-led engineering path. No runtime source modified; no architecture or persistence mechanism selected; no new fault-test ownership created; no consequential dispatch authorization granted.
