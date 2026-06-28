from app.modules.base_service import BaseAIService
from app.modules.moderations.prompt import SYSTEM_PROMPT, build_user_prompt
from app.modules.moderations.schema import (
    CampaignModerationRequest,
    CampaignModerationResponse
)

class ModerationsService(BaseAIService):
    async def analyze_campaign(
            self, request: CampaignModerationRequest
    )-> CampaignModerationResponse:
        
        user_prompt = build_user_prompt(
            title=request.title,
            description=request.description,
            goal_amount=request.goal_amount,
            category=request.category,
        )

        result = await self._call_gemini(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_model=CampaignModerationResponse,
        )

        return result