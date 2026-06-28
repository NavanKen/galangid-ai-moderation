from fastapi import APIRouter, Depends, HTTPException

from app.config.exceptions import GeminiExeptions, GeminiResponseError
from app.modules.moderations.dependencies import get_moderations_service
from app.modules.moderations.schema import(
    CampaignModerationRequest,
    CampaignModerationResponse
)
from app.modules.moderations.service import ModerationsService

router = APIRouter(
    prefix="/moderations",
    tags=["Moderation"]
)

@router.post(
    "/analyze",
    response_model=CampaignModerationResponse,
    summary="Analisis Campaign dengan AI",
    description=(
        "Menerima data campaign dari NestJS, menganalisis menggunakan "
        "Gemini AI, dan mengembalikan hasil moderasi dalam format JSON "
        "terstruktur (approved, risk_score, category, summary, reason, "
        "scam_indicators, suggestions)."
    ),
)
async def analyze_campaign(
    request: CampaignModerationRequest,
    service: ModerationsService = Depends(get_moderations_service),
):
    try:
        return await service.analyze_campaign(request)
    except GeminiResponseError as e:
        raise HTTPException(
            status_code=422,
            detail={
                "error": "ai_response_error",
                "message": str(e),
            }
        )
    except GeminiExeptions as e:
        raise HTTPException(
            status_code=502,
            detail={
                "error": "ai_service_error",
                "message": str(e),
            }
        )
