from app.routers.urls import api_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SlotMachine")

origins = [
    "http://localhost:5173",
    "https://localhost:5173",
    "https://mikeyland.netlify.app",
    "https://slotmachine777.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")
