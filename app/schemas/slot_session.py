from typing import List
from pydantic import BaseModel


class SlotSession(BaseModel):
    bet: int = None
    result: List = []
    change: int = None
