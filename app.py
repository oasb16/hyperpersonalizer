from flask import Flask, render_template, request, jsonify
import os
import requests  # or use an official OpenAI client library

app = Flask(__name__)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        command = request.form.get("command")
        # Call the AI model to generate sub-tasks
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
            json={
                "model": "gpt-4",
                "messages": [{"role": "user", "content": f"Break down this task into actionable steps: {command}"}]
            }
        )
        tasks = response.json().get("choices", [{}])[0].get("message", {}).get("content", "No tasks generated")
        return render_template("index.html", tasks=tasks, command=command)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
