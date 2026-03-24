#!/usr/bin/env python3
"""OMEGA AI – entry point.

Run with:
    python main.py
    python main.py --cycles 5
"""

from __future__ import annotations

import argparse
import sys

from omega_ai import OmegaAI


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="OMEGA AI – evolve 5 social-media platform personas towards infinity.",
    )
    parser.add_argument(
        "--cycles",
        type=int,
        default=3,
        help="Number of evolution cycles to run per persona (default: 3).",
    )
    parser.add_argument(
        "--platform",
        choices=["Facebook", "Instagram", "TikTok", "Threads", "YouTube"],
        default=None,
        help="Show detailed report for a single platform only.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)

    print("=" * 60)
    print("  OMEGA AI – Social-Media Evolution System")
    print("=" * 60)
    print(f"\nRunning {args.cycles} evolution cycle(s) for all 5 platforms…\n")

    omega = OmegaAI()
    omega.evolve(cycles=args.cycles)

    if args.platform:
        import json

        persona = omega.platform(args.platform)
        print(json.dumps(persona.status(), indent=2, ensure_ascii=False))
    else:
        print(omega.report())

    print("\nEvolution complete. Platforms are advancing towards infinity ∞\n")


if __name__ == "__main__":
    main(sys.argv[1:])
