# DINGOOS-MCIVP-001 — Mathematical Coherence & Scientific Evidence Oversight Protocol

- Revision: 0.1
- Date: 28 November 2026
- Repository: barnardphillip07-bot/Side-bet
- Branch: labs/mcivp-001
- Status: DERIVED PUBLIC-SAFE IMPLEMENTATION — PARTIAL CONTROLS — NOT OWNER-RATIFIED CANONICAL DINGOOS POLICY
- Scope: Physics Lab, Technology Lab, scientific evidence, measurements, statistical analyses, mathematical models and independent verification.

## 1. Governing rule

Scientific evidence and the mathematical analysis applied to it are subject to mandatory oversight. No scientific claim may be represented as validated solely because source bytes are intact, an equation is mathematically consistent, a sensor produced a reading, a statistical routine returned a number, or a simulation completed.

The protocol separates:
1. Source authenticity and provenance.
2. Byte-level data integrity.
3. Measurement and metrological validity.
4. Mathematical and statistical validity.
5. Independent scientific verification.
6. The scope and strength of the resulting conclusion.

A control result is limited to the property it actually tests.

## 2. Evidence provenance and integrity

Every evidence item should identify:
- Stable evidence identifier.
- Source kind and source reference.
- Acquisition timestamp with timezone.
- Acquiring person/system and acquisition method.
- Media type and original filename.
- Exact byte length and SHA-256 digest.
- Parent evidence identifiers for derivatives.
- Transformation description for derived data.

Original evidence must be retained byte-for-byte. Transformations create new derivative records linked to their parents; they do not overwrite originals.

**Integrity limitation:** SHA-256 comparison detects whether supplied bytes match a recorded digest. It does not authenticate the source, collector, instrument, time, truthfulness or scientific meaning. A manifest digest is not a digital signature. Authenticity requires independent source verification and, where applicable, signed chain-of-custody records.

