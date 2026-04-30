"""Hex-grid generation for rectangular beds."""

from __future__ import annotations

from math import sqrt

from pyfolia.models import Bed, HexPoint


def generate_hex_grid(bed: Bed, spacing_cm: float) -> tuple[HexPoint, ...]:
    """Generate staggered hex centres inside a rectangular bed."""

    if bed.width_cm <= 0 or bed.length_cm <= 0:
        msg = "Bed dimensions must be positive"
        raise ValueError(msg)
    if spacing_cm <= 0:
        msg = "Grid spacing must be positive"
        raise ValueError(msg)

    row_step = spacing_cm * sqrt(3) / 2
    points: list[HexPoint] = []
    r = 0
    y = spacing_cm / 2
    while y <= bed.length_cm - spacing_cm / 2:
        offset = spacing_cm / 2 if r % 2 else 0.0
        q = 0
        x = spacing_cm / 2 + offset
        while x <= bed.width_cm - spacing_cm / 2:
            points.append(HexPoint(q=q, r=r, x_cm=round(x, 3), y_cm=round(y, 3)))
            q += 1
            x += spacing_cm
        r += 1
        y += row_step
    return tuple(points)


def neighbour_points(
    point: HexPoint,
    points: tuple[HexPoint, ...],
    max_distance_cm: float,
) -> tuple[HexPoint, ...]:
    """Return nearby points using Euclidean distance in bed space."""

    nearby: list[HexPoint] = []
    for candidate in points:
        if candidate == point:
            continue
        dx = point.x_cm - candidate.x_cm
        dy = point.y_cm - candidate.y_cm
        if (dx * dx + dy * dy) ** 0.5 <= max_distance_cm:
            nearby.append(candidate)
    return tuple(nearby)
