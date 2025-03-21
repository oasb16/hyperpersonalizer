# config.py
import os

AWS_REGION = "us-east-1"
AWS_DYNAMODB_TABLE_NAME = "UserPersonaMapping"
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "supersecret")