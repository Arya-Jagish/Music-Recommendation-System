import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Set up credentials (replace with your own)
CLIENT_ID = "fefe4f2ea155449b89cf24d0b33f7d04"
CLIENT_SECRET = "8c23307dddcd46738b7a697612c5982c"

# Initialize Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

# Function to get playlist tracks
def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = []
    
    for item in results["items"]:
        track = item["track"]
        tracks.append({
            "name": track["name"],
            "artist": track["artists"][0]["name"],
            "album": track["album"]["name"],
            "release_date": track["album"]["release_date"],
            "popularity": track["popularity"]
        })
    
    return tracks

# Replace with your Spotify playlist ID
PLAYLIST_ID = "4zYDtwzu4hr54c3DgV4Odg"

# Fetch playlist data
playlist_data = get_playlist_tracks(PLAYLIST_ID)

# Convert to DataFrame and save as CSV
df = pd.DataFrame(playlist_data)
df.to_csv("data/songs.csv", index=False)  # ✅ Correct

print("Playlist data saved to songs.csv!")
