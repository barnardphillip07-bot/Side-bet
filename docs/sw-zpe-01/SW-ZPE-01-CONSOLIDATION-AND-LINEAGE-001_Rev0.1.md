# SW-ZPE-01 Consolidation and Source-Lineage Register — Rev 0.1

- **Record ID:** SWZ-CONSOL-001
- **Revision:** 0.1
- **Date:** 2026-11-27
- **Workspace:** `barnardphillip07-bot/Side-bet`
- **Branch:** `zpe/sw-zpe-01-consolidation-001`
- **Base commit:** `55d4ab4b0fc7f3c299bb1654bb6b5c8167140d28`
- **Status:** CONSOLIDATION INDEX CREATED / SOURCE FILES RETAINED IN ORIGINAL LIBRARY LOCATIONS / NOT A RELEASE OR CANONICAL-SOURCE DECLARATION

## 1. Purpose

This record establishes a controlled index for the recovered SW-ZPE-01 material and connects it to the mathematical reverse-engineering work. It does not replace the original Library archive, source packages, revision records, or protected intellectual property.

## 2. Inventory reconciliation

Two source collections were reconciled:

1. The recovered `SOURCE_REGISTER.csv`: **27 records**.
2. The Library tree `/DingoOS-Mathematics/SW-ZPE-01`: **125 files across 40 folders**.

Six files were present in both collections and were deduplicated by exact Library file ID. The resulting master register contains **146 unique file records**: 27 source-register records plus 119 additional Library-tree records.

The six overlap records are:
- `ZPE01-ENC-0001.md`
- `ZPE01-ENC-0001_Rev0.2.md`
- `ZPE01_RECIPROCAL.sub`
- `ZPE01_ENERGY_TEST.cir`
- `ZPE01_REFERENCE_TESTS.py`
- `ZPE01_REFERENCE_RESULTS.json`

The register retains each original Library locator and file ID. Distinct source copies are not collapsed merely because their bytes are identical. The original register's duplicate records for the FEM script, E07 sensitivity script and integrated virtual prototype remain separately traceable.

## 3. Consolidated structure

The 125-file Library tree contains two principal families:

### 3.1 Encyclopaedia and engineering records
- `ZPE-01-ENC-0001`: reciprocal piezoelectric cantilever model; Rev0.1 and Rev0.2.
- `ZPE-01-ENC-0002`: independent verification testbench audit; Rev0.1–Rev0.4.
- `ZPE-04A-ENC-0002`: SECE-004A topology, source-boundary, commutation and energy-ledger work; Rev0.1–Rev0.5.
- `ZPE-05-DEV-AUDIT-0001`: software/post-processor audit records.
- `ZPE-05-DEV-TEST-0002`: software hardening and regression records.
- `ZPE-05-RAW-ADAPTER-QUAL-0001`: raw-adapter qualification preparation records.

### 3.2 Verification packages
- ZPE-05 batch-runner test bundles Rev0.1–Rev0.4.
- ZPE-05 raw-adapter qualification bundles Rev0.1–Rev0.4_PREP.
- Per-revision manifests, static-audit outputs, regression logs, fixture manifests and SPICE testbenches.

## 4. Master register

`MASTER-SOURCE-REGISTER.csv` is the consolidated 146-record index. It distinguishes:
- hashes carried forward from the recovered 27-record register;
- hashes independently reverified in this pass;
- records indexed by Library metadata only, with no hash claim.

A blank SHA-256 field means **not computed in this consolidation pass**. A Library locator or filename is not proof that a source was executed, accepted, physically validated, or released.

## 5. Current byte-level checks

The following exact source hashes were independently reverified against the recovered register or materialized Library bytes:
- `ZPE01_REFERENCE_TESTS.py`: `8164e36383ba8af5331542680cdd63fec92423f0619be6067eaf4be591459651`.
- `sw_zpe_01_fem_aligned.py`: `8c3c3ef2d46b6076034ca2d117254b82d2a2052a945d2743aa127a728b6c3f9f`.
- `ZPE-04A-ENC-0002_Rev0.5.md`: `61e7d0d5b58c284b00053ec2d8fadc14e4be2c350f620ab7a745bea72d0e928d`.
- `ZPE-05-DEV-AUDIT-0001_Rev0.2.md`: `6d328a65fe95ecb61431a1b31d7b38757491dd2cb44d10368fb9fc0516d797ec`.
- `ZPE-05-DEV-TEST-0002_Rev0.3.md`: `2dc2e1c9e288ee499ff17d794fcbd3115376fc46948f4e7c48e9dce90f244752`.

The ODE reference output exactly matched the archived `ZPE01_REFERENCE_RESULTS.json`. The FEM script executed successfully and reproduced its documented mesh-convergence trend.

The SECE-004A Rev0.5 ZIP passed its internal 11-file SHA-256 manifest check. Its static audit returned `PASS_STATIC_LEDGER_AND_REQUIREMENTS_STRUCTURE_NOT_SPICE`. The ZPE-05 batch test bundle Rev0.4 passed its 12-member package checksum list. Its 56-test recorded regression log was not fully reproduced in this runtime: 55 tests passed; the timeout-retention test failed because the child Python interpreter did not start within its fixed 1.5 s timeout. A simple child interpreter launch took approximately 4.24 s in this runtime. This is recorded as an environment-sensitive test limitation, not silently counted as a pass.

## 6. Preservation and release controls

- No original ZPE source, binary package, SPICE file, FEM source, or BIF source was copied into this public repository branch.
- No original file or revision was modified, renamed, deleted, or merged.
- The branch is separate from `main`; `main` remains unchanged.
- The master register is a derived metadata index, not an authenticated canonical source register.
- Original BIF source remains excluded, private and protected.
- Simulator execution, native RAW parser qualification, hardware tests, manufacturing release and net-positive-energy claims remain separate gates.

## 7. Unresolved recovery items

1. Verify the remaining 119 indexed files by materializing and hashing their bytes against their local/package manifests.
2. Recover the exact controlled `TEST-001 Rev1.0` file.
3. Recover the exact controlled `ZPE-05-VER-0001 Rev0.1` specification and schema.
4. Recover the original ZPE-01 Rev0.4 testbench and runner bytes; the existing Rev0.4 audit describes source text reviewed from conversation, not authenticated source bytes.
5. Resolve parameter conflicts for `C0`, coupling coefficient `theta`, geometry, clamp and adhesive definitions.
6. Execute the appropriate LTspice/ngspice models with exact versions, logs, raw waveforms, exported data and hashes.
7. Qualify the native Spicelib parser with real simulator-produced RAW fixtures; synthetic parser tests do not qualify it.

## 8. Change history

- **Rev0.1 — 2026-11-27:** First controlled metadata consolidation of the 27-record source register and 125-file SW-ZPE-01 Library tree. Six duplicate locators deduplicated; 146 unique file records indexed. Original source files remain in their source locations.
