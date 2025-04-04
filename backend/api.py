from fastapi import FastAPI, Query
from backend.recommend import recommend_songs

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Music Recommendation API 🎵"}

@app.get("/recommend")
def get_recommendations(
    artist: str = Query(None, description="Filter by artist"),
    min_popularity: int = Query(50, description="Minimum song popularity"),
    num_songs: int = Query(5, description="Number of recommendations")
):
    recommendations = recommend_songs(preferred_artist=artist, min_popularity=min_popularity, num_songs=num_songs)
    return {"recommendations": recommendations}

