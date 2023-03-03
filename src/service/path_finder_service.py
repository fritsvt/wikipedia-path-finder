from service.wikipedia_service import is_valid_page


def find_shortest_path(start_title: str, end_title: str) -> None:
    assert is_valid_page(start_title) and is_valid_page(end_title)

    print('We are GO')
