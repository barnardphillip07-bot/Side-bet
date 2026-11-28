import pytest

from dingoos_labs.verification import (
    IndependentReview, ScientificEvidenceGate, VerificationError,
    assess_scientific_evidence,
)


def review(outcome="PASS"):
    return IndependentReview(
        review_id="REV-01", claim_id="CLAIM-01", originator_id="author-01",
        reviewer_id="reviewer-02", reviewed_at="2026-11-28T10:00:00Z",
        scope="reproduce analysis and inspect source data",
        methods=("independent recomputation", "source cross-check"),
        evidence_ids=("EV-RAW-01", "EV-CAL-01"),
        findings=("calculation reproduced within stated tolerance",), outcome=outcome,
    )


def test_independent_review_required_and_digest_stable():
    item = review()
    assert len(item.digest()) == 64
    assert item.digest() == item.digest()


def test_originator_cannot_review_own_claim():
    with pytest.raises(VerificationError, match="independent"):
        IndependentReview(
            review_id="REV", claim_id="C", originator_id="same", reviewer_id="same",
            reviewed_at="2026-11-28T10:00:00Z", scope="check",
            methods=("recompute",), evidence_ids=("EV-1",), findings=(), outcome="PASS",
        )


def test_scientific_gate_passes_only_when_all_checks_pass():
    gate = ScientificEvidenceGate(True, True, ("VALID", "VALID"), True, review())
    assert assess_scientific_evidence(gate).status == "VALIDATED"


def test_gate_blocks_unverified_measurement_and_failed_review():
    gate = ScientificEvidenceGate(True, True, ("VALID", "INDETERMINATE"), True, review("INCONCLUSIVE"))
    result = assess_scientific_evidence(gate)
    assert result.status == "BLOCKED"
    assert len(result.blockers) == 2


def test_gate_blocks_missing_provenance_and_integrity():
    gate = ScientificEvidenceGate(False, False, (), False, review())
    result = assess_scientific_evidence(gate)
    assert result.status == "BLOCKED"
    assert len(result.blockers) == 4
