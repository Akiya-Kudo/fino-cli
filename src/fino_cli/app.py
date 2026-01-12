import fino_cli.collector.app as collector
import typer
from fino_cli import test
from fino_cli.util.theme import create_console
from rich.panel import Panel
from rich.text import Text

app = typer.Typer(
    name="fino",
    invoke_without_command=True,
    no_args_is_help=False,
    context_settings={
        "help_option_names": ["-h", "--help"]
    },  # Global help option setting
)

app.add_typer(
    collector.app,
    name="collector",
)

app.add_typer(test.app)


ASCII_LOGO = r"""
  /$$$$$$  /$$                                     /$$ /$$
 /$$__  $$|__/                                    | $$|__/
| $$  \__/ /$$ /$$£$$$$   /$$$$$$         /$$$$$$$| $$ /$$
| $$$$    | $$| $$__  $$ /$$__  $$       /$$_____/| $¥| $$
| $$_/    | $$| $$  \ $$| $$  \ $$      | $$      | $$| $$
| $$      | $$| $$  | $$| $$  | $$      | $$      | $$| $$
| $$      | $$| $$  | $$|  $$$€$$/      |  $$$$$$$| $$| $$
|__/      |__/|__/  |__/ \______/        \_______/|__/|__/
"""


@app.callback(invoke_without_command=True)
def root(ctx: typer.Context):
    if ctx.invoked_subcommand is not None:
        return

    console = create_console()

    fino_logo = Text(ASCII_LOGO)

    logo_length = len(fino_logo)

    # グラデーション風に色付け
    fino_logo.stylize("brand.primary", 0, logo_length // 4)
    fino_logo.stylize("brand.secondary", logo_length // 4, logo_length // 2)
    fino_logo.stylize(
        "brand.tertiary",
        logo_length // 2,
        logo_length * 3 // 4,
    )
    fino_logo.stylize("brand.quaternary", logo_length * 3 // 4, logo_length)

    console.print(
        fino_logo,
        Panel.fit(
            f"""[bold {"brand.primary"}]Fino CLI[/bold {"brand.primary"}]
            - Financial data management CLI tool -
            [bold {"brand.secondary"}]Fino[/bold {"brand.secondary"}] is a powerful financial data platform for supporting your investment decisions.

            [bold {"brand.tertiary"}]Features:[/bold {"brand.tertiary"}]
            - raw data ingestion workflow.
            - data-lakehouse management.

            [{"brand.quaternary"}]***[/{"brand.quaternary"}] please check --help option what you can do with fino cli [{"brand.quaternary"}]***[/{"brand.quaternary"}]
            """,
            border_style="panel.border",
            title="welcome",
            subtitle="Financial Data Management CLI Tool",
        ),
    )

    raise typer.Exit()


if __name__ == "__main__":
    app()
