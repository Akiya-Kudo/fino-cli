import rich
import typer
from fino_cli.util.theme import FinoColors

app = typer.Typer()


@app.command()
def test_color() -> None:
    rich.print(
        f"[{FinoColors.LIGHT_SALMON3}]Hello, World![/{FinoColors.LIGHT_SALMON3}]"
    )
    rich.print(f"[{FinoColors.DEEP_PINK3}]Hello, World![/{FinoColors.DEEP_PINK3}]")
    rich.print(f"[{FinoColors.ORANGE3}]Hello, World![/{FinoColors.ORANGE3}]")
    rich.print(f"[{FinoColors.ORANGE3}]Hello, World![/{FinoColors.ORANGE3}]")
    rich.print(f"[{FinoColors.MAGENTA3}]Hello, World![/{FinoColors.MAGENTA3}]")
    rich.print(f"[{FinoColors.GOLD3}]Hello, World![/{FinoColors.GOLD3}]")
    rich.print(f"[{FinoColors.YELLOW3}]Hello, World![/{FinoColors.YELLOW3}]")
    rich.print(f"[{FinoColors.MISTY_ROSE3}]Hello, World![/{FinoColors.MISTY_ROSE3}]")
    rich.print(
        f"[{FinoColors.LIGHT_STEEL_BLUE1}]Hello, World![/{FinoColors.LIGHT_STEEL_BLUE1}]"
    )
    rich.print(f"[{FinoColors.LIGHT_CYAN1}]Hello, World![/{FinoColors.LIGHT_CYAN1}]")
    rich.print(f"[{FinoColors.ERROR}]Hello, World![/{FinoColors.ERROR}]")
    rich.print(f"[{FinoColors.SUCCESS}]Hello, World![/{FinoColors.SUCCESS}]")
    rich.print(f"[{FinoColors.INFO}]Hello, World![/{FinoColors.INFO}]")
    rich.print(f"[{FinoColors.WARNING}]Hello, World![/{FinoColors.WARNING}]")
