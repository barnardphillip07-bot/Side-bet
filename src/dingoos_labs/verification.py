"""Independent scientific review and claim-to-evidence gates for DingoOS MCIVP."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import hashlib
import json


class VerificationError(ValueError):
    """Invalid scientific verification record."""


def _required_tuple(name: str, values: tuple[str, ...]) -> None:
    if not values or any(not isinstance(x, str) or not x.strip() for x in values):
        raise VerificationError(f"{name} must contain nonblank entries")
    if len(set(values)) != len(values):
        raise VerificationError(f"{name} entries must be unique")


@dataclass(frozen=True, slots=True)
class ScientificClaim:
    claim_id: str
    statement: str
    scope: str
    supporting_evidence_ids: tuple[str, ...]
    contradictory_evidence_ids: tuple[str, ...]
    alternative_explanations: tuple[str, ...]
    falsification_conditions: tuple[str, ...]
    uncertainty_and_limitations: str

    def __post_init__(self):
        for name in ("claim_id", "statement", "scope", "uncertainty_and_limitations"):
            if not isinstance(getattr(self, name), str) or not getattr(self, name).strip():
                raise VerificationError(f"{name} is required")
        _required_tuple("supporting_evidence_ids", self.supporting_evidence_ids)
        if self.contradictory_evidence_ids:
            _required_tuple("contradictory_evidence_ids", self.contradictory_evidence_ids)
        if set(self.supporting_evidence_ids) & set(self.contradictory_evidence_ids):
            raise VerificationError("supporting and contradictory evidence lists must be distinct")
        _required_tuple("alternative_explanations", self.alternative_explanations)
        _required_tuple("falsification_conditions", self.falsification_conditions)


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
        _required_tuple("methods", self.methods)
        _required_tuple("evidence_ids", self.evidence_ids)
        _required_tuple("findings", self.findings)
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
    claim: ScientificClaim
    integrity_verified_evidence_ids: tuple[str, ...]
    provenance_reviewed_evidence_ids: tuple[str, ...]
    measurement_statuses: tuple[str, ...]
    statistical_analysis_reviewed: bool
    independent_review: IndependentReview


@dataclass(frozen=True, slots=True)
class GateDecision:
    status: str
    blockers: tuple[str, ...]


def assess_scientific_evidence(gate: ScientificEvidenceGate) -> GateDecision:
    """Check prerequisite controls; never pronounce a claim scientifically true."""
    blockers = []
    review = gate.independent_review
    required_refs = set(gate.claim.supporting_evidence_ids) | set(gate.claim.contradictory_evidence_ids)
    if not required_refs.issubset(set(gate.integrity_verified_evidence_ids)):
        blockers.append("raw evidence byte integrity not verified for every claim evidence reference")
    if not required_refs.issubset(set(gate.provenance_reviewed_evidence_ids)):
        blockers.append("source provenance not reviewed for every claim evidence reference")
    if not gate.measurement_statuses:
        blockers.append("no measurement assessments supplied")
    elif any(x != "VALID" for x in gate.measurement_statuses):
        blockers.append("one or more measurements are not VALID")
    if not gate.statistical_analysis_reviewed:
        blockers.append("statistical analysis has not been independently reviewed")
    if review.outcome != "PASS":
        blockers.append("independent scientific review did not PASS")
    if review.claim_id != gate.claim.claim_id:
        blockers.append("independent review references a different claim")
    if not required_refs.issubset(set(review.evidence_ids)):
        blockers.append("independent review did not inspect every claim evidence reference")
    status = "CONTROLS_PASSED" if not blockers else "BLOCKED"
    return GateDecision(status, tuple(blockers))
