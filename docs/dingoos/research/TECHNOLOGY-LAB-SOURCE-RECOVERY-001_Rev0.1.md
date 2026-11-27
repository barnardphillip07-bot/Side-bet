# TECHNOLOGY-LAB-SOURCE-RECOVERY-001 — Source Inventory, Mathematical Models, Tools and Revision Lineage

- Revision: Rev0.1
- Date: 27 November 2026
- Status: **SOURCE RECOVERY PARTIAL — ACTUAL MATHEMATICAL / TECHNOLOGY ARTEFACTS RECOVERED — DEDICATED TECHNOLOGY LAB CHARTER AND MULTIPLE PROGRAMME SOURCES UNRETRIEVED**
- Repository: `barnardphillip07-bot/Side-bet`
- Working baseline branch inspected: `dingoos/recovery-engine-adopted-requirements`
- Inspected branch head: `dd074e38923fd224521a0cfadaeb44df08426ace`
- Inspected tree SHA: `6cba139ff1cfdce77bef9943e1978526048aae2d`
- Scope: read-only recovery and provenance mapping. This report does not authenticate the private original DingoOS repository, adopt a proposed architecture, or authorize public release of original/private source files.

## 1. Executive disposition

This pass recovered real mathematical and engineering source artefacts associated with the DingoOS working baseline, including:
- the archived `dingoos_ai_math` package across Knowledge Snowflake v0.8.0, v0.10.0 and v0.11.0;
- numerical experiment, equation-memory, dimensional/tensor, coupled-multiphysics, spatial-multiphysics and VAQPC source modules;
- SW-ZPE-01 mathematical, FEM, ODE-reference, SPICE and controller-derivative artefacts, including a verified Rev0.5 source package;
- the Nano-Glass Holographic Technology research programme record;
- the Invention and Design Environment proposal and the existing PIDD / Competitive Design and Discovery Arena proposal records.

**The Side-bet Git working branch itself contains no Technology Lab directory or domain-specific Technology Lab programme source modules.** Its actual code is principally the WLC-001 architecture-comparison benchmark and the recovery-engine/indexer. Those are reusable mathematical/recovery tools, not evidence that the Technology Lab has been implemented.

The Library/archive source set is richer than the Git tree. The source artefacts have been recovered and inspected in the current working environment, but have **not** been copied into the public Side-bet repository. This preserves source provenance and avoids publishing project source or private IP without a separate release decision.

The dedicated canonical Technology Lab charter, master index, exact ownership boundary, and full programme/source register remain **NOT LOCATED IN THE INSPECTED SURFACES / UNRETRIEVED**.

## 2. Side-bet repository and branch reconciliation

### 2.1 Actual Git state

- `main`: inspected at commit `edd1b256284967b135cf9def8c983a714401d8ad`; its tree contains one 10-byte README and no substantive project source.
- Working baseline branch: `dingoos/recovery-engine-adopted-requirements`, head `dd074e38923fd224521a0cfadaeb44df08426ace`; recursive tree contains 73 files, tree SHA `6cba139ff1cfdce77bef9943e1978526048aae2d`.
- Exact tree search for Technology Lab, NanoGlass/NGH, E-HOVER, E-MOTO, D-REP, NMI, BIO, VAQPC and `zpe_model` returned **zero matching paths**.

The empty `main` branch must not be mistaken for the working source branch. The adopted-requirements branch is the substantive Side-bet working branch inspected here.

### 2.2 Actual mathematical and tool source already in Side-bet

