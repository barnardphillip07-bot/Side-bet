import pytest

from dingoos_labs.statistics import (
    StatisticalError, bootstrap_mean_interval, describe,
)


def test_descriptive_statistics_are_reproducible():
    result = describe([1, 2, 3, 4, 5])
    assert result.n == 5
    assert result.mean == pytest.approx(3)
    assert result.median == pytest.approx(3)
    assert result.sample_standard_deviation == pytest.approx(1.5811388301)


def test_bootstrap_interval_is_deterministic_and_contains_estimate():
    a = bootstrap_mean_interval([1, 2, 3, 4, 5], replicates=2000, seed=42)
    b = bootstrap_mean_interval([1, 2, 3, 4, 5], replicates=2000, seed=42)
    assert a == b
    assert a.lower <= a.estimate <= a.upper
    assert a.method == "NONPARAMETRIC_PERCENTILE_BOOTSTRAP_MEAN"
    assert len(a.assumptions) == 3


@pytest.mark.parametrize("data", [[], [1], [1, float("nan")]])
def test_invalid_data_rejected(data):
    with pytest.raises(StatisticalError):
        describe(data)


def test_bootstrap_parameters_validated():
    with pytest.raises(StatisticalError, match="replicates"):
        bootstrap_mean_interval([1, 2], replicates=99)
    with pytest.raises(StatisticalError, match="confidence_level"):
        bootstrap_mean_interval([1, 2], confidence_level=1.0)
