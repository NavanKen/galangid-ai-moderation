class ModerationService:
    
    async def moderate(self,title:str, description: str):
        return {
            "approved": True,
            "risk_score": 10,
            "reason": "Looks safe"
        }