from app.crud.user import UserCrud
from app.middleware.jwt import jwt_guard
from app.models.user import User
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/me")
def get_me(
    current_user: User = Depends(jwt_guard),
):
    print("current user: ", current_user)
    return UserCrud().get_user_info(1)
