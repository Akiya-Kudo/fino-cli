from enum import Enum
from typing import Annotated

import rich
import typer
from click.core import ParameterSource
from fino_cli.util.theme import FinoColors
from fino_core import DisclosureSource


# enum
class DisclosureSourceParamEnum(str, Enum):
    EDINET = "edinet"


# param
class DisclosureSourceParam:
    AnnotatedDisclosureSource = Annotated[
        DisclosureSource,
        typer.Option(...),
    ]

    AnnotatedEdinetApiKey = Annotated[str, typer.Option(...)]


# validation
def validate_disclosure_source(
    ctx: typer.Context, disclosure_source: DisclosureSourceParamEnum, edinet_api_key: str
) -> None:
    if ctx.get_parameter_source("disclosure_source") == ParameterSource.DEFAULT:
        rich.print(
            f"[{FinoColors.ORANGE3}]Since no disclosure source option specified, collect documents from the default Edinet[/{FinoColors.ORANGE3}]"
        )
    if (
        edinet_api_key == DisclosureSourceParamEnum.EDINET
        or ctx.get_parameter_source("edinet_api_key") == ParameterSource.DEFAULT
    ):
        raise typer.BadParameter("EDINET API key is required when disclosure source is EDINET")
