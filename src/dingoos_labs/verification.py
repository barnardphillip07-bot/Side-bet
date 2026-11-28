"""Independent scientific review gates for DingoOS MCIVP."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import hashlib
import json


class VerificationError(ValueError):
    """Invalid scientific verification record."""


@dataclass(frozen=True, slots=True)
class IndependentReview:
    review_id: str
    claim_id: str
    originator_id: str
    reviewer_id: str
    reviewed_at: str
    scope: str
    methods: tuple[str, ...]
    evidence_ids: tuple[str, ...]
    findings: tuple[str, ...]
    outcome: str

    def __post_init__(self):
        for name in ("review_id", "claim_id", "originator_id", "reviewer_id", "scope"):
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                raise VerificationError(f"{name} is required")
        try:
            timestamp = datetime.fromisoformat(self.reviewed_at.replace("Z", "+00:00"))
        except (TypeError, ValueError) as exc:
            raise VerificationError("reviewed_at must be ISO-8601") from exc
        if timestamp.tzinfo is None or timestamp.utcoffset() is None:
            raise VerificationError("reviewed_at must include a timezone")
        if self.originator_id == self.reviewer_id:
            raise VerificationError("reviewer must be independent of the originator")
        if not self.methods or any(not x.strip() for x in self.methods):
            raise VerificationError("review methods are required")
        if not self.evidence_ids or len(set(self.evidence_ids)) != len(self.evidence_ids):
            raise VerificationError("unique evidence references are required")
        if self.outcome not in {"PASS", "FAIL", "INCONCLUSIVE"}:
            raise VerificationError("outcome must be PASS, FAIL or INCONCLUSIVE")

    def digest(self) -> str:
        payload = {
            "review_id": self.review_id, "claim_id": self.claim_id,
            "originator_id": self.originator_id, "reviewer_id": self.reviewer_id,
            "reviewed_at": self.reviewed_at, "scope": self.scope,
            "methods": list(self.methods), "evidence_ids": list(self.evidence_ids),
            "findings": list(self.findings), "outcome": self.outcome,
        }
        return hashlib.sha256(json.dumps(payload, sort_keys=True,
            separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()


@dataclass(frozen=True, slots=True)
class ScientificEvidenceGate:
    evidence_integrity_verified: bool
    provenance_reviewed: bool
    measurement_statuses: tuple[str, ...]
    statistical_analysis_reviewed: bool
    independent_review: IndependentReview


@dataclass(frozen=True, slots=True)
class GateDecision:
    status: str
    blockers: tuple[str, ...]


def assess_scientific_evidence(gate: ScientificEvidenceGate) -> GateDecision:
    """Return VALIDATED only when all supplied mandatory checks pass.

    This is a workflow decision helper, not a substitute for expert judgement,
    source authentication, peer review credentials or legal sign-off.
    """
    blockers = []
    if not gate.evidence_integrity_verified:
        blockers.append("raw evidence byte integrity not verified")
    if not gate.provenance_reviewed:
        blockers.append("source provenance not reviewed")
    if not gate.measurement_statuses:
        blockers.append("no measurement assessments supplied")
    elif any(x != "VALID" for x in gate.measurement_statuses):
        blockers.append("one or more measurements are not VALID")
    if not gate.statistical_analysis_reviewed:
        blockers.append("statistical analysis has not been independently reviewed")
    if gate.independent_review.outcome != "PASS":
        blockers.append("independent scientific review did not PASS")
    status = "VALIDATED" if not blockers else "BLOCKED"
    return GateDecision(status, tuple(blockers))
