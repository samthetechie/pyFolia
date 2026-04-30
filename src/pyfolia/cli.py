"""Command line interface for pyFolia."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from pyfolia.models import Bed
from pyfolia.planner import plan_bed
from pyfolia.serialise import plan_to_json
from pyfolia.svg import plan_to_svg


def main(argv: Sequence[str] | None = None) -> int:
    """Run the pyFolia CLI."""

    parser = _build_parser()
    args = parser.parse_args(argv)
    if args.command == "plan":
        plant_names = [name.strip() for name in args.plants.split(",") if name.strip()]
        plan = plan_bed(
            Bed(width_cm=args.bed_width_cm, length_cm=args.bed_length_cm),
            args.zone,
            plant_names,
        )
        output = plan_to_svg(plan) if args.output == "svg" else plan_to_json(plan)
        sys.stdout.write(output)
        return 0
    parser.print_help(sys.stderr)
    return 2


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pyfolia")
    subparsers = parser.add_subparsers(dest="command")

    plan = subparsers.add_parser("plan", help="create a deterministic bed plan")
    plan.add_argument("--bed-width-cm", type=float, required=True)
    plan.add_argument("--bed-length-cm", type=float, required=True)
    plan.add_argument("--zone", required=True)
    plan.add_argument("--plants", required=True)
    plan.add_argument("--output", choices=("json", "svg"), default="json")
    return parser


if __name__ == "__main__":
    raise SystemExit(main())
