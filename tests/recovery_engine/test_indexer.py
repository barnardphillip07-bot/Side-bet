from __future__ import annotations

import hashlib
import io
import json
import zipfile

from dingoos_recovery.contracts import validate_source_artifact_record
from dingoos_recovery.indexer import index_bytes, index_zip_bytes


def assert_records_are_schema_valid(records):
    assert records
    for record in records:
        validate_source_artifact_record(record)


def assert_offsets_hash_exact(data, record):
    region = record["region"]
    raw = data[region["byte_offset_start"]:region["byte_offset_end"]]
    assert hashlib.sha256(raw).hexdigest() == region["content_sha256"]


def test_python_file_indexes_file_and_ast_symbols_with_exact_offsets():
    data = b"class Alpha:\n    def run(self):\n        return 7\n"
    records = index_bytes("alpha.py", data)
    assert_records_are_schema_valid(records)
    assert records[0]["classification"] == "source_file"
    identifiers = {r["symbols"][0]["identifier"] for r in records if r["symbols"]}
    assert {"Alpha", "run"} <= identifiers
    for record in records:
        assert_offsets_hash_exact(data, record)


def test_markdown_python_fence_indexes_ast_and_skips_duplicate_unfenced_hits():
    data = b"Intro\n\n```python\nclass Alpha:\n    def run(self):\n        return 1\n```\n"
    records = index_bytes("example.md", data)
    assert_records_are_schema_valid(records)
    identifiers = [r["symbols"][0]["identifier"] for r in records if r["symbols"]]
    assert identifiers.count("Alpha") == 1
    assert identifiers.count("run") == 1
    assert all(r["classification"] == "python_ast_symbol" for r in records)


def test_malformed_python_fence_is_retained_as_parse_failed():
    data = b"```python\ndef broken(:\n```\n"
    records = index_bytes("broken.md", data)
    assert_records_are_schema_valid(records)
    assert any(r["status"] == "parse_failed" for r in records)
    assert any("CONTAINS_EMBEDDED_SOURCE" in r["tags"] for r in records)


def test_unfenced_mixed_text_declarations_are_partial_candidates():
    data = b"Intro prose\nclass EmbeddedThing:\n    pass\n\ndef embedded_call():\n    return 1\n"
    records = index_bytes("paste.txt", data)
    assert_records_are_schema_valid(records)
    ids = {r["symbols"][0]["identifier"] for r in records}
    assert {"EmbeddedThing", "embedded_call"} <= ids
    assert all(r["status"] == "partial" for r in records)


def test_json_top_level_keys_are_indexed():
    data = b'{"schema":"x","required":["a"],"properties":{"a":{"type":"string"}}}\n'
    records = index_bytes("contract.json", data)
    assert_records_are_schema_valid(records)
    assert records[0]["classification"] == "json_structure"
    assert {s["identifier"] for s in records[0]["symbols"]} == {"schema", "required", "properties"}
    assert_offsets_hash_exact(data, records[0])


def test_tla_module_header_is_indexed():
    data = b"---- MODULE FenceProtocol ----\nVARIABLES fence, receipt\n====\n"
    records = index_bytes("FenceProtocol.tla", data)
    assert_records_are_schema_valid(records)
    assert records[0]["classification"] == "tla_module"
    assert records[0]["symbols"][0]["identifier"] == "FenceProtocol"


def test_zip_members_are_indexed_without_extracting_and_keep_parent_hash():
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("src/worker.py", "def run():\n    return True\n")
        archive.writestr("schemas/contract.json", '{"type":"object"}')
    data = stream.getvalue()
    records = index_zip_bytes("bundle.zip", data)
    assert_records_are_schema_valid(records)
    assert all(r["parent_artifact"]["path"] == "bundle.zip" for r in records)
    assert all(r["parent_artifact"]["sha256"] == hashlib.sha256(data).hexdigest() for r in records)
    assert {r["parent_artifact"]["archive_entry_path"] for r in records} == {
        "src/worker.py", "schemas/contract.json"
    }


def test_unsupported_format_is_explicit_not_silently_omitted():
    data = b"opaque binary-ish content"
    records = index_bytes("unknown.bin", data)
    assert_records_are_schema_valid(records)
    assert records[0]["status"] == "unsupported"
    assert "PARSE_INCOMPLETE" in records[0]["tags"]


def test_size_limit_is_explicit():
    records = index_bytes("large.py", b"x" * 20, max_file_bytes=10)
    assert_records_are_schema_valid(records)
    assert records[0]["status"] == "unsupported"
    assert "size limit" in records[0]["extractor"]["grammar"]



def test_empty_files_produce_no_invalid_zero_length_source_regions():
    assert index_bytes("empty.json", b"") == []
    assert index_bytes("empty.tla", b"") == []
    assert index_bytes("empty.py", b"") == []
