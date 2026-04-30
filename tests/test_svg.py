from pyfolia.models import Bed
from pyfolia.planner import plan_bed
from pyfolia.svg import plan_to_svg


def test_plan_to_svg_contains_printable_svg() -> None:
    plan = plan_bed(Bed(width_cm=40, length_cm=40), "8a", ["carrot"])

    svg = plan_to_svg(plan)

    assert svg.startswith("<svg")
    assert "<circle" in svg
    assert "pyFolia plan" in svg
