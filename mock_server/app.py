from flask import Flask, jsonify, request

app = Flask(__name__)

# Эмуляция данных
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.json
    new_user = {"id": len(users) + 1, "name": data["name"]}
    users.append(new_user)
    return jsonify(new_user), 201

@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user["name"] = data["name"]
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    updated_users = [u for u in users if u["id"] != user_id]
    if len(updated_users) == len(users):
        return jsonify({"error": "User not found"}), 404
    users = updated_users
    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)
