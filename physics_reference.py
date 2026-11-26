"""Independent standard-library physics reference calculations.

Scope: linear free damped oscillator and lossless dielectric interface optics.
This is a small educational/reference PoC, not a production solver.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
import math


def _finite_real(name: str, value: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a real number")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite")
    return result


@dataclass(frozen=True)
class OscillatorParameters:
    """Parameters for m*x'' + c*x' + k*x = 0, with m,k>0 and c>=0."""
    mass: float
    stiffness: float
    damping: float = 0.0

    def __post_init__(self) -> None:
        m = _finite_real("mass", self.mass)
        k = _finite_real("stiffness", self.stiffness)
        c = _finite_real("damping", self.damping)
        if m <= 0.0 or k <= 0.0 or c < 0.0:
            raise ValueError("mass and stiffness must be > 0; damping must be >= 0")
        object.__setattr__(self, "mass", m)
        object.__setattr__(self, "stiffness", k)
        object.__setattr__(self, "damping", c)

    @property
    def natural_angular_frequency(self) -> float:
        return math.sqrt(self.stiffness / self.mass)

    @property
    def natural_frequency_hz(self) -> float:
        return self.natural_angular_frequency / (2.0 * math.pi)

    @property
    def damping_ratio(self) -> float:
        return self.damping / (2.0 * math.sqrt(self.mass * self.stiffness))

    @property
    def quality_factor(self) -> float:
        return math.inf if self.damping == 0.0 else math.sqrt(self.mass * self.stiffness) / self.damping

    @property
    def discriminant(self) -> float:
        return self.damping**2 - 4.0 * self.mass * self.stiffness

    @property
    def regime(self) -> str:
        if self.discriminant < 0.0:
            return "underdamped"
        if self.discriminant > 0.0:
            return "overdamped"
        return "critically_damped"

    def free_response(
        self, time_s: float, initial_displacement_m: float = 1.0,
        initial_velocity_m_s: float = 0.0,
    ) -> float:
        """Analytic displacement for t>=0 and the declared initial conditions."""
        t = _finite_real("time_s", time_s)
        x0 = _finite_real("initial_displacement_m", initial_displacement_m)
        v0 = _finite_real("initial_velocity_m_s", initial_velocity_m_s)
        if t < 0.0:
            raise ValueError("time_s must be >= 0")
        m, c = self.mass, self.damping
        alpha, delta = c / (2.0 * m), self.discriminant
        if delta < 0.0:
            wd = math.sqrt(-delta) / (2.0 * m)
            return math.exp(-alpha*t) * (
                x0*math.cos(wd*t) + ((v0 + alpha*x0)/wd)*math.sin(wd*t)
            )
        if delta == 0.0:
            return (x0 + (v0 + alpha*x0)*t) * math.exp(-alpha*t)
        root = math.sqrt(delta)
        r1, r2 = (-c + root)/(2*m), (-c - root)/(2*m)
        a, b = (v0-r2*x0)/(r1-r2), (r1*x0-v0)/(r1-r2)
        return a*math.exp(r1*t) + b*math.exp(r2*t)

    def stored_energy_j(self, displacement_m: float, velocity_m_s: float) -> float:
        x = _finite_real("displacement_m", displacement_m)
        v = _finite_real("velocity_m_s", velocity_m_s)
        return 0.5*self.mass*v*v + 0.5*self.stiffness*x*x


def rk4_free_response(
    parameters: OscillatorParameters, duration_s: float, step_s: float,
    initial_displacement_m: float = 1.0, initial_velocity_m_s: float = 0.0,
) -> float:
    """Classical fixed-step RK4 comparison; shortens the last step to land at t."""
    if not isinstance(parameters, OscillatorParameters):
        raise TypeError("parameters must be OscillatorParameters")
    duration = _finite_real("duration_s", duration_s)
    step = _finite_real("step_s", step_s)
    x = _finite_real("initial_displacement_m", initial_displacement_m)
    v = _finite_real("initial_velocity_m_s", initial_velocity_m_s)
    if duration < 0.0 or step <= 0.0:
        raise ValueError("duration_s must be >= 0 and step_s must be > 0")
    m, c, k = parameters.mass, parameters.damping, parameters.stiffness

    def rhs(xx: float, vv: float) -> tuple[float, float]:
        return vv, -(c*vv + k*xx)/m

    elapsed = 0.0
    while elapsed < duration:
        h = min(step, duration-elapsed)
        k1x, k1v = rhs(x, v)
        k2x, k2v = rhs(x+0.5*h*k1x, v+0.5*h*k1v)
        k3x, k3v = rhs(x+0.5*h*k2x, v+0.5*h*k2v)
        k4x, k4v = rhs(x+h*k3x, v+h*k3v)
        x += h*(k1x+2*k2x+2*k3x+k4x)/6.0
        v += h*(k1v+2*k2v+2*k3v+k4v)/6.0
        elapsed += h
    return x


