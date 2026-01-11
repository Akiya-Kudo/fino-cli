import rich
import typer
from fino_cli.parameter.disclosure_source import (
    DisclosureSourceParam,
    EdinetApiKeyParam,
    validate_disclosure_source,
)
from fino_cli.parameter.format_type import FormatTypeParam
from fino_cli.parameter.storage import (
    StorageParam,
    StorageParamEnum,
    validate_storage,
)
from fino_cli.parameter.timescope import (
    DayParam,
    MonthParam,
    YearParam,
    validate_timescope,
)
from fino_cli.util.theme import FinoColors
from fino_core import (
    DocumentCollector,
    EdinetConfig,
    FormatTypeEnum,
    LocalStorageConfig,
    S3StorageConfig,
    TimeScope,
)

app = typer.Typer(no_args_is_help=True)


@app.command()
def collect(
    ctx: typer.Context,
    # Disclosure source options
    disclosure_source: DisclosureSourceParam,
    edinet_api_key: EdinetApiKeyParam,
    # Storage options
    storage: StorageParam.AnnotatedStorage,
    # Local storage options
    local_path: StorageParam.AnnotatedLocalPath,
    # S3 storage options
    s3_bucket: StorageParam.AnnotatedS3Bucket,
    s3_prefix: StorageParam.AnnotatedS3Prefix,
    s3_region: StorageParam.AnnotatedS3Region,
    # Time scope options
    year: YearParam,
    month: MonthParam,
    day: DayParam,
    # Format type options
    format_type: FormatTypeParam.AnnotatedFormatType = FormatTypeEnum.XBRL,
) -> None:
    """
    Collect data from the target disclosure source (EDINET).
    """
    # validation
    validate_disclosure_source(ctx, disclosure_source, edinet_api_key)
    validate_storage(ctx, storage, local_path, s3_bucket, s3_prefix, s3_region)
    validate_timescope(month, day)

    # Create storage based on storage type
    storage_config: LocalStorageConfig | S3StorageConfig
    if storage == StorageParamEnum.LOCAL:
        storage_config = LocalStorageConfig(base_dir=local_path)
        rich.print(
            f"[{FinoColors.MAGENTA3}]Storage: Local ({local_path})[/{FinoColors.MAGENTA3}]"
        )
    elif storage == StorageParamEnum.S3:
        storage_config = S3StorageConfig(
            bucket_name=s3_bucket,
            prefix=s3_prefix if s3_prefix else None,
            region=s3_region,
        )
        prefix_display = f" (prefix: {s3_prefix})" if s3_prefix else ""
        rich.print(
            f"[{FinoColors.MAGENTA3}]Storage: S3 (bucket: {s3_bucket}, region: {s3_region}{prefix_display})[/{FinoColors.MAGENTA3}]"
        )

    # Create fino core disclosure source
    edinet_config = EdinetConfig(api_key=edinet_api_key)

    # Create fino core collector
    collector = DocumentCollector(
        disclosure_config=edinet_config, storage_config=storage_config
    )

    # Create time scope
    timescope = TimeScope(year=year, month=month, day=day)

    collector.collect_document(timescope=timescope, format_type=FormatTypeEnum.XBRL)

    rich.print(
        f"[{FinoColors.BLUE3}]✓ DocumentCollector initialized successfully[/{FinoColors.BLUE3}]"
    )


if __name__ == "__main__":
    app()
