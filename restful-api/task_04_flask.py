from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory users dictionary
users = {}

# Root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# List all usernames
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

# Status endpoint
@app.route("/status")
def status():
    return "OK"

# Get user by username
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404

# Add a new user
@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json(force=True)
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

# Run the Flask server
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
