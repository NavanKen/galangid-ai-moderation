from fastapi import APIRouter, Depends, HTTPException

from app.config.exceptions import GeminiException, GeminiResponseError
from app.modules.categorization.dependencies import get_categorization_service
from app.modules.categorization.schema import (
    CategorizationRequest,
    CategorizationResponse,
)
from app.modules.categorization.service import CategorizationService

router = APIRouter(
    prefix="/categorization",
    tags=["Categorization"],
)


@router.post(
    "/predict",
    response_model=CategorizationResponse,
    summary="Auto-Kategorisasi Campaign",
    description=(
        "Menganalisis isi campaign dan memprediksi kategori yang paling tepat. "
        "Jika pengguna sudah memilih kategori, AI akan memvalidasi apakah "
        "pilihan tersebut sesuai dengan isi deskripsi."
    ),
)
async def predict_category(
    request: CategorizationRequest,
    service: CategorizationService = Depends(get_categorization_service),
):
    try:
        return await service.predict_category(request)

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
