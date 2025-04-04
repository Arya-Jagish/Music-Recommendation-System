import json
import hashlib

USER_FILE = "C:/Users/Arya Jagish/music_recommendation/data/users.json"

def load_users():
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    users = load_users()
    if username in users["users"]:
        return False, "User already exists."
    
    users["users"][username] = {
        "password": hash_password(password),
        "favorites": []
    }
    save_users(users)
    return True, "User registered successfully."

def login_user(username, password):
    users = load_users()
    if username in users["users"] and users["users"][username]["password"] == hash_password(password):
        return True
    return False