| Path | Current Git blob SHA | Source classification |
|---|---|---|
| `benchmarks/dingoos/wlc_001.py` | `c4f381fa8298d7d103b6236bb2d9b6a006628b4d` | Derived reconstruction of a historical damped-oscillator/DigitalTwin workload; not canonical DingoOS runtime source |
| `experiments/dingoos_architecture_comparison/ft03_partition_model.py` | `4fc86a09983366247975facf2f4cbb8d9f2104ed` | Bounded vector-clock/partition conflict model; model-level experiment only |
| `experiments/dingoos_architecture_comparison/runner.py` | `8bc47092f82dd4caf5c65b02eaad950936964cc8` | Three-topology architecture comparison runner; process-isolated single-host surrogate |
| `experiments/dingoos_architecture_comparison/worker.py` | `bbf1670bf57d829d0fdba82df277f48367ca1751` | Isolated role worker for the WLC-001 comparison |
| `src/dingoos_recovery/indexer.py` | `ff17cd38f6003ddbd5da940c434724bed5fc98a6` | Content-addressable file/text/ZIP source indexer |
| `src/dingoos_recovery/contracts.py` | `19a338cea8514d7d27afb2def5ec5d285fea408b` | Deterministic recovery receipt, source-index and lineage contract validation |
| `docs/dingoos/architecture-comparison/workloads/WLC-001-FROZEN-Rev0.2.json` | `9517151b6d34ffb6a7686634617ca5fd1592d202` | Frozen derived benchmark specification |

WLC-001 source history:
- `ecca0678477994655450c8db9e655b336188715f` — initial deterministic derived benchmark harness;
- `408ec6bcc49a0825dbdeecedfabf561653a9dae7` — independent beta characteristic-root verification;
- `889b225d0af9bd8c3ccbf688dd36531579c38a36` — explicit complex square root correction.

FT-03 source history:
- `e75bde0ea344ffe2cc16c625ad13342e6c4ac9de` — bounded partition/conflict model;
- `30d225d667fd3e3401d0bb02ff790a1409ecd817` — included FT-03 in architecture evidence.

Recovery-indexer history:
- `5ecf30f2635af770c7189b8f542d0b74168986d3` — initial content-addressable source indexer;
- subsequent commits hardened Markdown fence handling, duplicate declaration handling, empty files and byte-region coverage; latest inspected fix `2bafbd0731d8a943d6c54efa64199a013f220dee`.

These are real Side-bet code files with inspectable Git histories. They do not constitute the Technology Lab's domain programme models or tool adapters.

## 3. Recovered mathematical-engine source: Knowledge Snowflake archives

### 3.1 Archive identities

| Archive | SHA-256 |
|---|---|
| `dingoos_knowledge_snowflake_v0.8.0.zip` | `544bb9e080ac7d98f6dc88989c8ebde0dd166e74f8a578f42b90369bb482cb05` |
| `dingoos_knowledge_snowflake_v0.10.0.zip` | `605c63cc402386841882a710dca7408c43dd467a30d20f77aa2f069c9dabae1d` |
| `dingoos_knowledge_snowflake_v0.11.0.zip` | `6672810b3874d1822a213ee838954566197808241212078473e79a1645bb4c58` |

The v0.11.0 archive contains 198 ZIP entries / 147 files. Its README title still labels the package v0.8.0 while later sections describe v0.9/v0.11 additions; retain this as a version-label reconciliation issue.

### 3.2 Recovered source modules and revision presence

The following file hashes were calculated from the archived member bytes. “Same” means the exact source file is byte-identical in each listed archive; it does not prove canonical authenticity or correctness.

