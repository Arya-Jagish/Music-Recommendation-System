import json

USER_FILE = "C:/Users/Arya Jagish/music_recommendation/data/users.json"
FAVORITES_FILE = "C:/Users/Arya Jagish/music_recommendation/data/favorites.json"

def add_favorite(username, song_name):
    with open(USER_FILE, "r") as f:
        users = json.load(f)
    
    users["users"][username]["favorites"].append(song_name)

    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

    return f"'{song_name}' added to favorites!"

def get_favorites(username):
    """Retrieves a list of favorite songs for a user"""
    try:
        with open(FAVORITES_FILE, "r") as f:
            favorites = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    return favorites.get(username, [])
