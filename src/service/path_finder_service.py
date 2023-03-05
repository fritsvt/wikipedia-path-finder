from __future__ import annotations

from collections.abc import Collection
from dataclasses import dataclass
from functools import reduce, partial

from domain_model.wikipedia import WikipediaPageLink
from service.wikipedia_service import is_valid_page, get_related_titles


@dataclass(frozen=False)
class ScanningQueue:
    paths: dict[str, list[str]]
    to_scan: list[WikipediaPageLink]
    scanned: list[WikipediaPageLink]

    def append(
        self, link: WikipediaPageLink, to_scan: WikipediaPageLink
    ) -> ScanningQueue:
        if link not in self.scanned and link != to_scan:
            self.to_scan.append(link)

            if link.slug not in self.paths:
                self.paths[link.slug] = self.paths[to_scan.slug] + [link.slug]

        return self


def get_tree_for_titles(queue: ScanningQueue, end_title: str) -> ScanningQueue:
    if not queue.to_scan:
        raise ValueError("We outta things to scan")

    to_scan = queue.to_scan.pop(0)

    titles = get_related_titles(to_scan.slug)

    queue.scanned.append(to_scan)

    append_with_to_scan = partial(ScanningQueue.append, to_scan=to_scan)

    return reduce(append_with_to_scan, iter(titles), queue)


def find_shortest_path(start_title: str, end_title: str) -> Collection[str] | None:
    assert is_valid_page(start_title) and is_valid_page(end_title)

    queue = ScanningQueue(
        to_scan=[WikipediaPageLink(slug=start_title, title=start_title)],
        scanned=[],
        paths={start_title: [start_title]},
    )
    while len(queue.to_scan) > 0:
        get_tree_for_titles(
            queue,
            end_title,
        )

        if end_title in queue.paths:
            return queue.paths[end_title]

    return None
