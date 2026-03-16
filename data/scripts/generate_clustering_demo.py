"""
Generate the NIKH clustering demo CSV and interactive JSON data.

Reads 11 books from the full NIKH corpus, tokenizes with kiwipiepy,
computes TF-IDF vectors, runs Ward's hierarchical clustering, and
extracts per-cluster distinctive words.

Usage:
    python generate_clustering_demo.py

Requires:
    - nlp_corpora repo at ../../nlp_corpora (sibling of this repo)
      or update CORPUS_PATH below.
    - kiwipiepy, scikit-learn, scipy, pandas
"""

import json
import math
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
from kiwipiepy import Kiwi
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize

# ── Paths ─────────────────────────────────────────────────────────────
SCRIPT_DIR   = Path(__file__).resolve().parent          # data/scripts/
REPO_DIR     = SCRIPT_DIR.parent.parent                  # ba2_digital-korea/
GITHUB_DIR   = REPO_DIR.parent                           # Documents/GitHub/
CORPUS_PATH  = GITHUB_DIR / "nlp_corpora" / "data" / "nikh" / "nikh_corpus.csv"
STOPWORDS    = SCRIPT_DIR.parent / "stopwords_ko.txt"
DEMO_CSV_OUT = SCRIPT_DIR.parent / "nikh_textbooks" / "nikh_clustering_demo.csv"
JSON_OUT     = REPO_DIR / "interactive" / "clustering_data.json"

# ── Demo book selection (11 books) ────────────────────────────────────
# Colonial (3): 심상소학 materials, 1940
# Authoritarian (4): 3rd-5th curriculum, 1973-1987
# Democratic (4): 6th-7th curriculum, 1995-2002
DEMO_IDS = [
    "ta_p31r", "ta_p32r", "ta_p41r",          # Colonial
    "ta_m31",  "ta_m41",  "ta_h41", "ta_m51",  # Authoritarian
    "ta_m62",  "ta_h61",  "ta_e71", "ta_h71",  # Democratic
]

ERA_ORDER = {"Colonial": 0, "Authoritarian": 1, "Democratic": 2}
NOUN_TAGS = {"NNG", "NNP"}


def assign_era(period: str) -> str:
    """Collapse corpus periods into 3 demo eras."""
    if period == "Colonial":
        return "Colonial"
    if period == "Democratic":
        return "Democratic"
    return "Authoritarian"


def load_stopwords() -> set[str]:
    """Load Korean stopwords from file."""
    words = set()
    with open(STOPWORDS, encoding="utf-8") as f:
        for line in f:
            w = line.strip()
            if w:
                words.add(w)
    return words


def tokenize_text(kiwi: Kiwi, text: str, stopwords: set[str]) -> str:
    """Tokenize text with Kiwi, keep NNG/NNP nouns, remove stopwords."""
    tokens = []
    for token in kiwi.tokenize(text):
        form = token.form
        tag = token.tag
        if tag not in NOUN_TAGS:
            continue
        if len(form) < 2:
            continue
        if form.isdigit():
            continue
        if form in stopwords:
            continue
        tokens.append(form)
    return " ".join(tokens)


