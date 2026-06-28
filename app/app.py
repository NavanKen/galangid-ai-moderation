from fastapi import FastAPI
from app.routers import register_router

def create_app()-> FastAPI:
    app = FastAPI(
        title="GalangID AI Moderations"
    )

    register_router(app)

    return app