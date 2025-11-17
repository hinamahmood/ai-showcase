#!/bin/bash
# Deployment script for AWS EC2 (Free Tier)
# This script can be used with AWS CodeDeploy or run manually on EC2

set -e

echo "Starting deployment..."

# Update system packages
sudo apt-get update -y

# Install Python and pip if not present
sudo apt-get install -y python3 python3-pip python3-venv

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install gunicorn for production
pip install gunicorn

# Create systemd service file
sudo tee /etc/systemd/system/ai-showcase.service > /dev/null <<EOF
[Unit]
Description=AI Showcase Application
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/app
Environment="PATH=/home/ubuntu/app/venv/bin"
ExecStart=/home/ubuntu/app/venv/bin/gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd and start service
sudo systemctl daemon-reload
sudo systemctl enable ai-showcase
sudo systemctl restart ai-showcase

echo "Deployment completed successfully!"
echo "Check status with: sudo systemctl status ai-showcase"

