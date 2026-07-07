from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from agent import generate_document

# Create FastAPI app
app = FastAPI(
    title="Autonomous AI Agent API",
    description="AI Agent that creates execution plans and generate word documents.",
    version="1.0"
)

# Request Model
class AgentRequest(BaseModel):
    request: str


# Health Check
@app.get("/")
def home():
    return {
        "message": "AI Agent API is running successfully!"
    }

# Main API
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