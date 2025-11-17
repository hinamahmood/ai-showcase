"""
AI-Powered Showcase Application
A FastAPI application demonstrating local LLM integration, AWS deployment, and CI/CD
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import httpx
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Showcase",
    description="A showcase application using local LLM, AWS, and CI/CD",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gemma3:1b")

# Request/Response models
class ChatRequest(BaseModel):
    message: str
    model: Optional[str] = None
    context: Optional[List[str]] = None

class ChatResponse(BaseModel):
    response: str
    model: str
    tokens_used: Optional[int] = None

class HealthResponse(BaseModel):
    status: str
    ollama_connected: bool
    model: str

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "AI Showcase API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "chat": "/chat",
            "models": "/models",
            "docs": "/docs"
        }
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"{OLLAMA_BASE_URL}/api/tags")
            ollama_connected = response.status_code == 200
    except Exception as e:
        logger.error(f"Ollama connection error: {e}")
        ollama_connected = False
    
    return HealthResponse(
        status="healthy" if ollama_connected else "degraded",
        ollama_connected=ollama_connected,
        model=DEFAULT_MODEL
    )

@app.get("/models")
async def list_models():
    """List available Ollama models"""
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{OLLAMA_BASE_URL}/api/tags")
            if response.status_code == 200:
                models = response.json().get("models", [])
                return {
                    "models": [model.get("name", "") for model in models],
                    "default": DEFAULT_MODEL
                }
            else:
                raise HTTPException(status_code=503, detail="Ollama service unavailable")
    except httpx.RequestError as e:
        logger.error(f"Error connecting to Ollama: {e}")
        raise HTTPException(status_code=503, detail="Cannot connect to Ollama service")

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat endpoint that uses local LLM via Ollama
    """
    model = request.model or DEFAULT_MODEL
    
    try:
        # Prepare the prompt with context if provided
        prompt = request.message
        if request.context:
            context = "\n".join(request.context)
            prompt = f"Context:\n{context}\n\nQuestion: {request.message}\n\nAnswer:"
        
        # Call Ollama API
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                return ChatResponse(
                    response=result.get("response", ""),
                    model=model,
                    tokens_used=result.get("eval_count")
                )
            else:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Ollama API error: {response.text}"
                )
                
    except httpx.RequestError as e:
        logger.error(f"Error calling Ollama: {e}")
        raise HTTPException(
            status_code=503,
            detail="Cannot connect to Ollama service. Make sure Ollama is running."
        )
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/demo")
async def demo():
    """Demo endpoint showcasing the application"""
    return {
        "description": "AI Showcase Application",
        "features": [
            "Local LLM integration via Ollama",
            "FastAPI async web framework",
            "RESTful API design",
            "Health checks and monitoring",
            "AWS deployment ready",
            "CI/CD with GitHub Actions"
        ],
        "tech_stack": {
            "backend": "Python 3.11+",
            "framework": "FastAPI",
            "llm": "Ollama (local)",
            "deployment": "AWS (Lambda/EC2)",
            "ci_cd": "GitHub Actions"
        },
        "usage": {
            "start_server": "uvicorn app:app --reload",
            "health_check": "curl http://localhost:8000/health",
            "chat_example": "curl -X POST http://localhost:8000/chat -H 'Content-Type: application/json' -d '{\"message\": \"Hello!\"}'"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

