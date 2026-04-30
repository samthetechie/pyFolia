from pyfolia.models import Bed
from pyfolia.planner import plan_bed
from pyfolia.spacing import validate_spacing


def test_plan_filters_unknown_and_unsuitable_plants() -> None:
    plan = plan_bed(
        Bed(width_cm=120, length_cm=240),
        "11a",
        ["carrot", "tomato", "unknown"],
    )

    assert plan.selected_plants == ("tomato",)
    assert {rejected.name for rejected in plan.rejected_plants} == {
        "carrot",
        "unknown",
    }


def test_plan_is_deterministic_and_spacing_valid() -> None:
    args = (
        Bed(width_cm=120, length_cm=240),
        "8a",
        ["carrot", "tomato", "basil", "lettuce"],
    )

    first = plan_bed(*args)
    second = plan_bed(*args)

    assert first == second
    assert first.cells
    assert first.selected_plants == ("carrot", "tomato", "basil", "lettuce")
    assert validate_spacing(first.cells) == []


def test_duplicate_requested_plants_are_planned_once() -> None:
    plan = plan_bed(Bed(width_cm=60, length_cm=60), "8a", ["carrot", "carrot"])

    assert plan.requested_plants == ("carrot", "carrot")
    assert plan.selected_plants == ("carrot",)
