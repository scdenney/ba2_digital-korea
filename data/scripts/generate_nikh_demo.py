"""
Generate the NIKH demo CSV and interactive JSON data for the NIKH textbooks page.

Reads 9 books from the full NIKH corpus (nlp_corpora), builds the demo CSV,
and computes word-frequency and 통일-count data for the interactive visualizations.

No document-frequency filter is applied — all words from processed_text are counted.

Usage:
    python generate_nikh_demo.py

Requires:
    - nlp_corpora repo at ../../nlp_corpora (sibling of this repo)
      or update CORPUS_PATH below.
"""

import json
from collections import Counter
from pathlib import Path

import pandas as pd

# ── Paths ─────────────────────────────────────────────────────────────
SCRIPT_DIR   = Path(__file__).resolve().parent
REPO_ROOT    = SCRIPT_DIR.parent.parent
CORPUS_PATH  = REPO_ROOT / "nlp_corpora" / "data" / "nikh" / "nikh_corpus.csv"
DEMO_CSV_OUT = SCRIPT_DIR.parent / "nikh_textbooks" / "nikh_textbooks_demo.csv"
JSON_OUT     = REPO_ROOT / "ba2_digital-korea" / "interactive" / "nikh_data.json"

# ── Demo book selection ───────────────────────────────────────────────
# 3 books per era (Colonial / Authoritarian / Democratic)
# Postwar books (1954, 1963) are grouped into Authoritarian for pedagogical
# simplicity — both predate the democratic transition.
DEMO_IDS = [
    "ta_p31r", "ta_p32r", "ta_p41r",   # Colonial
    "ta_e11",  "ta_h21",  "ta_m41",    # Authoritarian (incl. Postwar)
    "ta_m62",  "ta_h61",  "ta_e71",    # Democratic
]

ERA_ORDER = {"Colonial": 0, "Authoritarian": 1, "Democratic": 2}


def assign_era(period: str) -> str:
    """Collapse 5 corpus periods into 3 demo eras."""
    if period == "Colonial":
        return "Colonial"
    if period == "Democratic":
        return "Democratic"
    return "Authoritarian"   # Postwar + Authoritarian → Authoritarian


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
    demo = demo.sort_values(["_sort", "year"]).drop(columns="_sort")

    print(f"Demo books ({len(demo)}):")
    for _, row in demo.iterrows():
        print(f"  [{row['book_id']}] era={row['era']}  period={row['period']}  year={row['year']}")

    # ── Save demo CSV ─────────────────────────────────────────────────
    demo_out = demo[["book_id", "title", "era", "period", "level", "year",
                      "full_text", "processed_text"]]
    DEMO_CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    demo_out.to_csv(DEMO_CSV_OUT, index=False)
    print(f"\nSaved demo CSV → {DEMO_CSV_OUT}")

    # ── Word frequencies from processed_text (no df filter) ───────────
    # processed_text = space-separated nouns (NNG/NNP), stopwords removed,
    # min 2 chars, numbers removed. Produced by Kiwi tokenization.
    era_top_words: dict[str, list] = {}
    for era in ["Colonial", "Authoritarian", "Democratic"]:
        sub = demo[demo["era"] == era]
        all_words: list[str] = []
        for _, row in sub.iterrows():
            pt = str(row["processed_text"])
            if pt and pt != "nan":
                all_words.extend(pt.split())
        counts = Counter(all_words)
        era_top_words[era] = [
            {"word": w, "count": c} for w, c in counts.most_common(50)
        ]
        top5 = [x["word"] for x in era_top_words[era][:5]]
        print(f"  {era}: top 5 = {top5}")

    # ── 통일 counts per book ──────────────────────────────────────────
    book_tongil: list[dict] = []
    for _, row in demo.iterrows():
        pt = str(row["processed_text"]) if str(row["processed_text"]) != "nan" else ""
        words = pt.split() if pt else []
        total = len(words)
        tongil = words.count("통일")
        title = str(row["title"])
        book_tongil.append({
            "book_id":      row["book_id"],
            "title":        title[:20] + "…" if len(title) > 20 else title,
            "full_title":   title,
            "era":          row["era"],
            "period":       row["period"],
            "level":        str(row["level"]) if str(row["level"]) != "nan" else "",
            "year":         str(row["year"]) if str(row["year"]) != "nan" else "",
            "tongil_count": tongil,
            "total_tokens": total,
        })

    # ── Write JSON ────────────────────────────────────────────────────
    out = {"era_top_words": era_top_words, "book_tongil_counts": book_tongil}
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(JSON_OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Saved JSON → {JSON_OUT}")


if __name__ == "__main__":
    main()
