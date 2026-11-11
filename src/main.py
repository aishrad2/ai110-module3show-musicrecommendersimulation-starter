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
    }

    recommendations = recommend_songs(profiles["default"], songs, k=5)

    print("\nTop recommendations")
    print("====================")
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']}  |  Score: {score:.2f}/100")
        print("   Reasons:")
        for reason in explanation.split("; "):
            if reason:
                print(f"   - {reason}")


if __name__ == "__main__":
    main()
