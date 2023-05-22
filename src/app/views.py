from fastapi import APIRouter

router = APIRouter()


@router.get("/ping/")
async def ping_view() -> str:
    return "pong"


@router.get("/compensation/")
async def compensation_view() -> str:
    return "pong"
