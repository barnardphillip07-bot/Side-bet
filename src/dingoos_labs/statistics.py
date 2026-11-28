"""Transparent descriptive and bootstrap statistics for DingoOS MCIVP.

Intervals are conditional on the stated sampling model. They are not a
universal significance test and do not repair biased or non-independent data.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, sqrt
import random
from statistics import mean, median, stdev


class StatisticalError(ValueError):
    """Invalid statistical input."""


@dataclass(frozen=True, slots=True)
class DescriptiveSummary:
    n: int
    mean: float
    median: float
    sample_standard_deviation: float
    standard_error: float
    minimum: float
    maximum: float


@dataclass(frozen=True, slots=True)
class BootstrapInterval:
    estimate: float
    lower: float
    upper: float
    confidence_level: float
    replicates: int
    seed: int
    method: str
    assumptions: tuple[str, ...]


def _values(data) -> tuple[float, ...]:
    values = tuple(float(x) for x in data)
    if len(values) < 2:
        raise StatisticalError("at least two observations are required")
    if any(not isfinite(x) for x in values):
        raise StatisticalError("all observations must be finite")
    return values


def describe(data) -> DescriptiveSummary:
    values = _values(data)
    sd = stdev(values)
    return DescriptiveSummary(len(values), mean(values), median(values), sd,
                              sd / sqrt(len(values)), min(values), max(values))


def _quantile(sorted_values: tuple[float, ...], probability: float) -> float:
    position = (len(sorted_values) - 1) * probability
    lower = int(position)
    upper = min(lower + 1, len(sorted_values) - 1)
    fraction = position - lower
    return sorted_values[lower] * (1 - fraction) + sorted_values[upper] * fraction


def bootstrap_mean_interval(
    data, *, confidence_level: float = 0.95,
    replicates: int = 10000, seed: int = 0,
) -> BootstrapInterval:
    """Percentile bootstrap CI for the arithmetic mean using a fixed RNG seed."""
    values = _values(data)
    if not 0 < confidence_level < 1:
        raise StatisticalError("confidence_level must be between zero and one")
    if not isinstance(replicates, int) or replicates < 1000:
        raise StatisticalError("at least 1000 bootstrap replicates are required")
    if not isinstance(seed, int):
        raise StatisticalError("seed must be an integer")
    rng = random.Random(seed)
    n = len(values)
    estimates = tuple(sorted(
        sum(values[rng.randrange(n)] for _ in range(n)) / n
        for _ in range(replicates)
    ))
    tail = (1 - confidence_level) / 2
    return BootstrapInterval(
        estimate=mean(values),
        lower=_quantile(estimates, tail),
        upper=_quantile(estimates, 1 - tail),
        confidence_level=confidence_level,
        replicates=replicates,
        seed=seed,
        method="NONPARAMETRIC_PERCENTILE_BOOTSTRAP_MEAN",
        assumptions=(
            "observations are representative of the target sampling process",
            "observations are independent and identically distributed",
            "the empirical distribution is an adequate bootstrap approximation",
        ),
    )
