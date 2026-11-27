"""Deterministic validation primitives for the DingoOS recovery-engine contracts.

This module implements the bounded inventory-digest profile documented in
CONTRACTS-v0.1.0.md. It is not a general RFC 8785 implementation.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

SCHEMA_DIR = Path(__file__).resolve().parents[2] / "docs" / "dingoos" / "recovery-engine" / "schemas"
SCHEMA_FILES = {
    "SEARCH_COVERAGE_RECEIPT": "search-coverage-receipt.schema.json",
    "SOURCE_ARTIFACT_INDEX_RECORD": "source-artifact-index-record.schema.json",
    "SOURCE_LINEAGE_NODE": "source-lineage-node.schema.json",
    "LINEAGE_DIFF_REPORT": "lineage-diff-report.schema.json",
    "EFFECTING_TARGET_REACHABILITY": "effecting-target-reachability.schema.json",
}
MAX_SAFE_INTEGER = (2**53) - 1


class ContractError(ValueError):
    """Raised when a record violates a schema or semantic invariant."""


def _utf16_sort_key(value: str) -> bytes:
    return value.encode("utf-16-be", errors="strict")


def _validate_jcs_subset(value: Any, path: str = "$") -> None:
    """Restrict inventory values to the JCS-safe deterministic data subset."""
    if value is None or isinstance(value, (str, bool)):
        if isinstance(value, str):
            value.encode("utf-8", errors="strict")
        return
    if isinstance(value, int) and not isinstance(value, bool):
        if abs(value) > MAX_SAFE_INTEGER:
            raise ContractError(f"{path}: integer exceeds interoperable safe range; encode it as a string")
        return
    if isinstance(value, float):
        raise ContractError(f"{path}: floating-point values are forbidden in inventory entries")
    if isinstance(value, list):
        for index, item in enumerate(value):
            _validate_jcs_subset(item, f"{path}[{index}]")
        return
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise ContractError(f"{path}: object keys must be strings")
            key.encode("utf-8", errors="strict")
            _validate_jcs_subset(item, f"{path}.{key}")
        return
    raise ContractError(f"{path}: unsupported inventory value type {type(value).__name__}")


def _sort_object_keys_utf16(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: _sort_object_keys_utf16(value[key])
            for key in sorted(value, key=_utf16_sort_key)
        }
    if isinstance(value, list):
        return [_sort_object_keys_utf16(item) for item in value]
    return value


def canonical_inventory_bytes(entries: Iterable[dict[str, Any]]) -> bytes:
    """Return canonical UTF-8 bytes for the ordered inventory entry array."""
    materialized = list(entries)
    seen: set[str] = set()
    for index, entry in enumerate(materialized):
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), str):
            raise ContractError(f"entries[{index}]: each inventory entry requires a string path")
        path = entry["path"]
        if path in seen:
            raise ContractError(f"duplicate inventory path: {path!r}")
        seen.add(path)
        _validate_jcs_subset(entry, f"entries[{index}]")
    ordered = sorted(materialized, key=lambda item: _utf16_sort_key(item["path"]))
    canonical = _sort_object_keys_utf16(ordered)
    try:
        return json.dumps(
            canonical, ensure_ascii=False, allow_nan=False,
            separators=(",", ":"), sort_keys=False,
        ).encode("utf-8")
    except (TypeError, ValueError, UnicodeEncodeError) as exc:
        raise ContractError(f"inventory canonicalization failed: {exc}") from exc


def inventory_sha256(entries: Iterable[dict[str, Any]]) -> str:
    return hashlib.sha256(canonical_inventory_bytes(entries)).hexdigest()


def load_schema(schema_id: str) -> dict[str, Any]:
    try:
        filename = SCHEMA_FILES[schema_id]
    except KeyError as exc:
        raise ContractError(f"unknown schema_id: {schema_id}") from exc
    path = SCHEMA_DIR / filename
    try:
        schema = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ContractError(f"cannot load schema {path}: {exc}") from exc
    Draft202012Validator.check_schema(schema)
    return schema


def validate_record(schema_id: str, record: dict[str, Any]) -> None:
    schema = load_schema(schema_id)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(record), key=lambda error: list(map(str, error.absolute_path)))
    if errors:
        details = "; ".join(
            f"{'/'.join(map(str, error.absolute_path)) or '$'}: {error.message}"
            for error in errors
        )
        raise ContractError(details)


def validate_coverage_receipt(receipt: dict[str, Any]) -> None:
    validate_record("SEARCH_COVERAGE_RECEIPT", receipt)
    for pass_name in ("pass_1_root_inventory", "pass_2_deep_inventory"):
        inventory = receipt[pass_name]
        entries = inventory["entries"]
        if inventory["entry_count"] != len(entries):
            raise ContractError(f"{pass_name}: entry_count does not match entries length")
        actual = inventory_sha256(entries)
        if actual != inventory["sha256"].lower():
            raise ContractError(f"{pass_name}: SHA-256 does not match canonical inventory entries")
    if receipt["conclusion_scope"] == "UNRETRIEVED_GLOBALLY":
        if receipt["coverage_assessment"] != "complete_within_declared_universe":
            raise ContractError("global negative claim requires complete declared-universe coverage")
        if receipt["omitted_surfaces"]:
            raise ContractError("global negative claim prohibited while omitted_surfaces is non-empty")
        validation = receipt.get("independent_coverage_validation", {})
        if validation.get("status") != "passed":
            raise ContractError("global negative claim requires passed independent coverage validation")
        for surface in receipt["surfaces"]:
            if surface["enumeration_status"] != "complete":
                raise ContractError("global negative claim includes a non-completely enumerated surface")
            if surface["inspection_status"] not in ("complete", "not_applicable"):
                raise ContractError("global negative claim includes an uninspected/inaccessible surface")
            if surface["pagination_status"] not in ("complete", "not_applicable"):
                raise ContractError("global negative claim includes incomplete/unknown pagination")


def validate_source_artifact_record(record: dict[str, Any]) -> None:
    validate_record("SOURCE_ARTIFACT_INDEX_RECORD", record)
    region = record["region"]
    if region["byte_offset_end"] <= region["byte_offset_start"]:
        raise ContractError("byte_offset_end must be greater than byte_offset_start")


def validate_lineage_node(record: dict[str, Any]) -> None:
    validate_record("SOURCE_LINEAGE_NODE", record)


def validate_reachability_report(record: dict[str, Any]) -> None:
    validate_record("EFFECTING_TARGET_REACHABILITY", record)
