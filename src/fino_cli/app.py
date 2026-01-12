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
        Panel.fit(
            fino_logo,
            border_style="panel.border",
            title="welcome",
            subtitle="Financial Data Management CLI Tool",
        )
    )

    raise typer.Exit()


# @app.callback(invoke_without_command=True)
# # def callback(ctx: typer.Context) -> None:
# #     # コマンドが指定されている場合はパネルを表示しない
# #     if ctx.invoked_subcommand is not None:
# #         return

# #     # コマンドなしで実行された場合のみオンボーディングパネルを表示
# #     console.print(
# #         Panel.fit(
# #             f"""[bold {FinoColors.ORANGE3}]Fino CLI[/bold {FinoColors.ORANGE3}]
# #             - Financial data management CLI tool -
# #             [bold {FinoColors.LIGHT_SALMON3}]Fino[/bold {FinoColors.LIGHT_SALMON3}] is a powerful financial data platform for supporting your investment decisions.

# #             [bold {FinoColors.DEEP_PINK3}]Features:[/bold {FinoColors.DEEP_PINK3}]
# #             - raw data ingestion workflow.
# #             - data-lakehouse management.

# #             [{FinoColors.GOLD3}]***[/{FinoColors.GOLD3}] please check --help option what you can do with fino cli [{FinoColors.GOLD3}]***[/{FinoColors.GOLD3}]
# #             """,
# #             title="🚀 Welcome Fino CLI",
# #             border_style=FinoColors.GOLD3,
# #         )
# #     )


if __name__ == "__main__":
    app()
