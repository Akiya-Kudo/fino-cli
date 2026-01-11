from typing import Annotated

import typer
from fino_core import FormatTypeEnum


class FormatTypeParam:
    AnnotatedFormatType = Annotated[
        FormatTypeEnum,
        typer.Option(
            help="Format type to collect documents from",
        ),
    ]
