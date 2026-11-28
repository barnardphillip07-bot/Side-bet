"""Evidence provenance and byte-integrity primitives for DingoOS MCIVP.

A digest establishes byte equality with a recorded digest; it does not prove
who created the bytes, whether the source is truthful, or whether the content
is scientifically valid.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import hashlib
import json
from typing import Iterable


class EvidenceError(ValueError):
    """Invalid evidence metadata or integrity operation."""


def _utc_timestamp(value: str) -> str:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError) as exc:
        raise EvidenceError("timestamp must be ISO-8601") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise EvidenceError("timestamp must include a timezone")
    return parsed.isoformat()


def _nonblank(name: str, value: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise EvidenceError(f"{name} is required")
    return value.strip()


@dataclass(frozen=True, slots=True)
class EvidenceRecord:
    evidence_id: str
    source_kind: str
    source_reference: str
    acquired_at: str
    acquired_by: str
    acquisition_method: str
    media_type: str
    original_filename: str
    byte_length: int
    sha256: str
    parent_evidence_ids: tuple[str, ...] = ()
    transformation: str = "ORIGINAL_BYTES"
    manifest_sha256: str = ""

    def __post_init__(self):
        for name in ("evidence_id", "source_kind", "source_reference",
                     "acquired_by", "acquisition_method", "media_type",
                     "original_filename", "transformation"):
            _nonblank(name, getattr(self, name))
        object.__setattr__(self, "acquired_at", _utc_timestamp(self.acquired_at))
        if not isinstance(self.byte_length, int) or isinstance(self.byte_length, bool) or self.byte_length < 0:
            raise EvidenceError("byte_length must be a nonnegative integer")
        if len(self.sha256) != 64 or any(c not in "0123456789abcdef" for c in self.sha256):
            raise EvidenceError("sha256 must be 64 lowercase hexadecimal characters")
        if len(set(self.parent_evidence_ids)) != len(self.parent_evidence_ids):
            raise EvidenceError("parent evidence IDs must be unique")
        if self.evidence_id in self.parent_evidence_ids:
            raise EvidenceError("evidence cannot be its own parent")
        expected = self.calculate_manifest_sha256()
        if self.manifest_sha256 and self.manifest_sha256 != expected:
            raise EvidenceError("manifest digest mismatch")
        object.__setattr__(self, "manifest_sha256", expected)

    def manifest_payload(self) -> dict:
        return {
            "evidence_id": self.evidence_id,
            "source_kind": self.source_kind,
            "source_reference": self.source_reference,
            "acquired_at": self.acquired_at,
            "acquired_by": self.acquired_by,
            "acquisition_method": self.acquisition_method,
            "media_type": self.media_type,
            "original_filename": self.original_filename,
            "byte_length": self.byte_length,
            "sha256": self.sha256,
            "parent_evidence_ids": list(self.parent_evidence_ids),
            "transformation": self.transformation,
        }

    def calculate_manifest_sha256(self) -> str:
        encoded = json.dumps(self.manifest_payload(), sort_keys=True,
                             separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()


def create_evidence_record(
    raw_bytes: bytes, *, evidence_id: str, source_kind: str,
    source_reference: str, acquired_at: str, acquired_by: str,
    acquisition_method: str, media_type: str, original_filename: str,
    parent_evidence_ids: Iterable[str] = (), transformation: str = "ORIGINAL_BYTES",
) -> EvidenceRecord:
    """Create metadata for exact bytes; callers must preserve raw_bytes unchanged."""
    if not isinstance(raw_bytes, bytes):
        raise EvidenceError("raw evidence must be bytes")
    return EvidenceRecord(
        evidence_id=evidence_id, source_kind=source_kind,
        source_reference=source_reference, acquired_at=acquired_at,
        acquired_by=acquired_by, acquisition_method=acquisition_method,
        media_type=media_type, original_filename=original_filename,
        byte_length=len(raw_bytes), sha256=hashlib.sha256(raw_bytes).hexdigest(),
        parent_evidence_ids=tuple(parent_evidence_ids), transformation=transformation,
    )


def verify_evidence_bytes(record: EvidenceRecord, raw_bytes: bytes) -> bool:
    """Return true only when byte length and SHA-256 match the recorded original."""
    if not isinstance(raw_bytes, bytes):
        raise EvidenceError("evidence verification requires bytes")
    return (len(raw_bytes) == record.byte_length and
            hashlib.sha256(raw_bytes).hexdigest() == record.sha256)


def verify_manifest(record: EvidenceRecord) -> bool:
    """Check internal manifest consistency, not source authenticity."""
    return record.manifest_sha256 == record.calculate_manifest_sha256()


def verify_evidence_lineage(records: Iterable[EvidenceRecord]) -> bool:
    """Require a complete, unique, acyclic parent graph for the supplied record set."""
    items = tuple(records)
    by_id = {item.evidence_id: item for item in items}
    if len(by_id) != len(items):
        raise EvidenceError("evidence IDs must be unique")
    for item in items:
        missing = set(item.parent_evidence_ids) - set(by_id)
        if missing:
            raise EvidenceError(f"{item.evidence_id}: missing parent evidence {sorted(missing)}")
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(evidence_id: str) -> None:
        if evidence_id in visiting:
            raise EvidenceError("evidence lineage contains a cycle")
        if evidence_id in visited:
            return
        visiting.add(evidence_id)
        for parent_id in by_id[evidence_id].parent_evidence_ids:
            visit(parent_id)
        visiting.remove(evidence_id)
        visited.add(evidence_id)

    for evidence_id in by_id:
        visit(evidence_id)
    return True
