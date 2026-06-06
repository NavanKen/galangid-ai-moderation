from fastapi import FastAPI
from app.routers.moderation import router as moderation_router

app = FastAPI(
    title="GalangID AI Moderation"
)

app.include_router(moderation_router)