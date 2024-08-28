from typing import Optional

from app.config.database import get_db
from fastapi import Depends, HTTPException
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security import OAuth2
from fastapi.security.utils import get_authorization_scheme_param
from starlette.requests import Request
from sqlalchemy.orm import Session

from app.crud.user import UserCrud
# from app.models import user
# from app.config import settings

# SECRET_KEY = settings.JWT_PUBLIC_KEY
# ALGORITHM = "RS256"

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class OAuth2PasswordBearerWithCookie(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: str = None,
        scopes: dict = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        authorization: str = request.cookies.get("access_token")

        scheme, param = get_authorization_scheme_param(authorization)

        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=401,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None

        return param


oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/auth/token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    print("---------", token)
    #     credentials_exception = HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Could not validate credentials",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )
    #     try:
    #         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    #         user_id: str = payload.get("id")
    #         if user_id is None:
    #             raise credentials_exception
    #     except JWTError:
    #         raise credentials_exception
    #     user = UserCrud().get_user_info(user_id)
    #     if user is None:
    #         raise credentials_exception
    #     return user
