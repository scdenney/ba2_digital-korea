"""
Korean Sentiment Preprocessing for Orange Data Mining (Windows)

Same as the Mac version but without auto-install. Before using this in
Orange, install kiwipiepy from a terminal:

    pip install kiwipiepy

Tokenizes Korean tweets with Kiwi and keeps content-word morphemes
(NNG, NNP, VA, VV) of length >= 2. Use in the Week 9 Orange workflow:

  File → Corpus → Python Script (this file)
                → Corpus (re-map text feature to processed_text)
                → Sentiment Analysis (Custom Dictionary: positive.txt + negative.txt)
                → Box Plot
"""

import re
import pandas as pd
from Orange.data import Domain, StringVariable
from kiwipiepy import Kiwi

kiwi = Kiwi()

# ===== CONFIGURATION =====
TEXT_COLUMN = 'text'  # <<< CHANGE to match your corpus column name

NOUN_TAGS = {'NNG', 'NNP'}


def is_verb_or_adj(tag):
    """Match VA, VV, and their irregular variants (VA-I, VV-I, VV-R, etc.)."""
    return tag == 'VA' or tag == 'VV' or tag.startswith('VA-') or tag.startswith('VV-')


# ===== PREPROCESSING =====
def preprocess(text):
    if pd.isna(text):
        return ""
    text = re.sub(r'https?://\S+', '', str(text))
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'^RT\s*:?', '', text)
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
