import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""
    numeric_fields = {
        "energy",
        "tempo_bpm",
        "valence",
        "danceability",
        "acousticness",
    }
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        songs = []
        for row in csv.DictReader(csv_file):
            row["id"] = int(row["id"])
            for field in numeric_fields:
                row[field] = float(row[field])
            songs.append(row)

    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return a song's weighted similarity score and feature-level reasons."""
    weights = {
        "genre": 0.15,
        "mood": 0.25,
        "energy": 0.30,
        "tempo_bpm": 0.10,
        "valence": 0.06,
        "danceability": 0.06,
        "acousticness": 0.06,
        "artist": 0.02,
    }
    preference_keys = {
        "genre": "favorite_genre",
        "mood": "favorite_mood",
        "energy": "target_energy",
        "tempo_bpm": "target_tempo_bpm",
        "valence": "target_valence",
        "danceability": "target_danceability",
        "acousticness": "target_acousticness",
        "artist": "favorite_artist",
    }
    categorical_features = {"genre", "mood", "artist"}

    available_weight = sum(
        weight
        for feature, weight in weights.items()
        if preference_keys[feature] in user_prefs
        and user_prefs[preference_keys[feature]] is not None
    )
    if available_weight == 0:
        raise ValueError("At least one taste-profile preference is required to score a song")

    weighted_similarities = []
    reasons = []

    for feature, weight in weights.items():
        preference_key = preference_keys[feature]
        if preference_key not in user_prefs or user_prefs[preference_key] is None:
            continue
        if feature not in song:
            raise ValueError(f"Song is missing the requested {feature!r} feature")

        preferred_value = user_prefs[preference_key]
        song_value = song[feature]
        if feature in categorical_features:
            similarity = float(str(preferred_value).casefold() == str(song_value).casefold())
            description = f"{feature} match" if similarity else f"{feature} mismatch"
        else:
            difference = abs(float(song_value) - float(preferred_value))
            scale = 160.0 if feature == "tempo_bpm" else 1.0
            similarity = max(0.0, 1.0 - difference / scale)
            label = "tempo" if feature == "tempo_bpm" else feature
            description = f"{label} similarity"

        contribution = 100.0 * weight * similarity / available_weight
        weighted_similarities.append(contribution)
        reasons.append(f"{description} (+{contribution:.1f})")

    score = sum(weighted_similarities)
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs as (song, score, explanation) tuples."""
    if k <= 0:
        return []

    recommendations = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        recommendations.append((song, score, "; ".join(reasons)))

    recommendations.sort(key=lambda recommendation: recommendation[1], reverse=True)
    del recommendations[k:]
    return recommendations
