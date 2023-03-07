from service.path_finder_service import find_shortest_path

if __name__ == "__main__":
    first_title = "Apple"
    second_title = "iPhone"

    result = find_shortest_path(first_title, second_title)
    print(result)
