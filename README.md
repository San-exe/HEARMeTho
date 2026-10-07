# HEARMeTho

### Let the data hear you out.

**HEARMeTho** is a student-level Data Warehousing & Mining project that analyzes music data to uncover listening patterns, classify songs, predict popularity, cluster music into "vibes", mine playlist associations, and generate a playful music-taste report.

> The meme is the interface. The data mining is real.

## Project goals

- Build a small ETL pipeline from a real Spotify tracks dataset.
- Store cleaned music data in a dimensional/warehouse-style schema.
- Perform preprocessing and exploratory data analysis.
- Demonstrate six DWM-oriented algorithms:
  - Decision Tree
  - Naive Bayes
  - Linear Regression
  - K-Means
  - Hierarchical Clustering
  - Apriori
- Compare model/cluster quality with appropriate metrics.
- Generate a rule-based "music vibe" interpretation and lightweight recommendations.
- Present the results through a Streamlit dashboard.

## Planned workflow

```text
Raw Spotify Dataset
        |
        v
      Extract
        |
        v
 Data Cleaning / Transformation
        |
        v
   Data Warehouse
        |
        v
    EDA / Analysis
        |
   +----+---------+----------------+
   |              |                |
   v              v                v
Classification  Regression     Clustering
DT / NB            LR          K-Means / HC
   |              |                |
   +--------------+----------------+
                  |
                  v
             Apriori Mining
                  |
                  v
             Vibe Engine
                  |
                  v
            Streamlit App
```

## Repository structure

```text
HEARMeTho/
├── app/
│   └── app.py
├── database/
│   └── .gitkeep
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   └── PROJECT_PLAN.md
├── notebooks/
├── src/
│   ├── association/
│   │   └── apriori.py
│   ├── clustering/
│   │   ├── hierarchical.py
│   │   └── kmeans.py
│   ├── etl/
│   │   └── pipeline.py
│   ├── models/
│   │   ├── decision_tree.py
│   │   ├── naive_bayes.py
│   │   └── regression.py
│   ├── preprocessing/
│   │   └── preprocess.py
│   ├── recommendation/
│   │   └── recommender.py
│   └── vibe/
│       └── vibe_engine.py
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting started

1. Put the downloaded Spotify dataset in `data/raw/`.
2. Create a Python virtual environment.
3. Install dependencies from `requirements.txt`.
4. Run the ETL pipeline.
5. Run the mining modules.
6. Launch the Streamlit app.

The implementation is intentionally kept explainable and student-level rather than using deep learning or a production recommendation stack.
