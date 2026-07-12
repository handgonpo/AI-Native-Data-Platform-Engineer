from fastapi import FastAPI

from collector.routes.collect import (
    router as collect_router,
)


app = FastAPI(
    title="Order Event Collector",
    description=(
        "주문 이벤트를 수집하고 "
        "Raw 또는 Dead Letter에 저장하는 API"
    ),
    version="1.0.0"
)

app.include_router(collect_router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "order-event-collector"
    }


