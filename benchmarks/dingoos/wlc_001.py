"""Deterministic derived harness for DingoOS WLC-001.

This is a separately authored DERIVED_RECONSTRUCTION of the historical
DigitalTwin algorithm. It does not modify or authenticate the source compilation.
Standard-library only; no clock, random IDs, sensor noise, or external services.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import math
from typing import Any


@dataclass(frozen=True)
class WLC001Inputs:
    mass_kg: float = 5.0
    stiffness_n_per_m: float = 500.0
    damping_n_s_per_m: float = 0.05
    duration_s: float = 2.0
    time_step_s: float = 0.001
    initial_displacement_m: float = 1.0
    initial_velocity_m_per_s: float = 0.0

    def validate(self) -> None:
        if self.mass_kg <= 0 or self.stiffness_n_per_m <= 0:
            raise ValueError("mass and stiffness must be positive")
        if self.damping_n_s_per_m < 0:
            raise ValueError("damping must be non-negative")
        if self.duration_s <= 0 or self.time_step_s <= 0:
            raise ValueError("duration and time step must be positive")
        ratio = self.duration_s / self.time_step_s
        if not math.isclose(ratio, round(ratio), rel_tol=0.0, abs_tol=1e-12):
            raise ValueError("duration must be an integer multiple of time step")


def analytical_undamped_frequency_hz(inputs: WLC001Inputs) -> float:
    inputs.validate()
    return math.sqrt(inputs.stiffness_n_per_m / inputs.mass_kg) / (2.0 * math.pi)


def analytical_damped_frequency_hz(inputs: WLC001Inputs) -> float:
    """Underdamped natural frequency, f_d = sqrt(k/m-(c/2m)^2)/(2*pi)."""
    inputs.validate()
    omega_squared = (
        inputs.stiffness_n_per_m / inputs.mass_kg
        - (inputs.damping_n_s_per_m / (2.0 * inputs.mass_kg)) ** 2
    )
    if omega_squared <= 0:
        raise ValueError("WLC-001 frequency estimator requires an underdamped system")
    return math.sqrt(omega_squared) / (2.0 * math.pi)


def source_faithful_explicit_euler(inputs: WLC001Inputs) -> dict[str, Any]:
    """Reproduce the historical DigitalTwin update and zero-crossing estimator."""
    inputs.validate()
    steps = int(inputs.duration_s / inputs.time_step_s)
    x = inputs.initial_displacement_m
    v = inputs.initial_velocity_m_per_s
    crossings: list[float] = []

    for index in range(steps):
        time_s = index * inputs.time_step_s
        acceleration = (
            -inputs.damping_n_s_per_m * v - inputs.stiffness_n_per_m * x
        ) / inputs.mass_kg
        velocity_next = v + acceleration * inputs.time_step_s
        displacement_next = x + v * inputs.time_step_s

        if index > 0 and (
            (x <= 0.0 and displacement_next > 0.0)
            or (x >= 0.0 and displacement_next < 0.0)
        ):
            crossings.append(time_s)
        x, v = displacement_next, velocity_next

    half_periods = [b - a for a, b in zip(crossings, crossings[1:])]
    mean_half_period = (
        sum(half_periods) / len(half_periods) if half_periods else None
    )
    estimated_hz = (
        1.0 / (2.0 * mean_half_period) if mean_half_period is not None else None
    )
    return {
        "step_count": steps,
        "zero_crossing_times_s": crossings,
        "half_periods_s": half_periods,
        "mean_half_period_s": mean_half_period,
        "estimated_frequency_hz": estimated_hz,
    }


def run_workload(inputs: WLC001Inputs | None = None) -> dict[str, Any]:
    inputs = inputs or WLC001Inputs()
    inputs.validate()
    numerical = source_faithful_explicit_euler(inputs)
    analytical_damped = analytical_damped_frequency_hz(inputs)
    analytical_undamped = analytical_undamped_frequency_hz(inputs)
    numerical_hz = numerical["estimated_frequency_hz"]
    return {
        "workload_id": "WLC-001",
        "inputs": asdict(inputs),
        "analytical_damped_frequency_hz": analytical_damped,
        "analytical_undamped_frequency_hz": analytical_undamped,
        "numerical": numerical,
        "absolute_error_vs_damped_hz": (
            abs(numerical_hz - analytical_damped) if numerical_hz is not None else None
        ),
        "epistemic_limit": (
            "Internal analytical/numerical model comparison only; not empirical "
            "measurement, experimental validation, or physical validation."
        ),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run_workload(), indent=2, sort_keys=True))
