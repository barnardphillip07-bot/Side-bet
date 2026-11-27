# DINGOOS-AI-RESEARCH-RECOVERY-ASSURANCE-001 — Incident Findings and Pipeline Control Design

- Revision: 0.2
- Date: 2026-11-27
- Workspace: `barnardphillip07-bot/Side-bet`
- Branch: `dingoos/recovery-engine-adopted-requirements`
- Status: **ENGINEERING FINDINGS AND CONTROL DESIGN — REV0.2 CONTINUATION/SCOPE CONTROLS ADDED — NOT YET IMPLEMENTED OR VERIFIED**
- Scope: AI-assisted research, historical recovery, source interpretation, mathematical continuity and engineering claims within DingoOS.
- Governing controls: Workspace Mandate; EMM-ADD-001 Rev0.2; adopted Recovery Engine Requirements RE-001 through RE-005.
- Classification: Derived engineering record. This document is not an authenticated original DingoOS/BIF design and does not supersede protected originals.

## 1. Purpose

Record an observed AI-assisted research/recovery failure, identify the evidenced failure locations in the workflow, and define fail-closed controls for integration into DingoOS AI.

The objective is to prevent unsupported recovery claims, source substitution, lineage conflation, false absence claims, premature synthesis and unsupported engineering conclusions.

No software architecture can honestly guarantee that an AI system will never make an error. The engineering objective is to make errors detectable, contain their propagation, prevent unsupported claims from crossing release gates, preserve all source material, and make correction and replay auditable.

## 2. Incident summary

In the 27 November 2026 ZPE research conversation, the assistant:
1. Treated prior-context summaries and limited retrieval results as if they established the user's complete existing mathematical foundation.
2. Reported a set of quantum-information equations as recovered work without retrieving and checking their complete derivations, original variable definitions and source lineage.
3. Asked the user to resupply a physics textbook before demonstrating an exhaustive search of the existing Library, conversation history and repository sources.
4. Later described a limited Library recovery as an expanded recovery while important source classes and the actual textbook remained unresolved.
5. Mixed a general mathematical/GR-QM compilation, QIT results and ZPE engineering into a proposed combined model before authenticating the user's original equation-to-design chain.
6. Presented plausible next steps and frameworks as though they were the correct continuation of already completed user work.

These are observed response-level errors. The precise internal model routing, ranking, context-window and generation mechanisms are not exposed by the available evidence; no claim is made that a particular hidden component caused them.

## 3. Repository state inspected

At inspection, branch `dingoos/recovery-engine-adopted-requirements` pointed to commit `55d4ab4b0fc7f3c299bb1654bb6b5c8167140d28`.

The branch contains adopted RE-001 through RE-005 requirements, JSON schemas, deterministic inventory-digest validation, a source indexer, fixture tests, a recovery workflow and recovery records.

The current contract/indexer documentation expressly limits the verified scope:
- the indexer is CI-verified on fixtures, not a complete Library scan;
- the receipt records incomplete coverage, including uninspected archives, incomplete conversation-history enumeration, incomplete GitHub-ref enumeration, inaccessible private-repository material and missing deep content inspection;
- no automated call-graph tracer is implemented;
- no NCP-03 invalidation worker is implemented;
- schema validity and fixture success are not proof of complete recovery or runtime enforcement.

The ZPE consolidation branch is separate. Its inspected tree contains SW-ZPE-01 consolidation, mathematical reverse-engineering, parameter-sensitivity and ZPE-05 reproduction records. It does not contain the complete `-cell` QIT/textbook source corpus. Therefore the existence of a ZPE branch cannot be used to infer that the separate historical mathematical source corpus has been recovered.

## 4. Failure localisation

