"""Derived public-safe DingoOS laboratory engineering tools."""
from .evidence import EvidenceError, EvidenceRecord, create_evidence_record, verify_evidence_bytes, verify_manifest
from .measurement import (
    CalibrationRecord, MeasurementAssessment, MeasurementError,
    MeasurementObservation, assess_measurement,
)
from .oie import (
    Candidate, CandidateResult, Comparison, Constraint, EvaluationError,
    Measurement, Metric, Report, evaluate,
)
from .statistics import (
    BootstrapInterval, DescriptiveSummary, StatisticalError,
    bootstrap_mean_interval, describe,
)
from .verification import (
    GateDecision, IndependentReview, ScientificClaim, ScientificEvidenceGate,
    VerificationError, assess_scientific_evidence,
)

__all__ = [
    "EvidenceError", "EvidenceRecord", "create_evidence_record",
    "verify_evidence_bytes", "verify_manifest",
    "CalibrationRecord", "MeasurementAssessment", "MeasurementError",
    "MeasurementObservation", "assess_measurement",
    "Candidate", "CandidateResult", "Comparison", "Constraint", "EvaluationError",
    "Measurement", "Metric", "Report", "evaluate",
    "BootstrapInterval", "DescriptiveSummary", "StatisticalError",
    "bootstrap_mean_interval", "describe",
    "GateDecision", "IndependentReview", "ScientificClaim",
    "ScientificEvidenceGate", "VerificationError", "assess_scientific_evidence",
]
