# Quick Start Guide

## 🚀 Fastest Way to Get Started

### 1. Run Setup Script

```bash
./setup.sh
```

This will:
- Create a virtual environment
- Install all dependencies
- Set up environment variables

### 2. Start Ollama

In a new terminal:

```bash
# Start Ollama service
ollama serve

# In another terminal, pull a model
ollama pull gemma3:1b
```

### 3. Run the Application

```bash
# Activate virtual environment (if not already active)
source venv/bin/activate

# Start the server
uvicorn app:app --reload
```

### 4. Test the API

Open your browser: http://localhost:8000/docs

Or test with curl:

```bash
# Health check
curl http://localhost:8000/health

# Chat with AI
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello! Tell me about Python."}'
```

## 📤 Upload to GitHub

### Option 1: Using the Helper Script

```bash
# Make script executable (if needed)
chmod +x upload_to_github.sh

# Run the script
./upload_to_github.sh
```

### Option 2: Manual Steps

```bash
# Initialize git
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: AI Showcase"

# Add remote (replace with your repo URL)
git remote add origin hhttps://github.com/hinamahmood/ai-showcase

# Push to GitHub
git branch -M main
git push -u origin main
```

## 🐳 Docker Quick Start

```bash
# Start everything with Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

## ☁️ AWS Deployment

See the main README.md for detailed AWS deployment instructions.

