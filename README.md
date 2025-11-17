# AI Showcase

A comprehensive Python project showcasing modern development practices including:
- **Local LLM Integration** (Ollama)
- **FastAPI** web framework
- **AWS Deployment** (Free Tier compatible)
- **Automated CI/CD** with GitHub Actions
- **Docker** containerization
- **Testing** and code quality checks

## 🚀 Features

- RESTful API with FastAPI
- Local LLM integration via Ollama
- Health checks and monitoring endpoints
- Docker containerization
- Automated testing and linting
- CI/CD pipeline with GitHub Actions
- AWS deployment ready (Lambda/EC2)

## 📋 Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- [Ollama](https://ollama.ai/) installed and running (for local LLM)
- Git (for version control)
- Docker (optional, for containerized deployment)

## 🛠️ Installation & Setup

### Step 1: Clone the Repository

```bash
cd /Users/hinamahmood/Documents/python_projects/ai-showcase
```

### Step 2: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Install and Setup Ollama

1. **Install Ollama:**
   ```bash
   # macOS
   brew install ollama
   
   # Or download from https://ollama.ai/
   ```

2. **Start Ollama service:**
   ```bash
   ollama serve
   ```

3. **Pull a model (in a new terminal):**
   ```bash
   ollama pull gemma3:1b
   # Or use a smaller model: ollama pull gemma3:1b
   ```

### Step 5: Configure Environment Variables

```bash
cp .env.example .env
# Edit .env with your settings (optional, defaults work for local dev)
```

### Step 6: Run the Application

```bash
# Development mode with auto-reload
uvicorn app:app --reload

# Or production mode
uvicorn app:app --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`

## 📖 API Documentation

Once the server is running, visit:
- **Interactive API Docs:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc

### Key Endpoints

- `GET /` - API information
- `GET /health` - Health check
- `GET /models` - List available Ollama models
- `POST /chat` - Chat with the LLM
- `GET /demo` - Demo information

### Example Usage

```bash
# Health check
curl http://localhost:8000/health

# Chat with LLM
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Python?"}'

# List models
curl http://localhost:8000/models
```

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)

This will start both the app and Ollama:

```bash
docker-compose up -d
```

### Using Docker Only

```bash
# Build the image
docker build -t ai-showcase .

# Run the container
docker run -p 8000:8000 \
  -e OLLAMA_BASE_URL=http://host.docker.internal:11434 \
  ai-showcase
```

## ☁️ AWS Deployment

### Option 1: AWS Lambda (Serverless - Free Tier)

1. **Install Serverless Framework:**
   ```bash
   npm install -g serverless
   npm install --save-dev serverless-python-requirements
   ```

2. **Configure AWS credentials:**
   ```bash
   aws configure
   ```

3. **Deploy:**
   ```bash
   cd aws
   serverless deploy
   ```

**Note:** For Lambda, you'll need to use an external Ollama service or AWS Bedrock for LLM access.

### Option 2: AWS EC2 (Free Tier)

1. **Launch EC2 Instance:**
   - Use t2.micro (Free Tier eligible)
   - Ubuntu 22.04 LTS
   - Configure security group to allow port 8000

2. **SSH into instance:**
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   ```

3. **Deploy:**
   ```bash
   git clone your-repo-url
   cd ai-showcase
   chmod +x aws/ec2_deploy.sh
   ./aws/ec2_deploy.sh
   ```

4. **Access the application:**
   - http://your-ec2-ip:8000

## 🔄 GitHub Actions CI/CD

The project includes automated CI/CD via GitHub Actions. The pipeline:

1. **Tests** - Runs linting, formatting checks, and unit tests
2. **Builds** - Creates Docker image
3. **Deploys** - Deploys to AWS (when pushing to main branch)

### Setup GitHub Secrets

For AWS deployment, add these secrets in GitHub Settings → Secrets:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `DOCKER_USERNAME` (optional, for Docker Hub)
- `DOCKER_PASSWORD` (optional, for Docker Hub)

## 📤 Uploading to GitHub

### Step 1: Initialize Git Repository

```bash
git init
```

### Step 2: Add All Files

```bash
git add .
```

### Step 3: Create Initial Commit

```bash
git commit -m "Initial commit: AI Showcase"
```

### Step 4: Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Don't initialize with README (we already have one)

### Step 5: Connect and Push

```bash
# Add remote (replace YOUR_USERNAME and YOUR_REPO with your details)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

## 🧪 Testing

Run tests with:

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/ -v

# With coverage
pytest tests/ -v --cov=app --cov-report=html
```

## 📁 Project Structure

```
ai-showcase/
├── app.py                 # Main FastAPI application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore rules
├── README.md            # This file
├── tests/               # Test files
│   ├── __init__.py
│   └── test_app.py
├── aws/                 # AWS deployment files
│   ├── lambda_function.py
│   ├── serverless.yml
│   └── ec2_deploy.sh
└── .github/
    └── workflows/
        └── ci-cd.yml    # GitHub Actions workflow
```

## 🎯 Interview Talking Points

This project demonstrates:

1. **Modern Python Development**
   - FastAPI for async web APIs
   - Type hints and Pydantic models
   - Clean code architecture

2. **AI/ML Integration**
   - Local LLM integration
   - API design for AI services
   - Error handling and fallbacks

3. **DevOps & Infrastructure**
   - Docker containerization
   - CI/CD automation
   - AWS cloud deployment
   - Infrastructure as code

4. **Best Practices**
   - Testing and code quality
   - Environment configuration
   - Logging and monitoring
   - Security considerations

## 🔧 Troubleshooting

### Ollama Connection Issues

- Ensure Ollama is running: `ollama serve`
- Check Ollama is accessible: `curl http://localhost:11434/api/tags`
- Verify model is installed: `ollama list`

### Port Already in Use

```bash
# Find process using port 8000
lsof -i :8000

# Kill the process or use a different port
uvicorn app:app --port 8001
```

### AWS Deployment Issues

- Verify AWS credentials: `aws configure list`
- Check IAM permissions for Lambda/EC2
- Review CloudWatch logs for errors

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and use this project as a template for your own showcase!

---

**Built with ❤️ for showcasing modern Python development skills**

