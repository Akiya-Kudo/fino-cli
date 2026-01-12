from enum import Enum
from typing import Annotated

import rich
import typer
from click.core import ParameterSource


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
    disclosure_source: DisclosureSourceParamEnum,
    edinet_api_key: str,
) -> None:
    if ctx.get_parameter_source("disclosure_source") == ParameterSource.DEFAULT:
        rich.print(
            f"[{'brand.secondary'}]Since no disclosure source option specified, collect documents from the default Edinet[/{'brand.secondary'}]"
        )
    if (
        edinet_api_key == DisclosureSourceParamEnum.EDINET
        or ctx.get_parameter_source("edinet_api_key") == ParameterSource.DEFAULT
    ):
        raise typer.BadParameter(
            "EDINET API key is required when disclosure source is EDINET"
        )
