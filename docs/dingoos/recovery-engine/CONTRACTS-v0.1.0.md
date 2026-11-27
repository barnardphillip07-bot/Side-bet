# Recovery-engine contracts v0.1.0 — implementation notes

Status: **ADOPTED REQUIREMENTS; CONTRACT DRAFT FOR IMPLEMENTATION; NOT YET IMPLEMENTED OR VERIFIED**

This directory contains the first machine-readable contract set for RE-001 through RE-004. The contracts are versioned independently from the EMM addendum. They do not by themselves constitute an executable recovery engine.

## Contract files

- `schemas/search-coverage-receipt.schema.json` — RE-001.
- `schemas/source-artifact-index-record.schema.json` — RE-002.
- `schemas/source-lineage-node.schema.json` — RE-003 provenance nodes.
- `schemas/lineage-diff-report.schema.json` — RE-003 pairwise comparison.
- `schemas/effecting-target-reachability.schema.json` — RE-004.

RE-005 is intentionally not assigned a new competing schema. Its integration must use the authoritative NCP-03 dependency and invalidation model after revision reconciliation.

## Deterministic inventory digest profile

For `pass_1_root_inventory.sha256` and `pass_2_deep_inventory.sha256`:

1. Construct the complete `entries` array for the declared pass.
2. Normalize each path to a repository/source-native relative path representation; do not silently rewrite case or Unicode normalization.
3. Sort entries by the UTF-8 byte sequence of `path`; reject duplicate path identities within the same inventory.
4. Serialize the entries array using RFC 8785 JSON Canonicalization Scheme (JCS), UTF-8, with no BOM and no trailing newline.
5. Compute SHA-256 over those exact bytes and encode as 64 lowercase hexadecimal characters.
6. Store the resulting digest in the inventory's `sha256` field. The digest does not include the `sha256` field itself, the receipt metadata, or an assertion of completeness.

The inventory must retain all entries and their states. Do not omit inaccessible, excluded, failed or uninspected entries from the inventory merely to obtain a clean digest.

A receipt is a signed/attested statement only if a separate, explicitly specified identity/signature mechanism is implemented. These v0.1.0 schemas do not claim authenticity or non-repudiation.

## Source byte ranges

- `byte_offset_start` is zero-based and inclusive.
- `byte_offset_end` is zero-based and exclusive.
- `content_sha256` is SHA-256 of the exact original byte slice `[start:end]`.
- Line numbers, when available, are one-based. They are supplementary and do not replace byte offsets.
- Archive-entry offsets refer to the uncompressed entry byte stream unless the record explicitly identifies another byte domain.

Never calculate offsets against decoded/reformatted text and then represent them as offsets into original bytes.

## Lineage invariants

- Source nodes are immutable records. Corrections create a new node/revision; they do not rewrite the old node.
- A `DERIVED_RECONSTRUCTION` must have at least one explicit attribution edge. The schema enforces this.
- Pairwise comparison reports are non-merging; `merge_performed` is constrained to false.
- A diff is not a semantic equivalence proof. Tool, parser, grammar, unsupported constructs and limitations must remain visible.
- A source tier is a provenance assertion and must be justified by the evidence recorded on the node.

## Reachability invariants

- `TRUE` is a closed-world result, not a confidence score. The schema requires a closed-world assumption, no uninspected dependencies, no recorded dynamic boundaries and no known bypass paths.
- `FALSE` requires at least one identified bypass path.
- Any incomplete source set, dynamic dispatch boundary, unresolved plugin/callback path or external target behavior requires `UNVERIFIED`.
- Passing schema validation is necessary but not sufficient for `TRUE`; independent review and runtime/target-side evidence are still required.

## Global negative-claim invariant

The search-receipt schema constrains `UNRETRIEVED_GLOBALLY` to require:
- complete coverage assessment;
- zero omitted surfaces;
- every declared surface completely enumerated and inspected, with pagination complete or not applicable;
- independent coverage validation marked passed.

These structural conditions are necessary, not sufficient. The declared search universe must itself be justified, and the independent validator must assess the actual coverage process. Empty omission lists cannot prove that the declared universe was adequate.

## Validation status and next implementation tasks

The five schemas were read back from the exact Side-bet branch, parsed as JSON, and passed Draft 2020-12 meta-schema checks in CI using the pinned validator. The source indexer v0.1.0 is implemented for Python, fenced/unfenced mixed text, JSON, TLA+ headers and ZIP members, with exact byte offsets and explicit partial/unsupported states. The latest CI run completed successfully: 25 passed, including schema meta-validation, coverage receipt integrity, embedded-source index records, lineage nodes, non-merging diff and indexer fixture tests. This is a verified contract/indexer fixture increment, not verification of a complete recovery engine or a complete Library scan. No automated call-graph tracer or NCP-03 invalidation worker has been implemented.

Next:
1. Expand tests for byte-range semantics, UTF-16 key-order edge cases, invalid Unicode, duplicate paths and resource-limit exhaustion.
2. Run the implemented indexer on selected authorized DingoOS source-bearing artifacts and ZIP archives; compare generated records against manual byte-indexed references before scaling to the Library.
3. Expand the indexer for additional source formats only when a parser/grammar and exact-offset tests are available; preserve immutable source records.
4. Add definition-to-effecting-target analysis with dynamic dispatch and incomplete source forced to UNVERIFIED.
5. Reconcile NCP-03 state/edge semantics before implementing RE-005; see `NCP03-RE005-INTEGRATION-BOUNDARY.md`.
6. Generate further receipts only from actual enumerations and inspections; never synthesize historical receipts.
