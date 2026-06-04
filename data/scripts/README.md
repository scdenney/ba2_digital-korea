# Scripts

Python scripts for Orange Data Mining Python Script widgets, plus R scripts for standalone use in RStudio.

## Student-facing scripts

### For Weeks 3–7 (BoW, clustering, topic modeling)

| File | Purpose |
|------|---------|
| [`custom_preprocessing_mac-users.py`](custom_preprocessing_mac-users.py) | Kiwi tokenization keeping NNG/NNP (nouns) by default. Auto-installs `kiwipiepy`. Use in Orange's Python Script widget for any task where you want bag-of-words style output. |
| [`custom_preprocessing_windows-users.py`](custom_preprocessing_windows-users.py) | Same as above, but assumes `kiwipiepy` is already installed (`pip install kiwipiepy` in a terminal). |
| [`korean_preprocessing_annotated-mac-ver.py`](korean_preprocessing_annotated-mac-ver.py) | Line-by-line annotated version of the Mac script. Read this if you want to understand what each step does. |

### For Hanmun-mixed corpora (Colonial Magazines, Kaebyok, older newspapers)

For text with heavy Hanja (Chinese characters). These convert each Hanja to its Korean **reading** (學生 → 학생 — a reading, *not* a meaning translation), tokenize with Kiwi, and route Classical-Chinese (Hanmun) articles to character-level tokenization. Output adds a `text_type` column (`korean` / `hanmun`) so you can analyze the two separately.

| File | Purpose |
|------|---------|
| [`hanja_preprocessing_mac-users.py`](hanja_preprocessing_mac-users.py) | Orange Python Script widget (Mac). Auto-installs `kiwipiepy` and `hanja`. |
| [`hanja_preprocessing_windows-users.py`](hanja_preprocessing_windows-users.py) | Same, Windows (assumes `pip install kiwipiepy hanja`). |
| [`hanja_preprocessing.R`](hanja_preprocessing.R) | RStudio version (reticulate → Kiwi + `hanja`). For students preprocessing in R. |

### For Week 9 (sentiment analysis)

| File | Purpose |
|------|---------|
| [`sentiment_preprocessing_mac-users.py`](sentiment_preprocessing_mac-users.py) | Kiwi tokenization keeping content words (NNG, NNP, VA, VV) of length ≥ 2. Paste into Orange's **Python Script** widget between Corpus and Sentiment Analysis to preprocess Korean tweets. Auto-installs `kiwipiepy`. |
| [`sentiment_preprocessing_windows-users.py`](sentiment_preprocessing_windows-users.py) | Same as above, Windows version (assumes `kiwipiepy` is already installed). |

These pair with `positive.txt` and `negative.txt` from [`../sentiment_dic/`](../sentiment_dic/) loaded into the Sentiment Analysis widget's Custom Dictionary option.

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
- `generate_sentiment_demo.py` — rebuilds `interactive/sentiment_data.json` for the Week 9 interactive using the same pipeline students run in Orange (Kiwi NNG/NNP/VV/VA + KNU `positive.txt`/`negative.txt` via Custom Dictionary)
- `sentence_splitter.py` — utility used by the dataset generators
- `wordcloud.png` — generated example image
