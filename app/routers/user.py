from fastapi import APIRouter, Depends

from app.crud.user import UserCrud
from app.middleware.jwt import get_current_user
from app.models.user import User


router = APIRouter()


@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user),
):
    print('current user: ', current_user)
    return UserCrud().get_user_info(1)
