import rich
import typer
from fino_cli.config import settings
from fino_cli.parameter.disclosure_source import (
    DisclosureSourceParam,
    DisclosureSourceParamEnum,
    EdinetApiKeyParam,
    validate_disclosure_source,
)
from fino_cli.parameter.format_type import FormatTypeParam
from fino_cli.parameter.storage import (
    LocalPathParam,
    S3BucketParam,
    S3PrefixParam,
    S3RegionParam,
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
from fino_cli.util.theme import create_console
from fino_core import (
    Document,
    DocumentCollector,
    EdinetConfig,
    FormatTypeEnum,
    LocalStorageConfig,
    S3StorageConfig,
    TimeScope,
)

app = typer.Typer()


@app.command()
def collect(
    ctx: typer.Context,
    # Time scope options
    year: YearParam,
    # Disclosure source options
    disclosure_source: DisclosureSourceParam = DisclosureSourceParamEnum.EDINET,
    edinet_api_key: EdinetApiKeyParam = settings.edinet.api_key,
    # Storage options
    storage: StorageParam = StorageParamEnum.LOCAL,
    # Local storage options
    local_path: LocalPathParam = settings.storage.local_path,
    # S3 storage options
    s3_bucket: S3BucketParam = settings.storage.s3_bucket,
    s3_prefix: S3PrefixParam = settings.storage.s3_prefix,
    s3_region: S3RegionParam = settings.storage.s3_region,
    # Time scope options
    month: MonthParam = None,
    day: DayParam = None,
    # Format type options
    format_type: FormatTypeParam = FormatTypeEnum.XBRL,
) -> None:
    """
    Collect financial disclosure documents from the target disclosure source.
    """
    # initialize console
    console = create_console()

    # validation
    validate_disclosure_source(ctx, console, disclosure_source, edinet_api_key)
    validate_storage(ctx, console, storage, local_path, s3_bucket, s3_prefix, s3_region)
    validate_timescope(month, day)

    # Create storage based on storage type
    storage_config: LocalStorageConfig | S3StorageConfig
    if storage == StorageParamEnum.LOCAL:
        storage_config = LocalStorageConfig(base_dir=local_path)
        console.print(f"[info]Storage: Local ({local_path})[info]")
    elif storage == StorageParamEnum.S3:
        storage_config = S3StorageConfig(
            bucket_name=s3_bucket,
            prefix=s3_prefix if s3_prefix else None,
            region=s3_region,
        )
        prefix_display = f" (prefix: {s3_prefix})" if s3_prefix else ""
        console.print(
            f"[info]Storage: S3 (bucket: {s3_bucket}, region: {s3_region}{prefix_display})[info]"
        )

    # Create fino core disclosure source
    edinet_config = EdinetConfig(api_key=edinet_api_key)

    # Create fino core collector
    collector = DocumentCollector(
        disclosure_config=edinet_config, storage_config=storage_config
    )

    # Create time scope
    timescope = TimeScope(year=year, month=month, day=day)

    result = collector.collect_document(
        timescope=timescope, format_type=FormatTypeEnum.XBRL
    )

    collected_document_list: list[Document] = result["collected_document_list"]

    rich.print(
        f"[{'brand.primary'}]✓ Collected {len(result)} documents[/{'brand.primary'}]"
    )
    for document in collected_document_list:
        rich.print(
            f"{document.document_id}: {document.disclosure_date}, {document.filing_name}, {document.disclosure_type}"
        )
