from fastapi import APIRouter

items_router = APIRouter()

@items_router.get("/items")
async def read_items():
    return {"items": ["item1", "item2"]}
