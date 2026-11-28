# DINGOOS-MCIVP-001 — Mathematical Coherence & Scientific Evidence Oversight Protocol

- Revision: 0.3
- Date: 28 November 2026
- Repository: barnardphillip07-bot/Side-bet
- Branch: labs/mcivp-001
- Status: DERIVED PUBLIC-SAFE IMPLEMENTATION — PARTIAL CONTROLS — NOT OWNER-RATIFIED CANONICAL DINGOOS POLICY

## 1. Mandatory scope and non-substitution

MCIVP governs scientific evidence and mathematical analysis across Physics Lab and Technology Lab. It separates source authenticity, provenance, byte integrity, measurement validity, mathematical/statistical validity, independent review and conclusion scope. A control proves only the property it tests.

## 2. Evidence provenance and integrity

EvidenceRecord identifies source kind/reference, timezone-aware acquisition time, actor, method, media type, original filename, byte length, SHA-256, parent evidence IDs and transformation description.

Original bytes must be retained unchanged. Derivatives receive new records linked to parent evidence. The lineage verifier requires unique IDs, all parent records present in the supplied record set and an acyclic graph.

SHA-256 comparison verifies that presented bytes match the recorded digest. It does not authenticate origin, authorship, instrument, time, custody or truth. Manifest digests are not signatures.

Implemented: \`src/dingoos_labs/evidence.py\`.

## 3. Measurement validity and metrology

CalibrationRecord and MeasurementObservation carry instrument/calibration identifiers, calibration status and validity interval, range, unit, traceability reference, timestamp, raw evidence reference, protocol, environment and standard uncertainty.

Assessment outcomes:
- VALID: supplied metadata and environmental checks pass and uncertainty combination is justified.
- INVALID: one or more explicit validity conditions fail.
- INDETERMINATE: uncertainty relationship is not established.

Root-sum-square combination is performed only when the caller explicitly declares measurement and calibration uncertainty components independent. Correlated components require covariance-aware treatment outside this helper.

The helper checks supplied metadata only. It does not authenticate certificates, verify issuing laboratories, establish SI traceability, validate instrument firmware or determine method suitability.

Implemented: \`src/dingoos_labs/measurement.py\`.

## 4. Statistical analysis

Descriptive summaries and deterministic nonparametric percentile bootstrap intervals require explicit evidence IDs and preserve those references in their output.

Bootstrap assumptions: representative sampling, IID observations and adequacy of the empirical distribution. It does not correct selection bias, confounding, autocorrelation, clustering, multiple testing, optional stopping or poor experimental design. A confidence interval is not by itself a significance test, causal inference or proof of a physical effect.

Implemented: \`src/dingoos_labs/statistics.py\`.

## 5. Claim-to-evidence traceability

ScientificClaim records the exact statement and scope, supporting evidence IDs, contradictory evidence IDs, alternative explanations, falsification conditions, uncertainty and limitations.

Supporting and contradictory evidence remain separately visible. The review gate requires every claim evidence reference to have per-item integrity verification, provenance review and independent review coverage.

## 6. Independent scientific review

IndependentReview identifies claim, originator, reviewer, timestamp, scope, methods, evidence references, findings and outcome. Reviewer ID must differ from originator ID. Outcomes are PASS, FAIL or INCONCLUSIVE.

The review digest is a reproducibility checksum, not a digital signature. Identifier separation does not authenticate identity, competence, institutional independence or conflicts of interest.

## 7. Conservative evidence gate

The gate returns CONTROLS_PASSED only if:
- Every supporting and contradictory evidence item has byte integrity verified.
- Every such item has provenance reviewed.
- Every supplied measurement assessment is VALID.
- Statistical analysis is independently reviewed.
- Independent review outcome is PASS.
- Review references the same claim.
- Review includes every supporting and contradictory evidence reference.

Otherwise it returns BLOCKED with explicit blockers.

**CONTROLS_PASSED is not a finding that the claim is true and is not release authorization.** Scientific acceptance still requires expert assessment of assumptions, alternative explanations, uncertainty, replication, falsifiability and validity domain.

Implemented: \`src/dingoos_labs/verification.py\`.

## 8. Mandatory oversight stages

SE-01 provenance and chain of custody; SE-02 raw-byte preservation and integrity; SE-03 acquisition protocol; SE-04 calibration and traceability; SE-05 measurement validity and uncertainty; SE-06 statistical design; SE-07 mathematical coherence; SE-08 contradictory evidence and alternatives; SE-09 independent recomputation/replication; SE-10 independent review; SE-11 conclusion-to-evidence scope; SE-12 correction and revision history.

Each stage is PASS, FAIL, OPEN, UNVERIFIED or justified NOT APPLICABLE. Missing evidence is never PASS.

## 9. Not implemented / not verified

Trusted identity, reviewer qualifications, conflict-of-interest and digital signatures; trusted timestamps; persistent append-only storage; direct instrument acquisition and parsing; external calibration and SI traceability verification; general covariance propagation; advanced time-series, clustered, multiple-testing, Bayesian and causal inference; external replication orchestration; canonical DingoOS evidence, identity, requirements and release-service integration; automated scientific truth determination.

## 10. Tests and boundaries

Tests reside in \`tests/labs/test_mcivp_*.py\`; workflow in \`.github/workflows/dingoos-labs-oie.yml\`. Automated tests verify software behaviour only, not a physical phenomenon or dataset.

Only public-safe derived material is committed. Protected DingoOS/BIF originals are excluded. The adopted Recovery Engine baseline and SW-ZPE-01 remain untouched.

## Revision history

| Revision | Date | Change |
|---|---|---|
| 0.1 | 28 Nov 2026 | Initial executable provenance, metrology, statistics and independent review controls. |
| 0.2 | 28 Nov 2026 | Adds evidence-linked statistics, scientific claim traceability, contradictory evidence, alternatives and falsification conditions. |
| 0.3 | 28 Nov 2026 | Adds complete acyclic evidence-lineage validation and per-evidence integrity/provenance gate coverage. |

**Governing principle:** preserve the observation, verify what can be checked, quantify uncertainty, challenge the interpretation, and limit the conclusion to what the evidence establishes.
