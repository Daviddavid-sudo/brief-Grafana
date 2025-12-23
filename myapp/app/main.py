from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.monitoring import REQUEST_COUNTER, REQUEST_LATENCY
import time

app = FastAPI()
instrumentator = Instrumentator()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    with REQUEST_LATENCY.time():
        REQUEST_COUNTER.inc()
        return {"item_id": item_id}

# Expose /metrics
instrumentator.instrument(app).expose(app)