def _positive_index(name: str, value: float) -> float:
    number = _finite_real(name, value)
    if number <= 0.0:
        raise ValueError(f"{name} must be > 0")
    return number


def _incidence_angle(angle_rad: float) -> float:
    angle = _finite_real("incidence_angle_rad", angle_rad)
    if angle < 0.0 or angle >= math.pi/2:
        raise ValueError("incidence angle must be in [0, pi/2)")
    return angle


@dataclass(frozen=True)
class FresnelPower:
    reflected_s: float
    transmitted_s: float
    reflected_p: float
    transmitted_p: float
    reflected_unpolarized: float
    transmitted_unpolarized: float
    transmitted_angle_rad: float | None
    total_internal_reflection: bool


def critical_angle_rad(n_incident: float, n_transmitted: float) -> float | None:
    n1, n2 = _positive_index("n_incident", n_incident), _positive_index("n_transmitted", n_transmitted)
    return math.asin(n2/n1) if n1 > n2 else None


def snell_angle_rad(n_incident: float, n_transmitted: float, incidence_angle_rad: float) -> float | None:
    n1, n2 = _positive_index("n_incident", n_incident), _positive_index("n_transmitted", n_transmitted)
    theta_i = _incidence_angle(incidence_angle_rad)
    sine_t = (n1/n2)*math.sin(theta_i)
    return None if sine_t >= 1.0 else math.asin(sine_t)


def fresnel_power(n_incident: float, n_transmitted: float, incidence_angle_rad: float) -> FresnelPower:
    """s/p and unpolarized POWER R/T for lossless isotropic non-magnetic media."""
    n1, n2 = _positive_index("n_incident", n_incident), _positive_index("n_transmitted", n_transmitted)
    theta_i = _incidence_angle(incidence_angle_rad)
    theta_t = snell_angle_rad(n1, n2, theta_i)
    if theta_t is None:
        return FresnelPower(1.0, 0.0, 1.0, 0.0, 1.0, 0.0, None, True)
    ci, ct = math.cos(theta_i), math.cos(theta_t)
    rs = ((n1*ci-n2*ct)/(n1*ci+n2*ct))**2
    rp = ((n2*ci-n1*ct)/(n2*ci+n1*ct))**2
    ts, tp = 1.0-rs, 1.0-rp
    return FresnelPower(rs, ts, rp, tp, 0.5*(rs+rp), 0.5*(ts+tp), theta_t, False)


def demo() -> dict[str, object]:
    oscillator = OscillatorParameters(1.0, 100.0, 1.0)
    optical = fresnel_power(1.5, 1.33, math.radians(45.0))
    return {
        "oscillator": {
            "natural_frequency_hz": oscillator.natural_frequency_hz,
            "damping_ratio": oscillator.damping_ratio,
            "quality_factor": oscillator.quality_factor,
            "regime": oscillator.regime,
            "displacement_at_1s_m": oscillator.free_response(1.0),
        },
        "optics": {
            "incidence_angle_deg": 45.0,
            "transmitted_angle_deg": math.degrees(optical.transmitted_angle_rad),
            "critical_angle_deg": math.degrees(critical_angle_rad(1.5, 1.33)),
            "reflectance_unpolarized": optical.reflected_unpolarized,
            "transmittance_unpolarized": optical.transmitted_unpolarized,
            "energy_sum": optical.reflected_unpolarized + optical.transmitted_unpolarized,
        },
    }


if __name__ == "__main__":
    print(json.dumps(demo(), indent=2, sort_keys=True, allow_nan=False))