| Source path | SHA-256 | Archive presence |
|---|---|---|
| `src/dingoos_ai_math/numerical.py` | `2529b2865122b0c4aa01f219c7379f72ea402f025ff48cd31c568657377dc3e2` | v0.8 / v0.10 / v0.11 identical |
| `src/dingoos_ai_math/research_memory.py` | `47275da1ee1045fa26297d04e837893e4c660f9af90cc26ed4e7a99aa893be78` | v0.8 / v0.10 / v0.11 identical |
| `src/dingoos_ai_math/coupled_multiphysics.py` | `5d6deac187b803558154cedcf02fd4a28bdd6e869ae121b0ab85360ee38dfe06` | v0.8 / v0.10 / v0.11 identical |
| `src/dingoos_ai_math/spatial_multiphysics.py` | `2f099f1548723c537239eee9de783d32bd3791533aa87135302c48fcc2b6d09e` | v0.8 / v0.10 / v0.11 identical |
| `src/dingoos_ai_math/verification.py` | `7baf06d08b7c13e5737c13551898101151173429edae6bdfc9e491e139bc390f` | v0.8 / v0.10 / v0.11 identical |
| `src/dingoos_ai_math/models.py` | `ce0a9df7952fa55681633f1f3480684de1e8be9d21856f82bf885f375aa3a157` | v0.8 / v0.10 / v0.11 identical |
| `src/dingoos_ai_math/multiphysics_platform.py` | `2beb55e6677d6492465f38a2ec832dd4ffeb0942313b42e9f015635061a9db4a` | v0.8 / v0.10 / v0.11 identical |
| `src/dingoos_ai_math/dimensional_tensor.py` | `4542d829a21e7c472ada22d41f72b0bb04d8161e9d0e1437e9ab5d4011776190` | v0.10 / v0.11 identical |
| `src/dingoos_ai_math/vaqpc.py` | `a7f19cd7b3b8ee5c74f6c6d5a3a9bd7962251601b0c6f4e9817faa799370eb56` | v0.10 / v0.11 identical |
| `src/dingoos_ai_math/vaqpc_noise.py` | `7ca73a57a1319764cbdf4a0ffbad0f64e5e36d4a2de00e6fdac493517473962c` | v0.11 only |

Additional preserved source/test artefacts:
- `examples/numerical_resonance.py` SHA-256 `c699024244ea578157a0c8485b62a72206f359ef336aba6efa34521806afe519`, byte-identical across all three archives;
- `tests/test_numerical.py`, `tests/test_coupled_multiphysics.py`, `tests/test_spatial_multiphysics.py` and object-store/pipeline tests are likewise present unchanged across the three inspected archives;
- `tests/test_dimensional_tensor.py` and `tests/test_vaqpc.py` appear in v0.10/v0.11;
- `tests/test_vaqpc_noise.py` appears in v0.11.

### 3.3 Actual tool capabilities and limitations

**NumericalExperimentEngine — `numerical.py`**
- deterministic model runs;
- Cartesian parameter sweeps;
- seeded normal/uniform/triangular Monte Carlo input uncertainty;
- empirical quantiles and summary statistics;
- resolution-based convergence comparisons;
- pluggable verification checks;
- JSON result artefacts and SHA-256 integrity verification.

Limitations explicitly documented: model ID does not prove the callable matches the declared source; no automatic unit inference, general solver-stability certification or constitutive-law validation; numerical verification is not formal proof or physical validation; current store is a prototype, not production WORM/transactional protected storage.

**ResearchMemory — `research_memory.py`**
- equation storage and retrieval;
- source/dependency reference extraction and version pinning;
- immutable correction records linked to prior versions;
- object-store integration and protected-source preservation boundary.

The v0.11 integrated object store contains 21 object versions but **zero `MATHEMATICAL_EQUATION` objects**. The code capability exists; an actual populated canonical equation registry was not recovered in these archives. The earlier `DNG-MECH-OSC-001` and PDE references therefore remain unresolved where previously recorded.

**Dimensional/tensor verification — `dimensional_tensor.py`**
- exact-rational physical dimensions;
- symbol, coordinate, index and quantity-type records;
- expression typing;
- equation, boundary-condition, action-integral and tensor-equation checks.

This is a bounded implementation, not a general theorem prover or proof assistant.

**Coupled multiphysics — `coupled_multiphysics.py`, `MULTIPHYSICS_SOLVER.md`**
- reduced-order five-domain demonstrator: lumped mechanics, one effective fluid velocity, lumped RLC/electromagnetic transducer, well-mixed temperature and global energy ledger;
- classical RK4 integration and energy/interface checks.

It is explicitly not general CFD, full Maxwell, FEM or arbitrary continuum multiphysics.

**Spatial multiphysics — `spatial_multiphysics.py`**
- periodic one-dimensional distributed mechanics, fluid, electromagnetic and thermal demonstrator;
- split numerical integration and energy diagnostics.

It remains a restricted 1-D numerical demonstrator, not a general 3-D solver or physically validated model.

