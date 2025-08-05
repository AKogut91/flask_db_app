from flask import Flask, request, jsonify
from flasgger import Swagger
import sqlite3
from db import init_db, get_all_users_full

app = Flask(__name__)
swagger = Swagger(app)
DATABASE = 'users.db'

@app.route('/hello')
def hello():
    """
    A hello world endpoint.
    ---
    responses:
      200:
        description: Returns hello world message
    """
    return jsonify(message="Hello, world!")


@app.route("/users", methods=["GET"])
def get_users():
    """
    Get all users with their home and work addresses
    ---
    responses:
      200:
        description: A list of users
        examples:
          application/json: [{"id":1,"name":"Alice","phone":1234567890,"home_address":"123 Street","work_address":""}]
    """
    users, message = get_all_users_full()
    if message:
        return jsonify({"message": message, "users": []}), 200
    return jsonify(users), 200

@app.route("/users", methods=["POST"])
def add_user():
    """
    Add a new user
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: User
          required:
            - name
            - phone
          properties:
            name:
              type: string
              example: Alice
            phone:
              type: integer
              example: 1234567890
    responses:
      201:
        description: User added successfully
    """
    data = request.get_json()
    name = data.get("name")
    phone = data.get("phone")

    if not name or not phone:
        return jsonify({"error": "Name and phone are required"}), 400

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, phone) VALUES (?, ?)', (name, phone))
    conn.commit()
    conn.close()

    return jsonify({"message": "User added successfully"}), 201

@app.route("/users/<int:user_id>/home", methods=["POST"])
def add_home(user_id):
    """
    Add home address for a user
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          properties:
            address:
              type: string
              example: "123 Home Street"
    responses:
      201:
        description: Home address added
    """
    data = request.get_json()
    address = data.get("address")

    if not address:
        return jsonify({"error": "Address is required"}), 400

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Home (user_id, address) VALUES (?, ?)', (user_id, address))
    conn.commit()
    conn.close()

    return jsonify({"message": "Home address added"}), 201

@app.route("/users/<int:user_id>/work", methods=["POST"])
def add_work(user_id):
    """
    Add work address for a user
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          properties:
            address:
              type: string
              example: "789 Work Avenue"
    responses:
      201:
        description: Work address added
    """
    data = request.get_json()
    address = data.get("address")

    if not address:
        return jsonify({"error": "Address is required"}), 400

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Work (user_id, address) VALUES (?, ?)', (user_id, address))
    conn.commit()
    conn.close()

    return jsonify({"message": "Work address added"}), 201

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
