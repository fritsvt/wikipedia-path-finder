from service.path_finder_service import find_shortest_path


def test_find_shortest_path() -> None:
    result = find_shortest_path("Pear", "IPhone")
    print(result)
