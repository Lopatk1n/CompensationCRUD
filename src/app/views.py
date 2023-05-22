from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.db import get_db

router = APIRouter()


@router.get("/ping/")
async def ping_view() -> str:
    return "pong"


@router.get("/compensation/")
async def compensation_view(request: Request, db: Session = Depends(get_db)) -> None:
    response = db.execute(text("SELECT * FROM compensation;"))
    print(request)
    print(response)
    return
