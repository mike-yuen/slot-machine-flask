from pydantic import BaseModel


class User(BaseModel):
    email: str = None
    name: str = None
    picture: str = None
    total_chip: int = None
