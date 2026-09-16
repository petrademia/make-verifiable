# Verification methods

Use this guide when choosing checks for the verification triangle or deciding whether two methods are meaningfully independent.

## Test independence

Two checks add distinct evidence when they can fail for different reasons. Ask:

- Do they observe different parts of the real system?
- Do they use different inputs, oracles, or sources of truth?
- Could one pass while the other exposes the claim as false?
- Did one check come from the implementation's assumptions, or from an independent contract?

Examples of weak combinations:

- three tests that call the same mocked dependency;
- two agents reviewing the same summary without reading the artifact;
- a unit test and snapshot that assert the same implementation detail;
- an agent checking its own claim by restating the reasoning.

Examples of stronger combinations:

- an acceptance criterion, a user-path execution, and a mutation that proves the check detects the defect;
- a database invariant and an API-level integration test;
- a compiler or schema check and a live compatibility probe;
- a benchmark and a profiler trace tied to the same workload.

## Scale the triangle to risk

The contract gate applies to every material claim. Use the execution gate whenever the artifact can be exercised. Critical claims require contract, execution, and challenge gates with meaningfully independent evidence.

For noncritical claims, add the challenge gate when any of these conditions holds:

- the claim is costly or hard to reverse;
- the implementation and primary check share assumptions;
- the bug or regression was previously missed by existing checks;
- a passing check could be insensitive to the changed behavior;
- the evidence is probabilistic, indirect, or incomplete;
- the agent is making a causal or broad compatibility claim.

If a gate cannot run, mark the criterion blocked or unverified. Do not silently lower the standard.

## Decision policy for critical claims

| Gate result | Triangle outcome | Criterion status |
|---|---|---|
| Three passed | Triangulated | Verified |
| Two passed and one blocked | Partially verified | Blocked |
| Any valid counterevidence | Contradicted | Falsified |
| No adequate execution evidence | Unverified | Unverified |

A failed command is not automatically counterevidence. Distinguish an environmental or tooling failure, which may block verification, from an observation that falsifies the claim.

## Methods by task

| Task | Contract gate | Execution gate | Challenge gate |
|---|---|---|---|
| Bug fix | Reported symptom and expected behavior | Failing-before and passing-after scenario, trace, or direct observation | Revert or mutate the fix, inject the failure condition, or exercise a different path |
| Feature | Acceptance criteria and user contract | Focused user-path or integration check | Negative, boundary, permission, or failure-path check |
| Refactor | Preserved behavior and interfaces | Existing focused tests and representative execution | Differential comparison between old and new behavior |
| Migration | Target schema, protocol, or configuration | Forward migration on representative data or environment | Compatibility, rollback, restart, or partial-failure check |
| Performance | Defined workload and threshold | Repeated before-and-after measurement | Profiler trace, alternate workload, or regression distribution |
| Documentation or configuration | Authoritative format and intended consumer | Parser, renderer, loader, or dry-run | Broken-reference scan, clean-environment check, or independent source comparison |

## Challenge patterns

Choose a challenge that can expose false confidence:

- **Sensitivity:** remove, revert, or mutate the relevant change and confirm that the check detects the difference.
- **Boundary:** exercise values immediately around a threshold or contract edge.
- **Negative path:** provide invalid, unauthorized, missing, or conflicting input.
- **Differential:** compare the same input across versions, configurations, or implementations.
- **Invariant:** inspect the resulting state rather than trusting a success response.
- **Independent source:** compare against an authoritative document, system of record, or separately collected observation.
- **Fault injection:** force the error, timeout, retry, crash, or partial completion that the claim says is handled.

Do not run every pattern. Select the smallest one that can falsify the material claim.

## Evidence record

For each material criterion, retain:

- criterion and claim;
- gate and method;
- command, action, or source;
- relevant input and environment;
- expected observation;
- actual observation;
- evidence location or concise output;
- final status and any contradiction.

Evidence must be reviewable without exposing credentials, personal data, or unrestricted production payloads.
