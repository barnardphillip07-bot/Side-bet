"""Measurement validity and uncertainty checks for DingoOS MCIVP."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from math import hypot, isfinite


class MeasurementError(ValueError):
    """Invalid calibration or measurement record."""


def _time(value: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError) as exc:
        raise MeasurementError("timestamps must be ISO-8601") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise MeasurementError("timestamps must include a timezone")
    return parsed


def _required(name: str, value: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise MeasurementError(f"{name} is required")


@dataclass(frozen=True, slots=True)
class CalibrationRecord:
    calibration_id: str
    instrument_id: str
    calibrated_at: str
    valid_until: str
    status: str
    unit: str
    range_lower: float
    range_upper: float
    standard_uncertainty: float
    traceability_reference: str

    def __post_init__(self):
        for field in ("calibration_id", "instrument_id", "status", "unit",
                      "traceability_reference"):
            _required(field, getattr(self, field))
        start, end = _time(self.calibrated_at), _time(self.valid_until)
        if end <= start:
            raise MeasurementError("calibration validity interval must be positive")
        if self.status not in {"VALID", "REVOKED", "SUSPENDED"}:
            raise MeasurementError("status must be VALID, REVOKED or SUSPENDED")
        if not all(isfinite(x) for x in
                   (self.range_lower, self.range_upper, self.standard_uncertainty)):
            raise MeasurementError("calibration values must be finite")
        if self.range_lower >= self.range_upper or self.standard_uncertainty < 0:
            raise MeasurementError("invalid calibration range or uncertainty")


@dataclass(frozen=True, slots=True)
class MeasurementObservation:
    observation_id: str
    instrument_id: str
    calibration_id: str
    measured_at: str
    value: float
    unit: str
    standard_uncertainty: float
    raw_evidence_id: str
    protocol_id: str
    environment: tuple[tuple[str, float], ...] = ()

    def __post_init__(self):
        for field in ("observation_id", "instrument_id", "calibration_id",
                      "unit", "raw_evidence_id", "protocol_id"):
            _required(field, getattr(self, field))
        _time(self.measured_at)
        if not all(isfinite(x) for x in (self.value, self.standard_uncertainty)):
            raise MeasurementError("measurement values must be finite")
        if self.standard_uncertainty < 0:
            raise MeasurementError("standard uncertainty cannot be negative")
        keys = [k for k, _ in self.environment]
        if len(keys) != len(set(keys)) or any(not k.strip() for k in keys):
            raise MeasurementError("environment keys must be nonblank and unique")
        if any(not isfinite(v) for _, v in self.environment):
            raise MeasurementError("environment values must be finite")


@dataclass(frozen=True, slots=True)
class MeasurementAssessment:
    observation_id: str
    status: str
    reasons: tuple[str, ...]
    combined_standard_uncertainty: float | None


def assess_measurement(
    observation: MeasurementObservation,
    calibration: CalibrationRecord,
    *,
    environment_limits: dict[str, tuple[float | None, float | None]] | None = None,
    independent_uncertainty_components: bool = False,
) -> MeasurementAssessment:
    """Assess documented metrological validity; does not authenticate calibration.

    Calibration uncertainty is combined by root-sum-square only when the caller
    explicitly states that the components are independent. Correlated components
    require a covariance-aware external calculation and remain uncombined here.
    """
    reasons: list[str] = []
    when = _time(observation.measured_at)
    start, end = _time(calibration.calibrated_at), _time(calibration.valid_until)
    if observation.instrument_id != calibration.instrument_id:
        reasons.append("instrument identifier does not match calibration")
    if observation.calibration_id != calibration.calibration_id:
        reasons.append("calibration identifier does not match observation")
    if calibration.status != "VALID":
        reasons.append("calibration is not in VALID status")
    if not start <= when <= end:
        reasons.append("measurement time is outside calibration validity interval")
    if observation.unit != calibration.unit:
        reasons.append("measurement and calibration units do not match")
    if not calibration.range_lower <= observation.value <= calibration.range_upper:
        reasons.append("measurement is outside calibrated range")
    observed_environment = dict(observation.environment)
    for key, bounds in (environment_limits or {}).items():
        if key not in observed_environment:
            reasons.append(f"required environmental quantity missing: {key}")
            continue
        low, high = bounds
        value = observed_environment[key]
        if low is not None and value < low or high is not None and value > high:
            reasons.append(f"environment outside permitted calibration condition: {key}")
    combined = None
    if independent_uncertainty_components:
        combined = hypot(observation.standard_uncertainty,
                         calibration.standard_uncertainty)
    elif calibration.standard_uncertainty == 0:
        combined = observation.standard_uncertainty
    status = "INVALID" if reasons else (
        "VALID" if combined is not None else "INDETERMINATE"
    )
    if combined is None and not reasons:
        reasons.append("uncertainty components not combined: covariance/independence not established")
    return MeasurementAssessment(observation.observation_id, status,
                                 tuple(reasons), combined)
