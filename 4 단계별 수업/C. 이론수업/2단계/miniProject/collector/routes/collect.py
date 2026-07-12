from typing import Any

from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError

from collector.schemas.events import OrderCreatedEvent
from collector.services.ingest import (
    ingest_order_event,
    save_order_dead_letter,
)


router = APIRouter(
    prefix="/api/collect",
    tags=["collect"]
)


@router.post(
    "/order",
    status_code=status.HTTP_201_CREATED
)
def collect_order_event(
    raw_body: dict[str, Any]
):
    """주문 이벤트 수집 Endpoint"""

    try:
        event = OrderCreatedEvent.model_validate(
            raw_body
        )

    except ValidationError as error:
        dead_letter_path = save_order_dead_letter(
            raw_body=raw_body,
            errors=error.errors()
        )

        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                "message": "주문 이벤트 검증 실패",
                "dead_letter_path": dead_letter_path,
                "errors": error.errors()
            }
        ) from error

    saved_path = ingest_order_event(event)

    return {
        "message": "주문 이벤트 저장 성공",
        "event_id": event.event_id,
        "order_id": event.payload.order_id,
        "saved_path": saved_path
    }
