# Scripts

Python scripts for Orange Data Mining Python Script widgets, plus R scripts for standalone use in RStudio.

## Student-facing scripts

### For Weeks 3–7 (BoW, clustering, topic modeling)

| File | Purpose |
|------|---------|
| [`custom_preprocessing_mac-users.py`](custom_preprocessing_mac-users.py) | Kiwi tokenization keeping NNG/NNP (nouns) by default. Auto-installs `kiwipiepy`. Use in Orange's Python Script widget for any task where you want bag-of-words style output. |
| [`custom_preprocessing_windows-users.py`](custom_preprocessing_windows-users.py) | Same as above, but assumes `kiwipiepy` is already installed (`pip install kiwipiepy` in a terminal). |
| [`korean_preprocessing_annotated-mac-ver.py`](korean_preprocessing_annotated-mac-ver.py) | Line-by-line annotated version of the Mac script. Read this if you want to understand what each step does. |

### For Week 9 (sentiment analysis)

**You don't need a script for the main Week 9 workflow.** Orange's Sentiment Analysis widget handles Korean automatically when you pick Method = *Multilingual* and Language = *Korean*.

The scripts below are **optional** — useful if you want to experiment with morphological tokenization (Kiwi) or use the KNU intensity dictionary via Custom Dictionary:

| File | Purpose |
|------|---------|
| [`sentiment_preprocessing_mac-users.py`](sentiment_preprocessing_mac-users.py) | Kiwi tokenization keeping NNG/NNP/VA/VV stems (length ≥ 2). Pair with the stem-indexed KNU dictionaries in [`../sentiment_dic/`](../sentiment_dic/). Auto-installs `kiwipiepy`. |
| [`sentiment_preprocessing_windows-users.py`](sentiment_preprocessing_windows-users.py) | Same as above, Windows version. |

### R scripts

| File | Purpose |
|------|---------|
| [`week03_preprocessing.R`](week03_preprocessing.R) | R version of the Week 3 preprocessing pipeline. |
| [`week04_text_wrangling.R`](week04_text_wrangling.R) | R version of the Week 4 text wrangling pipeline. |

## How to use a Python Script in Orange

1. Download the `.py` file appropriate for your operating system
2. In Orange, drag a **Python Script** widget onto the canvas and connect a Corpus widget to its input
3. Double-click the Python Script widget, paste the script into the editor
4. At the top of the script, change `TEXT_COLUMN = 'text'` to match your corpus's text column name
5. Click "Run" (▶). The output is a new corpus with a `processed_text` column added

## Instructor-only files

The following files are generator/reproducibility scripts used to prepare course datasets and the interactive exercises. Students can ignore them.

- `generate_clustering_demo.py` — builds the NIKH clustering demo dataset
- `generate_kmeans_demo.py` — builds the k-means speeches demo
- `generate_nikh_demo.py` — builds the NIKH textbooks demo
- `generate_preprocessing_demo.py` — builds the preprocessing example data
- `generate_sentiment_demo.py` — rebuilds `interactive/sentiment_data.json` for the Week 9 interactive (matches Orange's Multilingual Korean scoring exactly)
- `sentence_splitter.py` — utility used by the dataset generators
- `wordcloud.png` — generated example image
