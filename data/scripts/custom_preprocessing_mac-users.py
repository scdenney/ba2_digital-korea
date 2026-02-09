"""
Minimal Korean Text Preprocessing for Orange Data Mining
Auto-installs kiwipiepy and does Korean-specific POS tagging
"""

import subprocess
import sys
import re
import pandas as pd
from Orange.data import Table, Domain, StringVariable

# ===== AUTO-INSTALL =====
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

# Initialize Kiwi
kiwi = Kiwi()

# ===== CONFIGURATION =====
TEXT_COLUMN = 'full_text'  # <<< CHANGE to your column name

# Which POS tags to keep (nouns, verbs, adjectives, adverbs)
POS_TAGS = ['NNG', 'NNP'] # , 'VV', 'VA', 'MAG'

# Additional filtering options
REMOVE_NUMBERS = True  # Remove all numeric tokens
MIN_TOKEN_LENGTH = 2   # Minimum character length for tokens
MIN_DOC_FREQ = 1       # Minimum times a word must appear across all documents
MAX_DOC_FREQ = 0.9     # Maximum proportion of documents a word can appear in (0.9 = 90%)

# Korean stopwords
STOPWORDS = {
    '있다', '없다', '되다', '하다', '그', '저', '이', '것', '등', '및',
    '수', '때', '년', '월', '일', '더', '또', '즉', '통해', '위해'
}

# ===== PREPROCESSING =====
def clean_text(text):
    if pd.isna(text):
        return ""
    text = str(text)
    text = re.sub(r'http[s]?://\S+', '', text)  # URLs
    text = re.sub(r'\S+@\S+', '', text)  # Emails
    text = re.sub(r'@\w+', '', text)  # Mentions
    text = re.sub(r'[^\w\s\u3131-\u3163\uac00-\ud7a3\u1100-\u11ff]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess(text):
    text = clean_text(text)
    if not text:
        return ""
    
    # Kiwi tokenization with POS filtering
    tokens = kiwi.tokenize(text)
    morphemes = [token.form for token in tokens if token.tag in POS_TAGS]
    
    # Remove stopwords and apply filters
    filtered = []
    for w in morphemes:
        if w in STOPWORDS:
            continue
        if len(w) < MIN_TOKEN_LENGTH:
            continue
        if REMOVE_NUMBERS and w.isdigit():
            continue
        filtered.append(w)
    
    result = ' '.join(filtered)
    return result

# ===== PROCESS DATA =====
# Get text data from Orange
try:
    text_data = in_data.documents
except AttributeError:
    text_column_index = in_data.domain.index(TEXT_COLUMN)
    text_data = [str(row[text_column_index]) for row in in_data]

# Process all texts
processed = [preprocess(text) for text in text_data]

# ===== DOCUMENT FREQUENCY FILTERING =====
if MIN_DOC_FREQ > 1 or MAX_DOC_FREQ < 1.0:
    from collections import Counter
    
    # Count how many documents each word appears in
    word_doc_counts = Counter()
    for doc in processed:
        unique_words = set(doc.split())
        word_doc_counts.update(unique_words)
    
    total_docs = len(processed)
    
    # Filter words based on document frequency
    filtered_processed = []
    for doc in processed:
        words = doc.split()
        kept_words = [
            w for w in words 
            if word_doc_counts[w] >= MIN_DOC_FREQ 
            and word_doc_counts[w] / total_docs <= MAX_DOC_FREQ
        ]
        filtered_processed.append(' '.join(kept_words))
    
    processed = filtered_processed
    print(f"✓ Applied document frequency filtering")

# Create new Orange table with processed text column
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