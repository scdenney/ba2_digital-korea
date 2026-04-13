"""
Korean Sentiment Preprocessing for Orange Data Mining (Windows)

Same as custom_preprocessing_windows-users.py but with POS tags set for
sentiment analysis: keeps nouns, verbs, and adjectives (NNG, NNP, VA, VV).

Assumes kiwipiepy is already installed. If not, open a terminal and run:
    pip install kiwipiepy
"""

import re
import pandas as pd
from Orange.data import Table, Domain, StringVariable
from kiwipiepy import Kiwi

kiwi = Kiwi()

# ===== CONFIGURATION =====
TEXT_COLUMN = 'text'  # <<< CHANGE to match your corpus column name

# POS tags to keep — nouns, verbs, and adjectives carry sentiment
POS_TAGS = [
    'NNG',  # Common noun (일반명사)
    'NNP',  # Proper noun (고유명사)
    'VV',   # Verb (동사)
    'VA',   # Adjective (형용사)
    #'MAG', # Adverb (부사) — uncomment if you want intensifiers
]

REMOVE_NUMBERS = True
MIN_TOKEN_LENGTH = 2

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

    filtered = [
        w for w in morphemes
        if len(w) >= MIN_TOKEN_LENGTH and not (REMOVE_NUMBERS and w.isdigit())
    ]

    return ' '.join(filtered)

# ===== PROCESS DATA =====
try:
    text_data = in_data.documents
except AttributeError:
    text_column_index = in_data.domain.index(TEXT_COLUMN)
    text_data = [str(row[text_column_index]) for row in in_data]

processed = [preprocess(text) for text in text_data]

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
