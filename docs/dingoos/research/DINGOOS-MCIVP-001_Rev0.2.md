# DINGOOS-MCIVP-001 — Mathematical Coherence & Scientific Evidence Oversight Protocol

- Revision: 0.2
- Date: 28 November 2026
- Repository: barnardphillip07-bot/Side-bet
- Branch: labs/mcivp-001
- Status: DERIVED PUBLIC-SAFE IMPLEMENTATION — PARTIAL CONTROLS — NOT OWNER-RATIFIED CANONICAL DINGOOS POLICY

## 1. Mandatory governing scope

MCIVP governs scientific evidence and mathematical analysis across Physics Lab and Technology Lab. It separates source authenticity, provenance, byte integrity, measurement validity, mathematical/statistical validity, independent review and the scope of conclusions.

No single control is evidence of all the others.

## 2. Provenance and byte integrity

Each EvidenceRecord identifies source kind/reference, timezone-aware acquisition time, acquiring actor, method, media type, original filename, byte length, SHA-256, parent evidence IDs and transformation description.

Original bytes are preserved unchanged. Derived data receive new records and parent links.

Implemented: \`src/dingoos_labs/evidence.py\`.

**Limit:** hashes prove only that the bytes presented match a recorded digest. They do not authenticate origin, authorship, instrument, timestamp, custody or scientific truth. Manifest digests are not signatures.

## 3. Measurement validity and metrology

CalibrationRecord and MeasurementObservation carry instrument/calibration identity, calibration status and interval, range, unit, traceability reference, timestamp, raw evidence reference, protocol, environmental values and standard uncertainties.

Assessment outcomes:
- VALID: supplied metadata and required environmental checks pass and uncertainty combination is justified.
- INVALID: one or more explicit checks fail.
- INDETERMINATE: uncertainty relationship is not established.

Root-sum-square combination is performed only when the caller explicitly declares the measurement and calibration uncertainty components independent. Otherwise a nonzero calibration uncertainty leaves the result INDETERMINATE pending covariance-aware treatment.

Implemented: \`src/dingoos_labs/measurement.py\`.

**Limits:** metadata are not authenticated against calibration issuers; SI traceability, certificate validity, firmware, measurement method suitability and uncertainty budgets require external authoritative verification.

## 4. Statistical analysis

Descriptive summaries and deterministic nonparametric percentile bootstrap intervals are implemented. Both require explicit evidence IDs and preserve those references in the output.

Bootstrap assumptions are representative sampling, IID observations and adequacy of the empirical distribution. The routine does not repair selection bias, confounding, autocorrelation, clustering, multiple testing, optional stopping or poor design. A confidence interval is not by itself a significance test, causal inference or proof of a physical effect.

Implemented: \`src/dingoos_labs/statistics.py\`.

## 5. Claim-to-evidence traceability

ScientificClaim records:
- Exact claim statement and scope.
- Supporting evidence IDs.
- Contradictory evidence IDs.
- Alternative explanations.
- Falsification conditions.
- Uncertainty and limitations.

Supporting and contradictory evidence must remain separately visible. Independent review must cover every referenced evidence item.

## 6. Independent scientific review

IndependentReview identifies claim, originator, reviewer, timestamp, scope, methods, evidence references, findings and outcome. Reviewer ID must differ from originator ID. Outcomes are PASS, FAIL or INCONCLUSIVE.

The review digest is a reproducibility checksum, not a digital signature. Identifier separation does not authenticate reviewer identity, competence, organizational independence or conflicts of interest.

## 7. Conservative evidence gate

The gate returns CONTROLS_PASSED only if:
- Raw evidence byte integrity is verified.
- Provenance is reviewed.
- Every supplied measurement status is VALID.
- Statistical analysis is independently reviewed.
- Independent review outcome is PASS.
- Review references the same claim.
- Review includes every supporting and contradictory evidence reference.

Otherwise it returns BLOCKED with reasons.

**CONTROLS_PASSED is not a finding that the claim is true or a canonical release authorization.** Scientific acceptance still requires expert assessment of the claim, alternative explanations, uncertainty, replication, falsifiability and validity domain.

Implemented: \`src/dingoos_labs/verification.py\`.

## 8. Mandatory oversight stages

SE-01 provenance and chain of custody; SE-02 raw-byte preservation and integrity; SE-03 acquisition protocol; SE-04 calibration and traceability; SE-05 measurement validity and uncertainty; SE-06 statistical design; SE-07 mathematical coherence; SE-08 contradictory evidence and alternatives; SE-09 independent recomputation/replication; SE-10 independent review; SE-11 conclusion-to-evidence scope; SE-12 correction and revision history.

Each stage is PASS, FAIL, OPEN, UNVERIFIED or justified NOT APPLICABLE. Missing evidence is never PASS.

## 9. Explicitly not implemented / not verified

- Trusted identity, reviewer qualifications, conflict-of-interest and digital signatures.
- Trusted timestamps and authenticated source chain of custody.
- Persistent append-only evidence store and retention controls.
- Direct sensor acquisition, parsing and immutable archival.
- External calibration certificate and SI traceability verification.
- General covariance matrices and uncertainty propagation.
- Advanced time-series, clustered, multiple-testing, Bayesian and causal inference.
- External replication orchestration.
- Canonical DingoOS evidence, identity, requirements or release-service integration.
- Automated scientific truth determination.

## 10. Files and tests

- \`src/dingoos_labs/evidence.py\`
- \`src/dingoos_labs/measurement.py\`
- \`src/dingoos_labs/statistics.py\`
- \`src/dingoos_labs/verification.py\`
- \`tests/labs/test_mcivp_*.py\`
- \`.github/workflows/dingoos-labs-oie.yml\`

The test suite verifies software behaviour only. It does not validate a physical phenomenon or dataset.

## 11. IP and workstream boundaries

Only public-safe derived material is committed. Protected DingoOS/BIF originals are excluded. The adopted Recovery Engine baseline is not modified. SW-ZPE-01 remains separate.

## Revision history

| Revision | Date | Change |
|---|---|---|
| 0.1 | 28 Nov 2026 | Initial executable provenance, metrology, statistics and independent review controls. |
| 0.2 | 28 Nov 2026 | Adds evidence-linked statistical outputs, scientific claim record, contradictory evidence, alternatives, falsification conditions and non-overclaiming gate status. |

**Governing principle:** preserve the observation, verify what can be checked, quantify uncertainty, challenge the interpretation, and limit the conclusion to what the evidence establishes.
