import pytest

from domain_model.wikipedia_page_link import WikipediaPageLink
from service.wikipedia_service import get_related_titles, get_page_link_from_title


def test_get_related_titles() -> None:
    related = get_related_titles("Apple")

    assert len(related) > 0
    assert WikipediaPageLink(title="Apple Inc.", slug="Apple_Inc.") in related


def test_get_related_titles_invalid_title() -> None:
    with pytest.raises(ValueError):
        get_related_titles("XXXXXXX")


def test_get_page_link_from_title() -> None:
    page_link = get_page_link_from_title("Apple Inc.")

    assert page_link == WikipediaPageLink(title="Apple Inc.", slug="Apple_Inc.")


def test_get_page_link_from_invalid_title() -> None:
    with pytest.raises(ValueError):
        get_page_link_from_title("XXXXXXX")
