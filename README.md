# 🎧 Control+Shift+Mood — Mood-Based Spotify Playlist Generator

**Control+Shift+Mood** is a full-stack web app that lets you generate Spotify playlists based on your emotional journey — from one mood to another (e.g., Calm ➝ Energetic).

Built with Flask, integrated with the **Spotify OAuth API**, and styled with a clean pastel-glass aesthetic, this app curates songs from a mood-tagged dataset and saves them directly to your Spotify account.

---

## ✨ Features

- 🎵 Generate a Spotify playlist based on a **mood arc transition**
- 🧠 Smart song matching using `valence` and `energy` vectors
- 🔐 Secure login via **Spotify OAuth 2.0**
- 📀 Automatically saves the playlist to Spotify account
- 📱 Fully **responsive design** for desktop and mobile
- 🎨 Dynamic playlist display with artist/song separation

---

## 🧰 Tech Stack

| Layer        | Technology                  |
|--------------|------------------------------|
| **Backend**  | Python, Flask                 |
| **Frontend** | HTML, CSS, Bootstrap 5, JS        |
| **API**      | Spotify Web API (OAuth 2.0)   |
| **Database** | CSV Dataset (Bollywood + Pop) |
| **Hosting**  | Render                        |

---

## 🔗 Live Demo

👉 (https://moodwave-jxlc.onrender.com/create)]

---

## 📸 Screenshots

### 💻 Desktop View

![Screenshot 1](![Screenshot 2025-06-13 172852](https://github.com/user-attachments/assets/bf20acaa-575e-4902-9654-f3839ef9ebb3)
)
![Screenshot 2](![Screenshot 2025-06-13 173720](https://github.com/user-attachments/assets/2badeb80-f1bd-4261-8988-05b0b4545185)
)


### Mobile View

| Task & Timer                                      | Quotes & Footer                                   |
|--------------------------------------------------|---------------------------------------------------|
| ![Mobile 1](![WhatsApp Image 2025-06-13 at 17 10 07_81027258](https://github.com/user-attachments/assets/18ecf977-1848-44fc-bf90-7fc8f83fd6ba)) | ![Mobile 2](![WhatsApp Image 2025-06-13 at 17 10 07_54eb6004(https://github.com/user-attachments/assets/06446cce-9e1c-4b21-9186-36269cd76099)) |

---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/steffthomas/moodwave.git
cd moodwave

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file with your Spotify credentials
touch .env
```

Your `.env` file should look like:

```env
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=https://your-app-name.onrender.com/callback
```

```bash
# Run the Flask app
python app.py

# Then open your browser at:
http://localhost:8888
```

---

## 🔐 Spotify OAuth Setup

To use Spotify login, register an app at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and configure:

- Redirect URI: `http://localhost:8888/callback` (for local dev) or your deployed Render domain
- Enable the following scopes:
  - `playlist-modify-public`
  - `user-read-private`

---

## 👤 Author

**Stefy Thomas**  
GitHub: [@steffthomas](https://github.com/steffthomas)  
LinkedIn: [stefy-thomas](https://www.linkedin.com/in/stefy-thomas)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, share, and remix it.

---

> _“Let your playlist follow your mood.”_
