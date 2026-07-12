from pathlib import Path

import duckdb


PROJECT_ROOT = Path(__file__).resolve().parents[1]

STAGING_FILE = (
    PROJECT_ROOT
    / "data_lake"
    / "staging"
    / "order_events"
    / "order_events.parquet"
)


def query_staging() -> None:
    if not STAGING_FILE.exists():
        raise FileNotFoundError(
            f"Staging 파일을 찾을 수 없습니다: {STAGING_FILE}"
        )

    connection = duckdb.connect()

    try:
        print("\n[전체 주문 이벤트]")

        result = connection.execute(
            """
            SELECT
                event_id,
                order_id,
                customer_id,
                total_amount,
                currency,
                item_count,
                event_time
            FROM read_parquet(?)
            ORDER BY event_time
            """,
            [str(STAGING_FILE)]
        ).fetchdf()

        print(result)

        print("\n[주문 요약]")

        summary = connection.execute(
            """
            SELECT
                COUNT(*) AS order_count,
                SUM(total_amount) AS total_sales,
                AVG(total_amount) AS average_order_amount,
                SUM(item_count) AS total_item_count
            FROM read_parquet(?)
            """,
            [str(STAGING_FILE)]
        ).fetchdf()

        print(summary)

    finally:
        connection.close()


if __name__ == "__main__":
    query_staging()



    