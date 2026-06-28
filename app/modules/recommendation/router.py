from fastapi import APIRouter, Depends, HTTPException

from app.config.exceptions import GeminiException, GeminiResponseError
from app.modules.recommendation.dependencies import get_recommendation_service
from app.modules.recommendation.schema import (
    RecommendationRequest,
    RecommendationResponse,
)
from app.modules.recommendation.service import RecommendationService

router = APIRouter(
    prefix="/recommendation",
    tags=["Recommendation"],
)


@router.post(
    "/suggest",
    response_model=RecommendationResponse,
    summary="Saran Perbaikan Campaign",
    description=(
        "Menganalisis campaign dan memberikan saran perbaikan yang konstruktif "
        "dan actionable. Mengidentifikasi strengths, weaknesses, dan memberikan "
        "suggestions yang diprioritaskan untuk meningkatkan kualitas campaign."
    ),
)
async def suggest_improvements(
    request: RecommendationRequest,
    service: RecommendationService = Depends(get_recommendation_service),
):
    try:
        return await service.suggest_improvements(request)

    except GeminiResponseError as e:
        raise HTTPException(
            status_code=422,
            detail={"error": "ai_response_error", "message": str(e)},
        )

    except GeminiException as e:
        raise HTTPException(
            status_code=502,
            detail={"error": "ai_service_error", "message": str(e)},
        )
