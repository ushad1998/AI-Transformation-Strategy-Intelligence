from planner import create_plan
from tools import create_word_document

import time
import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()

# Read API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.4
)


def generate_document(user_request):
    """
    Main Autonomous AI Agent Workflow
    """

    # -----------------------------
    # Step 1: Create Execution Plan
    # -----------------------------
    plan = create_plan(user_request)

    # -----------------------------
    # Step 2: Build Prompt
    # -----------------------------
    prompt = f"""
You are an Autonomous AI Business Assistant.

User Request:
{user_request}

Execution Plan:
{plan}

Generate a professional business document.

The document should contain:

# Title

# Executive Summary

# Introduction

# Main Content

# Benefits

# Conclusion

Return only the document.
"""

    # ---------------------------------------------------
    # Step 3: Retry & Fallback Logic (Engineering Feature)
    # ---------------------------------------------------

    MAX_RETRIES = 3

    content = None

    for attempt in range(MAX_RETRIES):

        try:

            print(f"Attempt {attempt+1} of {MAX_RETRIES}")

            response = llm.invoke(
                [HumanMessage(content=prompt)]
            )

            content = response.content

            print("Document generated successfully.")

            break

        except Exception as e:

            print(f"Attempt {attempt+1} Failed : {e}")

            # Wait before retrying
            time.sleep(2)

    # -----------------------------
    # Fallback Response
    # -----------------------------

    if content is None:

        return {
            "status": "error",
            "message": "Unable to generate document after multiple retries."
        }

    # -----------------------------
    # Step 4: Create Word Document
    # -----------------------------

    document_path = create_word_document(
        user_request,
        plan,
        content
    )

    # -----------------------------
    # Step 5: Return API Response
    # -----------------------------

    return {

        "status": "success",

        "request": user_request,

        "plan": plan,

        "document": document_path,

        "engineering_improvement": "Retry & Fallback Logic",

        "message": "Document generated successfully."

    }