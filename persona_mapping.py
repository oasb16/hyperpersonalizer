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

# Define Personas (Enhanced)
PERSONAS = [
    {
        "Persona Name": "Strategic Visionary",
        "Primary Trait": "Analytical Thinker",
        "Secondary Trait": "Decisive Leader",
        "Archetype": "The Architect",
        "Description": "A high-level thinker who excels at planning long-term goals and strategies.",
        "Real-World Example": "Elon Musk",
        "Strengths": ["Long-term planning", "Innovation", "Risk management"],
        "Weaknesses": ["May overlook short-term issues", "Sometimes too idealistic"],
        "Decision-Making Style": "Data-driven with calculated risk-taking",
        "Communication Style": "Clear, direct, and visionary",
        "Emotional Intelligence": "Moderate – prioritizes logic over emotion",
        "Best Fit Roles": ["CEO", "CTO", "Futurist", "Strategic Consultant"],
        "Ideal Work Environment": "Fast-paced, innovation-driven, highly autonomous",
        "Motivations": ["Solving complex problems", "Building impactful projects"],
        "Challenges": ["Managing operational details", "Balancing vision with execution"],
        "Famous Counterparts": ["Steve Jobs", "Nikola Tesla", "Jeff Bezos"],
        "Personality Alignment": {
            "MBTI": "INTJ",
            "Big Five": {
                "Openness": "High",
                "Conscientiousness": "High",
                "Extraversion": "Moderate",
                "Agreeableness": "Low",
                "Neuroticism": "Low"
            }
        },
        "Influences": ["Science fiction", "Philosophy", "Systems thinking"],
        "Preferred Problem-Solving Approach": "Systems-based analysis with an experimental mindset",
        "Adaptability": "High – thrives in uncertainty and rapid change",
        "Leadership Style": "Transformational – inspires others towards a bold vision"
    }
]

# Function to match user to persona based on responses
def match_persona(user_responses):
    scores = {persona["Persona Name"]: 0 for persona in PERSONAS}

    for persona in PERSONAS:
        for key in persona:
            if isinstance(persona[key], list):
                scores[persona["Persona Name"]] += sum(1 for trait in persona[key] if trait in user_responses.get(key, []))
            elif isinstance(persona[key], dict):
                scores[persona["Persona Name"]] += sum(1 for subkey in persona[key] if user_responses.get(key, {}).get(subkey) == persona[key][subkey])
            elif user_responses.get(key) == persona[key]:
                scores[persona["Persona Name"]] += 2

    best_match = max(scores, key=scores.get)
    return best_match, scores
