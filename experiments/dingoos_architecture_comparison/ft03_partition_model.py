"""Bounded FT-03 network-partition model for DingoOS architecture research.

DERIVED_RECONSTRUCTION / MODEL-LEVEL EXPERIMENT ONLY.
No real network, durable replica, DDEP, event bus, or target service is exercised.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping


class Relation(str, Enum):
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    EQUAL = "EQUAL"
    CONCURRENT = "CONCURRENT"


class ReconciliationStatus(str, Enum):
    CONFLICT = "CONFLICT"
    DOMINATES = "DOMINATES"
    IDENTICAL = "IDENTICAL"


@dataclass(frozen=True)
class ReplicaUpdate:
    object_id: str
    value: str
    version: Mapping[str, int]
    domain_id: str


def compare_versions(left: Mapping[str, int], right: Mapping[str, int]) -> Relation:
    """Compare vector clocks; missing components are zero."""
    keys = set(left) | set(right)
    left_le = all(left.get(k, 0) <= right.get(k, 0) for k in keys)
    right_le = all(right.get(k, 0) <= left.get(k, 0) for k in keys)
    if left_le and right_le:
        return Relation.EQUAL
    if left_le:
        return Relation.BEFORE
    if right_le:
        return Relation.AFTER
    return Relation.CONCURRENT


def reconcile_updates(left: ReplicaUpdate, right: ReplicaUpdate) -> ReconciliationStatus:
    if left.object_id != right.object_id:
        raise ValueError("cannot reconcile different object identities")
    relation = compare_versions(left.version, right.version)
    if relation == Relation.CONCURRENT:
        return ReconciliationStatus.CONFLICT
    if relation == Relation.EQUAL:
        if left.value != right.value:
            # Same causal version with different content is an integrity conflict.
            return ReconciliationStatus.CONFLICT
        return ReconciliationStatus.IDENTICAL
    return ReconciliationStatus.DOMINATES


def simulate_ft03_partition(architecture_id: str) -> dict:
    """Model a core↔domain partition and conflicting offline branch updates."""
    supported = {
        "CENTRALIZED_MODULAR",
        "FEDERATED_PROCESS_ISOLATED_SURROGATE",
        "LOCAL_FIRST_HYBRID",
    }
    if architecture_id not in supported:
        raise ValueError(f"unsupported architecture_id: {architecture_id}")

    base_value = "design-baseline-v1"
    base_version = {"core": 1}
    # During the partition, each domain works from the same last-known base.
    # Neither branch is globally committed while the coordinator is unreachable.
    update_a = ReplicaUpdate(
        object_id="WLC-001/design-parameter",
        value="design-branch-alpha",
        version={"core": 1, "domain-a": 1},
        domain_id="domain-a",
    )
    update_b = ReplicaUpdate(
        object_id="WLC-001/design-parameter",
        value="design-branch-beta",
        version={"core": 1, "domain-b": 1},
        domain_id="domain-b",
    )
    status = reconcile_updates(update_a, update_b)
    return {
        "fault_id": "FT-03",
        "architecture_id": architecture_id,
        "execution_scope": "deterministic vector-clock partition model; not an actual network fault injection",
        "partition": {
            "link": "core<->domain",
            "global_coordination": "PAUSED",
            "local_mode": "BOUNDED_OFFLINE_SPECULATIVE",
            "base_object": {"object_id": update_a.object_id, "value": base_value, "version": base_version},
            "global_state_during_partition": "UNCHANGED",
        },
        "offline_updates": [
            {"domain_id": u.domain_id, "object_id": u.object_id, "value": u.value, "version": dict(u.version), "globally_committed": False}
            for u in (update_a, update_b)
        ],
        "reconnection": {
            "version_relation": compare_versions(update_a.version, update_b.version).value,
            "reconciliation_status": status.value,
            "automatic_merge": False,
            "global_state_after_reconnection": "UNCHANGED_PENDING_REVIEW",
            "conflict_domains": sorted([update_a.domain_id, update_b.domain_id]) if status == ReconciliationStatus.CONFLICT else [],
            "requires_explicit_resolution": status == ReconciliationStatus.CONFLICT,
        },
        "safety_assertions": {
            "global_coordination_paused_during_partition": True,
            "offline_updates_not_silently_committed": True,
            "concurrent_updates_detected": status == ReconciliationStatus.CONFLICT,
            "global_state_not_overwritten": True,
            "automatic_conflict_merge": False,
        },
        "assurance_limits": {
            "real_network_partition": "NOT_TESTED",
            "durable_replica_persistence": "NOT_TESTED",
            "restart_recovery": "NOT_TESTED",
            "production_version_vector_integration": "NOT_TESTED",
            "target_side_authority": "NOT_IN_SCOPE",
            "full_FT_03_acceptance": "NOT_ESTABLISHED",
            "gate_A_to_E": "NOT_ESTABLISHED",
        },
    }


def run_all_ft03() -> list[dict]:
    return [
        simulate_ft03_partition("CENTRALIZED_MODULAR"),
        simulate_ft03_partition("FEDERATED_PROCESS_ISOLATED_SURROGATE"),
        simulate_ft03_partition("LOCAL_FIRST_HYBRID"),
    ]
