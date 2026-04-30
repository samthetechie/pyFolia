"""Plant catalogue loading from local fixture data."""

from __future__ import annotations

import json
from importlib import resources
from typing import Any

from pyfolia.models import PlantProfile


def load_default_catalogue() -> dict[str, PlantProfile]:
    """Load the bundled deterministic plant fixture catalogue."""

    data_path = resources.files("pyfolia.data").joinpath("plants.json")
    raw = json.loads(data_path.read_text(encoding="utf-8"))
    return _parse_catalogue(raw)


def _parse_catalogue(raw: Any) -> dict[str, PlantProfile]:
    if not isinstance(raw, list):
        msg = "Plant catalogue must be a list of plant objects"
        raise ValueError(msg)

    profiles: dict[str, PlantProfile] = {}
    for item in raw:
        if not isinstance(item, dict):
            msg = "Plant catalogue entries must be objects"
            raise ValueError(msg)
        profile = PlantProfile(
            name=_required_str(item, "name").lower(),
            family=_required_str(item, "family"),
            spacing_cm=float(item["spacing_cm"]),
            height_cm=float(item["height_cm"]),
            zones=tuple(_required_str_list(item, "zones")),
            likes=tuple(value.lower() for value in item.get("likes", [])),
            dislikes=tuple(value.lower() for value in item.get("dislikes", [])),
            traits=tuple(item.get("traits", [])),
        )
        profiles[profile.name] = profile
    return profiles


def _required_str(item: dict[str, Any], key: str) -> str:
    value = item.get(key)
    if not isinstance(value, str) or not value:
        msg = f"Plant catalogue field {key!r} must be a non-empty string"
        raise ValueError(msg)
    return value


def _required_str_list(item: dict[str, Any], key: str) -> list[str]:
    value = item.get(key)
    if not isinstance(value, list) or not all(isinstance(v, str) for v in value):
        msg = f"Plant catalogue field {key!r} must be a list of strings"
        raise ValueError(msg)
    return value
