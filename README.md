# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

For each song, compare its attributes with the user's preferences and calculate a score from 0 to 100. Higher scores indicate a closer match.

### Proposed scoring rule

Use these weights:

| Feature | Weight |
|---|---:|
| Genre | 0.30 |
| Mood | 0.25 |
| Energy | 0.15 |
| Tempo | 0.10 |
| Valence | 0.06 |
| Danceability | 0.06 |
| Acousticness | 0.06 |
| Artist | 0.02 |

For genre, mood, and artist, the feature similarity is `1` for an exact match and `0` otherwise. For energy, valence, danceability, and acousticness (each already on a 0–1 scale), use:

```text
similarity = 1 - abs(song_value - preferred_value)
```

For tempo, convert the BPM difference into a 0–1 similarity using a 160 BPM reference range:

```text
similarity = max(0, 1 - abs(song_tempo_bpm - preferred_tempo_bpm) / 160)
```

Then calculate:

```text
score = 100 * sum(weight * similarity) / sum(weights for preferences provided)
```

Only include features for which the user has provided a preference in the sums, so missing preferences do not lower a song's score. Rank songs by score, highest first. Artist has only a small influence, while genre and mood together account for more than half of the score.

I opted for these rules because based on my research and personal thoughts, genre and mood should be the biggest contributors to the score. Then energy and tempo matter, but not as much as genre and mood. The rest of the factors come below this. Artist is below all because it could too heavily skew the results especially with a small data set.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Loaded songs: 20

Top recommendations
====================

1. Sunrise City  |  Score: 99.57/100
   Reasons:
   - genre match (+42.9)
   - mood match (+35.7)
   - energy similarity (+21.0)

2. Gym Hero  |  Score: 61.50/100
   Reasons:
   - genre match (+42.9)
   - mood mismatch (+0.0)
   - energy similarity (+18.6)

3. Rooftop Lights  |  Score: 56.29/100
   Reasons:
   - genre mismatch (+0.0)
   - mood match (+35.7)
   - energy similarity (+20.6)

4. Sunday Steps  |  Score: 21.21/100
   Reasons:
   - genre mismatch (+0.0)
   - mood mismatch (+0.0)
   - energy similarity (+21.2)

5. Midnight Carnival  |  Score: 20.79/100
   Reasons:
   - genre mismatch (+0.0)
   - mood mismatch (+0.0)
   - energy similarity (+20.8)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

```
Loaded songs: 20

Top recommendations
====================

1. Sunrise City  |  Score: 99.57/100
   Reasons:
   - genre match (+42.9)
   - mood match (+35.7)
   - energy similarity (+21.0)

2. Gym Hero  |  Score: 61.50/100
   Reasons:
   - genre match (+42.9)
   - mood mismatch (+0.0)
   - energy similarity (+18.6)

3. Rooftop Lights  |  Score: 56.29/100
   Reasons:
   - genre mismatch (+0.0)
   - mood match (+35.7)
   - energy similarity (+20.6)

4. Sunday Steps  |  Score: 21.21/100
   Reasons:
   - genre mismatch (+0.0)
   - mood mismatch (+0.0)
   - energy similarity (+21.2)

5. Midnight Carnival  |  Score: 20.79/100
   Reasons:
   - genre mismatch (+0.0)
   - mood mismatch (+0.0)
   - energy similarity (+20.8)
```

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


