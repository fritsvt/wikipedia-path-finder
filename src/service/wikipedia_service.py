from collections.abc import Collection

import requests
from bs4 import BeautifulSoup, Tag

from src.domain_model.wikipedia import WikipediaPageLink

_API_BASE_URL = "https://en.wikipedia.org/api/rest_v1"


def _get_page_contents(title: str) -> str:
    response = requests.get(url=f"{_API_BASE_URL}/page/html/{title}")

    if response.status_code != 200:
        raise ValueError(
            f"Unable to get Wikipedia page content for page: {title}\n"
            f"Status code: {response.status_code}"
        )

    return response.text


def _is_valid_wiki_link(link: Tag) -> bool:
    if not link.text:
        return False

    if not link.get("href") or not link.get("title"):
        return False

    if (
        "#" in link["href"]
        or "?" in link["href"]
        or "Special:Book" in link["href"]
        or "PMC_(identifier)" in link["href"]
        or "ISBN_(identifier)" in link["href"]
        or "Help:IPA" in link["href"]
    ):
        return False

    return True


def is_valid_page(title: str) -> bool:
    response = requests.get(url=f"{_API_BASE_URL}/page/title/{title}")

    return response.status_code == 200


def get_related_titles(title: str) -> Collection[WikipediaPageLink]:
    contents = _get_page_contents(title)

    soup = BeautifulSoup(contents, "html.parser")

    return [
        WikipediaPageLink(
            slug=link["href"].replace("./", ""),
            title=link["title"],
        )
        for link in soup.find_all("a", {"rel": "mw:WikiLink"})
        if _is_valid_wiki_link(link)
    ]
