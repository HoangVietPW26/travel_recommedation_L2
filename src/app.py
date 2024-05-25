from fastapi import FastAPI
from fastapi.routing import APIRouter

from src.routes.recommendation_management.recommendation import (
    router as recommendation_router
)


app = FastAPI()
api_router = APIRouter()

api_router.include_router(recommendation_router)

app.include_router(api_router, prefix="/api/v1")
