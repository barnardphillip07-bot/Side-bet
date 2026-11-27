# DINGOOS-SOURCE-RECOVERY-001 — Library Inventory and Embedded Source Findings

- Revision: 0.1
- Date: 27 November 2026 (Australia/Melbourne)
- Workspace: `barnardphillip07-bot/Side-bet`
- Branch: `dingoos/recovery-engine-adopted-requirements`
- Status: **PARTIAL SOURCE RECOVERY — INVENTORY RECEIPT CREATED — DEEP RECOVERY CONTINUES**
- Governing controls: EMM-ADD-001 Rev0.2 recovery controls; adopted RE-001 through RE-005.

## 1. Scope and non-claims

This record captures the first complete paginated metadata inventory of the ChatGPT Library root and the first byte-accurate indexing of source-bearing regions in `Pasted text(7).txt`.

It is not a global source-absence declaration, a complete DingoOS source migration, a canonical source authentication, or a DDEP implementation recovery. The user's reverse-engineered canonical DingoOS working baseline remains a distinct source-lineage target; the indexed compilation's relationship to that baseline has not yet been established.

## 2. Pass 1 — recursive Library-root inventory

The Library root was enumerated recursively with pagination to `next_cursor = null`.

| Measure | Observed |
|---|---:|
| Pages returned | 7 |
| Total items | 653 |
| Files | 594 |
| Folders | 59 |
| Listing warnings | 0 |

The inventory includes root-level files and nested DingoOS and encyclopaedia directories. It therefore corrects the earlier narrow-folder search failure.

**Coverage receipt:**  
`docs/dingoos/recovery-engine/evidence/receipts/SEARCH-COVERAGE-DINGOOS-LIBRARY-ROOT-20261127.json`

- Pass 1 inventory SHA-256: `fe2eca400d3392c117f3abf5ae4a1cb60f3d333579f6ecf04d9363e6baae32e5`
- Initial Pass 2 metadata inventory SHA-256: `e528226687e7138581ba63dcfbc2f44fa89a4e84e5f9d98cb3026f36bba7fcd5`  \n- Updated Pass 2 inventory SHA-256: `593ac5db4dae3d455a716320971328171b550d352edeca837848cd398aec45e9`
- Receipt conclusion: `UNRESOLVED`
- Coverage assessment: `incomplete`

The receipt explicitly records uninspected archives, incomplete conversation-history enumeration, incomplete GitHub ref enumeration, the inaccessible private repository and the absence of deep content inspection across the Library. It does not claim `UNRETRIEVED_GLOBALLY`.

## 3. Source-bearing artifact recovered and hashed

**Artifact:** `/Pasted text(7).txt`  
**Library file ID:** `file_00000000f90c81fa88a3b0980b5d9d69`  
**Size:** 133,685 bytes  
**Lines:** 2,778  
**Whole-file SHA-256:** `548a7a5595bd5d81863fbc8815e45e0b0423c51712883b585135cfea3d369752`

Classification: **HISTORICAL COMPILATION CONTAINING EMBEDDED SOURCE**.

The artifact contains CSRE1/CSRE2 master-reference material, Python-like source fragments, API/gateway definitions, Horizon caller methods, mathematics and knowledge-graph components, provenance/ledger material, digital-twin and other subsystem fragments.

The compilation contains repeated and differing versions of some definitions. It is preserved as one parent source artifact with separate excerpt nodes. No variants have been merged.

### 3.1 Exact API gateway source occurrences

| Variant | Source lines | Byte range (start inclusive, end exclusive) | Region SHA-256 |
|---|---:|---:|---|
| Gateway A | 223–271 | `[15512:17463]` | `4cd0929bc041c17e82fee8aba3a387e98f26d0c54492fb0bf3fb39972a727173` |
| Gateway B | 1559–1614 | `[88535:90627]` | `596568aeffced29b0664627ef2fad0e6acf9d4558207fb40ca561b6bb4cd4f1d` |

Both contain:
- `APIRequest`
- `APIResponse`
- `DingoOSGateway`
- `DingoOSGateway.dispatch(request)`

The actual dispatch branches shown in both excerpts are:

1. `SUBMIT_RESONANCE_HYPOTHESIS` — calls `self.c3po.propose_resonance_claim(...)`, stores the claim in an in-memory dictionary and returns a success response.
2. `RUN_VERIFICATION` — looks up the claim in an in-memory dictionary, calls `self.c4po.verify_resonance_evidence(...)`, stores evidence in an in-memory dictionary and returns a success response.
3. Unknown actions return an error response.

### 3.2 Exact caller regions

| Caller | Source lines | Byte range | Region SHA-256 |
|---|---:|---:|---|
| `HorizonDashboard` | 1617–1656 | `[90922:92466]` | `84f772f9717bf7ec63a9b0dca53ecf23af38be78fc354da372922d1d24846a85` |
| `main.py` orchestration excerpt | 1659–1685 | `[92743:93802]` | `35aa9263150b129cef76d1a9d5c5cb30aa82404d67ef45900bdc24fb1bb96ad3` |

Call sequence recorded in the compilation:

```text
main()
  -> DingoOSGateway(c3po_agent, c4po_agent)
  -> HorizonDashboard(gateway)
  -> HorizonDashboard.render_claim_submission()
       -> gateway.dispatch(SUBMIT_RESONANCE_HYPOTHESIS)
            -> C3POAgent.propose_resonance_claim()
  -> HorizonDashboard.render_verification_results()
       -> gateway.dispatch(RUN_VERIFICATION)
            -> C4POAgent.verify_resonance_evidence()
```

This is a recovered CSRE claim/verification path. It is not a DDEP consequential target operation.

### 3.3 Repeated EvolutionLedger fragments

Two exact occurrences were indexed separately:

- Lines 202–216, bytes `[14712:15318]`.
- Lines 459–473, bytes `[31853:32459]`.

Both have SHA-256 `038408f892423f35c8888af99c07177a17e088d9f0ac7838fd647090e10ccb2c`.

The fragment defines `EvolutionLedger.log_transition()` and `get_lineage()`, with an in-memory `history` list. This is not evidence of a durable DDEP target receipt store or distributed commit boundary.

## 4. Non-merging lineage comparison

The two API gateway variants conflict in exact identifiers and response serialization:

| Concern | Gateway A | Gateway B |
|---|---|---|
| Claim dictionary key | `claim.id` | `claim.claim_id` |
| Evidence dictionary key | `evidence.id` | `evidence.evidence_id` |
| Claim status in response | `claim.epistemic_status.value` | `claim.epistemic_status` |
| Action examples | No inline examples | `SUBMIT_CLAIM`, `EXECUTE_VERIFICATION`, `FETCH_LINEAGE` |

Both actual dispatch excerpts implement `SUBMIT_RESONANCE_HYPOTHESIS` and `RUN_VERIFICATION`; no `FETCH_LINEAGE` handler appears in the indexed dispatch method.

The Horizon caller reads `claim_data["claim_id"]`, while Gateway A uses `claim.id` internally. Whether model serialization aliases reconcile this difference is not established by the excerpt. Gateway B uses `claim.claim_id`, but its exact model revision is also not authenticated.

The main orchestration excerpt imports C3PO/C4PO from a test module, and contains a non-standard `if name == "main"` guard. The complete compilation has not been AST-parsed or executed as a clean source tree. These are unresolved source-quality and version-lineage findings, not proof of which variant is authoritative.

**Diff report:**  
`docs/dingoos/recovery-engine/index/diffs/DIFF-P7-API-GATEWAY-A-VS-B.json`

`merge_performed = false`. No composite gateway implementation was created.

## 5. Indexed provenance records

Parent node:

`SRC-P7-HISTORICAL-COMPILATION-001`

Excerpt nodes:
- `SRC-P7-API-GATEWAY-A`
- `SRC-P7-API-GATEWAY-B`
- `SRC-P7-HORIZON-CALLERS`
- `SRC-P7-MAIN-CALLSITE`
- `SRC-P7-EVOLUTION-A`
- `SRC-P7-EVOLUTION-B`

Each excerpt has an immutable source hash, exact byte offsets, line range and an explicit `excerpted_from` attribution edge to the parent. The index records are under:

`docs/dingoos/recovery-engine/index/source-artifacts/`

Lineage nodes are under:

`docs/dingoos/recovery-engine/index/lineage/`

## 6. DDEP / PR #76 recovery findings

The source-bearing compilation above contains no occurrences of:
- `DDEP`
- `DispatchOutcome`
- `ddep_resource_guard`
- `DDEPResearchRuntime`
- `DDEP_ADMISSION_DECISION_V1`

It therefore does not provide the DDEP fence-v1 operation definitions or their actual target call-sites.

Historical PR #76 recovery records identify these source-path leads:

| Historical path | Historical role |
|---|---|
| `core/ddep_resource_guard.py` | Resource admission / guard |
| `core/ddep_authoritative_adapters.py` | Signed authority/resource adapter ports |
| `core/workflow_execution_processor.py` | Workflow execution processor |
| `core/provenance_adapter.py` | Provenance handoff |
| `docs/runtime/DDEP_RESOURCE_ADMISSION_GUARD_V1.0.md` | Guard contract |
| `docs/runtime/DDEP_AUTHORITATIVE_ADAPTER_CONTRACT_V1.0.md` | Adapter contract |
| `tests/core/test_ddep_resource_guard.py` | Historical guard tests |
| `tests/core/test_ddep_authoritative_adapters.py` | Historical adapter tests |
| `tests/test_workflow_runner_conformance.py` | Historical workflow conformance tests |

These are **historical path leads only**. Their source bytes, exact definitions and call-sites have not been retrieved from the private repository in this pass. Historical PR #76 commit references are not established as a verified linear history or current HEAD.

The public/history records describe `PRE_DISPATCH` and `POST_PREPARED` admission decisions, a local ResearchLedger append-once dispatch claim and a second authoritative check after PREPARED. They explicitly do not establish external revocation serialization, actual target-side enforcement or distributed atomicity.

## 7. Requirements and target-boundary disposition

DINGOOS-DDEP-TARGET-FENCING-001 Rev0.2 is a requirements-level research proposal, not implementation source. It preserves P2-R01 through P2-R12 and existing AD-01…AD-12 ownership.

The source recovery still cannot identify:
- the exact consequential DDEP operation identifiers;
- actual target mutation functions;
- every external ingress and bypass path;
- target-side fence validation/consumption;
- the revocation/effect commit linearization point;
- target receipt persistence and lookup;
- receipt-to-provenance call-sites.

Accordingly, no operation may be marked target-enforced or receipt-recoverable from this evidence. Consequential dispatch remains **HOLD / NO-GO**.

## 8. Existing test ownership

Preserve the existing families:
- AD-01…AD-12 — Track A.
- PROV-FI-01…10 — Track B.
- SEARM-FI-01…18 — lifecycle persistence/recovery.
- C-01…C-19 — cross-track.

The Side-bet recovery-engine contract suite is a separate component suite because no existing recovery-engine test owner was recovered. Its 14 tests passed in CI; this does not execute or replace any of the DDEP test families above.

## 9. NCP-03 boundary

The recovered Library contains NCP-03 Rev0.3 and Rev0.4 local reference designs, both explicitly derived/unadopted, and a Rev0.6 normative specification draft explicitly not specification-locked and carrying no implementation authority.

Rev0.4 records that added dependencies, changed blind-spot digest/status, policy, expiry, revocation or scope changes invalidate prior residual-risk approval. Rev0.6 draft uses `STALE_REVERIFY_REQUIRED` for evaluator/policy/spec changes. These are candidate semantics, not authenticated canonical state-transition rules.

RE-005 remains adopted and binding, but runtime integration is blocked pending recovery of the authoritative NCP-03 state/edge registry and invalidation transitions. See `NCP03-RE005-INTEGRATION-BOUNDARY.md`.

## 10. Verification record

- Whole-file bytes were materialized and SHA-256 computed.
- Six source-bearing regions were byte-indexed and hashed.
- Two gateway variants were compared without merging.
- Parent and excerpt lineage nodes were recorded.
- The updated Library-root receipt remains `UNRESOLVED` / incomplete because only one of 594 files has been materialized and byte-indexed; archive members and complete conversation history have not been inspected.
- Side-bet contract CI: **16 passed**. This validates the recovery-engine schemas, saved inventory receipt, embedded-source index records, lineage nodes and non-merging diff report; it does not execute the DingoOS source compilation or DDEP runtime.
- No DDEP source tests, build, target execution or consequential dispatch were run.

## 11. Next controlled recovery sequence

1. Continue Pass 2 across the highest-value DingoOS source-bearing compilations and archives, preserving exact bytes and lineages.
2. Reconcile the reverse-engineered canonical working baseline's exact parent/source identity against the historical compilations; do not promote this compilation based on its title alone.
3. Recover exact PR #76 source bytes through a changed authorized access route or an owner-provided exact-SHA export; do not repeat the same failed private fetch without a material access change.
4. Once source bytes are recovered, enumerate every DDEP operation definition, caller, target mutation, bypass path, fence consumption and receipt lookup.
5. Map those exact source symbols to the existing AD/PROV-FI/SEARM-FI/C owners. Keep HOLD until target-side enforcement and recovery are demonstrated.

**Governing rule:** Recover what existed, establish what is true, derive what follows, and only then claim what is new.
