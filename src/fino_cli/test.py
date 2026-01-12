import typer
from fino_cli.util.theme import create_console
from rich.text import Text

app = typer.Typer()


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
