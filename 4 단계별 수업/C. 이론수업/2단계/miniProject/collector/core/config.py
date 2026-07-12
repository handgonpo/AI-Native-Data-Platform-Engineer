from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_LAKE_ROOT = PROJECT_ROOT / "data_lake"

RAW_ORDER_FILE = (
    DATA_LAKE_ROOT
    / "raw"
    / "order_events"
    / "order_events.jsonl"
)

DEAD_LETTER_ORDER_FILE = (
    DATA_LAKE_ROOT
    / "dead_letter"
    / "order_events"
    / "order_events_errors.jsonl"
)

STAGING_ORDER_FILE = (
    DATA_LAKE_ROOT
    / "staging"
    / "order_events"
    / "order_events.parquet"
)



