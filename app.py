# Persona_Matcher/
# ├── app.py               # Flask backend
# ├── config.py            # AWS Configs
# ├── persona_mapping.py   # Logic for persona matching + GPT scoring
# ├── requirements.txt     # Dependencies
# └── templates/
#     ├── index.html       # Landing UI
#     ├── dashboard.html   # Adaptive question UI

# app.py
from flask import Flask, request, jsonify, render_template, session
from persona_mapping import map_persona
from config import SECRET_KEY
from flask_cors import CORS
import logging

app = Flask(__name__)
app.secret_key = SECRET_KEY
CORS(app)

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/map-persona', methods=['POST'])
def map_persona_route():
    return map_persona()

if __name__ == '__main__':
    app.run(debug=True)

