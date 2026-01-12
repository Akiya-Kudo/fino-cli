from enum import Enum
from typing import Annotated

import rich
import typer
from click.core import ParameterSource


# enum
class StorageParamEnum(str, Enum):
    LOCAL = "local"
    S3 = "s3"


# param
StorageParam = Annotated[
    StorageParamEnum,
    typer.Option(help="Storage backend type (local or s3)"),
]
LocalPathParam = Annotated[
    str,
    typer.Option(help="Base directory path for local storage"),
]
S3BucketParam = Annotated[str, typer.Option(help="S3 bucket name for s3 storage")]
S3PrefixParam = Annotated[
    str,
    typer.Option(help="S3 prefix (folder path) for s3 storage"),
]
S3RegionParam = Annotated[str, typer.Option(help="S3 region for s3 storage")]


# validation
def validate_storage(
    ctx: typer.Context,
    storage: StorageParamEnum,
    local_path: str,
    s3_bucket: str,
    s3_prefix: str,
    s3_region: str,
) -> None:
    if ctx.get_parameter_source("storage") == ParameterSource.DEFAULT:
        rich.print(
            f"[{'brand.secondary'}]Using default storage: {storage.value}[/{'brand.secondary'}]"
        )

    if storage == StorageParamEnum.LOCAL:
        if local_path == "":
            raise typer.BadParameter(
                (
                    "local-path is required when storage type is 'local'. "
                    "Set via --local-path, config file, or STORAGE__LOCAL__PATH environment variable."
                )
            )
    elif storage == StorageParamEnum.S3:
        if s3_bucket == "" or s3_region == "":
            raise typer.BadParameter(
                (
                    "s3-bucket and s3-region is required when storage type is 's3'. "
                    "Set via --s3-bucket, config file, or STORAGE__S3__BUCKET environment variable."
                    "Set via --s3-region, config file, or STORAGE__S3__REGION environment variable."
                )
            )
    else:
        raise typer.BadParameter(f"Unknown storage type: {storage}")
