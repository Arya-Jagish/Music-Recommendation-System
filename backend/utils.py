import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up Spotify API credentials (Replace with actual credentials)
CLIENT_ID = "fefe4f2ea155449b89cf24d0b33f7d04"
CLIENT_SECRET = "8c23307dddcd46738b7a697612c5982c"

# Initialize Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, 
                                                           client_secret=CLIENT_SECRET))

def get_song_url(song_name):
    search_result = sp.search(q=song_name, limit=1)
    if search_result['tracks']['items']:
        return search_result['tracks']['items'][0]['external_urls']['spotify']
    return None
