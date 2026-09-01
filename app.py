from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from agent import generate_document

app = FastAPI(
    title="AI Transformation Strategy Intelligence API",
    description="Autonomous AI agent for generating AI transformation strategy documents.",
    version="1.0.0"
)


class AgentRequest(BaseModel):
    request: str


@app.get("/")
def home():
    return {
        "message": "AI Transformation Strategy Intelligence API is running successfully!"
    }


@app.post("/agent")
def run_agent(data: AgentRequest):
    try:
        result = generate_document(data.request)
        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )