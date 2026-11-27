# DINGOOS Recovery Engine — Adopted Engineering Requirements

- Programme: DingoOS engineering within Side-bet
- Requirement set: RE-001 through RE-005
- Status: **ADOPTED — BINDING ENGINEERING REQUIREMENTS**
- Implementation status: **NOT YET IMPLEMENTED OR VERIFIED**
- Approval basis: User confirmation in the active engineering conversation, 27 November 2026
- Repository: `barnardphillip07-bot/Side-bet`
- Branch: `dingoos/recovery-engine-adopted-requirements`
- Relationship: Subordinate implementation requirements for DINGOOS-EMM-ADD-001 Rev0.2; compatible with, and not a replacement for, existing NCP-03 governance.
- Provenance: Requirements originate as engineering derivations from the Rev0.2 recovery controls and the five innovations explicitly supplied and approved by the user. Their derived origin does not make their adopted status provisional.

## 1. Governing disposition

The five requirements in this document are adopted and binding on DingoOS recovery-engine design, implementation, review and operation in Side-bet.

Do not label these five requirements "proposed", "unadopted" or optional. Do not defer their application merely because the automation has not yet been implemented.

Keep requirement adoption distinct from implementation evidence:
- **ADOPTED** means the engineering requirement governs work.
- **NOT IMPLEMENTED** means no implementation has yet been established by inspected repository evidence.
- **IMPLEMENTED — UNVERIFIED** means code exists but has not passed its defined verification.
- **VERIFIED** requires reproducible test evidence and independent review appropriate to the claim.

No document, report or session may imply that adoption proves implementation or successful enforcement.

## 2. RE-001 — Search coverage receipts and negative-claim gate

Every negative source-recovery claim must be supported by a machine-readable `SEARCH_COVERAGE_RECEIPT`.

The receipt must record, at minimum:
- receipt schema/version and unique receipt identity;
- search objective, exact query/target identifiers and claim being evaluated;
- enumerated surfaces and exact scope boundaries, including Library root, nested directories, conversation-history scope, archive files and manifests, repository names/refs/commits, and other relevant connected sources;
- per-surface enumeration method, tool/connector identity and version where available, timestamps, pagination/completion state, errors and inspected/uninspected status;
- Pass 1 root inventory and Pass 2 deep inventory, with deterministic inventory serialization and SHA-256 digests;
- file/entry identity, path, size, content hash where content was read, and whether embedded content was inspected;
- `omitted_surfaces`, inaccessible surfaces, permission failures, unresolved pagination, excluded paths and other coverage limitations;
- discovered evidence references and the exact subset to which the conclusion applies.

A digest establishes integrity of the recorded inventory; it does not by itself establish that the inventory is complete or that a surface was actually inspected.

The system must enforce:
- If any relevant surface is omitted, inaccessible, not inspected, incompletely paginated or not verifiably enumerated, the strongest permitted conclusion is scoped, such as `UNRETRIEVED_WITHIN_SCOPED_SUBSET`, `INACCESSIBLE`, `NOT_INSPECTED` or `UNRESOLVED`.
- `UNRETRIEVED_GLOBALLY` is prohibited unless the declared search universe is explicitly bounded, all required surfaces are successfully enumerated and inspected, all pagination is complete, all archive entries and embedded-source candidates are accounted for, and independent coverage validation passes.
- Empty `omitted_surfaces` alone is not sufficient to authorize a global negative claim.
- A receipt must never be fabricated retrospectively to justify a conclusion already written.

## 3. RE-002 — Content-addressable source-bearing artifact index

Index source-bearing content by content and structure, not filename extension alone.

The indexer must inspect:
- ordinary source files and structured data;
- Markdown and text files, including fenced code blocks and embedded snippets;
- ZIP and other supported archive manifests and every enumerated entry;
- Python definitions/classes and AST signatures where parsing succeeds;
- TLA+ module headers and declarations where applicable;
- JSON structures and keys, using deterministic canonicalization where a canonical JSON digest is required.

For each discovered source-bearing region or symbol, record:
- immutable parent artifact identity and exact path/archive-entry path;
- byte-offset start/end against the original byte sequence;
- content SHA-256;
- parser/grammar and indexer version;
- symbol kind and exact identifier/signature;
- extraction status, parse errors and confidence/limitations;
- links to the original artifact and relevant coverage receipt.

Tag applicable artifacts with `CONTAINS_EMBEDDED_SOURCE`. A parser failure or unsupported language must produce an explicit incomplete/unsupported result, never a claim that the artifact contains no source.

The index must be reproducible from the same input bytes and declared toolchain.

## 4. RE-003 — Immutable lineage graph and non-merging structural diff

Every recovered source fragment must be represented as an immutable provenance node using one of these tiers:

1. `AUTHENTICATED_CANONICAL`
2. `REVERSE_ENGINEERED_BASELINE`
3. `HISTORICAL_COMPILATION`
4. `GENERATED_SOURCE`
5. `PARTIAL_EXCERPT`
6. `DERIVED_RECONSTRUCTION`

Each node must preserve source identity, byte hash, retrieval location, revision/commit where known, retrieval status, provenance evidence, and limitations. Tier assignment must be evidence-based; unknown provenance must remain unknown rather than being promoted.

Perform pairwise structural comparisons without mutating or merging source nodes. Reports must distinguish:
- symbols/blocks present only in A;
- symbols/blocks present only in B;
- matching structures;
- conflicting signatures or semantics;
- unresolved/unsupported comparisons.

Automated or manual synthesis is permitted only as a new `DERIVED_RECONSTRUCTION` node with explicit attribution edges to every contributing source node, transformation description, author/tool identity, and reproducible derivation record. Never represent a composite as an existing canonical or historical file.

## 5. RE-004 — Definition-to-effecting-target reachability and bypass audit

A recovered function definition does not prove that it is enforced on every consequential execution path.

For each guard, authorization check, admission decision or other control claimed to protect a consequential effect, produce a trace record containing:
- exact definition identity, file, line range, source hash and symbol signature;
- all discovered direct and indirect call-sites, callers and invocation contexts;
- external ingress and dispatch entry points;
- dynamic dispatch, reflection, plugin, callback, import, native/external and configuration-driven boundaries;
- effecting target identity and exact mutation/commit operation;
- path analysis, bypass-path findings and uninspected dependencies;
- analysis tool/version and limitations.

The `effecting_target_bound` result is three-valued:
- `TRUE` only when the inspected execution boundary is demonstrably closed and every relevant ingress-to-effect path is shown to pass through the required enforcement point;
- `FALSE` when a bypass path is established;
- `UNVERIFIED` whenever dynamic behavior, missing source, uninspected dependencies, external dispatch or analysis limitations prevent a complete proof.

Static call-graph reachability alone must never be presented as proof of runtime enforcement. A local ledger write, signature check or preflight check is not target-side enforcement unless the actual effecting target consumes and enforces the required authority/fence at commitment.

## 6. RE-005 — Coverage-triggered dependency reassessment through NCP-03

Search receipts, source nodes, lineage comparisons, call-graph results and derived audit claims must be represented as evidence/dependency inputs to the existing NCP-03 governance and invalidation model.

When a newly discovered root-level artifact, nested file, archive entry, repository ref or conversation record changes the relevant inventory or lineage:
- identify prior receipts and claims whose declared scope, inventory digest, omitted surfaces or evidence dependencies are affected;
- mark affected conclusions `DEPENDENCY_SUPERSEDED` or the exact applicable existing NCP-03 invalidation state;
- schedule or require reassessment of affected downstream claims;
- preserve prior records, hashes and decisions as immutable history;
- record the trigger, dependency path, invalidation reason, reassessment result and new evidence links.

Do not create a parallel invalidation engine or invent competing canonical NCP-03 edge/state semantics. Before implementation, reconcile the applicable NCP-03 revisions and establish the authoritative schema, transition rules and test ownership. Where NCP-03 authority is unresolved, record the integration as blocked/unverified rather than guessing.

## 7. Cross-cutting implementation and safety constraints

- Search all relevant surfaces before concluding that source is missing. A folder-only search is never a global search.
- Preserve recovered originals byte-for-byte. Indexing and analysis must not modify source artifacts.
- Never combine unrelated historical revisions into a fictitious canonical baseline.
- Do not infer a private repository's contents from a 404, an inaccessible ref or a similarly named public repository.
- Do not publish protected original IP, confidential BIF material, credentials, secrets or private user data into this public repository. Store only material authorized for public release; use redacted provenance references where needed.
- Preserve existing DingoOS test ownership and identifiers. Do not create a parallel test suite where existing owners apply.
- Do not claim tests, execution, repository mutations or enforcement succeeded unless the operation was actually performed and its result inspected.
- All negative claims must link to their coverage receipt. All source-derived claims must link to immutable source nodes and exact byte/line ranges where available.
- If a required tool, source surface or analysis capability is unavailable, state the limitation and narrow the claim.

## 8. Adoption and implementation gates

The requirements are adopted now. Implementation proceeds in controlled increments:

1. Define and validate versioned schemas for receipts, artifact index records, provenance nodes, structural-diff reports and reachability reports.
2. Reconcile NCP-03 authority and dependency semantics before wiring invalidation.
3. Build deterministic indexing and receipt generation with fixtures for root-level omissions, nested files, archives, embedded code, inaccessible surfaces and incomplete pagination.
4. Build non-merging lineage comparisons with adversarial fixtures for conflicting revisions and attempted silent synthesis.
5. Build call-graph/bypass analysis with dynamic-dispatch and missing-dependency cases that must return `UNVERIFIED`.
6. Integrate dependency-triggered reassessment through the established NCP-03 mechanism.
7. Require reproducible tests, independent review and evidence-backed status transitions before marking any implementation `VERIFIED`.

Until those gates pass, the five requirements remain **ADOPTED — BINDING**, while their software implementation remains **NOT YET IMPLEMENTED OR VERIFIED**.

## 9. Change control

- Initial requirement adoption: 2026-11-27.
- Source of authority: explicit user approval in the active conversation.
- This document does not amend or authenticate the private original Universal Engineering Methods Manual.
- This document does not assert that the private `phillipbarnard07-cell/DingoOS` repository has been accessed.
- Changes to these requirements require a traceable revision and must preserve prior versions and decision history.
