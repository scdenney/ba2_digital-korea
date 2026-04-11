---
layout: default
title: Data & Scripts
---

# Data & Scripts

Every dataset, dictionary, and script you need for this course lives on this page, grouped by the week you'll first use it. Check back each week — new resources are added as the term progresses.

Datasets on this page are sampled subsets of larger corpora maintained in the [NLP Corpora for Korean Studies](https://github.com/scdenney/nlp_corpora) repository. For the full corpora and detailed documentation, see that repository.

**Organizing your own files:** create subfolders inside your `/data` directory by corpus — e.g., `/data/president_speeches/`, `/data/moon_twitter/`. Your scripts go in `/data/scripts/`. This keeps things tidy as the semester accumulates files.

---

## By week

### Weeks 1–2 — Intro & foundations
No files yet.

### Week 3 — Preprocessing basics
- **Script** — [Korean Preprocessing (Mac)](scripts/custom_preprocessing_mac-users.py) · [Windows](scripts/custom_preprocessing_windows-users.py)
- **Annotated** — [Line-by-line walkthrough](scripts/korean_preprocessing_annotated-mac-ver.py)
- **Stopwords** — [Korean stopwords (TXT)](stopwords_ko.txt) — 678 common Korean stopwords

### Weeks 4–5 — BoW, TF-IDF, word clouds
- **Dataset** — [Presidential Speeches (full, 4.4 MB)](president_speeches/president_speeches_democratic_era.csv) · [small version, 500 KB](president_speeches/president_speeches_small.csv) · [README](president_speeches/README.md)
- **Dataset** — [NIKH Textbooks Demo (Week 5)](nikh_textbooks/nikh_textbooks_demo.csv) · [README](nikh_textbooks/README.md)

### Week 7 — Clustering
- **Dataset** — [NIKH Clustering Demo](nikh_textbooks/nikh_clustering_demo.csv) · [README](nikh_textbooks/README.md)

### Week 8 — Word embeddings
See the **[Interactive Exercises](../interactive/)** page for the embeddings explorer.

### Week 9 — Sentiment analysis

- **Dataset** — [Moon Jae-in Tweets (3,148 tweets, 2012–2020)](moon_twitter/moon_twitter.csv) · [README](moon_twitter/README.md)
- **Script (Orange)** — [Sentiment Preprocessing (Mac)](scripts/sentiment_preprocessing_mac-users.py) · [Windows](scripts/sentiment_preprocessing_windows-users.py)
- **Dictionaries (Orange)** — [positive_stems.txt](sentiment_dic/positive_stems.txt) · [negative_stems.txt](sentiment_dic/negative_stems.txt)
- **Dictionary (R)** — [SentiWord_Dict_stems.txt](sentiment_dic/SentiWord_Dict_stems.txt) — full KNU with −2 to +2 scores
- **README** — [Which sentiment file to use, and why](sentiment_dic/README.md)

---

## How to use a dataset

1. Download the CSV file
2. Save it to a subfolder in your course GitHub repo (e.g., `/data/moon_twitter/`)
3. Commit and push via GitHub Desktop
4. In Orange, drop a **Corpus** widget on the canvas and load the CSV

## How to use a Python script in Orange

1. Download the `.py` file for your OS (Mac or Windows)
2. In Orange, drop a **Python Script** widget onto the canvas and connect a Corpus widget to its input
3. Double-click the Python Script widget and paste the code
4. At the top of the script, change `TEXT_COLUMN = '...'` to match your corpus's text column name
5. Click the ▶ (Run) button — the output adds a `processed_text` column

## Reference

- [Scripts README](scripts/README.md) — what each script does, including instructor-only files
- [NLP Corpora for Korean Studies](https://github.com/scdenney/nlp_corpora) — full source corpora and documentation
