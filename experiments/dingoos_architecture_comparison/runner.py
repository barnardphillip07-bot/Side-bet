"""Run the same WLC-001 workload through three derived topology variants.

This is an architecture-comparison experiment, not canonical DingoOS runtime code.
The federated variant is a single-host, process-isolated surrogate; it is not a
production multi-host federation or a complete DDEP/authority implementation.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time
from typing import Any

from benchmarks.dingoos.wlc_001 import (
    WLC001Inputs,
    analytical_damped_frequency_hz,
    beta_independent_characteristic_root_frequency_hz,
    source_faithful_explicit_euler,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
WORKLOAD_SPEC_PATH = "docs/dingoos/architecture-comparison/workloads/WLC-001-FROZEN-Rev0.2.json"
WORKLOAD_SPEC_GIT_BLOB_SHA1 = "9517151b6d34ffb6a7686634617ca5fd1592d202"
WORKLOAD_HARNESS_GIT_BLOB_SHA1 = "c4f381fa8298d7d103b6236bb2d9b6a006628b4d"
SOURCE_ARTIFACT_SHA256 = "548a7a5595bd5d81863fbc8815e45e0b0423c51712883b585135cfea3d369752"


def _run_isolated_role(role: str, inputs: WLC001Inputs, inject_failure: bool = False) -> dict[str, Any]:
    env = os.environ.copy()
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = str(REPO_ROOT) + (os.pathsep + existing if existing else "")
    command = [sys.executable, "-m", "experiments.dingoos_architecture_comparison.worker", "--role", role]
    if inject_failure:
        command.append("--inject-failure")
    completed = subprocess.run(
        command,
        input=json.dumps(asdict(inputs), sort_keys=True),
        text=True,
        capture_output=True,
        cwd=REPO_ROOT,
        env=env,
        timeout=30,
        check=True,
    )
    return json.loads(completed.stdout)


def _assemble(
    architecture_id: str,
    alpha_a: dict[str, Any],
    alpha_b: dict[str, Any],
    beta: dict[str, Any],
    elapsed_wall_ns: int,
    topology: dict[str, Any],
) -> dict[str, Any]:
    beta_hz = beta["frequency_hz"]
    numerical_hz = alpha_b["estimated_frequency_hz"]
    return {
        "architecture_id": architecture_id,
        "topology": topology,
        "results": {
            "alpha_a_analytical_damped_hz": alpha_a["frequency_hz"],
            "alpha_b_numerical_hz": numerical_hz,
            "beta_independent_characteristic_root_hz": beta_hz,
            "absolute_numerical_beta_difference_hz": abs(numerical_hz - beta_hz),
            "alpha_b_numerical_detail": alpha_b,
        },
        "assurance": {
            "beta_receives_only_frozen_inputs": True,
            "beta_receives_alpha_outputs": False,
            "independent_codebase": False,
            "independent_toolchain": False,
            "gate_d_independence": "NOT_ESTABLISHED",
            "gamma_authority": "NOT_IN_SCOPE",
            "consequential_effects": False,
            "target_side_enforcement": "NOT_TESTED",
            "fault_gates_a_to_e": "NOT_RUN",
            "physical_validation": "NOT_ESTABLISHED",
        },
        "timing": {
            "elapsed_wall_ns": elapsed_wall_ns,
            "classification": "DIAGNOSTIC_ONLY_NOT_AN_ACCEPTANCE_METRIC",
        },
    }


def run_centralized(inputs: WLC001Inputs | None = None) -> dict[str, Any]:
    inputs = inputs or WLC001Inputs()
    started = time.perf_counter_ns()
    alpha_a = {"frequency_hz": analytical_damped_frequency_hz(inputs)}
    alpha_b = source_faithful_explicit_euler(inputs)
    beta = {"frequency_hz": beta_independent_characteristic_root_frequency_hz(inputs)}
    elapsed = time.perf_counter_ns() - started
    return _assemble(
        "CENTRALIZED_MODULAR", alpha_a, alpha_b, beta, elapsed,
        {"coordinator": "central", "execution": "single_process_direct_calls", "domain_nodes": 0},
    )


def run_federated_process_surrogate(inputs: WLC001Inputs | None = None) -> dict[str, Any]:
    inputs = inputs or WLC001Inputs()
    started = time.perf_counter_ns()
    # Each domain role receives the same frozen input envelope and owns its process.
    with ThreadPoolExecutor(max_workers=3) as pool:
        future_a = pool.submit(_run_isolated_role, "alpha_a", inputs)
        future_b = pool.submit(_run_isolated_role, "alpha_b", inputs)
        future_beta = pool.submit(_run_isolated_role, "beta", inputs)
        alpha_a, alpha_b, beta = future_a.result(), future_b.result(), future_beta.result()
    elapsed = time.perf_counter_ns() - started
    return _assemble(
        "FEDERATED_PROCESS_ISOLATED_SURROGATE", alpha_a, alpha_b, beta, elapsed,
        {"coordinator": "message_envelope_coordinator", "execution": "three_isolated_local_processes", "domain_nodes": 3,
         "federation_limit": "single_host_process_surrogate_no_network_partition_or_remote_state"},
    )


def run_local_first_hybrid(inputs: WLC001Inputs | None = None) -> dict[str, Any]:
    inputs = inputs or WLC001Inputs()
    started = time.perf_counter_ns()
    # Local analytical loops remain in-process; β runs in a separate process.
    alpha_a = {"frequency_hz": analytical_damped_frequency_hz(inputs)}
    alpha_b = source_faithful_explicit_euler(inputs)
    beta = _run_isolated_role("beta", inputs)
    elapsed = time.perf_counter_ns() - started
    return _assemble(
        "LOCAL_FIRST_HYBRID", alpha_a, alpha_b, beta, elapsed,
        {"coordinator": "local", "execution": "local_alpha_modules_plus_isolated_beta_process", "domain_nodes": 1,
         "federation_limit": "no_remote_domain_or_network_federation_in_this_poc"},
    )



def _ft02_summary(architecture_id: str, outcomes: dict[str, dict[str, Any]], elapsed_wall_ns: int) -> dict[str, Any]:
    completed = sorted(role for role, value in outcomes.items() if value["status"] == "COMPLETED")
    failed = sorted(role for role, value in outcomes.items() if value["status"] == "FAILED")
    missing = sorted(role for role in ("alpha_a", "alpha_b", "beta") if role not in completed)
    status = "INCOMPLETE" if failed or missing else "COMPLETE"
    return {
        "architecture_id": architecture_id,
        "fault_id": "FT-02",
        "execution_scope": "WLC-001 topology prototype subset only; not full FT-02 acceptance",
        "workflow_status": status,
        "role_outcomes": outcomes,
        "completed_roles": completed,
        "failed_roles": failed,
        "sigma": {
            "status": status,
            "missing_contributions": missing,
            "accepted_as_complete": status == "COMPLETE",
            "no_silent_promotion": True,
        },
        "timing": {
            "elapsed_wall_ns": elapsed_wall_ns,
            "classification": "DIAGNOSTIC_ONLY_NOT_AN_ACCEPTANCE_METRIC",
        },
    }


def run_ft02_centralized(inputs: WLC001Inputs | None = None) -> dict[str, Any]:
    """Inject Alpha-B failure in the single-process sequential baseline."""
    inputs = inputs or WLC001Inputs()
    started = time.perf_counter_ns()
    outcomes: dict[str, dict[str, Any]] = {}
    try:
        outcomes["alpha_a"] = {"status": "COMPLETED", "result": {"frequency_hz": analytical_damped_frequency_hz(inputs)}}
        raise RuntimeError("FT-02 injected Alpha-B module failure in centralized process")
    except RuntimeError as exc:
        outcomes["alpha_b"] = {"status": "FAILED", "failure": str(exc)}
    # Sequential central execution does not proceed to Beta after the Alpha-B failure.
    elapsed = time.perf_counter_ns() - started
    return _ft02_summary("CENTRALIZED_MODULAR", outcomes, elapsed)


def run_ft02_federated_process_surrogate(inputs: WLC001Inputs | None = None) -> dict[str, Any]:
    """Crash only the Alpha-B worker; collect unaffected Alpha-A and Beta results."""
    inputs = inputs or WLC001Inputs()
    started = time.perf_counter_ns()
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = {
            "alpha_a": pool.submit(_run_isolated_role, "alpha_a", inputs),
            "alpha_b": pool.submit(_run_isolated_role, "alpha_b", inputs, True),
            "beta": pool.submit(_run_isolated_role, "beta", inputs),
        }
        outcomes: dict[str, dict[str, Any]] = {}
        for role, future in futures.items():
            try:
                outcomes[role] = {"status": "COMPLETED", "result": future.result()}
            except subprocess.CalledProcessError:
                outcomes[role] = {"status": "FAILED", "failure": "isolated worker exited non-zero"}
    elapsed = time.perf_counter_ns() - started
    return _ft02_summary("FEDERATED_PROCESS_ISOLATED_SURROGATE", outcomes, elapsed)


def run_ft02_local_first_hybrid(inputs: WLC001Inputs | None = None) -> dict[str, Any]:
    """Catch a local Alpha-B module failure at its boundary while Beta continues isolated."""
    inputs = inputs or WLC001Inputs()
    started = time.perf_counter_ns()
    outcomes: dict[str, dict[str, Any]] = {
        "alpha_a": {"status": "COMPLETED", "result": {"frequency_hz": analytical_damped_frequency_hz(inputs)}}
    }
    try:
        raise RuntimeError("FT-02 injected Alpha-B local-module failure")
    except RuntimeError as exc:
        outcomes["alpha_b"] = {"status": "FAILED", "failure": str(exc)}
    outcomes["beta"] = {"status": "COMPLETED", "result": _run_isolated_role("beta", inputs)}
    elapsed = time.perf_counter_ns() - started
    return _ft02_summary("LOCAL_FIRST_HYBRID", outcomes, elapsed)


def run_all(inputs: WLC001Inputs | None = None) -> dict[str, Any]:
    inputs = inputs or WLC001Inputs()
    return {
        "workload_id": "WLC-001",
        "run_classification": "DERIVED_ARCHITECTURE_TOPOLOGY_SMOKE_TEST_NOT_ARCHITECTURE_ACCEPTANCE",
        "run_manifest": {
            "workload_spec_path": WORKLOAD_SPEC_PATH,
            "workload_spec_git_blob_sha1": WORKLOAD_SPEC_GIT_BLOB_SHA1,
            "workload_harness_git_blob_sha1": WORKLOAD_HARNESS_GIT_BLOB_SHA1,
            "source_artifact_sha256": SOURCE_ARTIFACT_SHA256,
            "git_commit_sha": os.environ.get("GITHUB_SHA") or os.environ.get("DINGOOS_COMMIT_SHA"),
            "git_branch": os.environ.get("GITHUB_REF_NAME") or os.environ.get("DINGOOS_GIT_BRANCH"),
            "github_run_id": os.environ.get("GITHUB_RUN_ID"),
            "github_run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
            "execution_source": "GITHUB_ACTIONS" if os.environ.get("GITHUB_ACTIONS") == "true" else "LOCAL",
            "python_version": platform.python_version(),
            "platform": platform.platform(),
            "inputs": asdict(inputs),
        },
        "architectures": [
            run_centralized(inputs),
            run_federated_process_surrogate(inputs),
            run_local_first_hybrid(inputs),
        ],
        "fault_experiments": {
            "FT-02": [
                run_ft02_centralized(inputs),
                run_ft02_federated_process_surrogate(inputs),
                run_ft02_local_first_hybrid(inputs),
            ]
        },
        "disposition": {
            "architecture_selected": False,
            "performance_thresholds_defined": False,
            "comparative_performance_acceptance": "NOT_PERFORMED",
            "physical_validation": "NOT_ESTABLISHED",
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_all(), indent=2, sort_keys=True))
