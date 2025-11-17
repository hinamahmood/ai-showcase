"""
AWS Lambda handler for the AI Showcase Application
For serverless deployment on AWS Lambda

Note: This file should be in the root directory when deploying to Lambda,
or adjust the import path accordingly.
"""

import sys
import os

# Add parent directory to path for Lambda deployment
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mangum import Mangum
from app import app

# Create ASGI handler for Lambda
handler = Mangum(app, lifespan="off")

def lambda_handler(event, context):
    """
    AWS Lambda handler function
    """
    return handler(event, context)

