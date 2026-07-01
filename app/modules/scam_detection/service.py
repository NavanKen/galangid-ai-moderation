from app.modules.base_service import BaseAIService
from app.modules.scam_detection.prompt import SYSTEM_PROMPT
from app.modules.scam_detection.schema import (
    ScamDetectionRequest,
    ScamDetectionResponse,
)
from app.config.ai.prompt_builder import build_user_prompt
from app.config.ai.prompt_intro import PromptIntro

class ScamDetectionService(BaseAIService):
    async def detect_scam(
        self, request: ScamDetectionRequest
    ) -> ScamDetectionResponse:

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
            response_model=ScamDetectionResponse,
        )
        
        return result

