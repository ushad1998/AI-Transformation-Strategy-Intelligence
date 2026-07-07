# 🤖 Autonomous AI Agent – Python AI Engineer Challenge

## Overview

This project is a submission for the **Python AI Engineer – Autonomous Agents**

The application is built using **Python** and **FastAPI**. It accepts a natural language request through a REST API, autonomously creates an execution plan, performs the required tasks using **Google Gemini**, and generates a professionally formatted **Microsoft Word (.docx)** document as the final output.

---

## Features

* REST API built with FastAPI
* Autonomous AI agent workflow
* Multi-step task planning
* Natural language request processing
* Google Gemini LLM integration
* Automatic Microsoft Word document generation
* Request validation using Pydantic
* Modular Python architecture
* Interactive Swagger UI for API testing

---

## Technology Stack

* Python
* FastAPI
* Uvicorn
* LangChain
* Google Gemini API
* Pydantic
* python-docx
* python-dotenv

---

## Project Structure

```
AI-Agent-Challenge/
│── app.py
│── agent.py
│── planner.py
│── tools.py
│── models.py
│── test.py
│── test_agent.py
│── test_doc.py
│── requirements.txt
│── .gitignore
│── .env
└── README.md
```

---

## API Endpoint

### POST /agent

Accepts a JSON request.

Example:

```json
{
  "request": "Create a business proposal for an AI recruitment system."
}
```

---

## Workflow

1. User submits a natural language request.
2. FastAPI receives the request.
3. Request is validated using Pydantic.
4. The autonomous planner creates an execution plan.
5. The agent executes each task using Google Gemini.
6. The generated content is formatted into a professional Microsoft Word document.
7. The API returns the response and the generated document.

---

## Sample Test Requests

### Standard Request

```
Create a business proposal for an AI recruitment system.
```

### Complex Request

```
Create a detailed business proposal for an AI-powered recruitment platform for a multinational company. Include objectives, architecture, implementation roadmap, estimated budget, risks, recommendations, and make reasonable assumptions where information is missing.
```

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
```

Navigate to the project folder.

```bash
cd AI-Agent-Challenge
```

Create and activate a virtual environment.

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file in the project root and add your Gemini API key.

```
GOOGLE_API_KEY=your_api_key_here
```

---

## Run the Application

```bash
uvicorn app:app --reload
```

Open Swagger UI.

```
http://127.0.0.1:8000/docs
```

---

## Engineering Improvement

This project implements **multi-step planning**. Instead of directly sending the complete prompt to the language model, the agent first generates an execution plan, breaks the request into manageable tasks, executes them sequentially, and finally produces a structured business document. This improves modularity, maintainability, and reasoning capability.

---

## Output

The system automatically generates a professionally formatted Microsoft Word (.docx) document containing structured business content based on the user's request.

---

## Author

**Usha D**
MCA Graduate | Python Developer | AI & Backend Enthusiast
