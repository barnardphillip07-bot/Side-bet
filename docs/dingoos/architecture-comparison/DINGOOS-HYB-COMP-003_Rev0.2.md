# DINGOOS-HYB-COMP-003 — WLC-001 Functional Topology Smoke Protocol

- Revision: Rev0.2
- Date: 27 November 2026
- Workspace: `barnardphillip07-bot/Side-bet`
- Branch: `dingoos/recovery-engine-adopted-requirements`
- Status: **FUNCTIONAL SMOKE PROTOCOL FROZEN — PERFORMANCE/ARCHITECTURE ACCEPTANCE PROTOCOL OPEN**
- Workload: `WLC-001-FROZEN Rev0.2`
- Parent: `DINGOOS-HYB-COMP-001 Rev0.8`

## 1. Scope

This protocol freezes the repeatable functional smoke procedure for the three derived WLC-001 topology variants and the bounded FT-02 prototype subset.

It does not freeze a controlled performance benchmark, establish comparable production fidelity, qualify any architecture, or authorize consequential dispatch.

## 2. Frozen inputs and source identity

Use the exact frozen workload specification:
- Path: `docs/dingoos/architecture-comparison/workloads/WLC-001-FROZEN-Rev0.2.json`
- Git blob SHA-1: `9517151b6d34ffb6a7686634617ca5fd1592d202`
- Derived WLC-001 harness path: `benchmarks/dingoos/wlc_001.py`
- Harness Git blob SHA-1: `c4f381fa8298d7d103b6236bb2d9b6a006628b4d`
- Source-bearing Library artifact: `Pasted text(7).txt`
- Source artifact SHA-256: `548a7a5595bd5d81863fbc8815e45e0b0423c51712883b585135cfea3d369752`

The workload inputs and analytical/numerical algorithms are controlled by the frozen JSON specification. Do not silently edit the input values or source algorithm. A change requires a new workload-specification revision and corresponding harness/test update.

## 3. Variants and execution order

Run:
1. `CENTRALIZED_MODULAR` — one process, direct role calls.
2. `FEDERATED_PROCESS_ISOLATED_SURROGATE` — three local worker processes for Alpha A, Alpha B and Beta; single-host surrogate only.
3. `LOCAL_FIRST_HYBRID` — Alpha A and Alpha B local modules; Beta in an isolated worker process.

All variants receive the same frozen input values. Beta receives only the frozen input envelope, not Alpha outputs. This is input separation, not organizational, codebase or toolchain independence.

The runner then executes the bounded `FT-02` subset against each topology:
- Alpha-B failure in the centralized sequential path.
- Alpha-B worker-process failure in the federated surrogate.
- Alpha-B local-module failure at the hybrid module boundary.

The expected synthesis disposition for every injected Alpha-B failure is `INCOMPLETE`; the missing contribution must be named and must not be promoted to complete.

## 4. CI environment and commands

GitHub Actions workflow:
`.github/workflows/dingoos-architecture-comparison.yml`

Environment:
- `ubuntu-latest` GitHub-hosted runner.
- Python major/minor selector: `3.12`.
- Exact Python patch version and platform are recorded at run time.
- Runner resources are ephemeral and not a controlled performance envelope.

Commands:
```sh
python -m unittest discover -s tests/dingoos -v
python -m unittest discover -s tests/architecture_comparison -v
python -m experiments.dingoos_architecture_comparison.runner > wlc001-architecture-smoke.json
```

The workflow preserves `wlc001-architecture-smoke.json` as an Actions artifact named `wlc001-architecture-smoke`.

One functional run occurs per workflow invocation/commit. This is a correctness and topology smoke check, not a statistical performance campaign.

## 5. Required run manifest

Every runner output must include:
- workload ID and specification path;
- frozen workload specification Git blob SHA-1;
- WLC-001 harness Git blob SHA-1;
- source artifact SHA-256;
- exact Git commit SHA and branch when supplied by GitHub Actions or an explicit local run environment;
- GitHub Actions run ID and attempt when available;
- execution source (`GITHUB_ACTIONS` or `LOCAL`);
- Python version, platform and frozen input values;
- architecture IDs, topology descriptions, role outputs and timing classification;
- fault ID, injected role failure, role outcomes and Σ disposition.

A missing commit/run field in a local invocation remains null; do not invent it. Git blob SHA-1 values must be labelled as Git blob identifiers, not SHA-256 content digests.

## 6. Functional acceptance assertions

The smoke protocol passes only when all of the following hold:

