# Make Verifiable

An agent skill that requires AI-produced engineering work to support its completion claims with checkable evidence.

`make-verifiable` turns a request, specification, or Jira ticket into observable acceptance criteria. It maps each material claim to relevant checks, runs those checks against the real artifact, records contradictions, and reports exactly what was verified, falsified, blocked, or left unverified.

## The verification triangle

```text
                   Contract
          What must be true?
                  /     \
                 /       \
                /         \
       Execution -------- Challenge
    Does it happen?      Can we disprove it?
```

- **Contract** checks the claim against the request, acceptance criteria, or another authoritative source.
- **Execution** observes the real artifact through a relevant user, runtime, compiler, data, or integration path.
- **Challenge** uses a different method to expose a false claim, insensitive check, or circular assumption.

The skill separates whether a criterion is required for completion from how much assurance its claim needs. A required typo correction may need a direct check. A required payment-integrity claim needs all three independent gates. A valid contradiction cannot be outvoted by passing checks.

Each gate catches a different mistake:

| Gate | Mistake it detects |
|---|---|
| Contract | Solving the wrong requirement |
| Execution | Producing an artifact that does not work |
| Challenge | Using weak, circular, or insensitive verification |

## Decision policy

Each criterion has a completion role and an assurance level:

- Required criteria gate the completion claim; supplemental criteria do not.
- Standard-assurance claims need Contract plus the most direct applicable observation.
- Elevated-assurance claims require Contract, Execution, and Challenge with independent evidence.

The outcome policy has explicit precedence:

1. Valid counterevidence means **Falsified**.
2. A known required check that cannot run means **Blocked**.
3. Missing or inadequate evidence means **Unverified**.
4. All required gates passing means **Verified**.

A verified claim is also **Triangulated** when all three independent gates pass.

Challenge checks must stay contained and reversible. Conflicting tickets, specifications, tests, documentation, or observed behavior block the contract gate until an authorized source resolves the disagreement.

## The workflow

```text
Understand the request and repository
    ↓
Extract observable acceptance criteria
    ↓
Map material claims to verification gates
    ↓
Establish the before state when relevant
    ↓
Implement or inspect the scoped change
    ↓
Run the checks and record evidence
    ↓
Report verified, falsified, blocked, and unverified criteria
```

The agent may claim full completion only when every required acceptance criterion is verified at its declared assurance level.

## Evidence instead of confidence

The skill reports observable results rather than an AI-generated confidence percentage:

```text
Material criteria:       5
Verified:                4
Falsified:               0
Blocked:                 1
Unverified:              0
Triangulated subset:     3
Required incomplete:     1
```

Passing an unrelated suite, repeating the same oracle, or asking several agents for opinions does not strengthen a claim. The verification record attributes each method to a specific claim, so aggregate counts cannot hide duplicated evidence.

## Behavioral evaluations

The [`evals/`](evals/) directory contains blind scenario inputs, small fixtures, expected decisions, a decision-based rubric, and recorded independent runs. The initial set covers a trivial edit, misleading passing tests, conflicting requirements, unavailable runtime access, and an unsafe destructive challenge.

Evaluators receive the skill, one scenario, and its fixture. They do not receive expected decisions or earlier run results until scoring. The evaluation checks decisions and evidence handling rather than matching generated wording.

## Example

Prompt:

```text
$make-verifiable Implement PROJ-123 and provide evidence for every material completion claim.
```

For a duplicate-payment bug, a useful verification record might include:

| Criterion | Contract | Execution | Challenge | Status |
|---|---|---|---|---|
| A retry causes at most one charge | Payment policy | Inject timeout and assert one committed charge | Remove the idempotency control and confirm the check detects the duplicate | Verified |
| Normal payments still succeed | Existing API contract | Focused integration scenario | Exercise a declined payment and retry boundary | Verified |
| The production incident had this exact cause | Incident report | Production trace unavailable | No safe replay available | Blocked |

The agent can claim that the change handles the verified retry scenario. It cannot claim that it established the production incident's exact cause.

## Unstable checks

Reproducibility is an optional verification technique. If a required check varies because of time, randomness, ordering, concurrency, or external inputs, the skill controls only the relevant source and then reruns the verification. It does not try to make the whole service deterministic.

## Install

Install with the Agent Skills installer:

```bash
npx skills add petrademia/make-verifiable
```

Or clone it into your agent's skills directory. For Codex:

```bash
git clone https://github.com/petrademia/make-verifiable.git ~/.codex/skills/make-verifiable
```

## Use

```text
$make-verifiable Review this change against the ticket. Define the material criteria, run independent checks where warranted, and report only the claims supported by evidence.
```

Agents with automatic skill discovery may also select it for implementation or review tasks that require an auditable completion record.

## Repository structure

```text
make-verifiable/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── evals/
│   ├── fixtures/
│   ├── scenarios/
│   ├── expected/
│   ├── runs/
│   └── rubric.md
└── references/
    ├── reproducibility.md
    └── verification-methods.md
```

## Design principle

> A material claim is verified only when intent, observed behavior, and an independent attempt to disprove it agree.
