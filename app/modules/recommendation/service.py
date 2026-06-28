from app.modules.base_service import BaseAIService
from app.modules.recommendation.prompt import SYSTEM_PROMPT
from app.modules.recommendation.schema import (
    RecommendationRequest,
    RecommendationResponse,
)
from app.config.ai.prompt_builder import build_user_prompt
from app.config.ai.prompt_intro import PromptIntro

class RecommendationService(BaseAIService):
    async def suggest_improvements(
        self, request: RecommendationRequest
    ) -> RecommendationResponse:

        user_prompt = build_user_prompt(
            intro=PromptIntro.RECOMMENDATION,
            title=request.title,
            description=request.description,
            category=request.category,
            goal_amount=request.goal_amount,
        )

        result = await self._call_gemini(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_model=RecommendationResponse,
        )

        return result


