"""
Generate JSON data for the k-means clustering interactive demo.

Reads 749 democratic-era presidential speeches, tokenizes with kiwipiepy,
computes TF-IDF vectors, runs k-means for k=2..8, computes silhouette
scores, and extracts per-cluster top words for the best k.

Usage:
    python generate_kmeans_demo.py

Requires:
    - kiwipiepy, scikit-learn, pandas, numpy
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd
from kiwipiepy import Kiwi
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import silhouette_score, silhouette_samples

# ── Paths ─────────────────────────────────────────────────────────────
SCRIPT_DIR   = Path(__file__).resolve().parent
REPO_DIR     = SCRIPT_DIR.parent.parent
SPEECHES_CSV = REPO_DIR / "data" / "president_speeches" / "president_speeches_democratic_era.csv"
STOPWORDS    = SCRIPT_DIR.parent / "stopwords_ko.txt"
JSON_OUT     = REPO_DIR / "interactive" / "kmeans_data.json"

NOUN_TAGS = {"NNG", "NNP"}


def load_stopwords() -> set[str]:
    words = set()
    with open(STOPWORDS, encoding="utf-8") as f:
        for line in f:
            w = line.strip()
            if w:
                words.add(w)
    return words


def tokenize_text(kiwi: Kiwi, text: str, stopwords: set[str]) -> str:
    tokens = []
    for token in kiwi.tokenize(text):
        if token.tag not in NOUN_TAGS:
            continue
        if len(token.form) < 2:
            continue
        if token.form.isdigit():
            continue
        if token.form in stopwords:
            continue
        tokens.append(token.form)
    return " ".join(tokens)


def main() -> None:
    # ── Load data ─────────────────────────────────────────────────────
    print(f"Loading speeches from {SPEECHES_CSV} ...")
    df = pd.read_csv(SPEECHES_CSV)
    print(f"  {len(df)} speeches, {df['president'].nunique()} presidents")

    # ── Tokenize ──────────────────────────────────────────────────────
    print("\nTokenizing with kiwipiepy ...")
    stopwords = load_stopwords()
    kiwi = Kiwi()
    df["processed"] = df["speech_text"].apply(
        lambda t: tokenize_text(kiwi, str(t), stopwords)
    )
    print(f"  Done. Mean tokens/speech: {df['processed'].str.split().str.len().mean():.0f}")

    # ── TF-IDF ────────────────────────────────────────────────────────
    print("\nComputing TF-IDF ...")
    vectorizer = TfidfVectorizer(max_features=10000)
    tfidf = vectorizer.fit_transform(df["processed"])
    feature_names = vectorizer.get_feature_names_out()
    print(f"  Matrix: {tfidf.shape[0]} docs × {tfidf.shape[1]} features")

    # ── K-means for k=2..8, with silhouette scores ───────────────────
    print("\nRunning k-means for k=2..8 ...")
    k_range = list(range(2, 9))
    results = {}

    for k in k_range:
        km = KMeans(n_clusters=k, n_init=10, random_state=42)
        labels = km.fit_predict(tfidf)
        sil_avg = silhouette_score(tfidf, labels)
        results[k] = {"labels": labels, "model": km, "silhouette": sil_avg}
        print(f"  k={k}: silhouette={sil_avg:.4f}")

    # ── Best k ────────────────────────────────────────────────────────
    best_k = max(results, key=lambda k: results[k]["silhouette"])
    print(f"\nBest k by silhouette: {best_k} (score={results[best_k]['silhouette']:.4f})")

    best_labels = results[best_k]["labels"]
    df["cluster"] = best_labels

    # ── Per-cluster top words ─────────────────────────────────────────
    print("\nExtracting per-cluster top words ...")
    cluster_words = {}
    for c in range(best_k):
        mask = best_labels == c
        cluster_mean = tfidf[mask].mean(axis=0).A1
        top_idx = cluster_mean.argsort()[::-1][:25]
        words = [
            {"word": feature_names[i], "tfidf": round(float(cluster_mean[i]), 4)}
            for i in top_idx
        ]
        cluster_words[str(c)] = words
        top5 = [w["word"] for w in words[:5]]
        print(f"  Cluster {c}: {top5}")

    # ── Per-cluster silhouette samples for the best k ─────────────────
    sil_samples = silhouette_samples(tfidf, best_labels)

    # ── President distribution per cluster ────────────────────────────
    cluster_president_dist = {}
    for c in range(best_k):
        sub = df[df["cluster"] == c]
        dist = sub["president"].value_counts().to_dict()
        cluster_president_dist[str(c)] = dist

    # ── Speech type distribution per cluster ──────────────────────────
    cluster_kind_dist = {}
    for c in range(best_k):
        sub = df[df["cluster"] == c]
        dist = sub["kind"].value_counts().to_dict()
        cluster_kind_dist[str(c)] = dist

    # ── Build JSON ────────────────────────────────────────────────────
    # Silhouette comparison across k values
    silhouette_comparison = [
        {"k": k, "silhouette": round(results[k]["silhouette"], 4)}
        for k in k_range
    ]

    # Per-speech data for best k (sample for size — include all)
    speeches_json = []
    for i, (_, row) in enumerate(df.iterrows()):
        speeches_json.append({
            "president": row["president"],
            "title": str(row["title"])[:50],
            "kind": row["kind"],
            "cluster": int(row["cluster"]),
            "silhouette": round(float(sil_samples[i]), 3),
            "tokens": len(str(row["processed"]).split()),
        })

    # President summary
    president_summary = []
    for pres in df["president"].unique():
        sub = df[df["president"] == pres]
        president_summary.append({
            "president": pres,
            "count": len(sub),
            "cluster_dist": sub["cluster"].value_counts().to_dict(),
        })

    out = {
        "best_k": best_k,
        "silhouette_comparison": silhouette_comparison,
        "cluster_words": cluster_words,
        "cluster_president_dist": cluster_president_dist,
        "cluster_kind_dist": cluster_kind_dist,
        "speeches": speeches_json,
        "president_summary": president_summary,
    }

    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(JSON_OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nSaved JSON → {JSON_OUT}")
    print("Done!")


if __name__ == "__main__":
    main()