1. All three no-fault variants produce identical Alpha A, Alpha B and Beta reference outputs for the frozen inputs.
2. Beta receives only the frozen inputs and does not consume Alpha output.
3. The federated topology is labelled as a single-host process-isolated surrogate.
4. For the FT-02 subset, the centralized sequential path reports missing Alpha-B and Beta; the federated and hybrid paths report missing Alpha-B while preserving unaffected role outputs.
5. Every FT-02 subset result is `INCOMPLETE`, names missing contributions, and has `accepted_as_complete=false`.
6. No γ authority, consequential effect, target-side enforcement, physical validation or Gate A–E acceptance is claimed.
7. All raw runner output is preserved as the named workflow artifact.

Current local result: **7/7 topology tests pass**. Current GitHub Actions topology, WLC-001 and recovery-engine contract workflows have each completed successfully on the working branch. The exact run and artifact references are maintained in `DINGOOS-HYB-COMP-002 Rev0.4` and subsequent evidence revisions.

## 7. Timing and performance restrictions

The runner records `elapsed_wall_ns` for diagnostic visibility only.

Do not use GitHub-hosted runner timings to:
- rank the architectures;
- set performance thresholds;
- estimate production throughput or latency;
- claim Pareto dominance;
- select an architecture.

The current process-isolated variants include process-startup and scheduling costs. One sample is not a stable steady-state measurement.

## 8. Open performance/acceptance protocol

The following remain deliberately **OPEN / NOT FROZEN**:
- controlled hardware/host identity and resource reservation;
- CPU model, core allocation, affinity/governor and memory limit;
- exact OS image, Python patch version and dependency environment;
- warm-up policy and repetition count;
- workload batch size, concurrency and arrival/load schedule;
- steady-state and tail-latency metric definitions;
- raw observation schema beyond the current smoke result;
- statistical treatment, outlier handling and stopping rule;
- owner-defined performance thresholds;
- complete FT-01–FT-16 mapping and applicable SEARM-FI/PROV-FI/AD/C cross-track scenarios.

These must be settled against recovered requirements, existing test ownership and an identified controlled execution environment. Do not fabricate thresholds or choose a performance environment merely because GitHub Actions is available.

## 9. Fault and assurance disposition

- FT-02: **bounded prototype subset executed**; full FT-02 acceptance **NOT ESTABLISHED**.
- Other FT-01…FT-16 scenarios: **NOT RUN** in this topology experiment.
- Gates A–E: **NOT PASSED / NOT ESTABLISHED**.
- SEARM-FI-01…18, PROV-FI-01…10, AD-01…12 and C-01…19: retain existing owners; no parallel suite created.
- Gate D independence: **NOT ESTABLISHED**.
- γ authority and target-side fencing: **NOT IMPLEMENTED/TESTED** in this prototype.
- Consequential dispatch: **HOLD / NO-GO**.
- Architecture selection: **NONE**.

## 10. Initial frozen-protocol execution record

Exact working-branch commit: `9b1235edef6d114c668e51fb00a6e4dc4bd081a4`.

| Workflow | Run ID | Result |
|---|---:|---|
| Architecture topology smoke | `45930966588` | **SUCCESS** |
| WLC-001 deterministic workload | `45930966561` | **SUCCESS** |
| Recovery-engine contracts | `45930966577` | **SUCCESS** |

Architecture workflow: https://github.com/barnardphillip07-bot/Side-bet/actions/runs/45930966588

Preserved artifact: `wlc001-architecture-smoke`, artifact ID `15168452060`, 2,125 bytes, not expired at inspection. The artifact contains the runner JSON output including commit/branch, Actions run metadata, Python/platform, exact frozen inputs, three topology results and the FT-02 subset outcomes.

Source identifiers bound in the runner:
- WLC-001 specification Git blob SHA-1: `9517151b6d34ffb6a7686634617ca5fd1592d202`.
- WLC-001 harness Git blob SHA-1: `c4f381fa8298d7d103b6236bb2d9b6a006628b4d`.
- Architecture runner Git blob SHA-1 at this protocol run: `1b6ff2b5bc055f3df7e9397daf4c4f890f62d22f`.
- Historical source artifact SHA-256: `548a7a5595bd5d81863fbc8815e45e0b0423c51712883b585135cfea3d369752`.

The local topology suite passed 7/7 and the WLC-001 harness suite passed 7/7. The GitHub Actions workflows passed on the exact commit above. These results establish the frozen functional smoke procedure only; they do not establish performance acceptance, complete FT-02, Gates A–E, Gate D independence, physical validation or architecture selection.

## 11. Change history

- Rev0.1 — 27 November 2026: froze the functional CI smoke procedure, run-manifest fields, expected topology equivalence and bounded FT-02 assertions. Kept performance and full architecture acceptance protocol open.
- Rev0.2 — 27 November 2026: recorded exact successful GitHub Actions runs and the preserved JSON artifact for commit `9b1235edef6d114c668e51fb00a6e4dc4bd081a4`; verified source Git blob identifiers and the remaining assurance limits.
