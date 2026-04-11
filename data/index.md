---
layout: default
title: Data & Scripts
---

# Data & Scripts

This page collects the datasets and scripts we use throughout the course. Resources are added each week as needed — check back for updates.

Datasets are sampled subsets of larger corpora maintained in the [NLP Corpora for Korean Studies](https://github.com/scdenney/nlp_corpora) repository. For full corpora and detailed documentation, see that repository.

**Organizing your files:** Create subfolders within your `/data` directory by corpus or file type — e.g., `/data/president_speeches/`, `/data/scripts/`. This keeps things tidy as we accumulate more files over the semester.

---

## Datasets

| Week(s) | Dataset | Description | Download |
|---------|---------|-------------|----------|
| 2–5+ | Presidential Speeches | 749 democratic-era presidential speeches (Roh Tae-woo–Moon Jae-in), sampled from 5,840. See [documentation](president_speeches/README.md). | [CSV](president_speeches/president_speeches_democratic_era.csv) (~4.4 MB) |
| 2–5+ | Presidential Speeches (Small) | 100 randomly selected speeches from the last three presidents (Lee Myung-bak, Park Geun-hye, Moon Jae-in). Use this if Orange runs slowly or crashes with the full file. | [CSV](president_speeches/president_speeches_small.csv) (~500 KB) |
| 5+ | NIKH History Textbooks (Demo) | 9 Korean history textbooks across 3 eras (Colonial, Authoritarian, Democratic), sampled from the 67-book NIKH corpus (1895–2016). Includes `processed_text` column (pre-tokenized nouns, ready for analysis). See [full corpus documentation](https://github.com/scdenney/nlp_corpora/tree/main/data/nikh). | [CSV](nikh_textbooks/nikh_textbooks_demo.csv) (~1.8 MB) |
| 7 | NIKH Clustering Demo | 11 Korean history textbooks (3 Colonial, 4 Authoritarian, 4 Democratic) for the Week 7 clustering exercise. Contains `full_text` for preprocessing in Orange or R. | [CSV](nikh_textbooks/nikh_clustering_demo.csv) (~3.1 MB) |
| 9+ | Moon Jae-in Tweets | 3,148 tweets from @moonriver365 (2012–2020), with date, engagement metrics, and period labels (pre-presidency, transition, presidency). See [documentation](moon_twitter/README.md). | [CSV](moon_twitter/moon_twitter.csv) (~350 KB) |
| 4+ | Korean Stopwords | 678 Korean stopwords (punctuation, numbers, and high-frequency grammatical words). Load in the Preprocess Text widget under Filtering → Stopwords → From File. | [TXT](stopwords_ko.txt) |

## Sentiment Dictionaries

Korean sentiment word lists for dictionary-based sentiment analysis (Week 9+). Use these with the **Score Documents** widget in Orange or with `str_detect()` in R.

| Dictionary | Entries | Scale | Description | Download |
|------------|---------|-------|-------------|----------|
| KNU Sentiment Lexicon | 14,854 | −2 to +2 | The standard Korean sentiment dictionary from Kunsan National University. Includes intensity scores: +2 (very positive), +1 (positive), 0 (neutral), −1 (negative), −2 (very negative). Built from the Standard Korean Dictionary with human validation. | [TXT](sentiment_dic/SentiWord_Dict.txt) (~302 KB) |
| Course Positive Words | ~4,800 | binary | Korean positive sentiment words, phrases, and emoticons. | [TXT](sentiment_dic/positive.txt) (~84 KB) |
| Course Negative Words | ~9,800 | binary | Korean negative sentiment words, phrases, and emoticons. | [TXT](sentiment_dic/negative.txt) (~176 KB) |

**KNU format:** Tab-separated, two columns — `word⟨tab⟩score`. No header row. Load directly in R with `read_tsv("SentiWord_Dict.txt", col_names = c("word", "score"))`.

## Scripts

| Week | Script | Description | Download |
|------|--------|-------------|----------|
| 3+ | Korean Preprocessing (Mac) | POS-based tokenization for Orange Data Mining. Auto-installs kiwipiepy. Defaults to nouns only — suitable for BoW, clustering, topic modeling. | [Python](scripts/custom_preprocessing_mac-users.py) |
| 3+ | Korean Preprocessing (Windows) | Same as above but requires kiwipiepy pre-installed. | [Python](scripts/custom_preprocessing_windows-users.py) |
| 4+ | Korean Preprocessing — Annotated (Mac) | Fully annotated version of the Mac preprocessing script. Read this to understand what each step does and why. | [Python](scripts/korean_preprocessing_annotated-mac-ver.py) |
| 9+ | Sentiment Preprocessing (Mac) | Sentiment-specific variant: keeps NNG, NNP, VA, VV. Outputs verbs/adjectives in citation form (e.g., `행복하다`, `극복하다`) so tokens match KNU / positive.txt / negative.txt entries. Auto-installs kiwipiepy. | [Python](scripts/sentiment_preprocessing_mac-users.py) |
| 9+ | Sentiment Preprocessing (Windows) | Same as above but requires kiwipiepy pre-installed. | [Python](scripts/sentiment_preprocessing_windows-users.py) |

---

## How to Use

**Datasets:**
1. Download the CSV file
2. Save it to a subfolder in your GitHub repository (e.g., `/data/president_speeches/`)
3. Commit and push via GitHub Desktop
4. Load the file in Orange Data Mining using the Corpus widget

**Scripts:**
1. Download the `.py` file for your operating system
2. In Orange, add a **Python Script** widget and paste the code
3. Change `TEXT_COLUMN` to match your corpus column name (see the script comments)
4. Connect it to your data flow and run
