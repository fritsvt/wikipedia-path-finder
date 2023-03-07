from __future__ import annotations

from collections.abc import Collection
from dataclasses import dataclass
from functools import reduce, partial

from domain_model.wikipedia_page_link import WikipediaPageLink
from service.wikipedia_service import get_related_titles, get_page_link_from_title


@dataclass(frozen=False)
class ScanningQueue:
    paths: dict[str, list[WikipediaPageLink]]
    to_scan: list[WikipediaPageLink]
    scanned: list[WikipediaPageLink]

    def append(
        self, link: WikipediaPageLink, to_scan: WikipediaPageLink
    ) -> ScanningQueue:
        if link not in self.scanned and link != to_scan:
            self.to_scan.append(link)

            if link.slug not in self.paths:
                self.paths[link.slug] = self.paths[to_scan.slug] + [link]

        return self


def get_tree_for_titles(queue: ScanningQueue) -> ScanningQueue:
    to_scan = queue.to_scan.pop(0)

    titles = get_related_titles(to_scan.slug)

    queue.scanned.append(to_scan)

    append_with_to_scan = partial(ScanningQueue.append, to_scan=to_scan)

    return reduce(append_with_to_scan, iter(titles), queue)


def find_shortest_path(
    start_title: str, end_title: str
) -> Collection[WikipediaPageLink] | None:
    start_page_link = get_page_link_from_title(start_title)
    end_page_link = get_page_link_from_title(end_title)

    queue = ScanningQueue(
        to_scan=[start_page_link],
        scanned=[],
        paths={start_page_link.slug: [start_page_link]},
    )

    while len(queue.to_scan) > 0:
        get_tree_for_titles(queue)

        if end_page_link.slug in queue.paths:
            return queue.paths[end_page_link.slug]

    return None
