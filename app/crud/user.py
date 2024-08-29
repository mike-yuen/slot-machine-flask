from typing import Any

from app.config.database import get_db
from app.models.user import User


class UserCrud:
    def __init__(self):
        self.db = next(get_db())

    def get_user_info(self, email: Any):
        user = self.db.query(User).filter(User.email == email).first()
        return user
