from app.api import views
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(views.router, prefix="/users", tags=["users"])
