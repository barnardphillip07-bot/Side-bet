import pytest
from dingoos_labs.oie import (
    Candidate, Comparison, Constraint, EvaluationError, Measurement, Metric, evaluate,
)


def m(v, lo=None, hi=None, unit="W", basis="MEASURED"):
    return Measurement(v, v if lo is None else lo, v if hi is None else hi,
                       unit, basis, f"evidence:{v}")


def c(name, p, e, protocol="P", envelope="25C/1atm", basis="MEASURED"):
    return Candidate(name, protocol, envelope, {
        "power": m(p, unit="W", basis=basis),
        "eff": m(e, unit="1", basis=basis),
    })


def spec():
    return Comparison("base", (Metric("power", "W", "minimize"),
                               Metric("eff", "1", "maximize")),
                      (Constraint("eff", lower=.80),))


def test_pareto_keeps_tradeoffs_without_composite_score():
    r = evaluate([c("base",100,.82), c("low-power",90,.81),
                  c("high-eff",98,.87)], spec())
    assert set(r.pareto_front) == {"low-power", "high-eff"}


def test_interval_dominance_and_overlap():
    metric = (Metric("loss","W","minimize"),)
    r = evaluate([Candidate("base","P","E",{"loss":m(10,9.8,10.2)}),
                  Candidate("better","P","E",{"loss":m(8,7.8,8.2)})],
                 Comparison("base",metric))
    assert r.dominance == (("better","base"),)
    r2 = evaluate([Candidate("base","P","E",{"loss":m(10,9,11)}),
                   Candidate("uncertain","P","E",{"loss":m(9.5,8.5,10.5)})],
                  Comparison("base",metric))
    assert set(r2.pareto_front) == {"base","uncertain"}


def test_constraint_is_conservative():
    metric=(Metric("eff","1","maximize"),)
    cs=[Candidate("base","P","E",{"eff":m(.85,unit="1")}),
        Candidate("overlap","P","E",{"eff":m(.81,.79,.83,unit="1")}),
        Candidate("fail","P","E",{"eff":m(.7,.68,.72,unit="1")})]
    r=evaluate(cs,Comparison("base",metric,(Constraint("eff",lower=.8),)))
    states={x.id:x.feasibility for x in r.results}
    assert states == {"base":"FEASIBLE","overlap":"INDETERMINATE","fail":"INFEASIBLE"}
    assert r.pareto_front == ("base",)


@pytest.mark.parametrize("kwargs, msg", [
    ({"protocol":"P2"},"protocol"),
    ({"envelope":"40C"},"operating envelope"),
])
def test_non_equivalent_conditions_rejected(kwargs,msg):
    with pytest.raises(EvaluationError,match=msg):
        evaluate([c("base",100,.82),c("other",90,.85,**kwargs)],spec())


def test_mixed_evidence_and_units_rejected():
    with pytest.raises(EvaluationError,match="mixed evidence"):
        evaluate([c("base",100,.82),c("other",90,.85,basis="SIMULATED")],spec())
    metric=(Metric("loss","W","minimize"),)
    with pytest.raises(EvaluationError,match="unit mismatch"):
        evaluate([Candidate("base","P","E",{"loss":m(10)}),
                  Candidate("other","P","E",{"loss":m(8,unit="kW")})],
                 Comparison("base",metric))


def test_direction_aware_baseline_improvement():
    candidates=[
        Candidate("base","P","E",{"power":m(100,99,101),"eff":m(.82,.81,.83,unit="1")}),
        Candidate("new","P","E",{"power":m(90,89,91),"eff":m(.85,.84,.86,unit="1")}),
    ]
    r=evaluate(candidates,Comparison("base",(Metric("power","W","minimize"),
                                               Metric("eff","1","maximize"))))
    new=next(x for x in r.results if x.id=="new")
    delta={x[0]:x for x in new.improvements}
    assert delta["power"][1:3] == (8,12)
    assert delta["power"][3] == delta["eff"][3] == "IMPROVED"


def test_invalid_interval_nonfinite_and_duplicate_ids_rejected():
    with pytest.raises(EvaluationError,match="lower <= value <= upper"):
        m(1,1.1,1.2)
    with pytest.raises(EvaluationError,match="finite"):
        m(float("nan"))
    with pytest.raises(EvaluationError,match="unique"):
        evaluate([c("same",100,.82),c("same",90,.84)],spec())


def test_baseline_and_evidence_reference_required():
    with pytest.raises(EvaluationError,match="baseline_id"):
        evaluate([c("a",100,.82),c("b",90,.84)],
                 Comparison("missing",spec().metrics,spec().constraints))
    with pytest.raises(EvaluationError,match="evidence_ref"):
        Measurement(1,1,1,"m","MEASURED","")
