# ZPE-05 Rev0.4 Bundle Independent Reproduction Record — Rev 0.1

- **Record ID:** ZPE05-REPRO-001
- **Revision:** 0.1
- **Date:** 2026-11-27
- **Project:** SW-ZPE-01 / ZPE-05
- **Source package:** `SWZPE01_ZPE05_batch_test_bundle_Rev0.4.zip`
- **Package SHA-256:** `bc4553365b2c7d5256803dd3fbb5cf56156892a4d66434410c6d296746e48065`
- **Package status:** SYNTHETIC SOFTWARE REGRESSION ONLY / NOT SIMULATOR-QUALIFIED / NOT RELEASED

## 1. Purpose

Independently recheck the recovered Rev0.4 candidate bundle and distinguish package integrity, software regression, process-startup environment effects, simulator/parser qualification and engineering qualification.

## 2. Package integrity

- ZIP integrity check: PASS; no corrupt member reported.
- Internal `SHA256SUMS.txt`: **12/12 member hashes matched**.
- Python compile check: PASS for the bundled Python modules.

## 3. Regression reproduction

The archived Rev0.4 README and regression log record **56 tests passed** on 2026-11-25.

A direct rerun using the default Python executable in this environment produced:
- 55 tests passed.
- One failure in `test_03_timeout_uses_case_and_override_limits_and_retains_partial_output`.
- The child Python interpreter did not begin executing the timeout stub within its fixed 1.5 s limit; no `partial.marker` was written and no pre-timeout stdout/stderr was captured.
- A simple child interpreter startup in this runtime took approximately 4.24 s, independently demonstrating that the fixed 1.5 s allowance is shorter than this environment's normal interpreter startup.

The test was then rerun using a temporary interpreter wrapper that invoked the same Python executable with `-S` (standard-library-only startup, disabling site initialization). The timeout stub uses only the Python standard library. Wrapper startup measured approximately 0.013 s.

**Result under the low-startup wrapper: 56 tests passed, 0 failures, 0 errors.**

This confirms that the timeout-retention test and the rest of the synthetic regression suite pass when the child process starts within the test's configured timeout. The wrapper is an environment-only test harness; no bundled source or test file was changed.

## 4. Test scope and limits

The 56 tests exercise:
- numerical product/square integration and ledger boundary handling;
- fail-closed evidence and disposition behaviour;
- batch orchestration, subprocess failures, timeout handling and artifact retention;
- SECE assertion logic, mandatory inventory and topology-evidence controls;
- raw-adapter control flow using fake parser objects.

They do **not** qualify:
- LTspice or ngspice execution;
- native Spicelib RAW parsing;
- simulator dialect compatibility;
- actual circuit topology or physical current direction;
- energy balance of a physical prototype;
- the production topology signer or locked verification specification;
- hardware behaviour, autonomy, net-positive energy or manufacturing release.

The 56/56 result is a software-regression result for this candidate bundle only. The default-interpreter startup sensitivity remains recorded because it affects reproducibility in some environments.

## 5. Disposition

- Package integrity: **PASS — 12/12**.
- Python compilation: **PASS**.
- Synthetic regression with default interpreter: **55/56**, one environment-sensitive startup-timeout failure.
- Synthetic regression with low-startup wrapper: **56/56**.
- Simulator/parser qualification: **NOT QUALIFIED**.
- Engineering qualification / release: **NOT APPROVED**.

## 6. Change history

- **Rev0.1 — 2026-11-27:** Independently verified the Rev0.4 package manifest and reran all 56 tests. Recorded default-interpreter timeout sensitivity and a successful full rerun with a low-startup standard-library interpreter wrapper. No source or test files modified.
