from pydantic import BaseModel

class ModerationRequest(BaseModel):
    title: str
    description: str


class ModerationResponse(BaseModel):
    approved: bool
    risk_scrore: int
    reason: str