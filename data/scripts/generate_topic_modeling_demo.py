"""
Generate the Week 10 topic-modeling interactive artifacts.

Reads the full 67-book NIKH corpus, tokenizes with kiwipiepy (NNG/NNP nouns),
filters stopwords and document frequency, fits gensim LDA at several k values,
computes c_v coherence for each, picks a default k, and emits:
  - interactive/topic_modeling_data.json  (topic/coherence/doc-mixture data)
  - interactive/topic_modeling_ldavis.html (pyLDAvis at the chosen k)

Usage:
    python generate_topic_modeling_demo.py

Requires a Python 3.12 venv with: gensim, pyLDAvis, kiwipiepy, pandas, scikit-learn.
"""

import html
import json
import math
import re
import warnings
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis
from gensim import corpora
from gensim.models import CoherenceModel, LdaModel
from kiwipiepy import Kiwi

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ── Paths ─────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_DIR = SCRIPT_DIR.parent.parent
CORPUS_PATH = Path(
    "/home/buddleman/Documents/GitHub/resources/nlp_corpora/data/nikh/nikh_corpus.csv"
)
STOPWORDS_FILE = SCRIPT_DIR.parent / "stopwords_ko.txt"
JSON_OUT = REPO_DIR / "interactive" / "topic_modeling_data.json"
LDAVIS_OUT = REPO_DIR / "interactive" / "topic_modeling_ldavis.html"

# ── Preprocessing settings ────────────────────────────────────────────
NOUN_TAGS = {"NNG", "NNP"}
MIN_TOKEN_LEN = 2
MIN_DOC_FREQ = 0.05        # words in <5% of books are dropped
MAX_DOC_FREQ_PROP = 0.95   # words in >95% of books are dropped

# ── LDA settings ──────────────────────────────────────────────────────
K_VALUES = [3, 4, 5, 6, 7, 8, 10, 12]
DEFAULT_K = 5              # anchor for the exported topics + LDAvis
RANDOM_SEED = 20260420
TOP_WORDS_PER_TOPIC = 15
LDA_PASSES = 15
LDA_ITERATIONS = 200


# ── Era collapsing ────────────────────────────────────────────────────
# The source corpus has 5 period labels. For the 3-era demo view we
# collapse them:
#   Late Choson (1895-1908) + Colonial (1940)         -> Colonial
#   Postwar (1946-1963) + Authoritarian (1973-1991)   -> Authoritarian
#   Democratic (1995-2016)                            -> Democratic
def assign_era(period: str) -> str:
    if period in ("Colonial", "Late Choson"):
        return "Colonial"
    if period == "Democratic":
        return "Democratic"
    return "Authoritarian"


ERA_ORDER = {"Colonial": 0, "Authoritarian": 1, "Democratic": 2}


def load_stopwords() -> set:
    words = {
        "있다", "없다", "되다", "하다", "그", "저", "이", "것", "등", "및",
        "때", "수", "또", "즉", "또는", "그리고",
    }
    if STOPWORDS_FILE.exists():
        with open(STOPWORDS_FILE, encoding="utf-8") as f:
            for line in f:
                w = line.strip()
                if w:
                    words.add(w)
    return words


def tokenize(kiwi: Kiwi, text: str, stopwords: set) -> list:
    tokens = []
    for t in kiwi.tokenize(text):
        if t.tag not in NOUN_TAGS:
            continue
        form = t.form
        if len(form) < MIN_TOKEN_LEN:
            continue
        if form.isdigit():
            continue
        if form in stopwords:
            continue
        tokens.append(form)
    return tokens


def short_title(title: str, book_id: str) -> str:
    """Produce a compact label for table display."""
    t = re.sub(r"\s+", " ", str(title)).strip()
    if len(t) > 30:
        t = t[:28] + "…"
    return t or book_id


