"""Derived, public-safe Objective Innovation Engineering comparison evaluator."""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Mapping, Sequence


class EvaluationError(ValueError):
    """Invalid or non-comparable engineering evaluation input."""


@dataclass(frozen=True, slots=True)
class Metric:
    id: str
    unit: str
    direction: str  # minimize | maximize

    def __post_init__(self):
        if not self.id.strip() or not self.unit.strip():
            raise EvaluationError("metric id and unit are required")
        if self.direction not in {"minimize", "maximize"}:
            raise EvaluationError("direction must be minimize or maximize")


@dataclass(frozen=True, slots=True)
class Measurement:
    value: float
    lower: float
    upper: float
    unit: str
    evidence_basis: str
    evidence_ref: str

    def __post_init__(self):
        if not all(isfinite(x) for x in (self.value, self.lower, self.upper)):
            raise EvaluationError("measurement values must be finite")
        if not self.lower <= self.value <= self.upper:
            raise EvaluationError("require lower <= value <= upper")
        if not all(isinstance(x, str) and x.strip() for x in
                   (self.unit, self.evidence_basis, self.evidence_ref)):
            raise EvaluationError("unit, evidence_basis and evidence_ref are required")


@dataclass(frozen=True, slots=True)
class Constraint:
    metric_id: str
    lower: float | None = None
    upper: float | None = None

    def __post_init__(self):
        if not self.metric_id.strip() or (self.lower is None and self.upper is None):
            raise EvaluationError("constraint requires metric id and at least one bound")
        if any(x is not None and not isfinite(x) for x in (self.lower, self.upper)):
            raise EvaluationError("constraint bounds must be finite")
        if self.lower is not None and self.upper is not None and self.lower > self.upper:
            raise EvaluationError("constraint lower bound exceeds upper bound")


@dataclass(frozen=True, slots=True)
class Candidate:
    id: str
    protocol_id: str
    operating_envelope: str
    measurements: Mapping[str, Measurement]

    def __post_init__(self):
        if not all(isinstance(x, str) and x.strip() for x in
                   (self.id, self.protocol_id, self.operating_envelope)):
            raise EvaluationError("candidate id, protocol and operating envelope are required")


@dataclass(frozen=True, slots=True)
class Comparison:
    baseline_id: str
    metrics: tuple[Metric, ...]
    constraints: tuple[Constraint, ...] = ()

    def __post_init__(self):
        ids = [m.id for m in self.metrics]
        cids = [c.metric_id for c in self.constraints]
        if not self.baseline_id.strip() or not ids or len(ids) != len(set(ids)):
            raise EvaluationError("baseline and unique objective metrics are required")
        if len(cids) != len(set(cids)) or set(cids) - set(ids):
            raise EvaluationError("constraints must uniquely reference declared metrics")


@dataclass(frozen=True, slots=True)
class CandidateResult:
    id: str
    feasibility: str  # FEASIBLE | INFEASIBLE | INDETERMINATE
    reasons: tuple[str, ...]
    improvements: tuple[tuple[str, float, float, str], ...]


@dataclass(frozen=True, slots=True)
class Report:
    baseline_id: str
    results: tuple[CandidateResult, ...]
    pareto_front: tuple[str, ...]
    dominance: tuple[tuple[str, str], ...]
    protocol_id: str
    operating_envelope: str
    evidence_basis: tuple[tuple[str, str], ...]


def _constraint(m: Measurement, c: Constraint) -> tuple[str, str]:
    if c.lower is not None and m.upper < c.lower:
        return "FAIL", f"{c.metric_id}: interval entirely below minimum"
    if c.upper is not None and m.lower > c.upper:
        return "FAIL", f"{c.metric_id}: interval entirely above maximum"
    if ((c.lower is None or m.lower >= c.lower) and
            (c.upper is None or m.upper <= c.upper)):
        return "PASS", f"{c.metric_id}: interval inside bounds"
    return "INDETERMINATE", f"{c.metric_id}: interval overlaps a limit"


