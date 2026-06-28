from fastapi import APIRouter, Depends, HTTPException

from app.config.exceptions import GeminiException, GeminiResponseError
from app.modules.scam_detection.dependencies import get_scam_detection_service
from app.modules.scam_detection.schema import (
    ScamDetectionRequest,
    ScamDetectionResponse,
)
from app.modules.scam_detection.service import ScamDetectionService
router = APIRouter(
    prefix="/scam-detection",
    tags=["Scam Detection"],
)

@router.post(
    "/check",
    response_model=ScamDetectionResponse,
    summary="Deteksi Potensi Penipuan Campaign",
    description=(
        "Menganalisis campaign secara mendalam untuk mendeteksi "
        "pola-pola penipuan. Mengembalikan daftar indikasi mencurigakan "
        "beserta severity, confidence score, dan rekomendasi untuk admin."
    ),
)
async def check_scam(
    request: ScamDetectionRequest,
    service: ScamDetectionService = Depends(get_scam_detection_service),
):
    try:
        return await service.detect_scam(request)

    except GeminiResponseError as e:
        raise HTTPException(
            status_code=422,
            detail={
                "error": "ai_response_error",
                "message": str(e),
            },
        )

    except GeminiException as e:
        raise HTTPException(
            status_code=502,
            detail={
                "error": "ai_service_error",
                "message": str(e),
            },
        )
