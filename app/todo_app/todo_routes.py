from fastapi import APIRouter

router = APIRouter()


@router.get("/todos")
async def todos():
    return {"todos": ["one", "two"]}