def main() -> None:
    # ── Load corpus ───────────────────────────────────────────────────
    print(f"Loading corpus from {CORPUS_PATH} ...")
    corpus = pd.read_csv(CORPUS_PATH)
    demo = corpus[corpus["book_id"].isin(DEMO_IDS)].copy()

    if len(demo) != len(DEMO_IDS):
        missing = set(DEMO_IDS) - set(demo["book_id"])
        raise ValueError(f"Missing books in corpus: {missing}")

    demo["era"] = demo["period"].apply(assign_era)
    demo["_sort"] = demo["era"].map(ERA_ORDER)
    demo = demo.sort_values(["_sort", "year"]).drop(columns="_sort").reset_index(drop=True)

    print(f"Demo books ({len(demo)}):")
    for _, row in demo.iterrows():
        print(f"  [{row['book_id']}] era={row['era']}  year={row['year']}  {row['title']}")

    # ── Tokenize ──────────────────────────────────────────────────────
    print("\nTokenizing with kiwipiepy ...")
    stopwords = load_stopwords()
    kiwi = Kiwi()

    demo["processed_text"] = demo["full_text"].apply(
        lambda t: tokenize_text(kiwi, str(t), stopwords)
    )

    for _, row in demo.iterrows():
        n = len(row["processed_text"].split())
        print(f"  [{row['book_id']}] {n} tokens")

    # ── Save demo CSV ─────────────────────────────────────────────────
    # Do NOT include processed_text — Orange's Corpus widget crashes
    # when a pre-tokenized column is present. Students preprocess
    # from full_text in their own workflow.
    demo_out = demo[["book_id", "title", "era", "period", "nikh_period",
                      "curriculum", "level", "year", "full_text"]]
    DEMO_CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    demo_out.to_csv(DEMO_CSV_OUT, index=False)
    print(f"\nSaved demo CSV → {DEMO_CSV_OUT}")

    # ── TF-IDF vectorization ──────────────────────────────────────────
    print("\nComputing TF-IDF ...")
    texts = demo["processed_text"].tolist()
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)

    # L2-normalize rows so that Euclidean distance = cosine distance.
    # (On unit vectors: ||a-b||^2 = 2 - 2*cos(a,b))
    # This matches Orange's Distances widget with "Cosine" selected.
    tfidf_norm = normalize(tfidf_matrix, norm="l2")

    # ── Hierarchical clustering (cosine distance + Ward's) ────────────
    print("Running Ward's hierarchical clustering (cosine distance) ...")
    dense = tfidf_norm.toarray()
    Z = linkage(dense, method="ward", metric="euclidean")

    # Cut at k=3 clusters
    labels = fcluster(Z, t=3, criterion="maxclust")
    demo["cluster"] = labels

    print("\nCluster assignments:")
    for _, row in demo.iterrows():
        print(f"  [{row['book_id']}] era={row['era']}  cluster={row['cluster']}")

    # ── Map clusters to eras ──────────────────────────────────────────
    # Find which era dominates each cluster
    cluster_era_mapping = {}
    for c in sorted(demo["cluster"].unique()):
        era_counts = demo[demo["cluster"] == c]["era"].value_counts()
        dominant_era = era_counts.index[0]
        cluster_era_mapping[str(c)] = dominant_era
        print(f"  Cluster {c} → {dominant_era} ({era_counts.to_dict()})")

    # ── Per-cluster distinctive words via TF-IDF on pseudo-documents ──
    print("\nExtracting per-cluster distinctive words ...")
    cluster_docs = {}
    for c in sorted(demo["cluster"].unique()):
        cluster_texts = demo[demo["cluster"] == c]["processed_text"].tolist()
        cluster_docs[c] = " ".join(cluster_texts)

    cluster_vectorizer = TfidfVectorizer(max_features=5000)
    cluster_tfidf = cluster_vectorizer.fit_transform(list(cluster_docs.values()))
    feature_names = cluster_vectorizer.get_feature_names_out()

    cluster_words = {}
    for i, c in enumerate(sorted(cluster_docs.keys())):
        scores = cluster_tfidf[i].toarray().flatten()
        top_indices = scores.argsort()[::-1][:30]
        words = [
            {"word": feature_names[idx], "tfidf": round(float(scores[idx]), 4)}
            for idx in top_indices if scores[idx] > 0
        ]
        cluster_words[str(c)] = words
        top5 = [w["word"] for w in words[:5]]
        print(f"  Cluster {c} ({cluster_era_mapping[str(c)]}): {top5}")

    # ── Build JSON output ─────────────────────────────────────────────
    books_json = []
    for _, row in demo.iterrows():
        title = str(row["title"])
        # Create short title: truncate if needed
        short = title[:20] + "…" if len(title) > 20 else title
        books_json.append({
            "book_id": row["book_id"],
            "title": title,
            "short_title": short,
            "era": row["era"],
            "year": int(row["year"]) if not math.isnan(row["year"]) else None,
            "level": str(row["level"]) if str(row["level"]) != "nan" else "",
            "total_tokens": len(str(row["processed_text"]).split()),
            "cluster": int(row["cluster"]),
        })

    # Linkage matrix as nested list
    linkage_list = Z.tolist()
    labels_list = demo["book_id"].tolist()

    out = {
        "books": books_json,
        "dendrogram": {
            "linkage": linkage_list,
            "labels": labels_list,
        },
        "cluster_words": cluster_words,
        "cluster_era_mapping": cluster_era_mapping,
    }

    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(JSON_OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nSaved JSON → {JSON_OUT}")
    print("Done!")


if __name__ == "__main__":
    main()