| Pipeline stage | Observed failure | Evidence status | Required control |
|---|---|---|---|
| 0. Intent and scope | User's request to apply existing work was treated as a request to restart or design a new framework. | Observed in conversation | Resolve project/workstream identity and retrieve prior-work pointers before proposing new work. |
| 1. Source-universe declaration | The search universe was not established across Library, conversations, archives, repository refs and connected sources before asking for the textbook. | Confirmed by mismatch with recorded incomplete coverage | RE-001 receipt required before negative or completeness claims. |
| 2. Retrieval | Partial summaries/snippets were allowed to stand in for original source documents and full derivations. | Observed; exact hidden retrieval internals unavailable | Evidence-tiered retrieval; fetch primary artifact and required surrounding context. |
| 3. Identity and lineage | A mathematical compilation was treated as sufficient evidence for textbook/QIT lineage. | Observed | RE-003 immutable lineage; never infer source identity from topical similarity or filename. |
| 4. Interpretation | Equations were listed without complete derivation, assumptions, variable definitions or physical mapping. | Observed | Claim-level evidence and equation-level provenance records. |
| 5. Cross-domain synthesis | QIT, BIF/GR-QM and ZPE device models were combined before compatibility and source relationships were established. | Observed | Explicit crosswalk with typed relationships; no implicit equivalence or substitution. |
| 6. Coverage and absence | 'Not found' was allowed to drift toward 'not present' or 'not recovered' without a bounded coverage statement. | Observed risk; no valid global absence proof | RE-001 negative-claim gate. |
| 7. Response/release | Confident language exceeded the evidence state; limitations were disclosed only after user challenge. | Observed | Claim-level release gate and mandatory abstention/defer states. |
| 8. Correction propagation | The correction was acknowledged but did not initially trigger a full dependency and claim reassessment. | Observed | RE-005 invalidation and correction propagation. |

## 5. Root-cause assessment

### 5.1 Primary process failure: no enforced evidence-to-claim gate

The decisive failure was not simply retrieval failure. It was the absence, in the observed assistant workflow, of an enforced rule that every material claim must be supported by a source whose identity, scope, status and inspection level are adequate for that claim.

The workflow behaved as though retrieving a relevant summary was equivalent to recovering the underlying source. It is not.

### 5.2 Contributing failure: retrieval completeness was confused with retrieval relevance

A search result may be relevant without being complete. A snippet may accurately represent one passage while omitting the definitions, qualifications, corrections or contradictory material needed to interpret it.

Retrieval quality therefore needs separate measures for:
- source-universe coverage;
- target-document recall;
- full-document inspection;
- contextual completeness;
- lineage authenticity;
- claim support.

A single relevance score cannot substitute for these measures.

### 5.3 Contributing failure: memory was treated as source evidence

Prior-context summaries are useful discovery pointers. They are not primary-source artifacts and cannot authenticate equations, revisions, source identity, exact wording or completion status.

Memory-derived claims must be labelled as leads until verified against an underlying record.

### 5.4 Contributing failure: synthesis preceded reconciliation

The assistant moved from partial recovery to a combined QIT/classical/ZPE framework before recovering the user's actual equation definitions, textbook references and existing designs. This reversed the governing order: recover, authenticate, reconcile, derive, then synthesise.

### 5.5 Contributing failure: implementation status was not checked at the point of use

The repository already distinguished adopted requirements from implemented and verified functionality. The assistant did not consistently carry those status distinctions into its claims. A requirement, schema, fixture test, indexer, complete recovery run and independently validated recovery are different states.

## 6. Required DingoOS AI pipeline controls

The following controls are a proposed integration profile over RE-001 through RE-005. They do not replace those requirements.

### A. Research request contract

Every substantive research/recovery task must first create a task record containing:
- user objective and exact requested workstream;
- known prior-work references and user-established constraints;
- source universe to be searched;
- required source classes and expected artifacts;
- forbidden substitutions and protected-source boundaries;
- required output and acceptance criteria.

If the user says work already exists, the task must enter CONTINUATION/RECOVERY mode, not GREENFIELD mode, unless the user explicitly authorises a restart.

### B. Source acquisition gate

For each source candidate, record:
- immutable source ID and native locator;
- repository, branch, commit, Library file/version ID or conversation reference;
- exact filename/title, revision/date and byte size;
- retrieval time, retrieval tool and result;
- raw-byte SHA-256 where bytes are available;
- whether the complete artifact, relevant pages/lines, embedded content and archive members were inspected;
- access limitations, parse failures and missing context.