Implemented: \`src/dingoos_labs/evidence.py\`.

## 3. Measurement validity

A measurement assessment requires:
- Instrument and calibration identifiers.
- Calibration status and validity interval.
- Traceability reference.
- Measurement range and unit.
- Instrument/calibration standard uncertainty.
- Observation timestamp, protocol and raw evidence reference.
- Required environmental conditions.

Assessment states:
- VALID: supplied calibration metadata and documented conditions pass the implemented checks and uncertainty combination is justified.
- INVALID: at least one explicit validity condition fails.
- INDETERMINATE: essential uncertainty relationship is not established.

Root-sum-square combination is permitted by this helper only when the caller explicitly declares the uncertainty components independent. Correlated inputs require covariance-aware propagation outside this helper.

**Limitations:** the implementation checks supplied metadata; it does not contact calibration laboratories, authenticate certificates, establish SI traceability, validate instrument firmware, or infer uncertainty from raw signals. Calibration reference authentication and the uncertainty budget remain human/authoritative-process responsibilities.

Implemented: \`src/dingoos_labs/measurement.py\`.

## 4. Statistical analysis

The current implementation provides descriptive statistics and a deterministic nonparametric percentile bootstrap interval for the arithmetic mean.

Every report must retain:
- Sample size and raw-data evidence reference.
- Sampling/selection method.
- Inclusion/exclusion rules.
- Missing-data handling.
- Dependence and distribution assumptions.
- Method, confidence level, replicate count and random seed.
- Relevant effect size and uncertainty.
- Deviations from preregistered analysis.

The bootstrap helper assumes observations are representative and IID. It does not correct selection bias, confounding, autocorrelation, clustering, multiple comparisons, optional stopping or poor experimental design. Its interval is not by itself a significance test or proof of a physical effect. Specialized designs require an appropriate statistical method and independent review.

Implemented: \`src/dingoos_labs/statistics.py\`.

## 5. Independent verification

A scientific review record must identify:
- Claim and review scope.
- Originator and reviewer.
- Review timestamp.
- Independent methods applied.
- Evidence reviewed.
- Findings and outcome.

The reviewer identifier must differ from the originator identifier. Outcomes are PASS, FAIL or INCONCLUSIVE.

The implemented identity comparison does not authenticate a person's identity, competence, independence of institution, conflicts of interest or digital signature. Those require the authoritative DingoOS identity, access-control and review processes once recovered.

Implemented: \`src/dingoos_labs/verification.py\`.

## 6. Scientific evidence gate

The gate helper returns VALIDATED only when:
- Evidence byte integrity is verified.
- Provenance has been reviewed.
- Every supplied measurement assessment is VALID.
- Statistical analysis has been reviewed.
- Independent scientific review outcome is PASS.

Otherwise it returns BLOCKED with explicit blockers.

This helper is a conservative workflow check, not an automated determination that a scientific claim is true. A claim-specific review must still examine alternative explanations, model assumptions, effect size, uncertainty, replication, falsifiability and the precise domain in which the evidence applies.

## 7. Mandatory oversight stages

- SE-01 Source provenance and chain of custody.
- SE-02 Original byte preservation and integrity.
- SE-03 Acquisition method and experimental protocol.
- SE-04 Instrument calibration and traceability.
- SE-05 Measurement range, environment and uncertainty.
- SE-06 Statistical design and analysis validity.
- SE-07 Mathematical derivation and dimensional coherence.
- SE-08 Alternative explanations and contradictory evidence.
- SE-09 Independent recomputation or replication.
- SE-10 Independent scientific review.
- SE-11 Claim-to-evidence traceability and conclusion scope.
- SE-12 Revision, correction and audit history.

Each stage must be marked PASS, FAIL, OPEN, UNVERIFIED or NOT APPLICABLE with a reason and supporting references. NOT APPLICABLE requires justification. Missing evidence is not a PASS.

## 8. Repository implementation map

- \`src/dingoos_labs/evidence.py\`: evidence record, content digest and byte verification.
- \`src/dingoos_labs/measurement.py\`: calibration metadata and measurement validity assessment.
- \`src/dingoos_labs/statistics.py\`: descriptive statistics and bootstrap interval.
- \`src/dingoos_labs/verification.py\`: independent review record and scientific evidence gate.
- \`tests/labs/test_mcivp_*.py\`: automated tests for the above controls.
- \`.github/workflows/dingoos-labs-oie.yml\`: automated test workflow.

## 9. Explicitly not implemented

The following remain OPEN / NOT VERIFIED:
- Authenticated identity, role and conflict-of-interest management.
- Cryptographic signatures and trusted timestamping.
- Persistent append-only evidence repository and retention policy.
- Automated source authenticity and chain-of-custody validation.
- Raw instrument acquisition, parsing and immutable archival.
- Calibration certificate verification against issuing authorities.
- Full SI traceability and metrology uncertainty budgets.
- Covariance matrices and general uncertainty propagation.
- Statistical models for time series, clustered data, multiple testing, Bayesian inference and causal inference.
- Independent reviewer credential verification and external replication orchestration.
- Automatic scientific claim validation or release authorization.
- Integration with canonical DingoOS evidence/requirements/identity services.

Do not claim these capabilities exist until recovered, implemented and verified.

## 10. Workstream and IP boundaries

Only public-safe derived material is committed to Side-bet. Protected original DingoOS/BIF source and confidential designs are excluded. The adopted Recovery Engine baseline is not modified by this increment. SW-ZPE-01 remains separate.

## Revision history

| Revision | Date | Change |
|---|---|---|
| 0.1 | 28 Nov 2026 | Initial executable evidence, metrology, descriptive/bootstrap statistics and independent review controls. |

**Governing principle:** preserve the observation, prove what can be checked, quantify what is uncertain, challenge the interpretation, and limit the conclusion to what the evidence establishes.
