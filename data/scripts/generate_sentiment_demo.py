"""
Generate sentiment_data.json for the Week 9 interactive exercise.

This is a reproducibility script for instructors. Students do not run it.
It regenerates `interactive/sentiment_data.json` using the same pipeline
students will run in Orange Data Mining:

  1. Read `data/moon_twitter/moon_twitter.csv`
  2. Clean URLs, @mentions, RT markers from each tweet
  3. Tokenize with Kiwi (kiwipiepy) — the standard Korean morphological
     analyzer. Keep content-word POS tags: NNG, NNP, VA, VV. Drop tokens
     shorter than 2 characters.
  4. Load `data/sentiment_dic/positive.txt` and `negative.txt` — KNU's
     positive and negative word lists, as published.
  5. For each tweet, compute Orange's Custom Dictionary score:
        100 * (|pos ∩ tokens_set| - |neg ∩ tokens_set|) / max(len(tokens), 1)
     This is the same formula Orange's Sentiment Analysis widget uses
     when you pick Method = "Custom Dictionary".
  6. Emit `interactive/sentiment_data.json`.

The interactive's displayed scores will exactly match what a student sees
in Orange when they run:

    File → Corpus → Python Script (sentiment_preprocessing_*.py)
      → Corpus (re-map to processed_text)
      → Sentiment Analysis (Custom Dictionary, positive.txt + negative.txt)
      → Box Plot

Usage (from repo root):
    python3 data/scripts/generate_sentiment_demo.py
"""
import csv
import json
import re
import os
from collections import Counter

from kiwipiepy import Kiwi

# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TWEETS_CSV = os.path.join(REPO_ROOT, "data", "moon_twitter", "moon_twitter.csv")
POS_FILE = os.path.join(REPO_ROOT, "data", "sentiment_dic", "positive.txt")
NEG_FILE = os.path.join(REPO_ROOT, "data", "sentiment_dic", "negative.txt")
OUT_JSON = os.path.join(REPO_ROOT, "interactive", "sentiment_data.json")

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------
# Nouns kept as-is; verbs and adjectives (incl. irregular -I/-R variants)
# are converted to their citation form (stem + 다) so they match KNU
# dictionary entries like 기쁘다, 고맙다, 행복하다.
NOUN_TAGS = {"NNG", "NNP"}

# Minimum token length (skip single-syllable morphemes — standard practice
# in Korean NLP, reduces noise from common grammatical fragments).
MIN_LEN = 2


def is_verb_or_adj(tag):
    """Match VA, VV, and their irregular variants (VA-I, VV-I, VV-R, etc.)."""
    return tag == "VA" or tag == "VV" or tag.startswith("VA-") or tag.startswith("VV-")

PERIOD_MAP = {"pre_presidency": "p", "transition": "t", "presidency": "r"}

# Pedagogically interesting tweets highlighted in the interactive's
# Step 2 (scoring walkthrough). Labels are editorial.
EXAMPLE_TARGETS = [
    ("2018-01-24", "Birthday: Purely Positive", "축하"),
    ("2019-07-08", "Japan Crisis: Mixed", "어려움의 해결에"),
    ("2020-04-12", "Easter: Hope in Crisis", "새로운 일상"),
    ("2018-05-15", "Women's Safety: Negative", "여성을 대상으로"),
    ("2020-03-30", "COVID Solidarity: Mixed", "어려움 속에서도"),
    ("2018-04-27", "Inter-Korean Summit", "판문점"),
]


# --------------------------------------------------------------------------
# Loading
# --------------------------------------------------------------------------
def load_lexicon(path):
    """One word per line, strip whitespace, drop empty lines."""
    with open(path, encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}


# --------------------------------------------------------------------------
# Preprocessing — matches sentiment_preprocessing_mac-users.py exactly
# --------------------------------------------------------------------------
def clean_text(text):
    if not text:
        return ""
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"^RT\s*:?", "", text)
    return text.strip()


