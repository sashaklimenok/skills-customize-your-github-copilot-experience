from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="FastAPI Starter: Simple Items API")


class Item(BaseModel):
    id: int | None = None
    name: str
    description: str | None = None


# In-memory storage
_ITEMS: List[Item] = []
_NEXT_ID = 1


@app.get("/items", response_model=List[Item])
def list_items():
    return _ITEMS


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for it in _ITEMS:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    global _NEXT_ID
    item.id = _NEXT_ID
    _NEXT_ID += 1
    _ITEMS.append(item)
    return item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