**VAQPC — `vaqpc.py`, `vaqpc_noise.py`**
- classical state-vector and density-matrix quantum-state simulation;
- single-DOF mechanical dynamics and modal frequencies;
- accelerating-frame apparent-gravity illustration;
- transparent workload scheduler;
- v0.2 vibration-to-error phenomenological model and idealised repetition-code estimate.

The VAQPC architecture document explicitly calls this a proposed research/engineering subsystem. It is not physical quantum hardware, does not establish quantum advantage, gravity shielding or anti-gravity propulsion, and has no hardware-calibrated noise model. The vibration-to-phase relationship is phenomenological, not a universal law or original BIF equation.

**Known retained numerical defect:** `examples/numerical_resonance.py` has the previously audited one-extra-state-step endpoint defect. The archived source remains unchanged in all three archives. No patch was made in this recovery pass.

## 4. Recovered programme and technology source artefacts

### 4.1 Invention and Design Environment proposal

- Source: `/DingoOS/Engineering/Architecture/DINGOOS-IDE-001_Rev0.1.md`
- SHA-256: `ac0bfb1a9cd2477e64c26698ecbf7a77bc6d8f1a7ff9bb4b2ee3b135803d9aca`
- Revision history: Rev0.1, 26 November 2026 only.
- Status: **CONTROLLED PROPOSED ARCHITECTURE / NOT CANONICAL / NOT IMPLEMENTED**.

It proposes an Engineering Lab for equations, notebooks, CAD/CAE, circuit/system modelling, simulation, optimisation and parameter studies, plus an Experiment Studio for hypotheses, protocols, instrumentation and measurement. It lists possible tool classes such as symbolic/numerical mathematics, optics/photonics/electromagnetics, circuits, control/robotics, statistics/optimisation, formal methods and specialist CAD/CAE.

This is a proposal for views and adapters. It is not an authenticated Technology Lab charter, a proof that adapters exist, or authority to create duplicate mathematical/evidence/workflow systems.

### 4.2 Nano-Glass Holographic Technology

- Source: `/DingoOS/Engineering/NanoGlass/NGH-RES-001_Rev0.1.md`
- SHA-256: `a7ef61c8485fc3d0f7e7866f1b428e5c4b322906d9bb43be955aced01a5fde86`
- A root-level copy was also recovered; its SHA-256 is identical, so the two copies are byte-identical, not separate revisions.
- Revision history: Rev0.1, 26 November 2026 only.
- Status: **PRELIMINARY RESEARCH SYNTHESIS / NOT DIMENSIONED / NOT SIMULATED / NOT EXPERIMENTALLY VERIFIED**.

The record preserves six branches: advanced nano-glass waveguides, adaptive/programmable photonics, computational holography/light-field optics, glass-free light-field displays, holographic light-sheet volumetric displays, and aerial laser-excited voxels. No candidate architecture, substrate, dimensions, nano-feature geometry or fabrication process is selected. No NGH simulation source code or physical test data was found in the inspected Side-bet tree or three Knowledge Snowflake archives.

### 4.3 SW-ZPE-01 — recovered mathematical and engineering source family

The SW-ZPE-01 Library source register contains 27 records. Its SHA-256 is `44f05b09861b123e889c1d66bbd4e5d4e62b4094b486f2ef0bcc91f538fd252b`. The register preserves source IDs, revisions, file paths, SHA-256 hashes and dispositions.

