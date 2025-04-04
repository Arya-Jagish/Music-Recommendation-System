import streamlit as st
import requests
import json
import pandas as pd
from backend.auth import login_user, register_user
from backend.favorites import add_favorite, get_favorites
from backend.utils import get_song_url

# Set page config
st.set_page_config(page_title="🎵 Music Recommendation", page_icon="🎶", layout="wide")

# Custom CSS for UI Styling
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
    }
    .main {
        background-color: #f0f2f6;
        padding: 20px;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #1DB954;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #1AA34B;
    }
    .song-card {
        background: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        text-align: center;
        transition: 0.3s;
        margin-bottom: 10px;
    }
    .song-card:hover {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .favorite-button {
        background-color: #FF5A5F;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 5px 15px;
        font-size: 14px;
        transition: 0.3s;
    }
    .favorite-button:hover {
        background-color: #FF1E22;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎵 Music Recommendation System")

# Sidebar Login/Register
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/8/84/Spotify_icon.svg", width=100)
menu = st.sidebar.selectbox("Menu", ["Login", "Register"], index=0)

if menu == "Register":
    st.sidebar.subheader("🚀 Create an Account")
    username = st.sidebar.text_input("Username", placeholder="Enter username")
    password = st.sidebar.text_input("Password", type="password", placeholder="Enter password")
    if st.sidebar.button("Register"):
        success, msg = register_user(username, password)
        if success:
            st.sidebar.success(str(msg))
        else:
            st.sidebar.error(str(msg))

elif menu == "Login":
    st.sidebar.subheader("🔐 Login to Your Account")
    username = st.sidebar.text_input("Username", placeholder="Enter username")
    password = st.sidebar.text_input("Password", type="password", placeholder="Enter password")
    if st.sidebar.button("Login"):
        if login_user(username, password):
            st.session_state["user"] = username
            st.session_state["favorites"] = get_favorites(username)  # Load favorites into session state
            st.sidebar.success("✅ Logged in successfully!")
        else:
            st.sidebar.error("❌ Invalid credentials")

# Main content layout
col1, col2 = st.columns([2, 1])

with col1:
    st.header("🎤 Get Song Recommendations")
    artist = st.text_input("🎵 Enter Artist Name (Optional)", placeholder="e.g. Ed Sheeran")
    min_popularity = st.slider("🔥 Minimum Popularity", 0, 100, 50)
    num_songs = st.number_input("🎧 Number of Recommendations", 1, 10, 5)

    if st.button("🎼 Get Recommendations"):
        url = f"http://127.0.0.1:8000/recommend?min_popularity={min_popularity}&num_songs={num_songs}"
        if artist:
            url += f"&artist={artist}"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            st.session_state["recommendations"] = data["recommendations"]  # Store recommendations in session state
        else:
            st.error("⚠️ Failed to fetch recommendations!")

    if "recommendations" in st.session_state:
        st.write("## 🎶 Recommended Songs")
        song_cols = st.columns(2)  # Display in 2 columns
        for idx, song in enumerate(st.session_state["recommendations"]):
            with song_cols[idx % 2]:  # Alternate columns
                song_name = song['name']
                artist_name = song['artist']
                song_url = get_song_url(song_name)

                if st.button(f"❤️ Add {song_name} to Favorites", key=f"rec_{song_name}_{idx}"):
                    msg = add_favorite(st.session_state["user"], song_name)
                    if "favorites" not in st.session_state:
                        st.session_state["favorites"] = []
                    st.session_state["favorites"].append(song_name)  # Update session state
                    st.success(msg)
                    st.rerun()  # Force UI update

                st.markdown(f"""
                    <div class="song-card">
                        <b>{song_name}</b><br>
                        {artist_name} ({song['album']})<br>
                        <a href="{song_url}" target="_blank">▶ Play on Spotify</a>
                    </div>
                """, unsafe_allow_html=True)

with col2:
    if "user" in st.session_state:
        st.subheader(f"❤️ Welcome, {st.session_state['user']}! Your Favorite Songs")

        # Display favorite songs
        if "favorites" in st.session_state and st.session_state["favorites"]:
            for song in st.session_state["favorites"]:
                st.write(f"🎵 {song}")
        else:
            st.info("No favorites added yet!")

        # Load all songs for discovery
        st.write("### 🎼 Discover More Music")
        df = pd.read_csv("C:/Users/Arya Jagish/music_recommendation/data/songs.csv")
        song_cols = st.columns(2)

        for idx, row in df.iterrows():
            song_name = row['name']
            artist_name = row['artist']

            with song_cols[idx % 2]:
                st.write(f"🎶 **{song_name}** - {artist_name}")
                if st.button(f"❤️ Add to Favorites", key=f"disc_{song_name}_{idx}"):
                    msg = add_favorite(st.session_state["user"], song_name)
                    if "favorites" not in st.session_state:
                        st.session_state["favorites"] = []
                    st.session_state["favorites"].append(song_name)  # Update session state
                    st.success(msg)
                    st.rerun()  # Force UI update

st.sidebar.write("🎵 Enjoy your music!")


