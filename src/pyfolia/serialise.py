"""JSON serialisation for plans."""

from __future__ import annotations

import json
from typing import Any

from pyfolia.models import GardenPlan


def plan_to_dict(plan: GardenPlan) -> dict[str, Any]:
    """Convert a plan to a stable JSON-compatible dictionary."""

    return {
        "bed": {
            "width_cm": plan.bed.width_cm,
            "length_cm": plan.bed.length_cm,
        },
        "zone": plan.zone,
        "grid_spacing_cm": plan.grid_spacing_cm,
        "requested_plants": list(plan.requested_plants),
        "selected_plants": list(plan.selected_plants),
        "rejected_plants": [
            {"name": rejected.name, "reason": rejected.reason}
            for rejected in plan.rejected_plants
        ],
        "cells": [
            {
                "q": cell.point.q,
                "r": cell.point.r,
                "x_cm": cell.point.x_cm,
                "y_cm": cell.point.y_cm,
                "plant": cell.plant.name,
                "spacing_cm": cell.plant.spacing_cm,
            }
            for cell in plan.cells
        ],
    }


def plan_to_json(plan: GardenPlan) -> str:
    """Render a plan as pretty, deterministic JSON."""

    return json.dumps(plan_to_dict(plan), indent=2, sort_keys=True) + "\n"
