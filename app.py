from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth
from persona_mapping import match_persona, table
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure random key

# Initialize OAuth
oauth = OAuth(app)

# Register AWS Cognito OIDC
oauth.register(
    name="oidc",
    client_id="5rvblhjkh3ocffgdties6g7gnn",
    client_secret=os.getenv("COGNITO_CLIENT_SECRET"),
    server_metadata_url="https://cognito-idp.us-east-1.amazonaws.com/us-east-1_EoTraXkZP/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

@app.route("/")
def home():
    user = session.get("user")
    if user:
        return render_template("dashboard.html", user=user)
    return render_template("index.html")

@app.route('/login')
def login():
    return oauth.oidc.authorize_redirect("https://hyperpersonalizer-a0808b1ef9ed.herokuapp.com/authorize")

@app.route('/authorize')
def authorize():
    token = oauth.oidc.authorize_access_token() 
    # Debugging: Print the full token response
    print("TOKEN RESPONSE:", token)
    user = token.get('userinfo', {})
    session['user'] = user
    return redirect(url_for('home'))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

@app.route("/map-persona", methods=["POST"])
def map_persona():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    user = session["user"]
    user_id = user.get("sub")  # Unique Cognito User ID

    data = request.json  # Expect JSON input
    best_match, scores = match_persona(data)

    # Save to AWS DynamoDB
    table.put_item(
        Item={
            "user_id": user_id,
            "email": user.get("email"),
            "responses": data,
            "Persona Name": best_match,
            "scores": scores,
        }
    )

    return jsonify({"persona": best_match, "likelihood": scores})

if __name__ == "__main__":
    app.run(debug=True)
