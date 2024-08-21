from typing import Any
from app.crud.base import CRUDBase
from app.models.user import User


class UserCrud:
    def get_user_info(self, id: Any):
        crud: Any = CRUDBase(User)
        user = crud.get_one(id=id)
        return user
