import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_distances
from mood_utils import MOOD_MAP

# Load the new dataset (update filename if needed)
df = pd.read_csv("tracks.csv")

# Filter for usable and recent tracks
df = df.dropna(subset=["valence", "energy", "song", "artist", "year"])
df = df[(df['valence'] >= 0) & (df['valence'] <= 1)]
df = df[(df['energy'] >= 0) & (df['energy'] <= 1)]
df = df[df['year'] >= 2000]  # Only songs from year 2000 onwards

if 'popularity' in df.columns:
    df = df[df['popularity'] >= 50]  # Optional: only popular songs

if 'explicit' in df.columns:
    df = df[df['explicit'] == False]  # Optional: exclude explicit songs

# Normalize valence and energy
scaler = MinMaxScaler()
df[["valence", "energy"]] = scaler.fit_transform(df[["valence", "energy"]])
df["vector"] = df.apply(lambda row: np.array([row["valence"], row["energy"]]), axis=1)

# Mood arc generator
def generate_mood_arc(start_vec, end_vec, num_points):
    return [start_vec * (1 - i / (num_points - 1)) + end_vec * (i / (num_points - 1)) for i in range(num_points)]

# Match closest songs
def match_songs_to_arc(arc, df):
    selected = []
    used_idx = set()

    for point in arc:
        distances = [np.linalg.norm(point - vec) for vec in df['vector']]
        sorted_idx = np.argsort(distances)
        for idx in sorted_idx:
            if idx not in used_idx:
                used_idx.add(idx)
                selected.append(df.iloc[idx])
                break
    return selected

# Playlist generator
def generate_playlist(start_mood, end_mood, num_songs, sp):
    arc = generate_mood_arc(MOOD_MAP[start_mood], MOOD_MAP[end_mood], num_songs)
    matched = match_songs_to_arc(arc, df)

    uris = []
    names = []

    for _, row in pd.DataFrame(matched).iterrows():
        query = f"track:{row['song']} artist:{row['artist']}"
        try:
            result = sp.search(q=query, type='track', limit=1)
            if result['tracks']['items']:
                uris.append(result['tracks']['items'][0]['uri'])
                names.append(f"{row['song']} — {row['artist']}")
        except Exception as e:
            print(f"Spotify search failed for {query}: {e}")

    return uris, names
