from dataclasses import dataclass


@dataclass(frozen=True)
class WikipediaPageLink:
    href: str
    title: str
