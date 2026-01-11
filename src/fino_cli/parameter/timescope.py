from typing import Annotated

import typer

type YearParam = Annotated[int, typer.Option(help="Year")]
type MonthParam = Annotated[int | None, typer.Option(help="Month")]
type DayParam = Annotated[int | None, typer.Option(help="Day")]


def validate_timescope(
    month: int | None,
    day: int | None,
) -> None:
    if month is None and day is not None:
        raise typer.BadParameter("Month is required when day is specified")