Key recovered sources:
- `SW-ZPE-01_Complete_POC_Engineering_Blueprint_Rev2.1.docx` — SHA-256 `25ee8dc88b4691b9778974078905ef734867f310e0c9eaaa42ea6af8d888d1b8`; preliminary working blueprint, not released manufacturing package.
- `SW-ZPE-01_Rev2.3_Engineering_Reconciliation_Reference_Report.pdf` — SHA-256 `9443c556d65699c464390f90052839c732e5e69e43569778b958dbe3db3f9cf4`; active preliminary engineering reconciliation baseline, not fabrication released.
- `SW-ZPE-01_Integrated_Virtual_Prototype_Rev0.1.md` — SHA-256 `38a2488ddff94582d07c66e451d1df3b9d3c25717defb15a6e9fc76988ecdcb4`; proposed/not frozen.
- `ZPE01-ENC-0001.md` Rev0.1 — SHA-256 `d55fd81014b7ddbcda2a9f18ce6c2c7bcffd12adb78caaa392f05950ce0fa90d`.
- `ZPE01-ENC-0001_Rev0.2.md` — SHA-256 `39a23f1882263197a266897ee58a4a3abcb9ec6fa283978cc31bb12678332354`; mathematical foundation reviewed, independent ODE reference executed, parameters provisional, SPICE not executed.
- `ZPE01_REFERENCE_TESTS.py` — SHA-256 `8164e36383ba8af5331542680cdd63fec92423f0619be6067eaf4be591459651`.
- `ZPE01_REFERENCE_RESULTS.json` — SHA-256 `dfa8e045b6541093fd6fca5fa36dc6767be282d888e6a9bbca193debe57b02d0`.
- `ZPE01_RECIPROCAL.sub` — SHA-256 `335e1d66fd48fed7740856868c1490d09d1755c229600d53a8b4d5df46085343`; draft, not simulator verified.
- `ZPE01_ENERGY_TEST.cir` — SHA-256 `8a38fa243f877f218f0795e74f9ba47921ccb755ed4cbe7b1d48d3bd370b72cb`; draft, not simulator verified.
- `sw_zpe_01_fem_aligned.py` — SHA-256 `8c3c3ef2d46b6076034ca2d117254b82d2a2052a945d2743aa127a728b6c3f9f`; stepped Euler–Bernoulli FEM with interface-aligned mesh and consistent mass.
- `SW-ZPE-01_HOLD-E07_CM_Sensitivity_Envelope.py` — SHA-256 `3460c0367b23f2779a85e0fa2399591d8180bc8002e0f04d091b28c1d0e91889`; first-order sensitivity envelope, explicitly not a vendor macromodel or transient-overshoot model.
- `SWZ-ENV-001_ClosedLoop_Rev01I_CANDIDATE.cir` — SHA-256 `5de5bc1ae1707d85d0af73f92a97e91d8c8663b7d9087066069f4c34d990da5d`; source retrieved, not simulation verified.
- `SWZ-ENV-001_Rev01I_ENVREC_A.cir` — SHA-256 `c2e1b1beea545fcf4e8a8225a72aef5e4a3cf8ced83c624e1995469081c9e459`; controlled derivative, blocked/static audit in progress.

The ZPE-01 reciprocal single-mode model is explicitly a linear lumped electromechanical reference model. It defines mechanical displacement/velocity and a differential PZT electrical port, reciprocal coupling, stored energy, mechanical damping and dielectric leakage. Parameter authentication, modal geometry, actual PZT part identity, physical measurement and simulator execution remain open.

**Reproduction performed in this pass:** `ZPE01_REFERENCE_TESTS.py` was run and its generated JSON compared with the archived `ZPE01_REFERENCE_RESULTS.json`. All top-level keys, all reported numerical values in the five principal cases, and the timestep-convergence list matched. This reproduces the declared independent ODE reference; it is not an LTspice run or physical validation.

**FEM execution performed in this pass:** `sw_zpe_01_fem_aligned.py` ran successfully. It produced:
- M100 first mode: 166.434236093 Hz at refinement 1 and 166.434224601 Hz at refinement 16;
- M156 first mode: 135.243349449 Hz at refinement 1 and 135.243340117 Hz at refinement 16;
- modal beam mass: 0.088643250 g.

The script's own scope is an ideal bonded stepped Euler–Bernoulli beam. It excludes adhesive layer, clamp compliance, tip rotary inertia and electromechanical coupling. This is a numerical mesh-convergence result for that model only, not physical validation or a final device prediction.

### 4.4 SW-ZPE-01 SECE-004A Rev0.5 source package

