from fastapi import APIRouter
from app.settings import Settings
router = APIRouter(prefix="/ping", tags=["ping-app, ping-db"])

@router.get("/db")
async def ping_db():
    settings = Settings()
    return {"message": settings.GOOGLE_TOKEN_ID}

@router.post("/")
async def ping():
    return {"ping": "pong"}
