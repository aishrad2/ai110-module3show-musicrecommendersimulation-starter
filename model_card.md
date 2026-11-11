# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**

**Answer:** Vibe Match

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for.

Prompts:

- What kind of recommendations does it generate
- What assumptions does it make about the user
- Is this for real users or classroom exploration

**Answer:** It suggests songs from a small catalog based on a taste profile. It assumes the profile describes what the listener wants. This is for classroom exploration, not a finished product for real users.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.

Prompts:

- What features of each song are used (genre, energy, mood, etc.)
- What user preferences are considered
- How does the model turn those into a score
- What changes did you make from the starter logic

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

**Answer:** The model compares genre, mood, energy, tempo, valence, danceability, acousticness, and artist with the user's preferences. Genre (30%) and mood (25%) matter most. Energy (15%) and tempo (10%) come next. Valence, danceability, and acousticness are 6% each, and artist is 2%. Exact genre, mood, or artist matches earn their feature's points. Numeric features score higher when closer to the target; tempo differences are scaled by 160 BPM. The total score is from 0 to 100 and only includes preferences provided. The model also gives reasons showing each feature's contribution. Compared with the starter, I added CSV loading, scoring, explanations, and sorting by score.

---

## 4. Data  

Describe the dataset the model uses.

Prompts:

- How many songs are in the catalog
- What genres or moods are represented
- Did you add or remove data
- Are there parts of musical taste missing in the dataset

**Answer:** The catalog has 20 sample songs. Genres include pop, lofi, rock, ambient, jazz, synthwave, indie pop, classical, country, reggae, metal, folk, blues, electronic, funk, soul, and latin. Moods include happy, chill, intense, relaxed, focused, moody, serene, hopeful, playful, angry, nostalgic, lonely, euphoric, confident, romantic, and mysterious. I added 10 songs. The sample does not cover every style of music and uses simplified song features.

---

## 5. Strengths  

Where does your system seem to work well

Prompts:

- User types for which it gives reasonable results
- Any patterns you think your scoring captures correctly
- Cases where the recommendations matched your intuition

**Answer:** It works best for listeners with clear genre and mood preferences. Those features have the strongest effect, while audio targets help separate songs with similar labels. For the pop/happy profile, “Sunrise City” ranks first, as expected. The lofi/chill profile also ranks lofi songs above intense rock.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly.

Prompts:

- Features it does not consider
- Genres or moods that are underrepresented
- Cases where the system overfits to one preference
- Ways the scoring might unintentionally favor some users

**Answer:** The catalog is small, so some genres and moods have only one song. The model does not consider lyrics, context, or changing moods. It uses exact matches for genre and mood, so “indie pop” does not count as “pop.” Genre and mood have high weights, so they can dominate other similarities. Users with more preferences in their profile may also get different score behavior because only provided preferences are counted.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected.

Prompts:

- Which user profiles you tested
- What you looked for in the recommendations
- What surprised you
- Any simple tests or comparisons you ran

No need for numeric metrics unless you created some.

**Answer:** I tried the pop/happy and lofi/chill profiles. I checked that songs matching the genre and mood ranked higher, with numeric features helping distinguish songs further. “Sunrise City” ranked first for the pop/happy profile, and lofi songs ranked above “Storm Runner” for the lofi/chill profile. These results matched my expectations. The existing starter tests pass, but they do not fully test every feature of the scoring logic.

---

## 8. Future Work  

Ideas for how you would improve the model next.

Prompts:

- Additional features or preferences
- Better ways to explain recommendations
- Improving diversity among the top results
- Handling more complex user tastes

**Answer:** I could add more songs, allow several favorite genres or moods, and give partial credit to related genres. I could also make the top results more varied and test more profiles.

---

## 9. Personal Reflection  

A few sentences about your experience.

Prompts:

- What you learned about recommender systems
- Something unexpected or interesting you discovered
- How this changed the way you think about music recommendation apps

**Answer:** I learned that a recommender's choices about features and weights shape what it calls similar. It was interesting how changing the profile changes the recommended songs. Music apps also depend on their data and scoring rules, even when their suggestions seem personal.
