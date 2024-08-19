"""
This file is work like view.py in DRF

"""
from typing import Any, List, Optional

from app.models import user
from app.schemas import user
from app.config.db.session import get_db
# from app.config.jwt import get_current_user
from app.crud.base import CRUDBase

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.responses import JSONResponse
from sqlalchemy import and_, func
from sqlalchemy.orm import Session

from app.crud.slot import SlotMachineService

router = APIRouter()


@router.post("/random")
def randomize_result(
    bet: int = 10,
    db: Session = Depends(get_db),
    # current_user: models.User = Depends(get_current_user),
):
    print(SlotMachineService().run_slot_session())
    return SlotMachineService().run_slot_session()
