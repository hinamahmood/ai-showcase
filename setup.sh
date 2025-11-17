#!/bin/bash
# Quick setup script for the AI Showcase

set -e

echo "🚀 Setting up AI Showcase..."

# Check Python version
echo "📋 Checking Python version..."
python3 --version

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Copy environment file
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp env.example .env
    echo "✅ Created .env file. Please edit it with your configuration."
else
    echo "ℹ️  .env file already exists, skipping..."
fi

# Check if Ollama is installed
if command -v ollama &> /dev/null; then
    echo "✅ Ollama is installed"
else
    echo "⚠️  Ollama is not installed. Please install it from https://ollama.ai/"
    echo "   On macOS: brew install ollama"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Start Ollama: ollama serve"
echo "3. Pull a model: ollama pull gemma3:1b"
echo "4. Run the app: uvicorn app:app --reload"
echo "5. Visit: http://localhost:8000/docs"

