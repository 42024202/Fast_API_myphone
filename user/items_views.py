from fastapi import APIRouter, Path
from typing import Annotated

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/items/")
def items():
    return {
        "item": "world"
            }

@router.get("/items/{item_id}/")
def get_item_by_id(item_id:Annotated[int, Path(ge=1,le=10000)]):
    return {
        "item": item_id
            }