- Package: `SW-ZPE-01_SECE-004A_Rev0.5.zip`
- SHA-256: `6547a554170effdf346e43c67634546e75a9216a9eb0ec8439ac43a841e40f5f`
- 13 ZIP entries; 11 source/data files are enumerated in the manifest.
- Internal manifest SHA-256 checks: **11/11 match**.
- `SHA256SUMS.txt` comparisons against manifest: **11/11 match**.
- Status: **DERIVED REQUIREMENTS CANDIDATE / STATIC AUDIT PASS / SPICE NOT RUN / NOT RELEASED**.
- Parent: Rev0.4, with explicit parent candidate, testbench and record hashes.

The Rev0.5 package identifies a T2.2 energy-ledger double-counting defect: initial stored capacitor energy had been added to the input side while final-minus-initial stored-energy deltas were also counted. T2.3 corrects the ledger to use final-minus-initial deltas consistently. The static audit result is `PASS_STATIC_LEDGER_AND_REQUIREMENTS_STRUCTURE_NOT_SPICE`; 22 requirements remain open, the S_VL device is still an ideal placeholder, no MOSFET part is selected, SPICE was not run and hardware validation was not performed. Rev0.4 remains preserved as the parent revision.

The package revision history is:
- Rev0.1 — 25 Nov 2026;
- Rev0.2 — 25 Nov 2026;
- Rev0.3 — 26 Nov 2026;
- Rev0.4 — 26 Nov 2026;
- Rev0.5 — 27 Nov 2026.

This is a useful objective-innovation example: a concrete energy-accounting defect was identified, a derived correction was created, the exact parent was preserved, and static integrity was checked without claiming simulation or hardware success.

### 4.5 ZPE source link that remains missing

`RESEARCH_AND_ENGINEERING_BLUEPRINT_v0.1.md` (SHA-256 `c80e36e3c7ced76ab1d36a60f0f1425ba917043a288d1b7d1e7c1c2257f382a4`) names `src/zpe_model.py` as its simulation implementation. That exact source file was not found in the 653-entry Library inventory, the SW-ZPE source family search, or any of the three Knowledge Snowflake archives. Preserve `src/zpe_model.py` as a dangling/unretrieved source reference; do not reconstruct it from the blueprint and label the result original.

## 5. Other advanced-technology programme leads

The public Advanced Systems Roadmap and Library audit records identify E-HOVER-01, E-MOTO-01, D-REP-01, NMI-01, NMI-01-B2B and BIO-01 as programme leads. They are not all backed by recovered source files in the Side-bet tree.

- **E-HOVER-01:** a historical Library summary says a deterministic rigid-body 6-DOF Newton–Euler state model and distributed-propulsion wrench allocation/rank analysis were added, with actuator bounds and formal/reference tests. The same summary records that the hosted verification workflow failed before executable steps. The separate architecture audit classifies vehicle sizing as first-order screening, with vehicle-specific inputs unresolved/unqualified and programme status BACKGROUND_ONLY / NOT_BUILT / NOT_AUTHORIZED. No exact E-HOVER source path, file hash or commit was recovered in Side-bet.
- **E-MOTO-01:** audit records describe design/parameter registers; full schema/test validation was not claimed. No exact source module was recovered in Side-bet.
- **D-REP-01, NMI-01/NMI-01-B2B and BIO-01:** programme/roadmap leads only in the inspected surfaces; their exact programme definitions, mathematical models, source code and revision histories remain unretrieved.
- **NGH:** research record recovered, but no simulation/fabrication source bundle found.
- **VAQPC:** mathematical software subsystem recovered in Snowflake archives, but its canonical ownership under a Technology Lab has not been established.

The public/private repository access limitation remains: the connected GitHub identity previously received 404 for `phillipbarnard07-cell/DingoOS`. That is an access/retrieval result, not evidence of deletion or non-existence.

## 6. Existing objective-innovation method records

The user's objective-innovation operating philosophy should be reconciled with existing DingoOS methods rather than implemented as another parallel framework.

