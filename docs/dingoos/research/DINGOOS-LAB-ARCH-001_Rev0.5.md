# DINGOOS-LAB-ARCH-001 — Physics Lab / Technology Lab Operating Architecture

- Revision: 0.5
- Date: 28 November 2026
- Repository: barnardphillip07-bot/Side-bet
- Branch: labs/mcivp-001
- Status: DERIVED IMPLEMENTATION BASELINE — MCIVP PARTIAL IMPLEMENTATION — NOT OWNER-RATIFIED CANONICAL DINGOOS ARCHITECTURE

## 1. Laboratory independence

Physics Lab retains authority over physical discovery, experimental methods, measurement validity, uncertainty, replication and empirical conclusions.

Technology Lab retains authority over objective innovation, engineering design, comparative evaluation, prototyping and qualification.

Neither laboratory certifies the other's conclusions. Both use shared quantitative foundations and independent scientific evidence oversight without merging research ownership.

## 2. Mandatory MCIVP oversight

DINGOOS-MCIVP-001 Rev0.2 is the cross-laboratory scientific evidence and mathematical oversight protocol.

Implemented public-safe controls:
- Evidence provenance metadata, parent lineage, manifest digest and SHA-256 byte verification.
- Calibration metadata checks and VALID / INVALID / INDETERMINATE measurement assessment.
- Explicit independence declaration for root-sum-square uncertainty combination.
- Evidence-linked descriptive statistics and deterministic percentile bootstrap.
- Scientific claim record with supporting/contradictory evidence, alternatives, falsification conditions and limitations.
- Independent reviewer/originator separation and claim/evidence coverage checks.
- Conservative CONTROLS_PASSED / BLOCKED gate.
- Automated unit tests and CI workflow.

## 3. Important boundaries

- A digest is not source authentication.
- Calibration metadata validation is not external certificate or SI traceability verification.
- RSS is not valid for correlated uncertainty components without covariance treatment.
- Bootstrap intervals assume representative IID observations and do not establish causality or significance.
- Reviewer ID separation is not identity or conflict-of-interest authentication.
- CONTROLS_PASSED is not a scientific truth determination or release approval.

## 4. Implementation references

- \`docs/dingoos/research/DINGOOS-MCIVP-001_Rev0.2.md\`
- \`src/dingoos_labs/evidence.py\`
- \`src/dingoos_labs/measurement.py\`
- \`src/dingoos_labs/statistics.py\`
- \`src/dingoos_labs/verification.py\`
- \`tests/labs/test_mcivp_*.py\`
- \`.github/workflows/dingoos-labs-oie.yml\`

## 5. Outstanding controls

Authenticated identity and reviewer credentials, cryptographic signatures, trusted timestamps, persistent append-only storage, raw instrument acquisition, external calibration verification, SI traceability, general covariance propagation, advanced statistical methods, external replication and canonical DingoOS service integration remain NOT IMPLEMENTED / NOT VERIFIED.

## 6. Release boundary

Automated tests establish software behaviour only. They do not validate a physical phenomenon, instrument, dataset, scientific hypothesis or canonical DingoOS deployment. No scientific or production release is authorized by this document.

## Revision history

| Revision | Date | Change |
|---|---|---|
| 0.3 | 28 Nov 2026 | Initial repository-controlled laboratory and OIE baseline. |
| 0.4 | 28 Nov 2026 | Adds MCIVP cross-laboratory oversight architecture. |
| 0.5 | 28 Nov 2026 | Adds evidence-linked statistical outputs, claim traceability and conservative review gate. |
