from app.routers import slot_session, user
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(
    slot_session.router, prefix="/slot-sessions", tags=["Slot Session"]
)
api_router.include_router(user.router, prefix="/users", tags=["User"])