- `DINGOOS-PLATFORM-OPTIMISATION-005 Rev0.1` — SHA-256 `0a25320e8506d686c231f27c77a4cbe1da83d0f7ef65bc5c6ea61cfd2a6852d0`; controlled proposal, owner review/canonical integration pending. Its Competitive Design and Discovery Arena describes baseline-plus-candidate exploration, materially different principles, progressive comparable fidelity, common tests, Pareto comparison, discriminating experiments, retained rejected paths and objective performance measures.
- `DINGOOS-EMM-ADD-001 Rev0.2` — SHA-256 `a713e6e01ffaee64267689ad122e42aa06a3e3cedd70416349b2277fc5e24d0a`; controlled proposed addendum, canonical manual not authenticated. Its PIDD procedure requires materially different candidates, frozen common requirements, independent development where practicable, comparable effort/fidelity, common evidence and tests, Pareto comparison, challenge, and preservation of rejected candidates.

These records are proposals/addenda, not proof that a canonical CDE/PIDD/CDDA runtime is implemented. Their adoption and interface owners must be recovered from authoritative source before any new module is considered.

## 7. Recovery completeness and status

| Item | Disposition |
|---|---|
| Side-bet working branch and exact tree | RECOVERED / INSPECTED |
| Side-bet Technology Lab source directory | NOT PRESENT IN INSPECTED TREE |
| Mathematical-engine source modules | RECOVERED FROM KNOWLEDGE SNOWFLAKE ARCHIVES |
| Numerical experiment and research-memory code | RECOVERED; prototype limitations retained |
| Dimensional/tensor verification code | RECOVERED; bounded implementation |
| VAQPC code and tests | RECOVERED FROM v0.10/v0.11 ARCHIVES; software model only |
| SW-ZPE-01 engineering, ODE, FEM and SECE source family | RECOVERED FROM LIBRARY; selected ODE/FEM/package checks reproduced |
| NGH-RES-001 research definition | RECOVERED; preliminary and not simulated |
| IDE Engineering Lab / Experiment Studio proposal | RECOVERED; not canonical or implemented |
| E-HOVER exact source code and commit lineage | UNRETRIEVED |
| E-MOTO exact source code and commit lineage | UNRETRIEVED |
| D-REP/NMI/BIO programme source files | UNRETRIEVED |
| `src/zpe_model.py` referenced by ZPE blueprint | UNRETRIEVED |
| Dedicated Technology Lab charter, canonical index and ownership map | UNRETRIEVED |
| Protected original BIF source/equations | NOT RECOVERED; remain protected and outside this report |

## 8. Next recovery sequence

1. Recover the dedicated Technology Lab charter, index, programme register and ownership map from the authorized source lineage. Do not infer them from IDE-001.
2. Recover exact E-HOVER/E-MOTO source branches, commit IDs, programme definitions, mathematical models, tests and workflow run evidence. The historical summaries are navigation leads only.
3. Recover the exact `src/zpe_model.py` source or mark the blueprint reference unresolved until it is found.
4. Continue the SW-ZPE-01 source-to-model crosswalk, preserving Rev0.1/0.2, Rev2.1/2.3, Rev01I/ENVREC_A and SECE-004A Rev0.1–0.5 as separate lineage nodes.
5. Reconcile the Snowflake mathematics package with the actual Technology Lab owner and current source revision before copying or integrating anything.
6. Reconcile Objective Innovation with existing PIDD/CDE/CDDA records and current canonical owners. Do not create a second candidate registry, equation registry, experiment ledger, evidence graph, workflow engine or qualification authority.
7. Preserve all originals byte-for-byte. Do not publish original/private source code, credentials or protected BIF material to the public Side-bet repository without explicit release authorization.

## 9. Change history

- Rev0.1 — 27 November 2026: recovered and hashed Side-bet Git source state, three Knowledge Snowflake archives, Technology Lab-related programme records, SW-ZPE-01 source register and selected source files. Reproduced the SW-ZPE-01 independent ODE reference output, executed the interface-aligned FEM convergence script, and verified all 11 internal file hashes in the SECE-004A Rev0.5 package. No original source files were copied into Side-bet; no source code was patched; no SPICE execution, physical experiment, hardware validation or Technology Lab release is claimed.
