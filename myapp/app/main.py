from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from contextlib import asynccontextmanager
from sqlmodel import SQLModel, create_engine
from app.routers.items import items_router  # <-- make sure this points to items.py

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    SQLModel.metadata.create_all(engine)
    yield
    # Optional shutdown code here

app = FastAPI(title="Items API", lifespan=lifespan)

# Prometheus instrumentation
instrumentator = Instrumentator(
    should_group_status_codes=False,
    should_ignore_untemplated=True,
    should_instrument_requests_inprogress=True,
    excluded_handlers=["/metrics"]
)
instrumentator.instrument(app).expose(app, endpoint="/metrics")

# Include API routes
app.include_router(items_router)

