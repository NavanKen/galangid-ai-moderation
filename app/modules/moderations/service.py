from app.modules.base_service import BaseAIService
from app.modules.moderations.prompt import SYSTEM_PROMPT
from app.modules.moderations.schema import (
    CampaignModerationRequest,
    CampaignModerationResponse
)
from app.config.ai.prompt_builder import build_user_prompt
from app.config.ai.prompt_intro import PromptIntro

class ModerationsService(BaseAIService):

    async def analyze_campaign(self, request: CampaignModerationRequest)-> CampaignModerationResponse:
        user_prompt = build_user_prompt(
            intro=PromptIntro.MODERATION,
            title=request.title,
            description=request.description,
            category=request.category,
            goal_amount=request.goal_amount,
        )

        result = await self._call_gemini(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_model=CampaignModerationResponse,
        )

        return result
    

