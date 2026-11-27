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

At this point, the JSON documents have been written to the Side-bet branch and read-back validation is still required. No runtime validator, indexer, AST parser, graph tracer, invalidation worker or automated test has been implemented by these schema files alone.

Next:
1. Read back all five schemas from the exact branch and parse each as JSON.
2. Validate each against a Draft 2020-12 meta-schema using a pinned validator version.
3. Add positive and negative fixtures, including forbidden global-negative claims, incomplete pagination, derived nodes without attribution, and `TRUE` reachability with dynamic/uninspected paths.
4. Preserve existing test ownership when mapping these fixtures into the established DingoOS test architecture.
5. Reconcile NCP-03 before implementing RE-005.
