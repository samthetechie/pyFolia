from pyfolia.hexgrid import generate_hex_grid
from pyfolia.models import Bed


def test_generate_hex_grid_keeps_points_inside_bed() -> None:
    points = generate_hex_grid(Bed(width_cm=30, length_cm=30), spacing_cm=10)

    assert points
    assert all(5 <= point.x_cm <= 25 for point in points)
    assert all(5 <= point.y_cm <= 25 for point in points)
    assert len({(point.q, point.r) for point in points}) == len(points)
