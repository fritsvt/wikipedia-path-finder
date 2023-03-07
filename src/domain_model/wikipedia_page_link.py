from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class WikipediaPageLink:
    slug: str
    title: str