def tokenize(text, kiwi):
    """
    Kiwi tokenize → keep content words (length >= 2).
    Nouns kept as-is; verbs/adjectives converted to citation form (+ 다).
    """
    if not text:
        return []
    out = []
    for t in kiwi.tokenize(text):
        if len(t.form) < MIN_LEN:
            continue
        if t.tag in NOUN_TAGS:
            out.append(t.form)
        elif is_verb_or_adj(t.tag):
            out.append(t.form + "다")
    return out


# --------------------------------------------------------------------------
# Scoring — matches Orange's compute_from_dict exactly
# --------------------------------------------------------------------------
def score_tweet(tokens, pos_set, neg_set):
    """
    Orange's formula:
        score = 100 * (|pos ∩ tokens_set| - |neg ∩ tokens_set|) / max(len(tokens), 1)

    Returns: (score, sorted_pos_matches, sorted_neg_matches, n_pos, n_neg).
    """
    doc_set = set(tokens)
    pos_matches = sorted(pos_set & doc_set)
    neg_matches = sorted(neg_set & doc_set)
    n_pos = len(pos_matches)
    n_neg = len(neg_matches)
    score = 100.0 * (n_pos - n_neg) / max(len(tokens), 1)
    return score, pos_matches, neg_matches, n_pos, n_neg


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main():
    print("Loading KNU positive/negative word lists...")
    pos_set = load_lexicon(POS_FILE)
    neg_set = load_lexicon(NEG_FILE)
    print(f"  positive.txt: {len(pos_set)} entries")
    print(f"  negative.txt: {len(neg_set)} entries")

    print("Initializing Kiwi...")
    kiwi = Kiwi()

    print("Loading tweets...")
    rows = []
    with open(TWEETS_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    print(f"  tweets: {len(rows)}")

    print("Processing...")
    all_pos_counter = Counter()
    all_neg_counter = Counter()
    timeline = []

    for i, row in enumerate(rows):
        text = row.get("text", "") or ""
        period_char = PERIOD_MAP.get(row["period3"], "p")

        if not text.strip():
            timeline.append({
                "d": row["tweet_date"], "y": int(row["tweet_year"]),
                "p": period_char, "s": 0.0, "f": int(row["favorites"] or 0),
                "pc": 0, "nc": 0, "t": "", "pm": [], "nm": [],
            })
            continue

        cleaned = clean_text(text)
        tokens = tokenize(cleaned, kiwi)
        score, pm, nm, n_pos, n_neg = score_tweet(tokens, pos_set, neg_set)

        for w in pm:
            all_pos_counter[w] += 1
        for w in nm:
            all_neg_counter[w] += 1

        timeline.append({
            "d": row["tweet_date"],
            "y": int(row["tweet_year"]),
            "p": period_char,
            "s": round(score, 2),
            "f": int(row["favorites"] or 0),
            "pc": n_pos,
            "nc": n_neg,
            "nt": len(tokens),  # total content tokens (for tooltip)
            "t": cleaned[:120],  # CLEANED text for display (no URLs/mentions)
            "pm": pm[:8],
            "nm": nm[:8],
        })

        if (i + 1) % 500 == 0:
            print(f"  {i + 1}/{len(rows)}")

    # Stats
    print("\nScores by period:")
    for pc, name in [("p", "pre_presidency"), ("t", "transition"), ("r", "presidency")]:
        scores = [e["s"] for e in timeline if e["p"] == pc and e["t"]]
        mean = sum(scores) / len(scores) if scores else 0.0
        print(f"  {name}: n={len(scores)}, mean={mean:.2f}")

    # period_stats
    period_stats = {}
    for pk, pc in [("pre_presidency", "p"), ("transition", "t"), ("presidency", "r")]:
        scores = sorted([e["s"] for e in timeline if e["p"] == pc and e["t"]])
        n = len(scores)
        if n == 0:
            continue
        period_stats[pk] = {
            "n": n,
            "mean": round(sum(scores) / n, 2),
            "median": scores[n // 2],
            "min": min(scores),
            "max": max(scores),
            "q1": scores[n // 4],
            "q3": scores[3 * n // 4],
            "pos_pct": round(100 * sum(1 for s in scores if s > 0) / n, 1),
            "neg_pct": round(100 * sum(1 for s in scores if s < 0) / n, 1),
            "neu_pct": round(100 * sum(1 for s in scores if s == 0) / n, 1),
        }

    # Histogram (bin scores to integers for display)
    bins = Counter()
    for e in timeline:
        if not e["t"]:
            continue
        bins[int(round(e["s"]))] += 1
    hmin, hmax = min(bins), max(bins)
    print(f"\nScore range: {hmin} to {hmax}")
    histogram = {str(s): bins.get(s, 0) for s in range(hmin, hmax + 1)}

    period_histograms = {}
    for pk, pc in [("pre_presidency", "p"), ("transition", "t"), ("presidency", "r")]:
        pbins = Counter()
        for e in timeline:
            if e["p"] == pc and e["t"]:
                pbins[int(round(e["s"]))] += 1
        period_histograms[pk] = {str(s): pbins.get(s, 0) for s in range(hmin, hmax + 1)}

    # Top matched words
    top_positive = [{"word": w, "count": c} for w, c in all_pos_counter.most_common(20)]
    top_negative = [{"word": w, "count": c} for w, c in all_neg_counter.most_common(20)]
    print(f"\nTop 10 positive: {[w['word'] for w in top_positive[:10]]}")
    print(f"Top 10 negative: {[w['word'] for w in top_negative[:10]]}")

    # Most extreme / most engaged
    non_empty = [e for e in timeline if e["t"]]
    most_positive = sorted(non_empty, key=lambda e: (-e["s"], -e["f"]))[:5]
    most_negative = sorted(non_empty, key=lambda e: (e["s"], -e["f"]))[:5]
    most_engaged = sorted(non_empty, key=lambda e: -e["f"])[:5]

    # Example tweets (cleaned text for display)
    examples = []
    for row in rows:
        text = row.get("text", "") or ""
        for target_date, label, needle in EXAMPLE_TARGETS:
            if row["tweet_date"] == target_date and needle in text \
                    and not any(e["label"] == label for e in examples):
                cleaned = clean_text(text)
                tokens = tokenize(cleaned, kiwi)
                score, pm, nm, n_pos, n_neg = score_tweet(tokens, pos_set, neg_set)
                examples.append({
                    "label": label,
                    "date": row["tweet_date"],
                    "period": row["period3"],
                    "text": cleaned,  # cleaned of URLs/mentions
                    "favorites": int(row["favorites"] or 0),
                    "retweets": int(row["retweets"] or 0),
                    "pos_matches": pm[:10],
                    "neg_matches": nm[:10],
                    "pos_count": n_pos,
                    "neg_count": n_neg,
                    "score": round(score, 2),
                    "n_tokens": len(tokens),
                })

    examples.sort(key=lambda e: -e["score"])
    print(f"\nExample tweets ({len(examples)}):")
    for e in examples:
        print(f"  {e['label']}: score={e['score']:.2f}, +{e['pos_count']}/-{e['neg_count']}, tokens={e['n_tokens']}")

    data = {
        "total_tweets": sum(1 for e in timeline if e["t"]),
        "dict_sizes": {
            "positive": len(pos_set),
            "negative": len(neg_set),
        },
        "preprocessing": {
            "tokenizer": "kiwi (kiwipiepy) NNG/NNP/VA/VV, len>=2",
            "dictionary": "KNU positive.txt / negative.txt (as published)",
            "score_method": "Orange Custom Dictionary: 100 * (pos - neg) / max(len(tokens), 1)",
        },
        "period_labels": {
            "p": "Pre-presidency",
            "t": "Transition",
            "r": "Presidency",
        },
        "period_stats": period_stats,
        "histogram": histogram,
        "period_histograms": period_histograms,
        "top_positive_words": top_positive,
        "top_negative_words": top_negative,
        "most_positive": most_positive,
        "most_negative": most_negative,
        "most_engaged": most_engaged,
        "example_tweets": examples,
        "timeline": timeline,
    }

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    size_kb = os.path.getsize(OUT_JSON) / 1024
    print(f"\nWrote {OUT_JSON} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
