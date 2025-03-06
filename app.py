from flask import Flask, render_template, request, jsonify
from persona_mapping import match_persona, table

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/map-persona', methods=['POST'])
def map_persona():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "Invalid data format"}), 400

        best_match, scores = match_persona(data)

        # Save to DynamoDB
        table.put_item(
            Item={
                "user_id": data.get("user_id"),
                "responses": data,
                "matched_persona": best_match,
                "scores": scores
            }
        )

        return jsonify({"persona": best_match, "likelihood": scores})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
