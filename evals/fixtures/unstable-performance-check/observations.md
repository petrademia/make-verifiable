# Benchmark observations

The acceptance threshold is `p95_ms <= 120` for a representative workload.

Recent runs of `python3 benchmark.py` produced both passing and failing results. The printed seeds and request counts included:

```text
seed=35 heavy_requests=1 p95_ms=80
seed=32 heavy_requests=5 p95_ms=180
seed=33 heavy_requests=2 p95_ms=180
```

No evidence points to clock drift, warmup, machine load, or service concurrency. The benchmark uses modeled durations and randomly selects the workload mix.
