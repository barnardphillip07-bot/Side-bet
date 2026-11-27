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
SOURCE_ARTIFACT_SHA256 = "548a7a5595bd5d81863fbc8815e45e0b0423c51712883b585135cfea3d369752"


def _run_isolated_role(role: str, inputs: WLC001Inputs) -> dict[str, Any]:
    env = os.environ.copy()
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = str(REPO_ROOT) + (os.pathsep + existing if existing else "")
    completed = subprocess.run(
        [sys.executable, "-m", "experiments.dingoos_architecture_comparison.worker", "--role", role],
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


def run_all(inputs: WLC001Inputs | None = None) -> dict[str, Any]:
    inputs = inputs or WLC001Inputs()
    return {
        "workload_id": "WLC-001",
        "run_classification": "DERIVED_ARCHITECTURE_TOPOLOGY_SMOKE_TEST_NOT_ARCHITECTURE_ACCEPTANCE",
        "run_manifest": {
            "workload_spec_path": WORKLOAD_SPEC_PATH,
            "source_artifact_sha256": SOURCE_ARTIFACT_SHA256,
            "git_commit_sha": os.environ.get("GITHUB_SHA") or os.environ.get("DINGOOS_COMMIT_SHA"),
            "git_branch": os.environ.get("GITHUB_REF_NAME") or os.environ.get("DINGOOS_GIT_BRANCH"),
            "python_version": platform.python_version(),
            "platform": platform.platform(),
            "inputs": asdict(inputs),
        },
        "architectures": [
            run_centralized(inputs),
            run_federated_process_surrogate(inputs),
            run_local_first_hybrid(inputs),
        ],
        "disposition": {
            "architecture_selected": False,
            "performance_thresholds_defined": False,
            "comparative_performance_acceptance": "NOT_PERFORMED",
            "physical_validation": "NOT_ESTABLISHED",
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_all(), indent=2, sort_keys=True))
