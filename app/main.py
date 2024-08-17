from app.api.urls import api_router
from fastapi import FastAPI

app = FastAPI(title="SlotMachine")

app.include_router(api_router, prefix="/v1")
