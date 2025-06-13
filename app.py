from flask import Flask, render_template, request, redirect, session
from playlist_engine import generate_playlist
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

app = Flask(__name__)
app.secret_key = "supersecret"

sp_oauth = SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="playlist-modify-public user-read-private",
    show_dialog=True,
    cache_path=".cache"
)

@app.route('/')
def home():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session['token_info'] = token_info
    return redirect('/create')

@app.route('/create', methods=['GET', 'POST'])
def create():
    token_info = session.get('token_info')
    if not token_info:
        return redirect('/')

    sp = spotipy.Spotify(auth=token_info['access_token'])

    if request.method == 'POST':
        start_mood = request.form['start_mood']
        end_mood = request.form['end_mood']
        num_songs = int(request.form['num_songs'])

        try:
            track_uris, display_names = generate_playlist(start_mood, end_mood, num_songs, sp)
            user_id = sp.current_user()['id']
            playlist = sp.user_playlist_create(user=user_id, name=f"{start_mood} ➝ {end_mood} Mood", public=True)
            sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)

            return render_template(
                "create.html",
                playlist_url=playlist['external_urls']['spotify'],
                track_list=display_names
            )
        except Exception as e:
            return render_template("create.html", error=str(e))

    return render_template("create.html")

if __name__ == '__main__':
    app.run(debug=True, port=8888)
