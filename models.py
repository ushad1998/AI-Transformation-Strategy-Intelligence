from pydantic import BaseModel
from typing import List

class AgentRequest(BaseModel):
    request: str

class AgentResponse(BaseModel):
    status: str
    request: str
    plan: List[str]
    document:str
    message: str