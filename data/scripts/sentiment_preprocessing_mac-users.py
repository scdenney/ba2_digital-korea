"""
Korean Sentiment Preprocessing for Orange Data Mining (Mac)

Tokenizes tweets with Kiwi and extracts content-word stems (nouns, verbs,
adjectives) for sentiment scoring. The output tokens match the stem-indexed
dictionaries on the course Data page:
  - positive_stems.txt
  - negative_stems.txt
  - SentiWord_Dict_stems.txt (full KNU with -2 to +2 scores, for R use)

Use this with Orange's Sentiment Analysis widget:
  File → Corpus → Python Script → Corpus (re-map) → Sentiment Analysis → Box Plot
"""

import subprocess
import sys
import re
import pandas as pd
from Orange.data import Domain, StringVariable

# ===== AUTO-INSTALL kiwipiepy =====
try:
    import kiwipiepy
except ImportError:
    print("Installing kiwipiepy...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "kiwipiepy", "--quiet"])

from kiwipiepy import Kiwi
kiwi = Kiwi()

# ===== CONFIGURATION =====
TEXT_COLUMN = 'text'  # <<< CHANGE to match your corpus column name

# Content-word POS tags: nouns, proper nouns, verbs, adjectives.
# These carry the sentiment. Particles, endings, pronouns are filtered out.
SENTIMENT_POS = {'NNG', 'NNP', 'VA', 'VV'}

# ===== PREPROCESSING =====
def preprocess(text):
    if pd.isna(text):
        return ""
    # Minimal cleanup: strip URLs, mentions, RT markers
    text = re.sub(r'https?://\S+', '', str(text))
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'^RT\s*:?', '', text)
    # Tokenize and keep content-word stems (length >= 2)
    tokens = kiwi.tokenize(text)
    stems = [t.form for t in tokens
             if t.tag in SENTIMENT_POS and len(t.form) >= 2]
    return ' '.join(stems)

# ===== PROCESS DATA =====
try:
    text_data = in_data.documents
except AttributeError:
    idx = in_data.domain.index(TEXT_COLUMN)
    text_data = [str(row[idx]) for row in in_data]

processed = [preprocess(t) for t in text_data]

# ===== OUTPUT =====
new_var = StringVariable('processed_text')
new_domain = Domain(
    in_data.domain.attributes,
    in_data.domain.class_vars,
    in_data.domain.metas + (new_var,),
)
out_data = in_data.transform(new_domain)
with out_data.unlocked():
    out_data.get_column(new_var)[:] = processed

print(f"Processed {len(processed)} documents")
print(f"Sample: {next((p for p in processed if p), '')[:150]}")
