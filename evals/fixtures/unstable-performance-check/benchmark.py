import argparse
import random


def benchmark(seed: int) -> tuple[int, int]:
    rng = random.Random(seed)
    durations = [180 if rng.random() < 0.2 else 80 for _ in range(20)]
    durations.sort()
    p95 = durations[18]
    return p95, sum(duration == 180 for duration in durations)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()

    seed = args.seed if args.seed is not None else random.SystemRandom().randrange(1_000_000)
    p95, heavy_requests = benchmark(seed)
    print(f"seed={seed} heavy_requests={heavy_requests} p95_ms={p95}")
    return 0 if p95 <= 120 else 1


if __name__ == "__main__":
    raise SystemExit(main())
