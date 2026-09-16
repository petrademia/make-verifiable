# Sources and treatments

Use this reference after selecting one behavioral slice. It is a diagnostic aid, not a checklist to apply across the repository.

## Find the source

For every suspected source, ask:

1. Can it change the selected observable result?
2. Is there evidence that it did so in the failing or variable execution?
3. Is the variability required by the product contract?
4. What is the earliest responsible boundary where it can be controlled?

Prefer the first causally relevant uncontrolled input, not the most obvious call to a clock or random function.

## Treatment guide

| Source | Useful evidence | Narrow treatments | Common mistake |
|---|---|---|---|
| Wall clock, timers, time zones | Captured timestamp, offset, timer state, deadline calculation | Pass the relevant instant; inject one clock; use a virtual timer; test boundary dates explicitly | Freezing all time or extending sleeps |
| Randomness and generated IDs | Seed, generated sequence, collision or branch selected | Accept the value as input; inject a scoped generator; preserve and print the seed | A global seed that couples unrelated tests |
| Implicit ordering | Query plan, iteration order, arrival sequence, differing serialized output | Add required ordering; canonicalize equivalent results; compare as an unordered collection | Sorting data when order is product-significant |
| Concurrency and scheduling | Happens-before evidence, task lifecycle, locks, queue state, failing schedule | Synchronize on state; make ownership explicit; use a controlled scheduler when supported | Sleeps, broad locks, or disabling concurrency |
| Environment and process state | Relevant variables, locale, filesystem, ports, caches, prior-test state | Declare the input; isolate state; use a temporary namespace; reset the owning resource | Clearing broad global state without finding its owner |
| Network or external service | Request, response, status, headers, latency, retry decisions | Use an existing adapter; capture/replay at the boundary; run a faithful local dependency | Mocking internal business logic or recording secrets |
| Database, queue, or event delivery | Transaction boundaries, offsets, duplicate/delayed events, isolation level | Explicit ordering; idempotency; controlled driver; state-machine or history invariant | Assuming exactly-once delivery or immediate consistency |
| Probabilistic service or LLM | Model/config version, request, response, tool trace, evaluation result | Record/replay calls; constrain structured output; assert semantic invariants statistically when needed | Exact text snapshots or retries until one answer passes |

## Control-point rules

- Prefer a value parameter over a new interface when only one call site needs control.
- Prefer an existing dependency boundary over adding a parallel abstraction.
- Add an adapter when production and verification genuinely need different implementations.
- Use record/replay at the narrowest external boundary, not around the whole application.
- Preserve real implementations in integration coverage when fakes are used for focused scenarios.
- Treat canonicalization as valid only when the differing representations are semantically equivalent.
- For distributed behavior, determinize inputs and histories where possible; verify safety or liveness invariants where schedules must remain variable.
