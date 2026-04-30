"""Core domain models."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class PlantProfile:
    """Traits and relationships used by the layout engine."""

    name: str
    family: str
    spacing_cm: float
    height_cm: float
    zones: tuple[str, ...]
    likes: tuple[str, ...] = ()
    dislikes: tuple[str, ...] = ()
    traits: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class Bed:
    """A rectangular bed, measured in centimetres."""

    width_cm: float
    length_cm: float


@dataclass(frozen=True, slots=True)
class HexPoint:
    """A hex-grid planting position in axial coordinates."""

    q: int
    r: int
    x_cm: float
    y_cm: float


@dataclass(frozen=True, slots=True)
class Cell:
    """A planned plant placement."""

    point: HexPoint
    plant: PlantProfile


@dataclass(frozen=True, slots=True)
class RejectedPlant:
    """A requested plant that could not be used."""

    name: str
    reason: str


@dataclass(frozen=True, slots=True)
class GardenPlan:
    """Complete deterministic planning result."""

    bed: Bed
    zone: str
    grid_spacing_cm: float
    cells: tuple[Cell, ...]
    requested_plants: tuple[str, ...]
    selected_plants: tuple[str, ...]
    rejected_plants: tuple[RejectedPlant, ...] = field(default_factory=tuple)
