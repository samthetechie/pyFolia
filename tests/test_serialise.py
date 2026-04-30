import json

from pyfolia.models import Bed
from pyfolia.planner import plan_bed
from pyfolia.serialise import plan_to_json


def test_plan_to_json_is_parseable() -> None:
    plan = plan_bed(Bed(width_cm=40, length_cm=40), "8a", ["carrot", "lettuce"])

    parsed = json.loads(plan_to_json(plan))

    assert parsed["bed"] == {"length_cm": 40, "width_cm": 40}
    assert parsed["zone"] == "8a"
    assert parsed["cells"][0]["plant"] in {"carrot", "lettuce"}
