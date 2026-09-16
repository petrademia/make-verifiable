# Make Reproducible

An agent skill for turning uncontrolled software variability into reproducible evidence.

`make-reproducible` helps coding agents investigate flaky tests, intermittent failures, timing dependencies, unstable ordering, races, randomness, and variable external inputs. It traces one important behavior, finds the causally relevant uncontrolled input, applies the smallest justified control, and proves the result without pretending the entire system is deterministic.

## The loop

```text
Select one important behavioral slice
    ↓
Trace it end to end and establish a baseline
    ↓
Map causally relevant nondeterminism and evidence gaps
    ↓
Define bounded properties and failure scenarios
    ↓
Choose the smallest high-leverage control point
    ↓
Make that input controllable and add the minimum proof mechanism
    ↓
Repeat, replay, or perturb the scenario to prove the contract
    ↓
Record remaining evidence-backed opportunities and stop
```

The skill treats clocks, seeded randomness, schedulers, adapters, simulators, and record/replay systems as optional techniques—not mandatory architecture.

## What makes it different

Generic verification asks whether a behavior works. `make-reproducible` asks why the same behavior can produce different outcomes and what the narrowest responsible control point is.

It is designed to:

- distinguish genuine nondeterminism from ordinary input-dependent bugs;
- follow evidence to the first uncontrolled input that changes the outcome;
- derive a small set of contract-level properties and causally credible failure scenarios;
- preserve production semantics while exposing a focused control seam;
- reuse the repository's existing tests and application-driving infrastructure;
- require repeatable proof rather than accepting one green run;
- stop after the selected behavior is reproducible.

It explicitly rejects arbitrary sleeps, timeout inflation, silent retries, broad serialization, and unsupported claims that an entire service is deterministic.

## Example

Prompt:

```text
$make-reproducible Diagnose why this payment-expiration test fails intermittently and make the behavior reproducible.
```

A good run should:

1. trace the payment-expiration behavior rather than scan the whole repository;
2. show whether wall-clock time actually causes the inconsistent result;
3. introduce a controllable instant or narrow clock boundary only if the evidence supports it;
4. state the deadline property and exercise the relevant boundary-crossing scenarios;
5. replace timing-dependent waiting with an explicit condition;
6. prove the deadline behavior without sleeping, including a perturbation that detects the boundary;
7. report the evidence and stop.

## Install

Install with the Agent Skills installer:

```bash
npx skills add petrademia/make-reproducible
```

Or clone it directly into your agent's skills directory. For Codex:

```bash
git clone https://github.com/petrademia/make-reproducible.git ~/.codex/skills/make-reproducible
```

The repository follows the portable Agent Skills layout: the root [`SKILL.md`](SKILL.md) is the entrypoint, conditional guidance lives in [`references/`](references/), and [`agents/openai.yaml`](agents/openai.yaml) provides Codex UI metadata.

## Use

Invoke it explicitly:

```text
$make-reproducible Investigate this flaky integration test. Find the causally relevant uncontrolled input, make the smallest justified change, and prove the scenario is reproducible.
```

Agents that support automatic skill discovery may also select it for flaky tests, intermittent failures, timing or ordering dependencies, races, randomness, and variable external inputs.

## Repository structure

```text
make-reproducible/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── proving-reproducibility.md
    └── sources-and-treatments.md
```

## Design principle

> Define what must hold, control one causally relevant source of variability, prove the improvement, record what remains, and stop.
