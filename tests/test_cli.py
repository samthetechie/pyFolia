import json

from pyfolia.cli import main


def test_cli_plan_json(capsys) -> None:  # type: ignore[no-untyped-def]
    exit_code = main(
        [
            "plan",
            "--bed-width-cm",
            "120",
            "--bed-length-cm",
            "240",
            "--zone",
            "8a",
            "--plants",
            "carrot,tomato,basil,lettuce",
        ]
    )

    captured = capsys.readouterr()
    parsed = json.loads(captured.out)

    assert exit_code == 0
    assert parsed["selected_plants"] == ["carrot", "tomato", "basil", "lettuce"]


def test_cli_plan_svg(capsys) -> None:  # type: ignore[no-untyped-def]
    exit_code = main(
        [
            "plan",
            "--bed-width-cm",
            "40",
            "--bed-length-cm",
            "40",
            "--zone",
            "8a",
            "--plants",
            "carrot",
            "--output",
            "svg",
        ]
    )

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.startswith("<svg")
