
# 🎵 Music Recommendation System 🎶

An interactive AI-powered web application that recommends songs based on artist preferences and popularity, allowing users to explore music, play tracks via Spotify, and manage their favorite songs. Built with **Streamlit**, **FastAPI**, and **Python**.

---

## 📌 Features

- 🔐 **User Authentication** – Secure login & registration system  
- 🎼 **Personalized Recommendations** – Based on artist input and popularity  
- ❤️ **Favorites Management** – Save your favorite tracks with one click  
- 🎧 **Explore Songs** – Browse a library of curated songs  
- ▶ **Play on Spotify** – Direct links to enjoy your recommendations instantly  
- 📊 **Clean UI** – Responsive and modern Streamlit design with custom CSS

---

## 🛠️ Tech Stack

| Layer       | Technology |
|-------------|------------|
| Frontend    | [Streamlit](https://streamlit.io/) |
| Backend     | [FastAPI](https://fastapi.tiangolo.com/) |
| Styling     | HTML & CSS (custom in Streamlit) |
| Database    | CSV/JSON File-based storage |
| Data Source | [Spotify](https://developer.spotify.com/) & curated song dataset |
| Libraries   | `requests`, `pandas`, `json`, `streamlit` |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/music-recommendation-app.git
cd music-recommendation-app


2. Create a virtual environment (optional) and install requirements:
pip install -r requirements.txt

3. Run the FastAPI backend
uvicorn backend.api:app --reload

4. Run the Streamlit frontend
streamlit run app.py


music-recommendation-app/
├── app.py                       # Main Streamlit frontend
├── backend/
│   ├── api.py                   # FastAPI backend for recommendations
│   ├── auth.py                  # User login/register logic
│   ├── favorites.py             # Favorite song storage and retrieval
│   └── utils.py                 # Spotify URL generation, helpers
├── data/
│   └── songs.csv                # Song dataset
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
