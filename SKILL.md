---
name: make-reproducible
description: Trace inconsistent or irreproducible software behavior, identify the causally relevant source of nondeterminism, apply the smallest appropriate control, and prove reproducibility. Use for flaky tests, intermittent failures, timing or ordering dependencies, races, randomness, variable external inputs, or requests to make an important behavior reliably verifiable. Do not use for ordinary deterministic bugs or generic test authoring.
---

# Make Reproducible

Turn uncontrolled variability into reproducible evidence.

Reproducibility means that the same declared inputs and controlled conditions produce the same relevant observable result. When exact output is intentionally variable, require a replayable trace or a stable invariant instead of forcing artificial sameness.

## Scope

Work on one important behavioral slice at a time. Trace it far enough to find the first uncontrolled input that causally affects the observed problem; do not attempt to determinize the entire repository.

Respect the requested mode:

- For diagnosis or assessment, gather evidence and recommend a bounded change without editing.
- For a requested fix or implementation, make the smallest justified change and verify it.

Reuse existing test, development, and application-driving infrastructure. Create a new harness only when no existing path can exercise the behavior, and keep it limited to the chosen slice.

## Workflow

### 1. Select and trace the behavior

Define the behavior in observable terms: entry point, declared inputs, state transitions, effects, and expected contract. Read repository instructions and follow the real runtime path across the components it touches.

### 2. Establish a baseline

Demonstrate the inconsistency when practical. Preserve the inputs and context needed to reason about it: seed, time, configuration, environment, ordering, schedule, external response, persisted state, and relevant logs.

Do not label a failure nondeterministic merely because it is difficult to reproduce. First rule out an ordinary input-dependent bug, stale state, or an incomplete test oracle.

### 3. Find the causal uncontrolled input

Inventory only sources that can affect the selected behavior. Typical sources include time, randomness and IDs, implicit ordering, concurrency, environment or process state, persistence, queues, networks, and probabilistic services.

Follow evidence to the earliest boundary where an uncontrolled value or event changes the outcome. Read [sources-and-treatments.md](references/sources-and-treatments.md) when classifying a source or choosing a treatment.

### 4. Choose the smallest control point

Prefer, in order:

1. Remove variability that has no product meaning.
2. Pass the value explicitly.
3. Canonicalize equivalent results.
4. Inject the narrow dependency that owns the variability.
5. Synchronize on a real condition instead of elapsed time.
6. Capture and replay an irreducible boundary.
7. Verify a stable invariant when exact output should remain variable.

Introduce only the control the evidence requires. A clock, RNG, scheduler, ID generator, adapter, simulator, or record/replay layer is an option, not a default deliverable.

### 5. Implement without changing the product contract

Keep production behavior intact unless the user requested a product change. Put the seam at the responsible boundary, preserve the normal production implementation, and make controlled behavior explicit in tests or verification scenarios.

Avoid unrelated cleanup. If the necessary change crosses multiple architectural boundaries or would materially serialize, mock, or redesign production behavior, stop and present the tradeoff before expanding scope.

### 6. Prove the result

Add or adapt the smallest regression scenario that would expose the original variability. Use the proof method appropriate to the source: repeated execution, seed replay, controlled schedule, recorded interaction, canonical comparison, or invariant checking.

Read [proving-reproducibility.md](references/proving-reproducibility.md) when selecting the proof or reporting confidence. A single green run is not evidence of reproducibility.

### 7. Report and stop

Report:

- the behavior and contract examined;
- the causally relevant uncontrolled input;
- the control introduced and why it is the narrowest useful one;
- the verification performed and its observed result;
- any limitations or remaining evidence-backed opportunities.

Create or update a backlog only when the user wants continuing evolution or multiple concrete candidates were discovered. Every entry must point to code or runtime evidence and state the affected behavior. Do not add speculative cleanup ideas.

Stop after the selected behavior is reproducible and the relevant checks pass.

## Guardrails

- Do not hide flakiness with arbitrary sleeps, timeout increases, silent retries, or quarantine.
- Do not seed randomness without surfacing the seed on failure.
- Do not globally serialize the system to conceal a race.
- Do not mock the component whose behavior is under investigation.
- Do not freeze every clock or replace every external dependency when one boundary is responsible.
- Do not require exact equality for intentionally probabilistic or distributed behavior; prove the meaningful invariant.
- Do not claim the repository or service is deterministic based on one corrected slice.
