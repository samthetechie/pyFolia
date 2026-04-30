from pyfolia.catalogue import load_default_catalogue


def test_default_catalogue_contains_relationships() -> None:
    catalogue = load_default_catalogue()

    assert catalogue["tomato"].spacing_cm == 60
    assert "basil" in catalogue["tomato"].likes
    assert "tomato" in catalogue["potato"].dislikes