def _improvement(candidate: Measurement, baseline: Measurement, metric: Metric):
    if metric.direction == "minimize":
        lo, hi = baseline.lower - candidate.upper, baseline.upper - candidate.lower
    else:
        lo, hi = candidate.lower - baseline.upper, candidate.upper - baseline.lower
    state = ("IMPROVED" if lo > 0 else "REGRESSED" if hi < 0 else
             "NO_CHANGE" if lo == hi == 0 else "INDETERMINATE")
    return (metric.id, lo, hi, state)


def _dominates(a: Candidate, b: Candidate, metrics: Sequence[Metric]) -> bool:
    strict = False
    for metric in metrics:
        x, y = a.measurements[metric.id], b.measurements[metric.id]
        if metric.direction == "minimize":
            if x.upper > y.lower:
                return False
            strict |= x.upper < y.lower
        else:
            if x.lower < y.upper:
                return False
            strict |= x.lower > y.upper
    return strict


def evaluate(candidates: Sequence[Candidate], spec: Comparison) -> Report:
    """Return feasibility, baseline deltas and robust Pareto dominance.

    All candidates must share protocol, operating envelope and evidence basis
    per metric. Units are exact-match strings; no conversion is attempted.
    """
    if len(candidates) < 2:
        raise EvaluationError("at least two candidates are required")
    ids = [c.id for c in candidates]
    if len(ids) != len(set(ids)):
        raise EvaluationError("candidate ids must be unique")
    if spec.baseline_id not in ids:
        raise EvaluationError("baseline_id must identify a supplied candidate")
    if len({c.protocol_id for c in candidates}) != 1:
        raise EvaluationError("candidates must share one protocol")
    if len({c.operating_envelope for c in candidates}) != 1:
        raise EvaluationError("candidates must share one operating envelope")

    metric_ids = {m.id for m in spec.metrics}
    bases = []
    for metric in spec.metrics:
        labels = set()
        for candidate in candidates:
            if set(candidate.measurements) != metric_ids:
                raise EvaluationError(f"{candidate.id}: metrics must exactly match specification")
            measurement = candidate.measurements[metric.id]
            if measurement.unit != metric.unit:
                raise EvaluationError(f"{candidate.id}/{metric.id}: unit mismatch")
            labels.add(measurement.evidence_basis)
        if len(labels) != 1:
            raise EvaluationError(f"{metric.id}: mixed evidence bases cannot be ranked")
        bases.append((metric.id, next(iter(labels))))

    baseline = next(c for c in candidates if c.id == spec.baseline_id)
    constraint_map = {c.metric_id: c for c in spec.constraints}
    results, eligible = [], []
    for candidate in candidates:
        failures, uncertain = [], []
        for metric_id, rule in constraint_map.items():
            state, reason = _constraint(candidate.measurements[metric_id], rule)
            if state == "FAIL":
                failures.append(reason)
            elif state == "INDETERMINATE":
                uncertain.append(reason)
        feasibility = ("INFEASIBLE" if failures else
                       "INDETERMINATE" if uncertain else "FEASIBLE")
        reasons = tuple(failures + uncertain)
        if feasibility == "FEASIBLE":
            eligible.append(candidate)
        improvements = tuple(
            (m.id, 0.0, 0.0, "BASELINE") if candidate.id == baseline.id else
            _improvement(candidate.measurements[m.id], baseline.measurements[m.id], m)
            for m in spec.metrics
        )
        results.append(CandidateResult(candidate.id, feasibility, reasons, improvements))

    pairs, dominated = [], set()
    for a in eligible:
        for b in eligible:
            if a.id != b.id and _dominates(a, b, spec.metrics):
                pairs.append((a.id, b.id))
                dominated.add(b.id)
    front = tuple(c.id for c in eligible if c.id not in dominated)
    return Report(spec.baseline_id, tuple(results), front, tuple(pairs),
                  candidates[0].protocol_id, candidates[0].operating_envelope, tuple(bases))
