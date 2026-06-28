from fastapi import FastAPI

from app.modules.moderations.router import router as moderation_router
from app.modules.categorization.router import router as categorization_router
from app.modules.recommendation.router import router as recommendation_router
from app.modules.scam_detection.router import router as scam_detection_router
from app.modules.summarization.router import router as summarization_router

def register_router(app: FastAPI):
    app.include_router(moderation_router)
    app.include_router(categorization_router)
    app.include_router(recommendation_router)
    app.include_router(scam_detection_router)
    app.include_router(summarization_router)    