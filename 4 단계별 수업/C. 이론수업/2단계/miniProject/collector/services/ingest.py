from datetime import datetime, timezone
from typing import Any

from collector.core.config import (
    DEAD_LETTER_ORDER_FILE,
    RAW_ORDER_FILE,
)
from collector.core.lakehouse import append_jsonl
from collector.schemas.events import OrderCreatedEvent


def ingest_order_event(
    event: OrderCreatedEvent
) -> str:
    """검증된 주문 이벤트를 Raw JSONL에 저장한다."""

    record = event.model_dump(mode="json")

    append_jsonl(
        file_path=RAW_ORDER_FILE,
        record=record
    )

    return str(RAW_ORDER_FILE)


def save_order_dead_letter(
    raw_body: dict[str, Any],
    errors: list[dict[str, Any]]
) -> str:
    """검증 실패 원본과 오류 내용을 Dead Letter에 저장한다."""

    dead_letter_record = {
        "failed_at": datetime.now(
            timezone.utc
        ).isoformat(),
        "dataset": "order_events",
        "raw_body": raw_body,
        "errors": errors
    }

    append_jsonl(
        file_path=DEAD_LETTER_ORDER_FILE,
        record=dead_letter_record
    )

    return str(DEAD_LETTER_ORDER_FILE)



