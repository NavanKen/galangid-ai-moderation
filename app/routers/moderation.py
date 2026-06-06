from fastapi import APIRouter

from app.schemas.moderation import (ModerationRequest)
from app.services.moderation_service import (ModerationService)

router = APIRouter(
    prefix="/moderation",
    tags=["Moderation"],
)

service = ModerationService()

@router.post("/")
async def moderate(
    data: ModerationRequest
):
    return await service.moderate(
        data.title,
        data.description
    )