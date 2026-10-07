# HEARMeTho — Project Plan

## Working title
**HEARMeTho: A Data Mining-Based Music Taste Analysis System**

## Core dataset
Primary dataset: Spotify tracks/audio-feature dataset.

Optional secondary dataset: Spotify Million Playlist Dataset (or a manageable subset) for playlist transactions used by Apriori.

## Algorithm mapping

| DWM concept | Implementation in HEARMeTho |
|---|---|
| ETL | Extract raw CSV, clean/transform, load to SQLite |
| Dimensional model | Song fact table + artist/genre/date dimensions |
| Preprocessing | Missing values, duplicates, encoding, scaling, feature preparation |
| EDA | Audio feature distributions, genre/popularity analysis, correlations |
| Decision Tree | Popular vs. non-popular classification |
| Naive Bayes | Music genre/category classification |
| Linear Regression | Popularity-score prediction |
| K-Means | Song/vibe clustering |
| Hierarchical clustering | Similar-song hierarchy and dendrogram |
| Apriori | Playlist/artist association rules |
| Vibe engine | Rule-based interpretation of mined features/clusters |

## Suggested warehouse schema

```text
DIM_ARTIST
- artist_id (PK)
- artist_name

DIM_GENRE
- genre_id (PK)
- genre_name

DIM_DATE
- date_id (PK)
- release_year

FACT_SONG
- song_id (PK)
- artist_id (FK)
- genre_id (FK)
- date_id (FK)
- popularity
- duration_ms
- danceability
- energy
- valence
- tempo
- acousticness
- speechiness
- instrumentalness
- liveness
```

## Dashboard pages

1. **Home** — upload/select songs and start analysis.
2. **Taste Analysis** — audio feature summaries and EDA.
3. **Cluster Lab** — K-Means + hierarchical clustering.
4. **Prediction Lab** — Decision Tree, Naive Bayes, regression.
5. **Pattern Lab** — Apriori support/confidence/lift.
6. **Vibe Report** — humorous final interpretation + recommendations.

## Scope rule

Keep the first version simple and explainable. Do not add Spotify OAuth, deep learning, LLMs, microservices, or a production-scale recommender before the core DWM pipeline works.
