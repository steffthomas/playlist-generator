import numpy as np
import pandas as pd

# 🎯 Mood coordinate mapping (valence, energy)
MOOD_MAP = {
    "Happy": np.array([0.9, 0.8]),
    "Sad": np.array([0.2, 0.3]),
    "Energetic": np.array([0.8, 0.9]),
    "Calm": np.array([0.4, 0.2]),
    "Romantic": np.array([0.7, 0.5]),
    "Angry": np.array([0.3, 0.9]),
    "Chill": np.array([0.5, 0.4])
}

# ✅ Load and preprocess dataset
def load_dataset(path="tracks.csv"):
    df = pd.read_csv(path)

    # Drop rows with missing values
    df = df.dropna(subset=['valence', 'energy', 'song', 'artist', 'year'])

    # ✅ Only keep tracks after 2000
    df = df[df['year'] >= 2000]

    # 🔁 Use song + artist as a fallback unique identifier
    df['id'] = df['song'] + " - " + df['artist']

    # 🎯 Add a vector for mood matching
    df['vector'] = df.apply(lambda row: np.array([row['valence'], row['energy']]), axis=1)

    return df

# 🌀 Generate a smooth transition arc between moods
def generate_mood_arc(start_vec, end_vec, num_points):
    return [
        start_vec * (1 - i / (num_points - 1)) + end_vec * (i / (num_points - 1))
        for i in range(num_points)
    ]

# 🎵 Match each point on the arc to the closest song
def match_songs_to_arc(arc, dataset_df):
    matched_rows = []
    used_indices = set()

    for point in arc:
        distances = [np.linalg.norm(point - vec) for vec in dataset_df['vector']]
        best_idx = np.argmin(distances)

        while best_idx in used_indices:
            distances[best_idx] = float('inf')
            best_idx = np.argmin(distances)

        used_indices.add(best_idx)
        matched_rows.append(dataset_df.iloc[best_idx])

    return matched_rows