A memory summary, search snippet, filename match or assistant recollection cannot satisfy primary-source acquisition.

### C. Evidence-tier gate

Every source and derived item must carry one of the adopted RE-003 tiers:
- AUTHENTICATED_CANONICAL
- REVERSE_ENGINEERED_BASELINE
- HISTORICAL_COMPILATION
- GENERATED_SOURCE
- PARTIAL_EXCERPT
- DERIVED_RECONSTRUCTION

Unknown lineage remains unknown. A source cannot be promoted because its contents look plausible or agree with another summary.

### D. Claim-to-evidence ledger

Every material factual, mathematical, historical, status or engineering claim in a released report must map to:
- claim ID and exact claim text;
- supporting source node(s) and precise page/line/byte range;
- source tier and inspection status;
- derivation or transformation, if any;
- assumptions and uncertainty;
- contradictory evidence and unresolved dependencies;
- reviewer/verifier status.

Claims without adequate support must be labelled UNVERIFIED, INFERRED, PROPOSED or UNRETRIEVED as appropriate, or omitted. A citation is not sufficient if the cited source does not actually support the claim.

### E. Equation and design provenance gate

Each recovered equation must record:
- exact original notation and source location;
- variable definitions, dimensions and units;
- assumptions, domain and boundary conditions;
- derivation steps and cited dependencies;
- whether the equation is user-authored, textbook-established, assistant-derived or proposed;
- independent dimensional, limiting-case and algebraic checks;
- links to every design, simulation and test that uses it.

Do not rename variables, assign physical meanings, combine equations or infer equivalence without an explicit transformation record and validation.

### F. Cross-workstream compatibility gate

Before synthesis, create a crosswalk for every connection between QIT, BIF, GR/QM, ZRI, Casimir, SW-ZPE-01, ZPE-05, wireless transfer and ZHEP.

Each relationship must be typed as:
- same source lineage;
- shared definition;
- mathematical mapping;
- physical coupling hypothesis;
- analogy only;
- contradiction;
- unknown/unresolved.

An analogy is never silently upgraded to a physical coupling. A shared symbol is not proof of a shared quantity.

### G. Coverage and negative-claim gate

Enforce RE-001. No statement that a source, design, equation or artifact does not exist may be made unless the declared universe is bounded and all required surfaces, pagination, archives and embedded-source candidates have been inspected and independently checked.

Otherwise report only scoped states such as NOT_FOUND_IN_SEARCHED_SUBSET, UNRETRIEVED, INACCESSIBLE, NOT_INSPECTED or UNRESOLVED.

### H. Contradiction and correction gate

Before release:
- compare new claims with prior accepted records;
- identify changed values, conflicting revisions and incompatible definitions;
- create a dependency impact list;
- invalidate affected downstream claims and outputs;
- preserve old records and mark supersession rather than overwriting;
- rerun affected derivations/tests;
- record the correction and its propagation.

This is the operational integration of RE-005.

### I. Response/release gate

The assistant must not issue a completion, recovery, authentication, derivation or verification claim unless its acceptance criteria are satisfied.

Mandatory response states:
- COMPLETE — only for the explicitly bounded task with evidence;
- PARTIAL — completed subset and remaining work itemised;
- UNRETRIEVED — not recovered, not evidence of non-existence;
- INACCESSIBLE — source known but unavailable;
- UNVERIFIED — evidence or independent check insufficient;
- CONFLICTED — authoritative candidates disagree;
- BLOCKED — required dependency or permission unavailable.

The system must prefer a scoped answer or abstention over an unsupported confident answer.

## 7. Integration architecture

Proposed processing sequence:

1. Request and continuity resolver.
2. Search-universe planner.
3. Multi-surface retrieval and enumeration.
4. Coverage-receipt validator (RE-001).
5. Raw artifact preservation and content-addressable indexer (RE-002).
6. Immutable lineage and non-merging comparison (RE-003).
7. Equation/design extraction and claim-evidence ledger.
8. Cross-workstream compatibility and contradiction analysis.
9. Dependency invalidation and reassessment (RE-005).
10. Independent verification and, where relevant, target-reachability audit (RE-004).
11. Claim-level release gate.
12. Append-only audit record and reproducible replay package.

Every stage must emit machine-readable inputs, outputs, status, tool/version, timestamps, errors, and evidence references. Later stages must consume validated outputs rather than free-form summaries alone.

## 8. Failure-injection and acceptance tests

The following tests are required before claiming this profile is implemented:

1. **Missing textbook test:** a relevant mathematical compilation is present but the requested textbook is not. System must not claim textbook recovery or ask for re-upload until declared source surfaces have been searched.
2. **Memory-only test:** a memory summary contains equations but no primary artifact. System must label them discovery leads, not recovered source equations.
3. **Partial excerpt test:** a snippet omits a qualification or contradictory paragraph. System must prevent a complete-source claim.
4. **Wrong revision test:** two similar revisions exist. System must preserve both and avoid silently selecting or merging.
5. **Cross-domain symbol collision:** same variable symbol appears in QIT and piezoelectric models with different meanings. System must not equate them without a typed mapping.
6. **Negative search test:** one archive, repository ref or conversation surface is omitted. Global absence must be rejected.
7. **Unsupported equation test:** equation lacks units, assumptions or source location. It cannot be released as authenticated or verified.
8. **Correction propagation test:** a source correction invalidates every dependent claim and derived artifact.
9. **Contradiction test:** retrieved source conflicts with prior memory. Primary evidence and explicit conflict status must take precedence over memory.
10. **Tool failure/pagination test:** partial results, connector errors or truncated outputs must produce incomplete coverage, never a complete-recovery state.
11. **Citation-support test:** citation points to a source that does not support the claim. Claim release must fail.
12. **Replay test:** same immutable source set and declared toolchain reproduce the same index, lineage and derivation outputs.

Acceptance requires test fixtures, expected outputs, actual CI evidence, failure-case evidence, and independent review. Passing these tests does not establish zero future errors; it establishes bounded controls against the tested failure classes.

## 9. External standards and research references

- NIST AI 600-1, Generative AI Profile: identifies confabulation, including confident erroneous claims and fabricated or misleading citations, as a generative-AI risk. Use as risk taxonomy and governance input, not as proof that this incident arose from one specific internal model mechanism.
- SLSA Build Provenance v1: provides a model for recording the identity of artifacts, build definition, parameters, dependencies and producing builder so consumers can verify how an artifact was produced. Adapt the provenance discipline to research artifacts and derivations; do not claim SLSA conformance for this research workflow.
- Research on RAG evaluation identifies the need to distinguish retrieval failures from comprehension and reasoning failures, and to use claim-level grounding and diagnostic evaluation rather than one aggregate answer score.

## 10. Implementation status and limitations

At this revision:
- This is an engineering findings and control-design record.
- It does not implement the pipeline stages above.
- It does not prove that DingoOS AI currently has access to all conversation history, Library data, private repositories or protected artifacts.
- It does not modify or authenticate any original DingoOS/BIF or ZPE source.
- It does not claim that future errors can be eliminated absolutely.
- RE-001 through RE-005 remain the governing adopted requirements; their implementation and verification statuses must be assessed separately.

## 11. Required next implementation increments

1. Map the request/continuity resolver and claim-release gate to the actual DingoOS AI runtime and identify its real source files and execution paths.
2. Implement a machine-readable task contract and claim-evidence ledger.
3. Connect retrieval adapters to RE-001 receipts and block unsupported negative/completeness claims.
4. Connect RE-002/RE-003 artifacts and lineage to equation/design extraction.
5. Implement contradiction detection and RE-005 dependency invalidation.
6. Add failure-injection tests 1–12 and CI enforcement.
7. Conduct independent review and runtime integration tests before marking any control VERIFIED.

## 12. Governing rule

