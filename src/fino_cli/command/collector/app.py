import rich
import typer
from fino_cli.config import settings
from fino_cli.parameter.disclosure_source import (
    DisclosureSourceParam,
    DisclosureSourceParamEnum,
    validate_disclosure_source,
)
from fino_cli.parameter.storage import (
    StorageParam,
    StorageParamEnum,
    validate_storage,
)
from fino_cli.util.theme import FinoColors
from fino_core import (
    DocumentCollector,
    EdinetConfig,
    LocalStorageConfig,
    S3StorageConfig,
)

app = typer.Typer(no_args_is_help=True)


@app.command()
def collector(
    ctx: typer.Context,
    # Disclosure source options
    disclosure_source: DisclosureSourceParam.AnnotatedDisclosureSource = DisclosureSourceParamEnum.EDINET,
    edinet_api_key: DisclosureSourceParam.AnnotatedEdinetApiKey = settings.get(
        "EDINET__API_KEY", default=""
    ),
    # Storage options
    storage: StorageParam.AnnotatedStorage = StorageParamEnum.LOCAL,
    # Local storage options
    local_path: StorageParam.AnnotatedLocalPath = settings.get(
        "STORAGE__LOCAL__PATH", default="./fino-data"
    ),
    # S3 storage options
    s3_bucket: StorageParam.AnnotatedS3Bucket = settings.get("STORAGE__S3__BUCKET", default=""),
    s3_prefix: StorageParam.AnnotatedS3Prefix = settings.get("STORAGE__S3__PREFIX", default=""),
    s3_region: StorageParam.AnnotatedS3Region = settings.get(
        "STORAGE__S3__REGION", default="ap-northeast-1"
    ),
) -> None:
    """
    Collect data from the target disclosure source (EDINET).
    """
    # validation
    validate_disclosure_source(ctx, disclosure_source, edinet_api_key)
    validate_storage(ctx, storage, local_path, s3_bucket, s3_prefix, s3_region)

    # Create storage config based on storage type
    storage_config: LocalStorageConfig | S3StorageConfig
    if storage == StorageParamEnum.LOCAL:
        storage_config = LocalStorageConfig(path=local_path)
        rich.print(f"[{FinoColors.GREEN3}]Storage: Local ({local_path})[/{FinoColors.GREEN3}]")
    elif storage == StorageParamEnum.S3:
        storage_config = S3StorageConfig(
            bucket_name=s3_bucket,
            prefix=s3_prefix if s3_prefix else None,
            region=s3_region,
        )
        prefix_display = f" (prefix: {s3_prefix})" if s3_prefix else ""
        rich.print(
            f"[{FinoColors.GREEN3}]Storage: S3 (bucket: {s3_bucket}, region: {s3_region}{prefix_display})[/{FinoColors.GREEN3}]"
        )

    # Create fino core collector
    edinet_config = EdinetConfig(api_key=edinet_api_key)
    collector = DocumentCollector(edinet_config=edinet_config, storage_config=storage_config)

    collector.

    rich.print(
        f"[{FinoColors.BLUE3}]✓ DocumentCollector initialized successfully[/{FinoColors.BLUE3}]"
    )


if __name__ == "__main__":
    app()
