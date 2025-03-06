import boto3
from config import AWS_REGION, AWS_ACCESS_KEY, AWS_SECRET_KEY, DYNAMODB_TABLE

# AWS DynamoDB client setup
dynamodb = boto3.resource(
    'dynamodb',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)
table = dynamodb.Table(DYNAMODB_TABLE)

# Define Personas
PERSONAS = [
    {
        "Persona Name": "Strategic Visionary",
        "Primary Trait": "Analytical Thinker",
        "Secondary Trait": "Decisive Leader",
        "Archetype": "The Architect",
        "Description": "A high-level thinker who excels at planning long-term goals and strategies.",
        "Example": "Elon Musk"
    },
    {
        "Persona Name": "Creative Explorer",
        "Primary Trait": "Innovative",
        "Secondary Trait": "Risk-Taker",
        "Archetype": "The Adventurer",
        "Description": "Loves exploring new ideas, creative solutions, and artistic endeavors.",
        "Example": "Steve Jobs"
    }
]

# Function to match user to persona based on responses
def match_persona(user_responses):
    scores = {persona["Persona Name"]: 0 for persona in PERSONAS}

    for persona in PERSONAS:
        if user_responses.get("thinking_style") == persona["Primary Trait"]:
            scores[persona["Persona Name"]] += 3
        if user_responses.get("decision_making") == persona["Secondary Trait"]:
            scores[persona["Persona Name"]] += 2
        if user_responses.get("risk_tolerance") == "High" and persona["Archetype"] == "The Adventurer":
            scores[persona["Persona Name"]] += 2

    best_match = max(scores, key=scores.get)
    return best_match, scores
