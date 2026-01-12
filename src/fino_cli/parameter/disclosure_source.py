from enum import Enum
from typing import Annotated

import typer
from click.core import ParameterSource
from rich.console import Console


# enum
class DisclosureSourceParamEnum(str, Enum):
    EDINET = "edinet"


# param
DisclosureSourceParam = Annotated[
    DisclosureSourceParamEnum,
    typer.Option(help="Disclosure source to collect documents from"),
]

EdinetApiKeyParam = Annotated[str, typer.Option(help="API key for EDINET")]


# validation
def validate_disclosure_source(
    ctx: typer.Context,
    console: Console,
    disclosure_source: DisclosureSourceParamEnum,
    edinet_api_key: str,
) -> None:
    if ctx.get_parameter_source("disclosure_source") == ParameterSource.DEFAULT:
        console.print(
            f"[info]Using default disclosure source: {disclosure_source.value}[info]"
        )
    if disclosure_source == DisclosureSourceParamEnum.EDINET and not edinet_api_key:
        raise typer.BadParameter(
            "EDINET API key is required when collect documents from EDINET"
        )
