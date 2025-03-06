import os

# AWS Configuration
AWS_REGION = "us-east-1"
DYNAMODB_TABLE = "UserPersonaMapping"

# AWS Credentials (Use ENV variables for security)
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# OAuth Configuration (AWS Cognito)
COGNITO_DOMAIN = "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_l2tI8cmwZ"
COGNITO_CLIENT_ID = "71mr4dkg933tqhsnokqd9nk13n"
COGNITO_CLIENT_SECRET = os.getenv("COGNITO_CLIENT_SECRET")  # Keep secret in env variables
COGNITO_REDIRECT_URI = "https://hyperpersonalizer-a0808b1ef9ed.herokuapp.com/authorize"

# AWS Cognito OpenID Configuration
COGNITO_METADATA_URL = f"{COGNITO_DOMAIN}/.well-known/openid-configuration"
