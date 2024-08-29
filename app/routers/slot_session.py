from app.crud.slot_session import SlotSessionCrud
from app.middleware.jwt import jwt_guard
from app.models.user import User
from app.schemas.slot_session import SlotSessionReq
from fastapi import APIRouter, Depends

router = APIRouter()


@router.post("/random")
def randomize_result(
    body: SlotSessionReq,
    current_user: User = Depends(jwt_guard),
):
    return SlotSessionCrud().run_slot_session()
