# RE-005 / NCP-03 integration boundary and reconciliation

- Record: DINGOOS-RE-RECON-001
- Revision: 0.1
- Status: **RE-005 ADOPTED — NCP-03 INTEGRATION BOUNDARY RECORDED; CANONICAL NCP-03 STATE MAPPING NOT YET ESTABLISHED**
- Workspace: Side-bet
- Date: 2026-11-27

## 1. Purpose

This record prevents the adopted recovery-engine invalidation requirement (RE-005) from accidentally creating a parallel NCP-03 invalidation model or promoting an unadopted NCP-03 candidate into canonical authority.

RE-005 is binding on DingoOS recovery-engine work. Its integration must use the applicable authoritative NCP-03 semantics once those semantics are recovered and reconciled. The existence of derived NCP-03 design records does not itself authorize changes to a canonical NCP-03 implementation.

## 2. Recovered NCP-03 records and their actual disposition

### NCP-03 Design Rev0.3

Library artifact: `NCP-03_DESIGN_REV0.3_DERIVED.md`.

The record describes a local reference design for a Merkle evidence/dependency DAG. It distinguishes structural adjacency completeness from discovery completeness, states that an absent edge is not proof of an absent relationship, and records stale-verdict invalidation when evaluator digest changes. It also explicitly says the PR #76 fixture cannot certify discovery completeness because canonical Git diff inspection, AST/interface checking and target-runtime execution were omitted.

Its own disposition is **DERIVED AND UNADOPTED — LOCAL REFERENCE DESIGN**. It does not amend canonical DingoOS.

### NCP-03 Design Rev0.4

Library artifact: `NCP-03_DESIGN_REV0.4_DERIVED.md`.

Rev0.4 explicitly extends Rev0.3 and preserves Rev0.3 engine, fixture and tests as a compatibility baseline. It says any added dependency, changed blind-spot digest/status, policy change, expiry, revocation or scope change invalidates the prior residual-risk approval and requires reassessment. It also distinguishes structural/lineage edges from scheduling-only `SCHEDULED_AFTER` and `PARALLEL_WITH` edges.

Its own disposition is **DERIVED — UNADOPTED**. Its reported 54 passing local tests are historical candidate evidence, not canonical DingoOS qualification or target enforcement.

### NCP-03 Rev0.6 normative specification draft

Library artifact: `NCP-03_DESIGN_REV0.6_NORMATIVE_SPECIFICATION_DERIVED_DRAFT_Rev0.1.md`.

The draft requires snapshot diff/recovery to preserve historical snapshots, unresolved references, provenance and reasons for changed blocker/standing results. It says evaluator/policy/spec changes invalidate dependent derived verdicts to `STALE_REVERIFY_REQUIRED`, while preserving historical verdicts. It also defines scoped discovery attestations and separate residual-risk approvals.

Its explicit status is **DERIVED — DRAFT; UNADOPTED; NOT SPECIFICATION-LOCKED; NO IMPLEMENTATION AUTHORITY**. It is not authority to implement or declare canonical NCP-03 semantics.

## 3. Exact mapping status

| RE-005 trigger | Recovered NCP-03 evidence | Current integration disposition |
|---|---|---|
| Newly discovered material dependency | Rev0.4 says added dependency invalidates prior residual-risk approval and requires reassessment | Semantic requirement supported in the candidate record; exact canonical event/state schema remains unresolved |
| Changed blind-spot digest/status | Rev0.4 says prior approval is invalidated | Candidate semantic supported; canonical state identifier and transition authority unresolved |
| Policy change | Rev0.4 says prior approval invalidated; Rev0.6 draft uses `STALE_REVERIFY_REQUIRED` for dependent derived verdicts | Candidate semantics recorded; Rev0.6 status prevents promotion to canonical state |
| Expiry or revocation | Rev0.4 says prior approval invalidated | Candidate semantics supported; exact canonical state/event mapping unresolved |
| Scope or closure change | Rev0.4 requires approval to bind exact closure/policy/scope and invalidates on change | Candidate semantics supported; exact canonical graph edge and transition mapping unresolved |
| New root-level source or changed search inventory | RE-001/RE-002 introduce coverage receipts and source index records; NCP-03 Rev0.6 draft requires scoped discovery attestation | Integration mapping required; no existing canonical receipt-to-NCP dependency edge has been authenticated |

## 4. Prohibited assumptions

- Do not introduce `DEPENDENCY_SUPERSEDED` as an NCP-03 state unless an authoritative NCP-03 schema or approved change explicitly defines it. It is not established by the recovered excerpts.
- Do not automatically substitute `STALE_REVERIFY_REQUIRED` for every dependency/approval invalidation. The exact state may depend on the affected object and canonical transition rules.
- Do not treat a Library-derived NCP-03 document as a canonical implementation.
- Do not assume a Merkle inventory or structural graph proves real-world discovery completeness.
- Do not convert missing, inaccessible or unresolved source relationships into `ABSENT`.
- Do not create a second invalidation engine, dependency graph or competing state registry.

## 5. Required closure before RE-005 implementation

1. Recover and hash the exact NCP-03 Rev0.3 and Rev0.4 source bundles, fixtures, schemas and tests—not only narrative design documents.
2. Reconcile Rev0.3/Rev0.4 with Rev0.5 and the Rev0.6 draft, preserving every retained, changed, deferred and retired requirement.
3. Recover the exact current NCP-03 state registry, edge registry, invalidation event definitions, dependency propagation rules and test owners.
4. Establish how RE-001 coverage receipts and RE-002 source-index records enter the NCP-03 evidence/dependency graph, including their provenance and scope.
5. Define deterministic change-impact traversal and immutable historical preservation using existing NCP-03 mechanisms.
6. Map each trigger to existing tests and add only tests assigned to the established owners.
7. Obtain the authority required to implement against the controlling NCP-03 specification.

Until these conditions are met, RE-005 remains **ADOPTED — BINDING**, while its NCP-03 runtime integration remains **BLOCKED — AUTHORITATIVE STATE MAPPING NOT RECOVERED**.

## 6. Evidence references

- Library file: `NCP-03_DESIGN_REV0.3_DERIVED.md` (140 lines).
- Library file: `NCP-03_DESIGN_REV0.4_DERIVED.md` (85 lines).
- Library file: `NCP-03_DESIGN_REV0.6_NORMATIVE_SPECIFICATION_DERIVED_DRAFT_Rev0.1.md` (562 lines).
- Related closure matrix: `NCP-03_REV06_SPECIFICATION_CLOSURE_MATRIX_DERIVED_Rev0.2.md`.

These references identify recovered Library documents; this record does not claim the complete source bundles or canonical implementations have been retrieved.
