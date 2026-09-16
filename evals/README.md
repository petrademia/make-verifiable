# Behavioral evaluations

These evaluations test whether an agent using `make-verifiable` makes the intended verification decisions. They do not grade exact wording.

## Layout

```text
evals/
├── fixtures/       Small artifacts available to the evaluating agent
├── scenarios/      Prompts given to the evaluating agent
├── expected/       Expected decisions hidden during the run
├── runs/           Recorded outcomes and rubric scores
└── rubric.md       Decision-based scoring rules
```

## Run an evaluation

1. Start an independent agent context.
2. Provide `SKILL.md`, the relevant reference guides, one scenario, and its fixture directory.
3. Tell the agent not to read `evals/expected`, `evals/rubric.md`, or prior runs.
4. Keep the run read-only unless the scenario explicitly authorizes changes.
5. Record the response, then score its decisions against the rubric and expected decision file.
6. Record the agent or model, repository commit, date, scenario result, and any observed ambiguity.

Do not coach the evaluator with the expected answer. A scenario passes only when every required decision invariant passes. Add scenarios when a real use exposes a decision failure that the existing set does not cover.

## Included scenarios

| Scenario | Behavior under test |
|---|---|
| `trivial-edit` | Required work does not automatically receive elevated assurance |
| `misleading-passing-tests` | Passing checks that miss the claim do not count as evidence |
| `conflicting-requirements` | Material contract conflicts block completion |
| `unavailable-runtime` | Missing runtime access prevents unsupported completion claims |
| `unsafe-challenge` | Stronger evidence does not justify unauthorized destructive action |
| `unreproduced-bug` | A verified failure condition does not establish an unobserved incident cause |
| `shared-oracle` | Multiple checks that share one oracle do not provide independent evidence |
| `unstable-performance-check` | Reproducibility controls only the diagnosed source of check variation |
