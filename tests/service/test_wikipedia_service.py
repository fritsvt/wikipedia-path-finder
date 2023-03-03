import pytest

from service.wikipedia_service import get_related_titles


def test_get_related_titles() -> None:
    related = get_related_titles("Apple")

    assert len(related) == 794


def test_get_related_titles_invalid_title() -> None:
    with pytest.raises(ValueError):
        get_related_titles("XXXXXXX")
