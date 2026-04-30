"""USDA zone parsing and comparison."""

from __future__ import annotations

import re

ZONE_RE = re.compile(r"^(?P<number>\d{1,2})(?P<half>[ab])?$", re.IGNORECASE)


def normalise_zone(zone: str) -> str:
    """Return a canonical USDA zone label such as ``8a``."""

    match = ZONE_RE.match(zone.strip())
    if match is None:
        msg = f"Invalid USDA zone: {zone!r}"
        raise ValueError(msg)
    number = int(match.group("number"))
    half = (match.group("half") or "").lower()
    return f"{number}{half}"


def zone_sort_key(zone: str) -> float:
    """Convert a USDA zone into a sortable numeric key."""

    canonical = normalise_zone(zone)
    if canonical[-1:] == "a":
        return float(canonical[:-1])
    if canonical[-1:] == "b":
        return float(canonical[:-1]) + 0.5
    return float(canonical)


def zone_in_range(zone: str, supported_zones: tuple[str, ...]) -> bool:
    """Return true when ``zone`` is present in a profile's supported zone list."""

    canonical = normalise_zone(zone)
    return canonical in {normalise_zone(candidate) for candidate in supported_zones}
