import pytest

from dingoos_labs.measurement import (
    CalibrationRecord, MeasurementError, MeasurementObservation, assess_measurement,
)


def calibration(**kwargs):
    values = dict(
        calibration_id="CAL-01", instrument_id="SENSOR-01",
        calibrated_at="2026-11-01T00:00:00Z", valid_until="2027-01-01T00:00:00Z",
        status="VALID", unit="m/s", range_lower=0.0, range_upper=100.0,
        standard_uncertainty=0.3, traceability_reference="LAB-CERT-77",
    )
    values.update(kwargs)
    return CalibrationRecord(**values)


def observation(**kwargs):
    values = dict(
        observation_id="OBS-01", instrument_id="SENSOR-01", calibration_id="CAL-01",
        measured_at="2026-11-28T00:00:00Z", value=12.0, unit="m/s",
        standard_uncertainty=0.4, raw_evidence_id="EV-RAW-01",
        protocol_id="PROTOCOL-01", environment=(("temperature_C", 22.0),),
    )
    values.update(kwargs)
    return MeasurementObservation(**values)


def test_valid_measurement_combines_independent_uncertainties():
    result = assess_measurement(
        observation(), calibration(),
        environment_limits={"temperature_C": (15.0, 30.0)},
        independent_uncertainty_components=True,
    )
    assert result.status == "VALID"
    assert result.combined_standard_uncertainty == pytest.approx(0.5)


def test_uncertainty_not_combined_without_independence_claim():
    result = assess_measurement(observation(), calibration())
    assert result.status == "INDETERMINATE"
    assert result.combined_standard_uncertainty is None


def test_expired_or_out_of_range_calibration_is_invalid():
    expired = assess_measurement(
        observation(measured_at="2027-02-01T00:00:00Z"), calibration(),
        independent_uncertainty_components=True,
    )
    assert expired.status == "INVALID"
    out_of_range = assess_measurement(
        observation(value=120.0), calibration(),
        independent_uncertainty_components=True,
    )
    assert out_of_range.status == "INVALID"


def test_missing_or_out_of_limits_environment_is_invalid():
    missing = assess_measurement(
        observation(environment=()), calibration(),
        environment_limits={"temperature_C": (10.0, 30.0)},
        independent_uncertainty_components=True,
    )
    assert missing.status == "INVALID"
    outside = assess_measurement(
        observation(environment=(("temperature_C", 35.0),)), calibration(),
        environment_limits={"temperature_C": (10.0, 30.0)},
        independent_uncertainty_components=True,
    )
    assert outside.status == "INVALID"


def test_invalid_environment_limits_rejected():
    with pytest.raises(MeasurementError, match="invalid environmental limits"):
        assess_measurement(
            observation(), calibration(),
            environment_limits={"temperature_C": (30.0, 10.0)},
            independent_uncertainty_components=True,
        )


def test_naive_time_rejected():
    with pytest.raises(MeasurementError, match="timezone"):
        observation(measured_at="2026-11-28T00:00:00")
