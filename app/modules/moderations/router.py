from fastapi import APIRouter
from fastapi import Depends

from app.modules.moderations.service import (ModerationsService)

from app.modules.moderations.dependencies import (get_moderations_service)

router = APIRouter(
    prefix="/moderations",
    tags=["Moderations"]
)

@router.get("/test")
async def test_moderations(service: ModerationsService = Depends(get_moderations_service)):
    return await service.test()