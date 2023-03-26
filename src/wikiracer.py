from datetime import datetime

import typer
from rich.console import Console
from rich.text import Text

from service.path_finder_service import find_shortest_path


console = Console()


def main(first_title: str, second_title: str) -> None:
    start = datetime.now()

    with console.status(
        f"[bold green] Finding a link between {first_title} and {second_title}..."
    ):
        result = find_shortest_path(first_title, second_title)

    for index, path in enumerate(result):
        text = Text()

        if index == 0:
            text.append("🛫 START: ", style="bold green")
        elif index == len(result) - 1:
            text.append("🛬️  END: ", style="bold green")
        else:
            text.append("➡️ CLICK: ", style="bold magenta")

        text.append(f"{path.title} ({path})")
        console.print(text)

    console.print(
        f"Path found! Took: {(datetime.now() - start).total_seconds()} seconds"
    )


if __name__ == "__main__":
    typer.run(main)
