from flask import Flask, jsonify

app = Flask(__name__)

# In-memory user database
USERS = {
    "1": {"id": "1", "name": "Alice Johnson", "email": "alice@example.com"},
    "2": {"id": "2", "name": "Bob Smith", "email": "bob@example.com"},
    "3": {"id": "3", "name": "Charlie Brown", "email": "charlie@example.com"},
}


@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    """
    Retrieve user by ID.
    
    Returns:
        - 200: User object with id, name, email
        - 404: Error message if user not found
    """
    user = USERS.get(user_id)
    
    if user is None:
        return jsonify({"error": "User not found", "id": user_id}), 404
    
    return jsonify(user), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
