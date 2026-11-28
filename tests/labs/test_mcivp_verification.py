import pytest

from dingoos_labs.verification import (
    IndependentReview, ScientificClaim, ScientificEvidenceGate, VerificationError,
    assess_scientific_evidence,
)


def claim():
    return ScientificClaim(
        claim_id="CLAIM-01", statement="The measured effect exceeds the baseline.",
        scope="Instrument configuration A under protocol P at 20-25 C.",
        supporting_evidence_ids=("EV-RAW-01", "EV-CAL-01"),
        contradictory_evidence_ids=("EV-NULL-02",),
        alternative_explanations=("sensor drift", "environmental interference"),
        falsification_conditions=("independent calibrated replication finds no effect",),
        uncertainty_and_limitations="Limited to the stated operating envelope; uncertainty budget attached.",
    )


def review(outcome="PASS", claim_id="CLAIM-01", evidence_ids=("EV-RAW-01", "EV-CAL-01", "EV-NULL-02")):
    return IndependentReview(
        review_id="REV-01", claim_id=claim_id, originator_id="author-01",
        reviewer_id="reviewer-02", reviewed_at="2026-11-28T10:00:00Z",
        scope="reproduce analysis and inspect source data",
        methods=("independent recomputation", "source cross-check"),
        evidence_ids=evidence_ids,
        findings=("calculation reproduced within stated tolerance",), outcome=outcome,
    )


def gate(**kwargs):
    values = dict(
        claim=claim(), evidence_integrity_verified=True, provenance_reviewed=True,
        measurement_statuses=("VALID", "VALID"), statistical_analysis_reviewed=True,
        independent_review=review(),
    )
    values.update(kwargs)
    return ScientificEvidenceGate(**values)


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


def test_scientific_gate_passes_controls_without_claiming_truth():
    assert assess_scientific_evidence(gate()).status == "CONTROLS_PASSED"


def test_gate_blocks_unverified_measurement_and_failed_review():
    result = assess_scientific_evidence(gate(
        measurement_statuses=("VALID", "INDETERMINATE"),
        independent_review=review("INCONCLUSIVE"),
    ))
    assert result.status == "BLOCKED"
    assert len(result.blockers) == 2


def test_gate_blocks_missing_provenance_and_integrity():
    result = assess_scientific_evidence(gate(
        evidence_integrity_verified=False, provenance_reviewed=False,
        measurement_statuses=(), statistical_analysis_reviewed=False,
    ))
    assert result.status == "BLOCKED"
    assert len(result.blockers) == 4


def test_gate_requires_review_of_all_supporting_and_conflicting_evidence():
    result = assess_scientific_evidence(gate(
        independent_review=review(evidence_ids=("EV-RAW-01", "EV-CAL-01")),
    ))
    assert result.status == "BLOCKED"
    assert "independent review did not inspect every claim evidence reference" in result.blockers


def test_gate_rejects_review_for_different_claim():
    result = assess_scientific_evidence(gate(independent_review=review(claim_id="OTHER")))
    assert result.status == "BLOCKED"
    assert "independent review references a different claim" in result.blockers


def test_claim_requires_alternatives_and_falsification_conditions():
    with pytest.raises(VerificationError, match="alternative_explanations"):
        ScientificClaim(
            claim_id="C", statement="s", scope="scope",
            supporting_evidence_ids=("E1",), contradictory_evidence_ids=(),
            alternative_explanations=(), falsification_conditions=("test",),
            uncertainty_and_limitations="unknown",
        )
