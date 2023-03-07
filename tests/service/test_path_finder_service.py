import pytest

from domain_model.wikipedia_page_link import WikipediaPageLink
from service.path_finder_service import find_shortest_path


def test_find_shortest_path() -> None:
    result = find_shortest_path("Apple", "IPhone")

    assert result == [
        WikipediaPageLink(slug="Apple", title="Apple"),
        WikipediaPageLink(slug="Apple_Inc.", title="Apple Inc."),
        WikipediaPageLink(slug="IPhone", title="IPhone"),
    ]


def test_find_shortest_path_same_start_and_end() -> None:
    result = find_shortest_path("Apple", "Apple")

    assert result == [
        WikipediaPageLink(slug="Apple", title="Apple"),
    ]


def test_find_shortest_path_invalid_start() -> None:
    with pytest.raises(ValueError):
        find_shortest_path("XXXXXXX", "IPhone")


def test_find_shortest_path_invalid_end() -> None:
    with pytest.raises(ValueError):
        find_shortest_path("Apple", "XXXXXXX")
