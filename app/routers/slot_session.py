from app.crud.slot_session import SlotSessionCrud
from app.schemas.slot_session import SlotSessionReq
from fastapi import APIRouter

router = APIRouter()


@router.post("/random")
def randomize_result(
    body: SlotSessionReq,
    # current_user: models.User = Depends(get_current_user),
):
    return SlotSessionCrud().run_slot_session()
