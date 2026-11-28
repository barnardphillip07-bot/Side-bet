import pytest

from dingoos_labs.evidence import (
    EvidenceError, create_evidence_record, verify_evidence_bytes, verify_manifest,
)


def record(data=b"raw sensor bytes"):
    return create_evidence_record(
        data, evidence_id="EV-001", source_kind="INSTRUMENT_EXPORT",
        source_reference="instrument-session-17", acquired_at="2026-11-28T10:00:00+11:00",
        acquired_by="operator-01", acquisition_method="direct binary export",
        media_type="application/octet-stream", original_filename="capture.bin",
    )


def test_evidence_digest_and_manifest_verify():
    item = record()
    assert verify_evidence_bytes(item, b"raw sensor bytes")
    assert verify_manifest(item)
    assert not verify_evidence_bytes(item, b"altered sensor bytes")


def test_manifest_records_parent_and_transformation():
    item = create_evidence_record(
        b"derived", evidence_id="EV-002", source_kind="DERIVED_DATA",
        source_reference="analysis-run-2", acquired_at="2026-11-28T10:00:00Z",
        acquired_by="analyst-02", acquisition_method="documented conversion",
        media_type="text/csv", original_filename="derived.csv",
        parent_evidence_ids=("EV-001",), transformation="CSV_EXPORT_V1",
    )
    assert item.parent_evidence_ids == ("EV-001",)
    assert item.transformation == "CSV_EXPORT_V1"


def test_naive_timestamp_and_nonbytes_rejected():
    with pytest.raises(EvidenceError, match="timezone"):
        create_evidence_record(
            b"x", evidence_id="E", source_kind="FILE", source_reference="s",
            acquired_at="2026-11-28T10:00:00", acquired_by="a",
            acquisition_method="copy", media_type="text/plain", original_filename="x",
        )
    with pytest.raises(EvidenceError, match="bytes"):
        create_evidence_record(
            "not bytes", evidence_id="E", source_kind="FILE", source_reference="s",
            acquired_at="2026-11-28T10:00:00Z", acquired_by="a",
            acquisition_method="copy", media_type="text/plain", original_filename="x",
        )
