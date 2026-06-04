"""
Korean + Hanja + Hanmun Text Preprocessing for Orange Data Mining (Mac).

For mixed-script historical corpora (Colonial Magazines, Kaebyok, older
newspapers). Each document is ROUTED by its Hanja density:

  * KOREAN / mixed  (Hanja share < HANMUN_THRESHOLD)
      Every Hanja is converted to its Hangul READING (學生 -> 학생) and the
      text is tokenized with Kiwi, keeping nouns. This is reading
      substitution, NOT translation of meaning.

  * HANMUN / Classical Chinese  (Hanja share >= HANMUN_THRESHOLD)
      Kiwi is a modern-Korean analyzer and cannot parse literary Chinese, so
      these documents are tokenized at the CHARACTER level — each Hanja is one
      token — with a Classical-Chinese function-word stoplist applied. They are
      marked text_type = "hanmun" so you can analyze them separately.

Output: two new columns on the corpus —
    processed_text   the tokens, space-joined
    text_type        "korean" or "hanmun"

Why route? ~31% of the Colonial Magazines corpus is 60%+ Hanja. Converting
those to readings and feeding them to Kiwi produces unsegmentable strings of
syllables, not analyzable Korean. The `language` column does not catch them
all, so we route on measured Hanja density instead.

Auto-installs `kiwipiepy` and `hanja` on first run.
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
install_package('hanja')
from kiwipiepy import Kiwi
import hanja

kiwi = Kiwi()

# ===== CONFIGURATION =====
TEXT_COLUMN = 'text'        # <<< CHANGE to match your corpus column name
HANMUN_THRESHOLD = 0.60     # Hanja share at/above which a doc is treated as Classical Chinese

# --- Korean branch settings ---
POS_TAGS = [
    'NNG',  # Common noun (일반명사)
    'NNP',  # Proper noun (고유명사)
    #'VV',  # Verb (동사)
    #'VA',  # Adjective (형용사)
    #'MAG', # Adverb (부사)
]
REMOVE_NUMBERS = True
MIN_TOKEN_LENGTH = 2

# Korean stopwords (Korean branch)
STOPWORDS = {
    '있다', '없다', '되다', '하다', '그', '저', '이', '것', '등', '및',
    '수', '때', '년', '월', '일', '더', '또', '즉', '통해', '위해'
}

# Classical-Chinese function words to drop in the HANMUN branch (허사 / particles,
# not content). Edit freely — this is the Hanmun equivalent of a stopword list.
HANMUN_STOPWORDS = set(
    "之 而 不 則 其 也 矣 乎 焉 者 以 於 于 所 乃 且 亦 即 既 故 "
    "哉 耳 歟 耶 邪 兮 諸 斯 蓋 凡 惟 唯".split()
)

# Document-frequency filter (applied across both branches)
MIN_DOC_FREQ = 0.01   # keep tokens appearing in >= 1% of documents
MAX_DOC_FREQ = 0.99   # keep tokens appearing in <= 99% of documents

# ===== CHAR HELPERS =====
def is_hanja(c):
    o = ord(c)
    return (0x3400 <= o <= 0x9FFF) or (0xF900 <= o <= 0xFAFF) or (0x20000 <= o <= 0x2FA1F)

def is_hangul(c):
    return 0xAC00 <= ord(c) <= 0xD7A3

def hanja_ratio(text):
    """Hanja share among Hanja+Hangul letters — used to route each document."""
    h = sum(1 for c in text if is_hanja(c))
    k = sum(1 for c in text if is_hangul(c))
    return h / (h + k) if (h + k) else 0.0

def strip_residual_hanja(text):
    """Blank out any rare Hanja with no Hangul reading (Korean branch safety net)."""
    return ''.join(' ' if is_hanja(c) else c for c in text)

def clean_light(text):
    if pd.isna(text):
        return ""
    text = str(text)
    text = re.sub(r'http[s]?://\S+', ' ', text)
    text = re.sub(r'\S+@\S+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# ===== BRANCHES =====
def preprocess_korean(text):
    text = hanja.translate(text, 'substitution')   # Hanja -> Hangul reading
    text = strip_residual_hanja(text)               # safety net
    out = []
    for t in kiwi.tokenize(text):
        w = t.form
        if t.tag not in POS_TAGS:
            continue
        if len(w) < MIN_TOKEN_LENGTH:
            continue
        if REMOVE_NUMBERS and w.isdigit():
            continue
        if w in STOPWORDS:
            continue
        out.append(w)
    return out

def preprocess_hanmun(text):
    # Classical Chinese: 1 Hanja = 1 token; drop function words.
    return [c for c in text if is_hanja(c) and c not in HANMUN_STOPWORDS]

def preprocess(text):
    text = clean_light(text)
    if not text:
        return "", "korean"
    if hanja_ratio(text) >= HANMUN_THRESHOLD:
        return ' '.join(preprocess_hanmun(text)), "hanmun"
    return ' '.join(preprocess_korean(text)), "korean"

# ===== PROCESS DATA =====
try:
    text_data = in_data.documents
except AttributeError:
    text_column_index = in_data.domain.index(TEXT_COLUMN)
    text_data = [str(row[text_column_index]) for row in in_data]

results = [preprocess(text) for text in text_data]
processed = [r[0] for r in results]
text_types = [r[1] for r in results]

# ===== DOCUMENT FREQUENCY FILTERING =====
if MIN_DOC_FREQ > 0 or MAX_DOC_FREQ < 1.0:
    from collections import Counter

    word_doc_counts = Counter()
    for doc in processed:
        word_doc_counts.update(set(doc.split()))

    total_docs = len(processed)

    filtered_processed = []
    for doc in processed:
        kept_words = [
            w for w in doc.split()
            if MIN_DOC_FREQ <= word_doc_counts[w] / total_docs <= MAX_DOC_FREQ
        ]
        filtered_processed.append(' '.join(kept_words))

    processed = filtered_processed
    print(f"✓ Applied document frequency filtering (keep {MIN_DOC_FREQ:.0%}–{MAX_DOC_FREQ:.0%})")

# ===== OUTPUT =====
var_proc = StringVariable('processed_text')
var_type = StringVariable('text_type')
new_domain = Domain(
    in_data.domain.attributes,
    in_data.domain.class_vars,
    in_data.domain.metas + (var_proc, var_type)
)

out_data = in_data.transform(new_domain)
with out_data.unlocked():
    out_data.get_column(var_proc)[:] = processed
    out_data.get_column(var_type)[:] = text_types

n_hanmun = text_types.count("hanmun")
print(f"✓ Processed {len(processed)} documents "
      f"({len(processed) - n_hanmun} Korean, {n_hanmun} Hanmun/Classical Chinese)")
