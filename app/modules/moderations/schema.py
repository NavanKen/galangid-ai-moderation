from pydantic import BaseModel

class ModerationsRequest(BaseModel):
    title: str
    descriptions: str

class ModerationsResponse(BaseModel):
    message: str

    