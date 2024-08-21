from fastapi import APIRouter

# from app.config.jwt import get_current_user
from app.crud.user import UserCrud


router = APIRouter()


@router.post("/get-me")
def get_me(
    # current_user: models.User = Depends(get_current_user),
):
    return UserCrud().get_user_info(1)
