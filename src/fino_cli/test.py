import time
from typing import Generator

import typer
from fino_cli.util.theme import create_console
from rich.console import Console, Group
from rich.live import Live
from rich.progress import BarColumn, Progress, TextColumn
from rich.table import Table
from rich.text import Text

app = typer.Typer()
console = Console()


@app.command()
def test_color() -> None:
    console = create_console()
    text = Text()
    _ = text.append("Fino CLI\n", style="success")
    _ = text.append("Fino CLI\n", style="warning")
    _ = text.append("Fino CLI\n", style="info")
    _ = text.append("Fino CLI\n", style="error")
    _ = text.append("Hello, World!\n", style="brand.primary")
    _ = text.append("Hello, World!\n", style="brand.secondary")
    _ = text.append("Hello, World!\n", style="brand.tertiary")
    _ = text.append("Hello, World!\n", style="brand.quaternary")
    console.print(text)


def task_stream() -> Generator[str, None, None]:
    for task in ["extract", "transform", "load"]:
        yield task


def build_table(completed: list[str]) -> Table:
    table = Table(title="Completed Tasks")
    table.add_column("Task")
    table.add_column("Status")

    for task in completed:
        table.add_row(task, "✅ Done")

    return table


@app.command()
def test_progress():
    completed: list[str] = []

    progress = Progress(
        TextColumn("[bold cyan]{task.description}"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%"),
    )

    # 初期レイアウト
    layout = Group(
        progress,
        build_table(completed),
    )

    with Live(layout, refresh_per_second=10) as live:
        for task_name in task_stream():
            task_id = progress.add_task(task_name, total=100)

            for _ in range(10):
                time.sleep(0.1)
                progress.update(task_id, advance=10)

            # 完了したらリスト更新
            completed.append(task_name)

            # ★ここが重要：Liveを明示更新
            live.update(
                Group(
                    progress,
                    build_table(completed),
                )
            )
