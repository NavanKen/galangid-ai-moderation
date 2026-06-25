from fastapi import FastAPI
from app.modules.moderations.router import (
    router as moderation_router
)


app = FastAPI(
    title="GalangID AI Moderations"
)

app.include_router(moderation_router)

