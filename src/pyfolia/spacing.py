"""Plant spacing validation."""

from __future__ import annotations

from math import hypot

from pyfolia.models import Cell, HexPoint, PlantProfile


def distance_cm(a: HexPoint, b: HexPoint) -> float:
    """Return Euclidean distance between two planting points."""

    dx = a.x_cm - b.x_cm
    dy = a.y_cm - b.y_cm
    return hypot(dx, dy)


def required_spacing_cm(a: PlantProfile, b: PlantProfile) -> float:
    """Return minimum allowed centre-to-centre spacing for a pair."""

    return max(a.spacing_cm, b.spacing_cm)


def can_place(
    cell_point: HexPoint,
    plant: PlantProfile,
    placed: tuple[Cell, ...],
) -> bool:
    """Return whether ``plant`` can be placed without violating spacing."""

    for cell in placed:
        if distance_cm(cell_point, cell.point) < required_spacing_cm(plant, cell.plant):
            return False
    return True


def validate_spacing(cells: tuple[Cell, ...]) -> list[str]:
    """Return human-readable spacing violations."""

    violations: list[str] = []
    for index, left in enumerate(cells):
        for right in cells[index + 1 :]:
            actual = distance_cm(left.point, right.point)
            required = required_spacing_cm(left.plant, right.plant)
            if actual < required:
                violations.append(
                    f"{left.plant.name} at ({left.point.q},{left.point.r}) and "
                    f"{right.plant.name} at ({right.point.q},{right.point.r}) "
                    f"are {actual:.1f} cm apart; require {required:.1f} cm"
                )
    return violations
