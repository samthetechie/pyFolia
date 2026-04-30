"""Deterministic greedy garden planning."""

from __future__ import annotations

from pyfolia.catalogue import load_default_catalogue
from pyfolia.hexgrid import generate_hex_grid
from pyfolia.models import Bed, Cell, GardenPlan, HexPoint, PlantProfile, RejectedPlant
from pyfolia.spacing import can_place, distance_cm
from pyfolia.zones import normalise_zone, zone_in_range


def plan_bed(
    bed: Bed,
    zone: str,
    plant_names: list[str],
    *,
    catalogue: dict[str, PlantProfile] | None = None,
) -> GardenPlan:
    """Plan a bed using local plant data and a deterministic greedy optimiser."""

    canonical_zone = normalise_zone(zone)
    profiles = catalogue or load_default_catalogue()
    requested = tuple(
        _normalise_plant_name(name) for name in plant_names if name.strip()
    )
    selected, rejected = _select_plants(requested, canonical_zone, profiles)

    if not selected:
        return GardenPlan(
            bed=bed,
            zone=canonical_zone,
            grid_spacing_cm=0,
            cells=(),
            requested_plants=requested,
            selected_plants=(),
            rejected_plants=tuple(rejected),
        )

    grid_spacing = min(profile.spacing_cm for profile in selected)
    points = generate_hex_grid(bed, grid_spacing)
    cells = _greedy_layout(points, selected)

    return GardenPlan(
        bed=bed,
        zone=canonical_zone,
        grid_spacing_cm=grid_spacing,
        cells=tuple(cells),
        requested_plants=requested,
        selected_plants=tuple(profile.name for profile in selected),
        rejected_plants=tuple(rejected),
    )


def _select_plants(
    requested: tuple[str, ...],
    zone: str,
    catalogue: dict[str, PlantProfile],
) -> tuple[list[PlantProfile], list[RejectedPlant]]:
    selected: list[PlantProfile] = []
    rejected: list[RejectedPlant] = []
    seen: set[str] = set()

    for name in requested:
        if name in seen:
            continue
        seen.add(name)
        profile = catalogue.get(name)
        if profile is None:
            rejected.append(RejectedPlant(name=name, reason="unknown plant"))
            continue
        if not zone_in_range(zone, profile.zones):
            rejected.append(
                RejectedPlant(name=name, reason=f"not suitable for zone {zone}")
            )
            continue
        selected.append(profile)

    return selected, rejected


def _greedy_layout(
    points: tuple[HexPoint, ...],
    plants: list[PlantProfile],
) -> list[Cell]:
    placed: list[Cell] = []
    counts = {plant.name: 0 for plant in plants}
    ordered_plants = sorted(plants, key=lambda plant: (-plant.spacing_cm, plant.name))

    for point in points:
        candidate = _best_plant_for_point(point, ordered_plants, tuple(placed), counts)
        if candidate is None:
            continue
        placed.append(Cell(point=point, plant=candidate))
        counts[candidate.name] += 1
    return placed


def _best_plant_for_point(
    point: HexPoint,
    plants: list[PlantProfile],
    placed: tuple[Cell, ...],
    counts: dict[str, int],
) -> PlantProfile | None:
    valid = [plant for plant in plants if can_place(point, plant, placed)]
    if not valid:
        return None
    return max(
        valid,
        key=lambda plant: (
            _relationship_score(point, plant, placed),
            -counts[plant.name],
            plant.spacing_cm,
            plant.name,
        ),
    )


def _relationship_score(
    point: HexPoint,
    plant: PlantProfile,
    placed: tuple[Cell, ...],
) -> int:
    score = 0
    for cell in placed:
        distance = distance_cm(point, cell.point)
        neighbour_radius = max(plant.spacing_cm, cell.plant.spacing_cm) * 1.75
        if distance > neighbour_radius:
            continue
        if cell.plant.name in plant.dislikes or plant.name in cell.plant.dislikes:
            score -= 10
        if cell.plant.name in plant.likes:
            score += 3
        if plant.name in cell.plant.likes:
            score += 2
        if plant.family != cell.plant.family:
            score += 1
    return score


def _normalise_plant_name(name: str) -> str:
    return name.strip().lower().replace("_", " ").replace("-", " ")