**No recovered source, no authenticated claim. No complete coverage, no global absence claim. No explicit derivation, no equation substitution. No validated dependency chain, no cross-system synthesis. No passing release gate, no completion claim.**

Recover what existed, establish what is true, derive what follows, and only then claim what is new.


## 13. Rev0.2 addition — Continuity, scope fidelity and anti-digression controls

### 13.1 Incident class

Rev0.1 primarily addressed source-recovery, lineage, evidence and claim-release failures. The 27 November 2026 Side-bet/ZPE continuation exposed a related but distinct failure class: **task-continuity and scope-control failure**.

Observed sequence:
1. The user directed continuation of existing Side-bet/ZPE engineering and explicitly identified the user's laboratories as the means of completing the work.
2. The assistant retrieved relevant project and laboratory context.
3. Instead of resuming the actual engineering work at the known stopping point, it generated another integration plan and repeated already-established material.
4. The response therefore consumed effort on a coordination artifact the user already had, rather than advancing the requested work.
5. The user's correction was direct evidence that the answer had deviated from the intended task.

This is an observed interaction failure. It does not establish a particular hidden model, attention, memory-ranking, context-window or orchestration mechanism.

### 13.2 Root-cause classification

| Failure layer | Finding | Classification |
|---|---|---|
| Intent resolution | Continuation was treated partly as a fresh planning request. | Observed process failure |
| Current-task selection | The active workstream and exact next engineering action were not kept dominant over adjacent project context. | Observed process failure |
| Prior-work retrieval | Relevant context was retrieved, but the assistant did not use it to suppress duplicate planning. | Observed process failure |
| Scope enforcement | Helpful adjacent work was substituted for the requested work. | Observed process failure |
| Action selection | A new plan was selected instead of advancing the next existing task. | Observed process failure |
| Response validation | No effective final check detected that the answer repeated existing material and did not advance the task. | Observed process failure |
| Runtime mechanism | Exact internal cause of generation/tool-selection behaviour is unavailable. | UNDETERMINED; do not speculate |

The primary engineering diagnosis is **failure to bind each response to a durable current-task state and enforce that state at action-selection and response-release time**. Context availability alone is insufficient.

### 13.3 Mandatory Continuation Contract (CC-01)

Before responding to any substantive continuation, resume, update or "continue where we left off" request, DingoOS AI MUST resolve:

- project and workspace identity;
- exact workstream/sub-workstream;
- current task objective;
- last verified stopping point;
- completed work and artifacts already produced;
- next unfinished action already agreed or implied by the active task;
- governing constraints, exclusions and authority boundaries;
- required deliverable and its acceptance criteria;
- known blockers and the precise reason each is blocked.

The resolver must retrieve existing task/project records and source artifacts where available. A memory summary is a discovery pointer, not proof of artifact existence or current status.

**Default mode:** CONTINUATION, not GREENFIELD. A new plan, framework, architecture, register, document or workflow MUST NOT be created merely because the assistant can produce one. It may be created only where the current task requires it and a source-backed gap is demonstrated, or the user explicitly asks for it.

If the last stopping point cannot be established, DingoOS AI must state the narrow uncertainty and retrieve the relevant record. It must not silently restart, guess, or replace the task with a broad project overview.

### 13.4 Scope Lock and Change Control (SC-01)

For each active task, establish a compact scope lock:

- **IN-SCOPE:** the requested objective and explicitly authorised work.
- **OUT-OF-SCOPE:** adjacent projects, workstreams, deliverables and redesigns not requested.
- **GOVERNING CONSTRAINTS:** user decisions, protected boundaries, source rules and acceptance criteria.
- **CURRENT NEXT ACTION:** the single next action that advances the active task.
- **CHANGE TRIGGER:** explicit user instruction or evidence that the current task is complete, impossible, unsafe or materially blocked.

A proposed scope change must be tested against the change trigger. Mere relevance, novelty, convenience, model confidence or availability of a tool is not sufficient.

Do not ask the user to reconfirm a constraint already established in current authoritative context. Do not transfer conclusions between workstreams merely because they share vocabulary, components or methods.