def main() -> None:
    print(f"Loading corpus from {CORPUS_PATH} ...")
    corpus = pd.read_csv(CORPUS_PATH)
    print(f"  corpus: {len(corpus)} rows, columns = {list(corpus.columns)}")

    # some rows may be empty; drop and dedupe on book_id
    corpus = corpus.dropna(subset=["full_text", "book_id"])
    corpus = corpus.drop_duplicates(subset=["book_id"]).reset_index(drop=True)
    corpus["era"] = corpus["period"].apply(assign_era)
    corpus = corpus.sort_values(["era", "year"]).reset_index(drop=True)
    print(f"  after cleanup: {len(corpus)} books")

    era_counts = corpus["era"].value_counts().to_dict()
    print(f"  era breakdown: {era_counts}")

    # ── Tokenize ──────────────────────────────────────────────────────
    print("\nTokenizing with kiwipiepy ...")
    stopwords = load_stopwords()
    kiwi = Kiwi()

    tokenized = []
    for i, row in corpus.iterrows():
        toks = tokenize(kiwi, str(row["full_text"]), stopwords)
        tokenized.append(toks)
        if (i + 1) % 10 == 0 or i == len(corpus) - 1:
            print(f"  [{i+1}/{len(corpus)}] {row['book_id']}: {len(toks)} tokens")

    corpus["n_tokens"] = [len(t) for t in tokenized]

    # ── Build dictionary + BoW with doc-freq filtering ────────────────
    print("\nBuilding dictionary ...")
    dictionary = corpora.Dictionary(tokenized)
    before = len(dictionary)
    dictionary.filter_extremes(
        no_below=max(2, int(MIN_DOC_FREQ * len(corpus))),
        no_above=MAX_DOC_FREQ_PROP,
        keep_n=20000,
    )
    after = len(dictionary)
    print(f"  vocabulary: {before} → {after} after doc-freq filter")

    bow_corpus = [dictionary.doc2bow(toks) for toks in tokenized]
    total_kept = sum(sum(c for _, c in doc) for doc in bow_corpus)
    print(f"  total tokens after filter: {total_kept}")

    # ── Fit LDA at each k + c_v coherence ─────────────────────────────
    print("\nFitting LDA at multiple k and scoring coherence ...")
    coherence_rows = []
    models = {}
    for k in K_VALUES:
        lda = LdaModel(
            corpus=bow_corpus,
            id2word=dictionary,
            num_topics=k,
            random_state=RANDOM_SEED,
            passes=LDA_PASSES,
            iterations=LDA_ITERATIONS,
            alpha="auto",
            eta="auto",
            per_word_topics=False,
        )
        cm = CoherenceModel(
            model=lda,
            texts=tokenized,
            dictionary=dictionary,
            coherence="c_v",
            processes=1,
        )
        score = float(cm.get_coherence())
        coherence_rows.append({"k": k, "coherence_cv": round(score, 4)})
        models[k] = lda
        print(f"  k={k:>2}  c_v = {score:.4f}")

    best_row = max(coherence_rows, key=lambda r: r["coherence_cv"])
    print(f"\nBest k by c_v: k={best_row['k']} (coherence={best_row['coherence_cv']})")
    print(f"Exporting topics + LDAvis at DEFAULT_K = {DEFAULT_K}")

    lda = models[DEFAULT_K]

    # ── Extract top words per topic ───────────────────────────────────
    topics_json = []
    for t in range(DEFAULT_K):
        top = lda.show_topic(t, topn=TOP_WORDS_PER_TOPIC)
        topics_json.append({
            "topic_id": t,
            "top_words": [{"word": w, "weight": round(float(p), 5)} for w, p in top],
        })

    # ── Document-topic mixtures (theta) ───────────────────────────────
    doc_mix = []
    for i, row in corpus.iterrows():
        dist = lda.get_document_topics(bow_corpus[i], minimum_probability=0.0)
        weights = [0.0] * DEFAULT_K
        for t, p in dist:
            weights[t] = round(float(p), 4)
        doc_mix.append({
            "book_id": row["book_id"],
            "title": short_title(row["title"], row["book_id"]),
            "full_title": str(row["title"]),
            "era": row["era"],
            "year": int(row["year"]) if not pd.isna(row["year"]) else None,
            "level": str(row["level"]) if not pd.isna(row["level"]) else "",
            "n_tokens": int(row["n_tokens"]),
            "weights": weights,
            "dominant_topic": int(np.argmax(weights)),
        })

    # ── Era × topic average mixture ───────────────────────────────────
    era_topic = {}
    for era in ERA_ORDER:
        rows = [d["weights"] for d in doc_mix if d["era"] == era]
        if not rows:
            continue
        avg = np.mean(np.array(rows), axis=0)
        era_topic[era] = [round(float(x), 4) for x in avg]

    # ── pyLDAvis HTML ─────────────────────────────────────────────────
    print("\nGenerating pyLDAvis HTML ...")
    vis_data = gensimvis.prepare(lda, bow_corpus, dictionary, sort_topics=False)
    LDAVIS_OUT.parent.mkdir(parents=True, exist_ok=True)
    pyLDAvis.save_html(vis_data, str(LDAVIS_OUT))
    print(f"  saved → {LDAVIS_OUT}")

    # ── Build JSON output ─────────────────────────────────────────────
    preprocessing_summary = {
        "tokenizer": "kiwipiepy (Kiwi)",
        "pos_tags_kept": sorted(NOUN_TAGS),
        "min_token_length": MIN_TOKEN_LEN,
        "stopwords_count": len(stopwords),
        "min_doc_freq_books": max(2, int(MIN_DOC_FREQ * len(corpus))),
        "max_doc_freq_prop": MAX_DOC_FREQ_PROP,
        "vocabulary_size_before_filter": before,
        "vocabulary_size_after_filter": after,
        "total_tokens_after_filter": int(total_kept),
    }

    out = {
        "corpus": {
            "n_books": len(corpus),
            "source": "NIKH (국사편찬위원회) via nlp_corpora",
            "era_counts": era_counts,
            "year_min": int(corpus["year"].min()),
            "year_max": int(corpus["year"].max()),
        },
        "preprocessing": preprocessing_summary,
        "lda": {
            "k_values": K_VALUES,
            "default_k": DEFAULT_K,
            "best_k_by_cv": best_row["k"],
            "best_coherence_cv": best_row["coherence_cv"],
            "passes": LDA_PASSES,
            "iterations": LDA_ITERATIONS,
            "random_seed": RANDOM_SEED,
        },
        "coherence": coherence_rows,
        "topics": topics_json,
        "documents": doc_mix,
        "era_topic_mix": era_topic,
        "ldavis_html_path": "topic_modeling_ldavis.html",
    }

    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(JSON_OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"  saved → {JSON_OUT}")

    print("\nDone.")


if __name__ == "__main__":
    main()
