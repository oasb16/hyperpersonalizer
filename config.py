import os

AWS_REGION = "us-east-1"
DYNAMODB_TABLE = "UserPersonaMapping"

# AWS Credentials - Use environment variables for security
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

if not AWS_ACCESS_KEY or not AWS_SECRET_KEY:
    raise ValueError("AWS credentials are missing! Set them as environment variables.")
