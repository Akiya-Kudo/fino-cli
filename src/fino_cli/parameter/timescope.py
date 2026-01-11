from typing import Annotated

import typer

YearParam = Annotated[int, typer.Option(help="Year")]
MonthParam = Annotated[int | None, typer.Option(help="Month")]
DayParam = Annotated[int | None, typer.Option(help="Day")]


# validation
def validate_timescope(
    month: int | None,
    day: int | None,
) -> None:
    if month is None and day is not None:
        raise typer.BadParameter("Month is required when day is specified")
