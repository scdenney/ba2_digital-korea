"""
Korean Sentiment Preprocessing for Orange Data Mining (Mac)

Tokenizes Korean tweets with Kiwi (a standard morphological analyzer)
and keeps content-word morphemes — nouns (NNG/NNP), verbs (VV), and
adjectives (VA) — that are at least 2 characters long.

Use this in the Week 9 Orange workflow:

  File → Corpus → Python Script (this file)
                → Corpus (re-map text feature to processed_text)
                → Sentiment Analysis (Method = Custom Dictionary,
                                      load positive.txt + negative.txt
                                      from data/sentiment_dic/)
                → Box Plot (subgroup: period3)

Why Kiwi? Korean is agglutinative — 행복합니다 is one "word" by whitespace
tokenization but contains the stem 행복 plus inflectional suffixes. Kiwi
splits these apart so Orange can match individual tokens against the KNU
sentiment dictionary.
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

# Nouns we keep as-is; verbs and adjectives (including irregular -I/-R
# variants) are converted to their citation form by adding 다, so they
# match KNU dictionary entries like 기쁘다, 고맙다, 행복하다.
NOUN_TAGS = {'NNG', 'NNP'}


def is_verb_or_adj(tag):
    """Match VA, VV, and their irregular variants (VA-I, VV-I, VV-R, etc.)."""
    return tag == 'VA' or tag == 'VV' or tag.startswith('VA-') or tag.startswith('VV-')


# ===== PREPROCESSING =====
def preprocess(text):
    if pd.isna(text):
        return ""
    # Minimal cleanup: strip URLs, mentions, RT markers
    text = re.sub(r'https?://\S+', '', str(text))
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'^RT\s*:?', '', text)
    # Tokenize with Kiwi; keep content words (length >= 2)
    out = []
    for t in kiwi.tokenize(text):
        if len(t.form) < 2:
            continue
        if t.tag in NOUN_TAGS:
            out.append(t.form)
        elif is_verb_or_adj(t.tag):
            # Citation form = stem + 다 (matches KNU dictionary entries)
            out.append(t.form + '다')
    return ' '.join(out)

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
