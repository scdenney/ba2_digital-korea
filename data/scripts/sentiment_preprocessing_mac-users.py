"""
Korean SENTIMENT Preprocessing for Orange Data Mining (Mac)

Tokenizes with Kiwi, keeps content POS tags (NNG, NNP, VA, VV), and outputs
lemmas in citation form so they match sentiment dictionary entries like
the KNU lexicon, positive.txt, and negative.txt.

KEY DIFFERENCES from the standard preprocessing script:

1. POS tags include VA (adjectives) and VV (verbs) by default
   — sentiment lives in evaluative adjectives and action verbs, not just nouns

2. Verbs and adjectives are output in CITATION FORM (stem + 다)
   — KNU entries are like "행복하다", "기쁘다", "어렵다" (dictionary forms)
   — Kiwi gives us the stem "행복하", "기쁘", "어렵"; we add 다 to match

3. Noun + 하 (XSV/XSA) compounds are reconstructed as "noun하다"
   — Kiwi tokenizes "극복하다" as ["극복"/NNG, "하"/XSV, "다"/EF]
   — We reassemble this to "극복하다" so it matches the KNU entry

4. NO stopword removal, NO document frequency filtering
   — Sentiment analysis is sensitive to function words (for negation)
   — High-frequency words like "함께" (together) ARE meaningful sentiment
"""

import subprocess
import sys
import re
import pandas as pd
from Orange.data import Table, Domain, StringVariable

# ===== AUTO-INSTALL (Mac only) =====
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

kiwi = Kiwi()

# ===== CONFIGURATION =====
TEXT_COLUMN = 'text'  # <<< CHANGE to match your corpus column name

# POS tags to keep for sentiment analysis
# NNG = common noun, NNP = proper noun, VA = adjective, VV = verb
# Adjectives and verbs are essential — they carry most evaluative sentiment.
SENTIMENT_POS = {'NNG', 'NNP', 'VA', 'VV'}

MIN_TOKEN_LENGTH = 1  # Keep short tokens; some sentiment words are short

# ===== CLEANING =====
def clean_text(text):
    """Minimal cleaning: remove URLs, mentions, retweet markers."""
    if pd.isna(text):
        return ""
    text = str(text)
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'\S+@\S+', '', text)  # email addresses
    text = re.sub(r'@\w+', '', text)     # @mentions
    text = re.sub(r'^RT\s*:?', '', text) # retweet markers
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# ===== SENTIMENT-AWARE TOKENIZATION =====
def preprocess_sentiment(text):
    """
    Tokenize with Kiwi, filter to content POS, and output in citation form
    so tokens match KNU / positive.txt / negative.txt entries.
    """
    text = clean_text(text)
    if not text:
        return ""

    tokens = list(kiwi.tokenize(text))
    output = []
    i = 0

    while i < len(tokens):
        t = tokens[i]

        # Pattern 1: Noun + 하/XSV/XSA → reconstruct as "noun하다"
        # e.g. 극복/NNG + 하/XSV + 다/EF → output "극복하다"
        # This matches compound verbs/adjectives that KNU stores in citation form.
        if (t.tag in ('NNG', 'NNP')
                and i + 1 < len(tokens)
                and tokens[i + 1].form == '하'
                and tokens[i + 1].tag in ('XSV', 'XSA')):
            output.append(t.form + '하다')
            i += 2  # consume both the noun and the 하
            continue

        # Pattern 2: Verb (VV) or Adjective (VA) → citation form (stem + 다)
        # Kiwi gives the stem; adding 다 produces the dictionary form.
        # e.g. 기쁘/VA → 기쁘다, 이기/VV → 이기다, 크/VA → 크다
        if t.tag in ('VV', 'VA'):
            lemma = t.form + '다'
            if len(lemma) >= MIN_TOKEN_LENGTH:
                output.append(lemma)
            i += 1
            continue

        # Pattern 3: Plain nouns (NNG, NNP) that weren't consumed above
        if t.tag in ('NNG', 'NNP'):
            if len(t.form) >= MIN_TOKEN_LENGTH and not t.form.isdigit():
                output.append(t.form)
            i += 1
            continue

        # Everything else (particles, endings, pronouns, etc.) is skipped.
        # This filters out the 저는 / 지지 / 없다 kind of noise automatically.
        i += 1

    return ' '.join(output)

# ===== PROCESS DATA =====
try:
    text_data = in_data.documents
except AttributeError:
    text_column_index = in_data.domain.index(TEXT_COLUMN)
    text_data = [str(row[text_column_index]) for row in in_data]

processed = [preprocess_sentiment(text) for text in text_data]

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

# Sanity check: show a sample of the first processed document
sample = next((p for p in processed if p), "")
print(f"✓ Processed {len(processed)} documents for sentiment analysis")
print(f"  Sample tokens: {sample[:200]}")
print(f"  Connect this to Score Documents with positive.txt / negative.txt")
