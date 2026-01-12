import typer
from fino_cli.util.theme import create_console

app = typer.Typer()


@app.command()
def test_color() -> None:
    console = create_console()
    console.print("[{'brand.primary'}]Hello, World![/{'brand.primary'}]")
    console.print("[{'brand.secondary'}]Hello, World![/{'brand.secondary'}]")
    console.print("[{'brand.tertiary'}]Hello, World![/{'brand.tertiary'}]")
    console.print("[{'brand.quaternary'}]Hello, World![/{'brand.quaternary'}]")
