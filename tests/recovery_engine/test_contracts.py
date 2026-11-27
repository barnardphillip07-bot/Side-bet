from __future__ import annotations

from copy import deepcopy

import pytest

from dingoos_recovery.contracts import (
    ContractError,
    SCHEMA_FILES,
    canonical_inventory_bytes,
    inventory_sha256,
    load_schema,
    validate_coverage_receipt,
    validate_lineage_node,
    validate_reachability_report,
)


def inventory(entries):
    return {
        "serialization_profile": "RFC8785-JCS-UTF8",
        "entry_count": len(entries),
        "entries": entries,
        "sha256": inventory_sha256(entries),
    }


def receipt(conclusion="NOT_FOUND_WITHIN_SCOPED_SUBSET"):
    entries = [
        {"path": "root.txt", "entry_type": "file", "enumeration_status": "enumerated",
         "size_bytes": 4, "content_sha256": None, "embedded_source_inspected": True,
         "notes": []}
    ]
    return {
        "schema_id": "SEARCH_COVERAGE_RECEIPT",
        "schema_version": "0.1.0",
        "receipt_id": "receipt-test-001",
        "created_at": "2026-11-27T00:00:00Z",
        "search_objective": "Test scoped recovery",
        "claim_scope": {"subject": "test-symbol", "declared_universe": ["test-library-root"]},
        "surfaces": [{
            "surface_id": "library-root", "surface_type": "library_root",
            "locator": "/Library", "enumeration_method": "fixture enumerator",
            "tool_identity": "test", "tool_version": "1",
            "enumerated_at": "2026-11-27T00:00:00Z",
            "enumeration_status": "complete", "inspection_status": "complete",
            "pagination_status": "complete", "entry_count": 1, "errors": [], "notes": []
        }],
        "pass_1_root_inventory": inventory(entries),
        "pass_2_deep_inventory": inventory(entries),
        "omitted_surfaces": [],
        "coverage_assessment": "complete_within_declared_universe",
        "conclusion_scope": conclusion,
        "evidence_refs": [],
        "independent_coverage_validation": {"status": "passed", "method": "independent fixture check",
            "reviewer": "test", "validated_at": "2026-11-27T00:00:00Z", "findings": []}
    }


def test_all_contracts_are_valid_draft_2020_12_schemas():
    assert len(SCHEMA_FILES) == 5
    for schema_id in SCHEMA_FILES:
        schema = load_schema(schema_id)
        assert schema["$schema"].endswith("/2020-12/schema")


def test_inventory_digest_is_order_independent_by_path():
    a = [{"path": "b", "entry_type": "file"}, {"path": "a", "entry_type": "file"}]
    b = list(reversed(a))
    assert canonical_inventory_bytes(a) == canonical_inventory_bytes(b)
    assert inventory_sha256(a) == inventory_sha256(b)


def test_inventory_digest_rejects_duplicate_paths():
    entries = [{"path": "same"}, {"path": "same"}]
    with pytest.raises(ContractError, match="duplicate inventory path"):
        inventory_sha256(entries)


def test_inventory_digest_rejects_unsafe_numbers_and_floats():
    with pytest.raises(ContractError, match="safe range"):
        inventory_sha256([{"path": "x", "size": 2**60}])
    with pytest.raises(ContractError, match="floating-point"):
        inventory_sha256([{"path": "x", "ratio": 0.5}])


def test_scoped_receipt_validates_and_hashes_match():
    validate_coverage_receipt(receipt())


def test_global_negative_rejected_when_surface_is_not_fully_inspected():
    item = receipt("UNRETRIEVED_GLOBALLY")
    item["surfaces"][0]["inspection_status"] = "partial"
    with pytest.raises(ContractError):
        validate_coverage_receipt(item)


def test_global_negative_rejected_when_any_surface_is_omitted():
    item = receipt("UNRETRIEVED_GLOBALLY")
    item["omitted_surfaces"] = ["private-repository"]
    with pytest.raises(ContractError):
        validate_coverage_receipt(item)


def test_global_negative_rejected_without_independent_validation():
    item = receipt("UNRETRIEVED_GLOBALLY")
    item["independent_coverage_validation"]["status"] = "not_performed"
    with pytest.raises(ContractError):
        validate_coverage_receipt(item)


def test_inventory_tampering_is_detected():
    item = receipt()
    item["pass_1_root_inventory"]["entries"][0]["path"] = "tampered"
    with pytest.raises(ContractError, match="SHA-256"):
        validate_coverage_receipt(item)


def test_derived_lineage_node_requires_attribution_edge():
    node = {
        "schema_id": "SOURCE_LINEAGE_NODE", "schema_version": "0.1.0",
        "node_id": "derived-1", "tier": "DERIVED_RECONSTRUCTION",
        "source_identity": {"locator": "generated", "artifact_name": "composite"},
        "content_sha256": "a" * 64, "retrieval_status": "generated",
        "provenance_evidence": ["build record"], "limitations": []
    }
    with pytest.raises(ContractError):
        validate_lineage_node(node)
    node["attribution_edges"] = [{
        "source_node_id": "source-1", "relationship": "derived_from",
        "transformation": "explicit reconstruction"
    }]
    validate_lineage_node(node)


def reachability(bound="UNVERIFIED"):
    return {
        "schema_id": "EFFECTING_TARGET_REACHABILITY", "schema_version": "0.1.0",
        "audit_id": "reach-1",
        "guard_definition": {"symbol": "guard", "file": "guard.py", "source_sha256": "b" * 64},
        "entry_points": ["api.request"], "call_sites": [],
        "effecting_target": {"identity": "target-1", "operation": "commit"},
        "analysis": {"tool": "test", "version": "1", "closed_world_assumption": False,
            "uninspected_dependencies": ["plugin"], "dynamic_boundaries": ["plugin dispatch"],
            "bypass_paths": [], "limitations": ["dynamic dispatch"]},
        "effecting_target_bound": bound
    }


def test_true_reachability_rejected_with_dynamic_or_uninspected_path():
    with pytest.raises(ContractError):
        validate_reachability_report(reachability("TRUE"))


def test_false_reachability_requires_identified_bypass():
    item = reachability("FALSE")
    item["analysis"]["uninspected_dependencies"] = []
    item["analysis"]["dynamic_boundaries"] = []
    with pytest.raises(ContractError):
        validate_reachability_report(item)
    item["analysis"]["bypass_paths"] = ["api.request -> direct_target.commit"]
    validate_reachability_report(item)


def test_unverified_reachability_accepts_open_world_limitations():
    validate_reachability_report(reachability("UNVERIFIED"))
