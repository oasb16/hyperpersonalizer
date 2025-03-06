import os

AWS_REGION = "us-west-2"
DYNAMODB_TABLE = "UserPersonaMapping"

# AWS Credentials should be set as ENV variables or in ~/.aws/credentials
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
