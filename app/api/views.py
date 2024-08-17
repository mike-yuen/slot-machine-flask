"""
This file is work like view.py in DRF

"""
from typing import Any, List, Optional

from app import models
from app.api import schemas
from app.config.db.session import get_db
from app.config.jwt import get_current_user
from app.services.crud.base import CRUDBase

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.responses import JSONResponse
from sqlalchemy import and_, func
from sqlalchemy.orm import Session

from app.services.slot import SlotMachineService

router = APIRouter()

@router.get("/random-slot/")
def get_channels_view(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    search: Optional[str] = None,
    # current_user: models.User = Depends(get_current_user),
):
    print(SlotMachineService().run_slot_session())
    return SlotMachineService().run_slot_session()
