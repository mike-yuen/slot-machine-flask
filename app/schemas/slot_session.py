from typing import List

from pydantic import BaseModel


class SlotSessionReq(BaseModel):
    bet: int = None


class SlotSessionRes(BaseModel):
    bet: int = None
    result: List = []
    change: int = None
