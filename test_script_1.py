import os
import sqlite3
import subprocess
import hashlib
import random
import pickle
from flask import Flask, request

app = Flask(__name__)

# Hardcoded secret (bad practice)
SECRET_KEY = "my_super_secret_key_123"

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchall()


def run_system_command(user_input):
    # Command Injection vulnerability
    subprocess.call("ls " + user_input, shell=True)


def calculate_hash(password):
    # Weak hashing algorithm
    return hashlib.md5(password.encode()).hexdigest()


def insecure_random_token():
    # Insecure randomness
    return str(random.random())


def unsafe_eval(data):
    # Dangerous eval usage
    return eval(data)


def insecure_deserialization(data):
    # Insecure pickle loading
    return pickle.loads(data)


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    users = get_user(username)

    if users:
        return "Login successful"
    return "Login failed"


if __name__ == "__main__":
    # Debug mode enabled in production
    app.run(debug=True)
