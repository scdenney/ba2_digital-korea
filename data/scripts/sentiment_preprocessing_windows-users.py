"""
Korean SENTIMENT Preprocessing for Orange Data Mining (Windows)

Same as the Mac version but without auto-install. If you see an error
importing kiwipiepy, open a terminal and run:
    pip install kiwipiepy

See the Mac version's header for full documentation of what this script does
differently from the standard preprocessing script. In short:

  - POS tags include VA (adjectives) and VV (verbs) for sentiment
  - Verbs/adjectives output in citation form (stem + 다)
  - Noun + 하/XSV reconstructed as "noun하다" to match KNU citation forms
  - No stopword removal, no document frequency filtering
"""

import re
import pandas as pd
from Orange.data import Table, Domain, StringVariable
from kiwipiepy import Kiwi

kiwi = Kiwi()

# ===== CONFIGURATION =====
TEXT_COLUMN = 'text'  # <<< CHANGE to match your corpus column name

SENTIMENT_POS = {'NNG', 'NNP', 'VA', 'VV'}
MIN_TOKEN_LENGTH = 1

# ===== CLEANING =====
def clean_text(text):
    if pd.isna(text):
        return ""
    text = str(text)
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'^RT\s*:?', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# ===== SENTIMENT-AWARE TOKENIZATION =====
def preprocess_sentiment(text):
    text = clean_text(text)
    if not text:
        return ""

    tokens = list(kiwi.tokenize(text))
    output = []
    i = 0

    while i < len(tokens):
        t = tokens[i]

        # Noun + 하/XSV → "noun하다"
        if (t.tag in ('NNG', 'NNP')
                and i + 1 < len(tokens)
                and tokens[i + 1].form == '하'
                and tokens[i + 1].tag in ('XSV', 'XSA')):
            output.append(t.form + '하다')
            i += 2
            continue

        # Verb or adjective → citation form (stem + 다)
        if t.tag in ('VV', 'VA'):
            lemma = t.form + '다'
            if len(lemma) >= MIN_TOKEN_LENGTH:
                output.append(lemma)
            i += 1
            continue

        # Plain noun
        if t.tag in ('NNG', 'NNP'):
            if len(t.form) >= MIN_TOKEN_LENGTH and not t.form.isdigit():
                output.append(t.form)
            i += 1
            continue

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

sample = next((p for p in processed if p), "")
print(f"Processed {len(processed)} documents for sentiment analysis")
print(f"Sample tokens: {sample[:200]}")
