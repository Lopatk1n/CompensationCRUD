import pydantic
from fastapi import FastAPI

from app.settings import get_settings
from app.views import router

settings: pydantic.BaseSettings = get_settings()

app = FastAPI(
    title="WaveAccess Test Task",
)

app.include_router(router)
