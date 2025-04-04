import pandas as pd
import random

# Load the dataset
def load_songs():
    return pd.read_csv("data/songs.csv")

# Recommend songs based on artist or popularity
def recommend_songs(preferred_artist=None, min_popularity=50, num_songs=5):
    songs = load_songs()
    
    if preferred_artist:
        filtered_songs = songs[songs["artist"].str.contains(preferred_artist, case=False, na=False)]
    else:
        filtered_songs = songs[songs["popularity"] >= min_popularity]

    if filtered_songs.empty:
        return "No recommendations found!"
    
    return filtered_songs.sample(min(len(filtered_songs), num_songs)).to_dict(orient="records")
