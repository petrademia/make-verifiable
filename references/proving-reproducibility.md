# Proving reproducibility

Use a proof that directly exercises the diagnosed cause. Repetition alone is weak when the causal condition can be controlled explicitly.

## Define bounded proof obligations

For the chosen behavioral slice, identify the smallest useful set of proof obligations:

- **Property:** a contract-level statement that must remain true, such as at-most-once charging, deterministic output for a declared seed, or convergence after reordered events.
- **Failure scenario:** a causally credible condition that could violate the property, such as a retry after timeout, a deadline crossing, a hidden RNG in another process, or a critical concurrent interleaving.
- **Proof:** the focused observation, replay, perturbation, or invariant check that can confirm or refute the property under that scenario.

Rank scenarios by observed evidence first, then impact and likelihood. Usually a few obligations are enough. Do not build an exhaustive matrix for unrelated components or list theoretical failures that cannot affect the selected behavior.

Where practical, test causality rather than stability alone: apply the control, perturb the suspected source, confirm the proof detects the meaningful change, and verify that removing the control can expose the original variability. This guards against a test that passes repeatedly for an unrelated reason.

| Behavior | Property | Failure scenario | Suitable proof |
|---|---|---|---|
| Idempotent command | At most one committed effect | Timeout followed by retry | Inject the boundary failure and assert one effect |
| Deadline policy | Result changes at the declared instant | Clock crosses the boundary | Drive a controlled clock across the instant |
| Event projection | Equivalent histories converge | Relevant events arrive in different orders | Exercise permutations and assert the invariant |
| Seeded computation | A captured seed replays the outcome | A worker uses undeclared randomness | Replay across workers and surface every seed |

## Establish the before-and-after claim

When practical, retain evidence that the original scenario could fail or vary before the change. The regression scenario should fail for the original reason, not because it matches incidental wording, timing, or implementation details.

After the change, prove both:

1. the controlled scenario produces the required result; and
2. the normal production path still uses the intended real dependency and preserves its contract.

## Choose the proof

| Situation | Strong proof |
|---|---|
| Randomized behavior | Re-run the captured failing seed and additional seeds; print a replay command or seed on failure |
| Timing boundary | Drive an explicit or virtual time across the relevant boundary without sleeping |
| Ordering dependence | Exercise multiple relevant orders or compare a canonical representation when order is irrelevant |
| Race or schedule dependence | Force the critical interleaving with synchronization or a scheduler; preserve the failing schedule if supported |
| External interaction | Replay the captured boundary interaction after removing or redacting secrets; retain a live-boundary integration check where appropriate |
| Distributed or eventually consistent behavior | Replay operation history when possible and check the stated safety or liveness invariant |
| Probabilistic output | Replay captured calls for deterministic regression; separately evaluate stable semantic properties across representative live runs |

There is no universal repetition count. If the triggering condition is known, force it. If only a historical failure rate is known, run enough independent attempts to materially exceed the prior exposure and state what was observed rather than claiming certainty.

## Required replay information

On a failure, retain the minimum information necessary to reproduce it safely:

- exact focused command or scenario identifier;
- seed, simulated time, or schedule identifier when applicable;
- relevant configuration and dependency versions;
- captured input or a safe pointer to it;
- expected contract and observed violation.

Never store credentials, personal data, or unrestricted production payloads merely to enable replay.

## Evidence standards

- A single passing run proves functionality, not reproducibility.
- A retry that eventually passes is evidence of instability, not success.
- A test that mocks the behavior under investigation is not a regression proof.
- A broad suite passing does not substitute for a focused scenario tied to the cause.
- A focused scenario passing does not establish that an entire service is deterministic.

## Handoff language

State evidence precisely. Prefer:

> Controlled the expiration clock at the policy boundary. The regression scenario crossed the deadline without wall-clock sleeps and passed on every observed run. The payment gateway remains live in integration coverage.

Avoid:

> The service is now deterministic.
