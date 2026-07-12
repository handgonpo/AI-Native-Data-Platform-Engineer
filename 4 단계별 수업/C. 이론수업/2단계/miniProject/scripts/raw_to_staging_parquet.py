import json
from pathlib import Path
from typing import Any

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = (
    PROJECT_ROOT
    / "data_lake"
    / "raw"
    / "order_events"
    / "order_events.jsonl"
)

STAGING_FILE = (
    PROJECT_ROOT
    / "data_lake"
    / "staging"
    / "order_events"
    / "order_events.parquet"
)


def read_jsonl(
    file_path: Path
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []

    if not file_path.exists():
        raise FileNotFoundError(
            f"Raw 파일을 찾을 수 없습니다: {file_path}"
        )

    with file_path.open(
        "r",
        encoding="utf-8"
    ) as file:
        for line_number, line in enumerate(
            file,
            start=1
        ):
            stripped_line = line.strip()

            if not stripped_line:
                continue

            try:
                records.append(
                    json.loads(stripped_line)
                )

            except json.JSONDecodeError as error:
                raise ValueError(
                    f"{line_number}번째 줄의 JSON 형식이 잘못되었습니다."
                ) from error

    return records


def flatten_order_event(
    record: dict[str, Any]
) -> dict[str, Any]:
    payload = record.get("payload", {})

    return {
        "event_id": record.get("event_id"),
        "event_type": record.get("event_type"),
        "schema_version": record.get("schema_version"),
        "source_system": record.get("source_system"),
        "event_time": record.get("event_time"),
        "order_id": payload.get("order_id"),
        "customer_id": payload.get("customer_id"),
        "total_amount": payload.get("total_amount"),
        "currency": payload.get("currency"),
        "item_count": payload.get("item_count")
    }


def build_staging_parquet() -> None:
    raw_records = read_jsonl(RAW_FILE)

    if not raw_records:
        print("변환할 Raw 데이터가 없습니다.")
        return

    staging_records = [
        flatten_order_event(record)
        for record in raw_records
    ]

    dataframe = pd.DataFrame(staging_records)

    dataframe["event_time"] = pd.to_datetime(
        dataframe["event_time"],
        errors="coerce",
        utc=True
    )

    dataframe["total_amount"] = pd.to_numeric(
        dataframe["total_amount"],
        errors="coerce"
    )

    dataframe["item_count"] = pd.to_numeric(
        dataframe["item_count"],
        errors="coerce"
    ).astype("Int64")

    STAGING_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    dataframe.to_parquet(
        STAGING_FILE,
        index=False
    )

    print(
        f"Staging Parquet 생성 완료: {STAGING_FILE}"
    )
    print(
        f"변환 건수: {len(dataframe)}"
    )


if __name__ == "__main__":
    build_staging_parquet()




    