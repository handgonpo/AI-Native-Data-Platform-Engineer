from datetime import datetime

from pydantic import BaseModel, Field


class OrderPayload(BaseModel):
    """주문 이벤트 payload 데이터 계약"""

    order_id: str = Field(
        min_length=1,
        description="주문 고유 ID"
    )
    customer_id: str = Field(
        min_length=1,
        description="고객 고유 ID"
    )
    total_amount: float = Field(
        ge=0,
        description="총 주문 금액"
    )
    currency: str = Field(
        min_length=3,
        max_length=3,
        description="통화 코드"
    )
    item_count: int = Field(
        ge=1,
        description="주문 상품 개수"
    )


class OrderCreatedEvent(BaseModel):
    """주문 생성 이벤트 전체 데이터 계약"""

    event_id: str = Field(min_length=1)
    event_type: str = Field(min_length=1)
    schema_version: str = Field(min_length=1)
    source_system: str = Field(min_length=1)
    event_time: datetime
    payload: OrderPayload



    