"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

if __package__:
    from .recommender import load_songs, recommend_songs
else:
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    profiles = {
        "default": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.8,
        },
        "lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.4,
            "target_tempo_bpm": 80,
            "target_valence": 0.6,
            "target_danceability": 0.6,
            "target_acousticness": 0.75,
            "favorite_artist": "LoRoom",
        },
        "high_energy_pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.9,
            "target_tempo_bpm": 130,
            "target_valence": 0.85,
            "target_danceability": 0.9,
            "target_acousticness": 0.1,
        },
        "deep_intense_rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.95,
            "target_tempo_bpm": 160,
            "target_valence": 0.4,
            "target_danceability": 0.55,
            "target_acousticness": 0.05,
        },
        "mellow_acoustic_folk": {
            "favorite_genre": "folk",
            "favorite_mood": "nostalgic",
            "target_energy": 0.3,
            "target_tempo_bpm": 82,
            "target_valence": 0.58,
            "target_danceability": 0.45,
            "target_acousticness": 0.85,
        },
        "high_energy_sad": {
            "favorite_genre": "lofi",
            "favorite_mood": "lonely",
            "target_energy": 0.95,
            "target_acousticness": 0.9,
        },
        "conflicting_match": {
            "favorite_genre": "pop",
            "favorite_mood": "angry",
            "target_energy": 0.95,
        },
        "impossible_combination": {
            "favorite_genre": "classical",
            "favorite_mood": "euphoric",
            "favorite_artist": "LoRoom",
        },
        "single_preference": {
            "favorite_artist": "LoRoom",
        },
        "out_of_range_targets": {
            "favorite_genre": "pop",
            "target_energy": 1.5,
            "target_tempo_bpm": 1000,
        },
        "case_variation": {
            "favorite_genre": "POP",
            "favorite_mood": "HAPPY",
        },
    }

    for profile_name, profile in profiles.items():
        recommendations = recommend_songs(profile, songs, k=5)

        print(f"\nTop recommendations for {profile_name}")
        print("=" * (27 + len(profile_name)))
        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"\n{rank}. {song['title']}  |  Score: {score:.2f}/100")
            print("   Reasons:")
            for reason in explanation.split("; "):
                if reason:
                    print(f"   - {reason}")


if __name__ == "__main__":
    main()
