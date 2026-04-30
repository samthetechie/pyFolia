"""Printable SVG output for garden plans."""

from __future__ import annotations

from html import escape

from pyfolia.models import GardenPlan

PALETTE = {
    "basil": "#6a994e",
    "bean": "#2a9d8f",
    "carrot": "#f28c28",
    "lettuce": "#90be6d",
    "onion": "#b8a77a",
    "pepper": "#d62828",
    "potato": "#9c6644",
    "radish": "#e63946",
    "tomato": "#c1121f",
}


def plan_to_svg(plan: GardenPlan) -> str:
    """Render a printable SVG plan."""

    margin = 24
    scale = 3
    width = plan.bed.width_cm * scale + margin * 2
    height = plan.bed.length_cm * scale + margin * 2 + 40
    lines = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" '
            f'height="{height:.0f}" viewBox="0 0 {width:.0f} {height:.0f}">'
        ),
        "<style>",
        "text { font-family: sans-serif; font-size: 10px; fill: #1f2933; }",
        ".label { font-size: 14px; font-weight: 700; }",
        "</style>",
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        (
            f'<rect x="{margin}" y="{margin + 24}" '
            f'width="{plan.bed.width_cm * scale:.0f}" '
            f'height="{plan.bed.length_cm * scale:.0f}" fill="#f7f3e8" '
            'stroke="#3d405b" stroke-width="1.5"/>'
        ),
        (
            f'<text class="label" x="{margin}" y="{margin}">'
            f'pyFolia plan: zone {escape(plan.zone)}, '
            f'{plan.bed.width_cm:g} x {plan.bed.length_cm:g} cm</text>'
        ),
    ]

    for cell in plan.cells:
        x = margin + cell.point.x_cm * scale
        y = margin + 24 + cell.point.y_cm * scale
        radius = max(5.0, min(cell.plant.spacing_cm * scale / 2, 22.0))
        colour = PALETTE.get(cell.plant.name, "#577590")
        label = escape(cell.plant.name[:3])
        lines.extend(
            [
                (
                    f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius:.1f}" '
                    f'fill="{colour}" fill-opacity="0.82" stroke="#1f2933" '
                    'stroke-width="0.6"/>'
                ),
                (
                    f'<text x="{x:.1f}" y="{y + 3:.1f}" text-anchor="middle">'
                    f"{label}</text>"
                ),
            ]
        )

    lines.append("</svg>")
    return "\n".join(lines) + "\n"
