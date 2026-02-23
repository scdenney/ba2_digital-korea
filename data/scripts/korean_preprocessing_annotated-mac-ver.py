"""
Korean Text Preprocessing for Orange Data Mining (Mac)
Auto-installs kiwipiepy, then does POS-based tokenization and filtering.

HOW TO USE:
  - In Orange, connect your Corpus to a Python Script widget
  - Paste this entire script into the widget
  - The output is your original data with a new 'processed_text' column
"""

import subprocess
import sys
import re
import pandas as pd
from Orange.data import Table, Domain, StringVariable

# ===== AUTO-INSTALL =====
# This checks whether kiwipiepy is installed on your machine.
# If not, it installs it automatically so you don't have to use the terminal.
def install_package(package):
    try:
        __import__(package)
        return True
    except ImportError:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
        print(f"✓ {package} installed")
        return True

install_package('kiwipiepy')
from kiwipiepy import Kiwi

# Initialize the Kiwi morphological analyzer.
# This is the tool that breaks Korean text into morphemes (형태소) —
# the smallest meaningful units of language (stems, particles, endings, etc.)
kiwi = Kiwi()

# ===== CONFIGURATION =====
# Change this to match the column name that holds your text in the Corpus.
TEXT_COLUMN = 'full_text'

# --- POS (Part-of-Speech) Tag Filter ---
# Kiwi assigns a POS tag to each morpheme it finds.
# We list the tags we want to KEEP here. Everything else gets discarded.
# Think of this as telling the script: "I only care about nouns."
# Uncomment VV, VA, or MAG if you also want verbs, adjectives, or adverbs.
POS_TAGS = [
    'NNG',  # Common noun (일반명사)  e.g., 사회, 경제, 학생
    'NNP',  # Proper noun (고유명사)  e.g., 서울, 한국
    #'VV',  # Verb (동사)            e.g., 가다, 먹다
    #'VA',  # Adjective (형용사)      e.g., 크다, 좋다
    #'MAG', # Adverb (부사)           e.g., 매우, 아주
]

REMOVE_NUMBERS = True     # Drop any token that is purely digits
MIN_TOKEN_LENGTH = 2      # Drop single-character tokens (often noise)

# --- Document Frequency Thresholds ---
# These filter words based on how many documents they appear in.
# MIN_DOC_FREQ = 0.1 means: drop words appearing in fewer than 10% of documents
#   (too rare to reveal patterns)
# MAX_DOC_FREQ = 0.9 means: drop words appearing in more than 90% of documents
#   (too common to be informative — similar logic to TF-IDF's downweighting)
MIN_DOC_FREQ = 0.1
MAX_DOC_FREQ = 0.9

# --- Stopwords ---
# High-frequency function words or light verbs that aren't useful for analysis.
# Kiwi's morphological analysis already strips particles (이/가/을/를),
# but these words still slip through because they are tagged as nouns or verbs.
STOPWORDS = {
    '있다', '없다', '되다', '하다', '그', '저', '이', '것', '등', '및',
    '수', '때', '년', '월', '일', '더', '또', '즉', '통해', '위해'
}

# ===== PREPROCESSING FUNCTIONS =====

def clean_text(text):
    """
    Basic cleaning BEFORE morphological analysis.
    Removes URLs, emails, mentions, and non-Korean/non-alphanumeric characters.
    This gives Kiwi cleaner input to work with.
    """
    if pd.isna(text):
        return ""
    text = str(text)
    text = re.sub(r'http[s]?://\S+', '', text)                              # URLs
    text = re.sub(r'\S+@\S+', '', text)                                      # emails
    text = re.sub(r'@\w+', '', text)                                         # @mentions
    text = re.sub(r'[^\w\s\u3131-\u3163\uac00-\ud7a3\u1100-\u11ff]', ' ', text)  # keep only Korean + alphanumeric
    text = re.sub(r'\s+', ' ', text).strip()                                 # collapse whitespace
    return text

def preprocess(text):
    """
    The main pipeline for a single document:
      1. Clean the raw text
      2. Run Kiwi's morphological analysis (형태소 분석)
         — this is the Korean equivalent of lemmatization.
         Kiwi decomposes each word into morphemes and returns their base forms.
         e.g., 학생들이 → 학생/NNG + 들/XSN + 이/JKS
      3. Keep only morphemes whose POS tag is in our POS_TAGS list
      4. Apply stopword, length, and number filters

    The result is a space-separated string of clean base-form tokens,
    ready to be turned into a document-term matrix (via Bag of Words).
    """
    text = clean_text(text)
    if not text:
        return ""

    # Kiwi tokenize: returns a list of Token objects with .form and .tag attributes
    tokens = kiwi.tokenize(text)

    # Keep only the base forms (.form) of morphemes with our target POS tags
    morphemes = [token.form for token in tokens if token.tag in POS_TAGS]

    # Apply additional filters
    filtered = []
    for w in morphemes:
        if w in STOPWORDS:
            continue
        if len(w) < MIN_TOKEN_LENGTH:
            continue
        if REMOVE_NUMBERS and w.isdigit():
            continue
        filtered.append(w)

    return ' '.join(filtered)

# ===== PROCESS THE CORPUS =====
# Orange passes your data in as `in_data`.
# We try to grab the text from the Corpus's .documents attribute first;
# if that fails, we fall back to reading the column by name.
try:
    text_data = in_data.documents
except AttributeError:
    text_column_index = in_data.domain.index(TEXT_COLUMN)
    text_data = [str(row[text_column_index]) for row in in_data]

# Run preprocessing on every document
processed = [preprocess(text) for text in text_data]

# ===== DOCUMENT FREQUENCY FILTERING =====
# After tokenizing, we do a second pass to remove words that are
# too rare or too common across the entire corpus.
if MIN_DOC_FREQ > 0 or MAX_DOC_FREQ < 1.0:
    from collections import Counter

    # Count how many documents each word appears in (not how many times — just presence)
    word_doc_counts = Counter()
    for doc in processed:
        unique_words = set(doc.split())   # set() so each word counted once per doc
        word_doc_counts.update(unique_words)

    total_docs = len(processed)

    # Filter each document's tokens against the frequency thresholds
    filtered_processed = []
    for doc in processed:
        words = doc.split()
        kept_words = [
            w for w in words
            if word_doc_counts[w] / total_docs >= MIN_DOC_FREQ
            and word_doc_counts[w] / total_docs <= MAX_DOC_FREQ
        ]
        filtered_processed.append(' '.join(kept_words))

    processed = filtered_processed
    print(f"✓ Applied document frequency filtering (keep {MIN_DOC_FREQ:.0%}–{MAX_DOC_FREQ:.0%})")

# ===== OUTPUT =====
# We add a new metadata column called 'processed_text' to the Orange table.
# This column holds the cleaned, tokenized text for each document.
# Downstream, you connect this to a Bag of Words widget (set to use 'processed_text')
# to build your document-term matrix.
new_var = StringVariable('processed_text')
new_domain = Domain(
    in_data.domain.attributes,
    in_data.domain.class_vars,
    in_data.domain.metas + (new_var,)
)

out_data = in_data.transform(new_domain)
with out_data.unlocked():
    out_data.get_column(new_var)[:] = processed

print(f"✓ Processed {len(processed)} documents")
