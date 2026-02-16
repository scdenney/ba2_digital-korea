"""
Korean Text Preprocessing for Orange Data Mining (Windows)
Requires kiwipiepy pre-installed, then does POS-based tokenization and filtering.
"""

import re
import pandas as pd
from Orange.data import Table, Domain, StringVariable
from kiwipiepy import Kiwi

kiwi = Kiwi()

# ===== CONFIGURATION =====
TEXT_COLUMN = 'full_text'  # <<< CHANGE to match your corpus column name

# POS tags to keep — uncomment tags you want to include
POS_TAGS = [
    'NNG',  # Common noun (일반명사)
    'NNP',  # Proper noun (고유명사)
    #'VV',  # Verb (동사)
    #'VA',  # Adjective (형용사)
    #'MAG', # Adverb (부사)
]

REMOVE_NUMBERS = True
MIN_TOKEN_LENGTH = 2
MIN_DOC_FREQ = 0.1   # Minimum proportion of documents a word must appear in (10%)
MAX_DOC_FREQ = 0.9   # Maximum proportion of documents a word can appear in (90%)

STOPWORDS = {
    '있다', '없다', '되다', '하다', '그', '저', '이', '것', '등', '및',
    '수', '때', '년', '월', '일', '더', '또', '즉', '통해', '위해'
}

# ===== PREPROCESSING =====
def clean_text(text):
    if pd.isna(text):
        return ""
    text = str(text)
    text = re.sub(r'http[s]?://\S+', '', text)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'[^\w\s\u3131-\u3163\uac00-\ud7a3\u1100-\u11ff]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess(text):
    text = clean_text(text)
    if not text:
        return ""

    tokens = kiwi.tokenize(text)
    morphemes = [token.form for token in tokens if token.tag in POS_TAGS]

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

# ===== PROCESS DATA =====
try:
    text_data = in_data.documents
except AttributeError:
    text_column_index = in_data.domain.index(TEXT_COLUMN)
    text_data = [str(row[text_column_index]) for row in in_data]

processed = [preprocess(text) for text in text_data]

# ===== DOCUMENT FREQUENCY FILTERING =====
if MIN_DOC_FREQ > 0 or MAX_DOC_FREQ < 1.0:
    from collections import Counter

    word_doc_counts = Counter()
    for doc in processed:
        unique_words = set(doc.split())
        word_doc_counts.update(unique_words)

    total_docs = len(processed)

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
