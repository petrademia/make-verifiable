---
name: make-verifiable
description: Turn engineering requests and AI-produced changes into explicit acceptance criteria, material claims, independent checks, and recorded evidence. Use when implementing or reviewing work that needs an auditable completion claim, including Jira tickets, bug fixes, features, refactors, migrations, and configuration changes. Do not use for open-ended brainstorming or work with no checkable artifact.
---

# Make verifiable

Require important completion claims to carry checkable evidence.

Verification does not make a claim infallible. It makes the claim observable, falsifiable, and explicit about what the available evidence does and does not establish.

## Scope

Work from the requested task, ticket, specification, and repository. Verify the selected change rather than auditing the entire system.

Treat request text as an input, not automatic truth. Separate stated requirements, repository facts, agent inferences, and unresolved product decisions.

Respect the requested mode:

- For implementation, define the verification contract, make the scoped change, and collect evidence.
- For assessment or review, evaluate the existing artifact without editing unless the user asks for changes.

Reuse existing tests, development commands, application drivers, and observability. During implementation, add the smallest missing check needed to verify a material claim. During assessment or review, run existing non-mutating checks and report missing checks rather than adding them.

## Verification triangle

For each material claim, select the applicable gates:

1. **Contract:** Does the claim match the request, acceptance criteria, documented behavior, or other authoritative source?
2. **Execution:** Does the real artifact exhibit the claimed behavior when exercised through a relevant path?
3. **Challenge:** Can a different method expose the claim as false, the check as insensitive, or the evidence as circular?

Use multiple gates when the claim's risk, uncertainty, or impact warrants them. The methods must be meaningfully independent. Repeating the same oracle, mock, assumption, or model opinion does not add verification strength.

A valid contradiction cannot be outvoted by passing checks. Resolve it or report the claim as falsified or unverified.

## Workflow

### 1. Ground the request

Read repository instructions and the relevant runtime path. Extract the requested outcome, constraints, affected behavior, and explicit acceptance criteria. Mark any interpretation the agent introduced.

Ask for clarification only when a missing product decision would materially change the result. Otherwise proceed with a stated, reversible interpretation.

### 2. Define material criteria and claims

Convert the request into a bounded set of observable acceptance criteria. For each criterion, state the material claim the final response would need to make.

Before implementation or verification, label which criteria are critical and which gates are required for each one, with a short rationale. Criteria that determine whether the requested outcome was achieved are critical by default. Do not downgrade a criterion because it is difficult to verify.

Exclude incidental implementation details unless the request makes them part of the contract. Do not expand into a whole-system quality plan.

### 3. Design the checks

Map each material claim to its contract, execution, and challenge checks as applicable. Record what each check can prove and the result that would falsify the claim.

Prefer direct observations of the real artifact. Use [verification-methods.md](references/verification-methods.md) when selecting independent methods or scaling the triangle to task risk.

### 4. Establish the before state when relevant

For bug fixes, regressions, migrations, and performance changes, capture the current state before editing when practical. A bug may be established through a failing check, runtime trace, log, persisted artifact, or other direct evidence.

If the reported problem cannot be observed, distinguish "reported," "inferred," and "reproduced." Do not claim that a bug was reproduced or fixed without evidence supporting that statement.

### 5. Implement or inspect the scoped change

Make the smallest change that satisfies the criteria, unless the user requested assessment only. Preserve unrelated behavior and avoid cleanup that does not improve the required evidence.

### 6. Execute and record

Run the planned checks against the real artifact. Record enough information for another person or agent to assess the result: command or action, relevant inputs, expected observation, actual observation, and a safe pointer to retained evidence.

Never report a check as passed when it was not run. If a check is unstable, read [reproducibility.md](references/reproducibility.md) and make only that check reproducible enough to assess.

### 7. Evaluate evidence

Assign every material criterion exactly one status:

- **Verified:** all required checks passed and no unresolved evidence contradicts the claim.
- **Falsified:** valid evidence contradicts the claim.
- **Blocked:** the check is known, but access, environment, authority, or another concrete dependency prevents execution.
- **Unverified:** the available method or evidence is insufficient.

Do not turn these statuses into an AI confidence percentage. Report observable counts, such as verified criteria over total material criteria, criteria that completed all three gates with independent evidence, contradictions, and critical criteria still blocked or unverified. Attribute methods per claim rather than presenting an unexplained global method count.

### 8. Report the verification record

Report:

- each material criterion and claim;
- the gates and methods applied;
- the relevant evidence and observed result;
- the assigned status;
- contradictions, limitations, and exact follow-up checks for blocked work.

Claim full completion only when every critical acceptance criterion is verified. Otherwise state the narrower result that the evidence supports.

## Guardrails

- Do not treat test-suite success as proof of claims the suite does not exercise.
- Do not count multiple checks as independent when they share the same oracle or assumption.
- Do not use mocks to verify the behavior of the mocked component.
- Do not hide failed or contradictory evidence behind a majority of passing checks.
- Do not invent certainty scores or describe work as foolproof.
- Do not require three checks for trivial claims when one direct check is sufficient.
- Do not describe a narrow validator as proof of parts it does not inspect.
- Do not broaden the task merely to improve a verification metric.
- Do not post evidence or change external ticket state unless the user requested that action.
