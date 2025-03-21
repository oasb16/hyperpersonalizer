
# persona_mapping.py
import boto3, logging, openai, time
from flask import request, jsonify
from config import AWS_REGION, AWS_DYNAMODB_TABLE_NAME, AWS_ACCESS_KEY, AWS_SECRET_KEY, OPENAI_API_KEY

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# OpenAI Config
openai.api_key = OPENAI_API_KEY

# DynamoDB
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)
dynamodb = session.resource("dynamodb")
table = dynamodb.Table(AWS_DYNAMODB_TABLE_NAME)

def analyze_with_gpt(persona_input):
    prompt = f"""
    You are a hyper-personalization engine. Analyze the following user attributes and map to the most likely persona among a database of 18,711:

    {persona_input}

    Return a JSON with:
    - Persona Name
    - Explanation of Match
    - Relevance Score (0–100)
    - Confidence Label (High, Medium, Low)
    """
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message.content

def map_persona():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request, no JSON received"}), 400

        gpt_result = analyze_with_gpt(data)

        item = {
            "user_id": f"sess_{int(time.time())}",
            "input": data,
            "gpt_analysis": gpt_result
        }

        table.put_item(Item=item)
        return jsonify({"result": gpt_result}), 200

    except Exception as e:
        logger.error(f"GPT Mapping Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500