from app.modules.base_service import BaseAIService
from app.modules.categorization.prompt import SYSTEM_PROMPT
from app.modules.categorization.schema import (
    CategorizationRequest,
    CategorizationResponse,
)
from app.config.ai.prompt_builder import build_user_prompt
from app.config.ai.prompt_intro import PromptIntro

class CategorizationService(BaseAIService):
    async def predict_category(
        self, request: CategorizationRequest
    ) -> CategorizationResponse:
        """Prediksi kategori campaign berdasarkan isi deskripsi."""

        user_prompt = build_user_prompt(
            intro=PromptIntro.CATEGORIZATION,
            title=request.title,
            description=request.description,
            category=request.category,
            goal_amount=request.goal_amount,
        )
        result = await self._call_gemini(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_model=CategorizationResponse,
        )

        return result
