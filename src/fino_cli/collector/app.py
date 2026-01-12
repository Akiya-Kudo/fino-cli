import typer
from fino_cli.collector import collect

app = typer.Typer(no_args_is_help=True)

app.add_typer(
    collect.app,
    help="collect financial disclosure documents by compatible with disclosure source",
)


@app.callback(invoke_without_command=True)
def collector() -> None:
    """
    Collector of financial disclosure documents."""
    pass


if __name__ == "__main__":
    app()
