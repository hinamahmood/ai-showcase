"""
Tests for the AI Showcase Application
"""

import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "version" in response.json()

def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "ollama_connected" in data
    assert "model" in data

def test_demo():
    """Test demo endpoint"""
    response = client.get("/demo")
    assert response.status_code == 200
    data = response.json()
    assert "description" in data
    assert "features" in data
    assert "tech_stack" in data

def test_models_endpoint():
    """Test models listing endpoint"""
    response = client.get("/models")
    # This might fail if Ollama is not running, which is okay for CI
    assert response.status_code in [200, 503]

def test_chat_endpoint_invalid():
    """Test chat endpoint with invalid request"""
    response = client.post("/chat", json={})
    assert response.status_code == 422  # Validation error

def test_chat_endpoint_valid():
    """Test chat endpoint with valid request"""
    response = client.post("/chat", json={"message": "Hello"})
    # This might fail if Ollama is not running, which is okay for CI
    assert response.status_code in [200, 503]

