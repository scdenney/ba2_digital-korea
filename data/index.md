---
layout: default
title: Data & Scripts
---

# Data & Scripts

This page collects the datasets, scripts, and dictionaries used throughout the course. Resources are added each week — check back for updates.

Datasets are sampled subsets of larger corpora maintained in the [NLP Corpora for Korean Studies](https://github.com/scdenney/nlp_corpora) repository. For full corpora and documentation, see that repository.

**Organizing your files:** Create subfolders within your `/data` directory by corpus or file type — e.g., `/data/president_speeches/`, `/data/scripts/`. This keeps things tidy as the semester accumulates files.

---

## Datasets

| Week(s) | Dataset | Description | Download |
|---------|---------|-------------|----------|
| 2–5 | Presidential Speeches | 749 democratic-era presidential speeches (Roh Tae-woo – Moon Jae-in), sampled from 5,840. See [README](president_speeches/README.md). | [CSV](president_speeches/president_speeches_democratic_era.csv) (~4.4 MB) |
| 2–5 | Presidential Speeches (Small) | 100 randomly selected speeches from the last three presidents. Use this if Orange runs slowly with the full file. | [CSV](president_speeches/president_speeches_small.csv) (~500 KB) |
| 5 | NIKH History Textbooks (Demo) | 9 Korean history textbooks across 3 eras (Colonial, Authoritarian, Democratic), sampled from the 67-book NIKH corpus (1895–2016). Includes a pre-tokenized `processed_text` column. See [full corpus documentation](https://github.com/scdenney/nlp_corpora/tree/main/data/nikh). | [CSV](nikh_textbooks/nikh_textbooks_demo.csv) (~1.8 MB) |
| 7 | NIKH Clustering Demo | 11 Korean history textbooks (3 Colonial, 4 Authoritarian, 4 Democratic) for the Week 7 clustering exercise. Contains `full_text` for preprocessing in Orange. | [CSV](nikh_textbooks/nikh_clustering_demo.csv) (~3.1 MB) |
| 9 | Moon Jae-in Tweets | 3,148 tweets from @moonriver365 (2012–2020), with `favorites`, `retweets`, and a `period3` column (Pre-presidency / Transition / Presidency). See [README](moon_twitter/README.md). | [CSV](moon_twitter/moon_twitter.csv) |

---

## Scripts

| Week(s) | Script | Description | Download |
|---------|--------|-------------|----------|
| 3–8 | Korean Preprocessing (Mac) | POS-based Kiwi tokenization for Orange Data Mining. Auto-installs kiwipiepy. Keeps NNG and NNP tags (nouns only). | [Python](scripts/custom_preprocessing_mac-users.py) |
| 3–8 | Korean Preprocessing (Windows) | Same as above; kiwipiepy must be pre-installed. | [Python](scripts/custom_preprocessing_windows-users.py) |
| 3 | Korean Preprocessing — Annotated | Fully annotated Mac version. Read this to understand what each step does and why. | [Python](scripts/korean_preprocessing_annotated-mac-ver.py) |
| 9 | Sentiment Preprocessing (Mac) | Kiwi tokenization for sentiment analysis. Auto-installs kiwipiepy. Keeps NNG, NNP, VV, and VA tags (nouns + verbs + adjectives). | [Python](scripts/sentiment_preprocessing_mac-users.py) |
| 9 | Sentiment Preprocessing (Windows) | Same as above; kiwipiepy must be pre-installed. | [Python](scripts/sentiment_preprocessing_windows-users.py) |

---

## Dictionaries & Word Lists

| Week(s) | File | Description | Download |
|---------|------|-------------|----------|
| 4–8 | Korean Stopwords | 678 Korean stopwords (particles, auxiliaries, common grammatical words). Load in Preprocess Text → Filtering → Stopwords → From File. | [TXT](stopwords_ko.txt) |
| 9 | KNU Positive Word List | 4,868 positive-polarity Korean words (Park et al. 2018, Kunsan National University). Load in the Sentiment Analysis widget as the positive word list. | [TXT](sentiment_dic/positive.txt) |
| 9 | KNU Negative Word List | 9,824 negative-polarity Korean words (Park et al. 2018). Load in the Sentiment Analysis widget as the negative word list. | [TXT](sentiment_dic/negative.txt) |
| Reference | KNU Full Dictionary | Original SentiWord_Dict with polarity and intensity scores. For use in R with `read_tsv()` for weighted sentiment analysis. | [TXT](sentiment_dic/SentiWord_Dict.txt) |

---

## How to Use

**Datasets:**
1. Download the CSV file
2. Save it to a subfolder in your GitHub repository (e.g., `/data/moon_twitter/`)
3. Commit and push via GitHub Desktop
4. Load the file in Orange using the **Corpus** widget

**Scripts:**
1. Download the `.py` file for your operating system
2. In Orange, add a **Python Script** widget and paste the code
3. Change `TEXT_COLUMN` to match your corpus's text column name
4. Connect it to your data flow and run

**Dictionaries:**
1. Download the `.txt` file and save it somewhere you can find it (e.g., `/data/sentiment_dic/`)
2. In Orange, open the relevant widget — Preprocess Text for stopwords, Sentiment Analysis for the KNU lists
3. Point the widget to the file using the file picker in its settings