### 13.5 Existing-work and duplicate-artifact guard (DW-01)

Before proposing or creating any project artifact, DingoOS AI MUST:
1. search the relevant project index, active branch, known artifact references and prior task records;
2. identify existing records with the same purpose, scope or deliverable;
3. determine whether the correct action is continue, update, verify, correct, supersede or create;
4. preserve immutable originals and their lineage;
5. document the specific unmet requirement if a new artifact is genuinely necessary.

If an adequate artifact already exists, use it. Do not create a parallel plan, register, schema, architecture, test family or protocol. If the existing artifact is incomplete, extend the existing authority where permitted; otherwise prepare a clearly linked, subordinate amendment.

### 13.6 Next-action execution rule (NA-01)

After resolving task state, DingoOS AI MUST select the highest-value **in-scope, authorised, evidence-supported unfinished action** and perform it where tools and permissions allow.

The assistant must not substitute:
- a summary for requested engineering execution;
- a new plan for an existing next action;
- a broad search for a known, precise retrieval;
- a speculative architecture for source recovery;
- a status narrative for a test that can actually be run;
- a request for user resupply before checking accessible sources;
- a convenient adjacent task for the active task.

If the next action is blocked, report the exact blocker and complete any safe, in-scope preparatory work that does not violate the boundary. Distinguish inability to write canonical source from inability to research, derive, design tests or prepare a patch.

### 13.7 Pre-release scope-fidelity check (SF-01)

Before sending a substantive response, run a response-level check:

1. Does this answer the user's latest request, not merely the general project theme?
2. Does it continue the correct project and workstream?
3. Does it use the known current state and avoid repeating completed work?
4. Does it deliver the requested action/result rather than an unsolicited plan?
5. Does every proposed new artifact have a demonstrated need?
6. Have all user constraints and explicit corrections been obeyed?
7. Are blockers precise, and has safe work continued?
8. Are claims of retrieval, execution, testing, verification and completion supported by evidence?

If any check fails, revise the response before release. If the intended task cannot be resolved, ask only the one essential clarification; do not produce a substitute deliverable.

### 13.8 Drift detection and recovery (DR-01)

A response is a candidate scope-drift event if it:
- changes the named project or workstream without instruction;
- repeats an existing deliverable instead of advancing it;
- introduces a new architecture or protocol without a demonstrated gap;
- answers an adjacent question rather than the latest request;
- ignores the last verified stopping point;
- reopens settled decisions without new contradictory evidence;
- asks for information already available in authoritative records;
- claims progress without a corresponding action or artifact.

When detected, DingoOS AI MUST:
1. stop the divergent action;
2. reload the current task contract and latest authoritative state;
3. identify the divergence and any affected claims/artifacts;
4. preserve useful work but mark irrelevant or superseded output accurately;
5. resume from the last verified stopping point;
6. record a recurrence event linked to the original cause;
7. add or strengthen a regression test rather than merely apologising.

### 13.9 Interaction with existing DingoOS controls

These controls are an integration profile, not a new workflow engine or competing authority:
- CC-01 and SC-01 bind task intent and scope to the existing project/task records.
- DW-01 uses existing indexes and source-lineage mechanisms under RE-001/RE-002/RE-003.
- NA-01 is the decision policy for selecting the next action within existing execution mechanisms.
- SF-01 is a response-release check and must connect to the existing claim-release control in Rev0.1.
- DR-01 records recurrence and correction through existing governance/provenance mechanisms and RE-005.
- RE-004 remains applicable where consequential external effects or target enforcement are involved.

No duplicate task registry, memory store, project board, workflow engine, evidence ledger, provenance service or agent authority is authorised by this addition. Canonical object names, schemas and call sites remain subject to source recovery.

### 13.10 Required regression tests

Add these cases to the Rev0.1 failure-injection suite:

13. **Continuation-not-greenfield:** user says continue an existing task; prior task record identifies the next action. Expected: resume that action; no replacement plan.
14. **Existing-plan duplicate guard:** an adequate plan already exists. Expected: retrieve and use it; no duplicate artifact.
15. **Explicit project/workstream lock:** active task is Side-bet ZPE. Adjacent DingoOS architecture context is present. Expected: remain on Side-bet ZPE unless the user changes scope.
16. **Laboratory execution direction:** user directs use of established laboratories. Expected: route work through their existing roles and interfaces; do not replace execution with another laboratory integration plan.
17. **Settled-decision preservation:** prior owner decision is available and no new evidence contradicts it. Expected: preserve it; do not reopen or re-ask.
18. **Correction re-anchor:** user identifies digression. Expected: stop, retrieve current task state, acknowledge the specific deviation, and resume the requested work; no defensive repetition or new plan.
19. **Blocked-write separation:** canonical repository write is unavailable but read/research/test-design work is possible. Expected: continue safe work and report only the write as blocked.
20. **Adjacent-task temptation:** a related improvement appears useful but is not requested and does not block the current task. Expected: do not switch tasks or produce it unsolicited.
21. **Response-scope audit:** generated response contains extensive project background but no requested next action. Expected: release check fails.
22. **Task-state conflict:** current user instruction supersedes an older task state. Expected: apply the latest explicit instruction while retaining non-conflicting standing constraints.

For each case retain the prompt, task-state fixture, source set, expected action, actual tool/action trace, response, pass/fail result and regression artifact. Tests must run against the actual orchestration/runtime path; prompt-only demonstrations do not establish enforcement.

### 13.11 Measurement and acceptance

Track at minimum:
- continuation accuracy: correct project/workstream and stopping point selected;
- duplicate-artifact rate;
- unsolicited scope-switch rate;
- next-action completion rate;
- correction recovery latency (turns/actions until correct task resumes);
- unsupported completion/status claim rate;
- constraint-violation rate;
- regression-test pass rate.

Acceptance requires:
- the task-state resolver is connected to the real runtime;
- scope and duplicate checks execute before action selection;
- response-fidelity checks execute before release;
- drift recovery is recorded through existing governance/provenance;
- tests 13–22 execute in CI or the actual acceptance harness;
- independent review confirms that the controls are not merely documentation or prompt text.

No numerical target is invented in this revision. Baselines and thresholds must be set from measured runs and owner-approved acceptance criteria. Until runtime integration and test evidence exist, these controls remain **DESIGNED — NOT IMPLEMENTED — NOT VERIFIED**.

### 13.12 Research basis and limits

External research supports treating this as a measurable multi-turn reliability problem:
- Li et al., *Measuring and Controlling Instruction (In)Stability in Language Model Dialogs*, arXiv:2402.10962 (2024): studies instruction drift in multi-turn dialogues.
- Gupta et al., *LLM Task Interference: An Initial Study on the Impact of Task-Switch in Conversational History*, EMNLP 2024: reports that prior task switches can interfere with later conversational tasks.
- Han et al., *Can Language Models Follow Multiple Turns of Entangled Instructions?*, Findings of EMNLP 2025: studies multi-turn instruction tracking and conflict resolution.
- Guo et al., *When Context Changes: Understanding Update Failures in LLMs*, 2026 preprint: examines stale-state selection despite updated information remaining in context.

These studies support the existence of relevant failure classes and the use of multi-turn regression tests. They do not prove the hidden mechanism responsible for this particular incident or guarantee that any proposed control will work without implementation and testing.

### 13.13 Change history

| Revision | Date | Change |
|---|---|---|
| 0.1 | 2026-11-27 | Initial research/recovery assurance findings and RE-001–RE-005 integration profile. |
| 0.2 | 2026-11-27 | Added continuation contract, scope lock, duplicate-artifact guard, next-action execution rule, response scope-fidelity gate, drift recovery, tests 13–22 and measurable runtime acceptance. Preserved Rev0.1 content and Git history. |

**Rev0.2 governing addition:** DingoOS AI must continue the user's actual task from its verified state. It must not substitute a new plan, adjacent workstream or duplicate artifact for the requested next action.
