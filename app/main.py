from app.routers.urls import api_router
from fastapi import FastAPI

app = FastAPI(title="SlotMachine")

app.include_router(api_router, prefix="/api")
