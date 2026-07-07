import os
import json
import re

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage


# Load enviroonment variables
load_dotenv()

# Read Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini Model
llm = ChatGoogleGenerativeAI(
 model="gemini-2.5-flash",
 google_api_key=GEMINI_API_KEY,
 temperature=0.3
 )

def create_plan(user_request):

    prompt = f"""
You are an autonomous AI Planning agent. 
Create a step-by-step execution plan for the user's request.
Return ONLY a JSON array.

Example:
[
    "Understand the request",
    "Create document outline",
    "Write document",
    "Review document",
    "Generate Word document",
]

User Request:
{user_request}
""" 
    
    try:
        response = llm.invoke([HumanMessage(content=prompt)])

        content = response.content

        # Remove markdown if Gemini returns ```json
        content = re.sub("```json|```", "", content).strip()

        print("\nGemini Response:\n")
        print(content)

        # Convert JSON string to python list
        plan = json.loads(content)

        return plan

    except Exception as e:
        print("Planner Error:", e)

        # Fallback Plan
        return [
            "Understand user request",
            "Create document outline",
            "Write document",
            "Review document",
            "Generate Word document"
        ]
