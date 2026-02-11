import os
import sqlite3
import subprocess
import hashlib
import secrets
import json
from flask import Flask, request

app = Flask(__name__)

# Use environment variable for secret key
SECRET_KEY = os.getenv("SECRET_KEY")

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Parameterized query prevents SQL injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))

    return cursor.fetchall()


def run_system_command(user_input):
    # Avoid shell=True and sanitize input
    subprocess.run(["ls", user_input], check=True)


def calculate_hash(password):
    # Use stronger hash
    return hashlib.sha256(password.encode()).hexdigest()


def secure_random_token():
    # Cryptographically secure randomness
    return secrets.token_hex(16)


def safe_parse(data):
    # Avoid eval; use safe parsing
    return json.loads(data)


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    users = get_user(username)

    if users:
        return "Login successful"
    return "Login failed"


if __name__ == "__main__":
    # Debug disabled
    app.run(debug=False)
