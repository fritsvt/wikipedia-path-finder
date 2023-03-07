from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class WikipediaPageLink:
    slug: str
    title: str

    def __str__(self) -> str:
        return f"https://en.wikipedia.org/wiki/{self.slug}"
