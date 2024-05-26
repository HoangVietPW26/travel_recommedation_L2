from fastapi import FastAPI
from fastapi.routing import APIRouter
from fastapi.exceptions import RequestValidationError
from openai import APIConnectionError

from src.errors.error_handler import (
    validation_error_handler,
    openai_connection_error_handler,
    generic_exception_handler
)
from src.routes.recommendation_management.recommendation import (
    router as recommendation_router
)


app = FastAPI()
api_router = APIRouter()

app.add_exception_handler(RequestValidationError, validation_error_handler)
app.add_exception_handler(APIConnectionError, openai_connection_error_handler)
app.add_exception_handler(Exception, generic_exception_handler)

api_router.include_router(recommendation_router)

app.include_router(api_router, prefix="/api/v1")
