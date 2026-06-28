from fastapi import APIRouter, Depends, HTTPException

from app.config.exceptions import GeminiException, GeminiResponseError
from app.modules.summarization.dependencies import get_summarization_service
from app.modules.summarization.schema import (
    SummarizationRequest,
    SummarizationResponse,
)
from app.modules.summarization.service import SummarizationService

router = APIRouter(
    prefix="/summary",
    tags=["Summarization"],
)

@router.post(
    "/generate",
    response_model=SummarizationResponse,
    summary="Generate Ringkasan Campaign",
    description=(
        "Menghasilkan ringkasan campaign dalam 2 level: "
        "short_summary (untuk card/preview) dan full_summary (untuk admin). "
        "Juga mengekstrak key points, beneficiary, purpose, dan urgency level."
    ),
)
async def generate_summary(
    request: SummarizationRequest,
    service: SummarizationService = Depends(get_summarization_service),
):
    try:
        return await service.generate_summary(request)

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
