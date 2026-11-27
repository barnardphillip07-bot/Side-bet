"""Single-role worker process for the WLC-001 topology experiment."""
from __future__ import annotations

import argparse
import json
import sys

from benchmarks.dingoos.wlc_001 import (
    WLC001Inputs,
    analytical_damped_frequency_hz,
    beta_independent_characteristic_root_frequency_hz,
    source_faithful_explicit_euler,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--role", choices=("alpha_a", "alpha_b", "beta"), required=True)
    args = parser.parse_args()
    payload = json.load(sys.stdin)
    inputs = WLC001Inputs(**payload)
    if args.role == "alpha_a":
        result = {"frequency_hz": analytical_damped_frequency_hz(inputs)}
    elif args.role == "alpha_b":
        result = source_faithful_explicit_euler(inputs)
    else:
        result = {"frequency_hz": beta_independent_characteristic_root_frequency_hz(inputs)}
    json.dump(result, sys.stdout, sort_keys=True, separators=(",", ":"))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
