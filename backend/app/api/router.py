from fastapi import APIRouter
from app.api.routes import bets

api_router = APIRouter()
api_router.include_router(bets.router)
