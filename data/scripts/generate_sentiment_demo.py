"""
Generate sentiment_data.json for the Week 9 interactive exercise.

This is a ONE-TIME reproducibility script used by instructors. Students do
not run it. It regenerates `interactive/sentiment_data.json` by:

  1. Reading `data/moon_twitter/moon_twitter.csv`
  2. Tokenizing each tweet with a regex that matches NLTK's WordPunctTokenizer
     (which is what Orange's Corpus widget uses by default on Korean text)
  3. Looking up tokens in Chen & Skiena's (2014) Korean sentiment lexicon
     (`positive_words_ko.txt`, `negative_words_ko.txt`) — the same dictionary
     Orange's built-in Multilingual Sentiment method uses
  4. Computing Orange's exact scoring formula:
        score = 100 * (|pos ∩ tokens| - |neg ∩ tokens|) / max(len(tokens), 1)
  5. Emitting `interactive/sentiment_data.json`

The interactive's displayed scores will exactly match what a student sees
in Orange's Sentiment Analysis widget when Method = Multilingual and
Language = Korean.

Usage (from repo root):
    python3 data/scripts/generate_sentiment_demo.py
"""
import csv
import json
import re
import os
from collections import Counter

# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TWEETS_CSV = os.path.join(REPO_ROOT, "data", "moon_twitter", "moon_twitter.csv")
POS_FILE = os.path.join(REPO_ROOT, "data", "sentiment_dic", "positive_words_ko.txt")
NEG_FILE = os.path.join(REPO_ROOT, "data", "sentiment_dic", "negative_words_ko.txt")
OUT_JSON = os.path.join(REPO_ROOT, "interactive", "sentiment_data.json")

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------
# NLTK's WordPunctTokenizer regex. Splits on word characters (\w+) or
# runs of non-word-non-whitespace characters ([^\w\s]+). This is what
# Orange's Corpus widget uses by default.
WORD_PUNCT_RE = re.compile(r"\w+|[^\w\s]+", re.UNICODE)

PERIOD_MAP = {"pre_presidency": "p", "transition": "t", "presidency": "r"}

# Six pedagogically interesting tweets to highlight in Step 2 of the
# interactive (scoring walkthrough). Labels are editorial.
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
    """One word per line, strip whitespace, drop empties."""
    with open(path, encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}


def tokenize(text):
    """Match Orange's default Corpus tokenization (NLTK WordPunctTokenizer)."""
    if not text:
        return []
    return WORD_PUNCT_RE.findall(text)


# --------------------------------------------------------------------------
# Scoring (exactly matches Orange's compute_from_dict)
# --------------------------------------------------------------------------
def score_tweet(tokens, pos_set, neg_set):
    """
    Orange's formula:
        100 * (|pos ∩ tokens| - |neg ∩ tokens|) / max(len(tokens), 1)

    Returns:
        (score, pos_matches, neg_matches, n_pos, n_neg)
    where n_pos/n_neg are set-intersection counts (unique, not frequency).
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
    print("Loading Chen & Skiena Korean lexicon...")
    pos_set = load_lexicon(POS_FILE)
    neg_set = load_lexicon(NEG_FILE)
    print(f"  positive: {len(pos_set)} entries")
    print(f"  negative: {len(neg_set)} entries")

    print("Loading tweets...")
    rows = []
    with open(TWEETS_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    print(f"  tweets: {len(rows)}")

    # Score every tweet
    all_pos_counter = Counter()
    all_neg_counter = Counter()
    timeline = []
    full_results = []  # with full text for example tweets

    for row in rows:
        text = row.get("text", "") or ""
        period_char = PERIOD_MAP.get(row["period3"], "p")

        if not text.strip():
            entry = {
                "d": row["tweet_date"], "y": int(row["tweet_year"]),
                "p": period_char, "s": 0.0, "f": int(row["favorites"] or 0),
                "pc": 0, "nc": 0, "t": "", "pm": [], "nm": [],
            }
            timeline.append(entry)
            full_results.append({**entry, "full_text": ""})
            continue

        tokens = tokenize(text)
        score, pm, nm, n_pos, n_neg = score_tweet(tokens, pos_set, neg_set)

        for w in pm:
            all_pos_counter[w] += 1
        for w in nm:
            all_neg_counter[w] += 1

        entry = {
            "d": row["tweet_date"],
            "y": int(row["tweet_year"]),
            "p": period_char,
            "s": round(score, 2),
            "f": int(row["favorites"] or 0),
            "pc": n_pos,
            "nc": n_neg,
            "t": text[:120],
            "pm": pm[:8],
            "nm": nm[:8],
        }
        timeline.append(entry)
        full_results.append({**entry, "full_text": text,
                             "retweets": int(row["retweets"] or 0),
                             "period3": row["period3"]})

    # Stats by period
    print("\nScores by period:")
    for pc, name in [("p", "pre_presidency"), ("t", "transition"), ("r", "presidency")]:
        scores = [e["s"] for e in timeline if e["p"] == pc and e["t"]]
        mean = sum(scores) / len(scores) if scores else 0.0
        print(f"  {name}: n={len(scores)}, mean={mean:.2f}")

    # Build period_stats
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

    # Histogram (bin scores into integer buckets for display)
    # Scores are floats like 7.14 or -12.5 — bin to integers for the histogram
    bins = Counter()
    for e in timeline:
        if not e["t"]:
            continue
        bins[int(round(e["s"]))] += 1
    hmin, hmax = min(bins), max(bins)
    print(f"\nScore range: {hmin} to {hmax}")
    histogram = {str(s): bins.get(s, 0) for s in range(hmin, hmax + 1)}

    # Period histograms
    period_histograms = {}
    for pk, pc in [("pre_presidency", "p"), ("transition", "t"), ("presidency", "r")]:
        pbins = Counter()
        for e in timeline:
            if e["p"] == pc and e["t"]:
                pbins[int(round(e["s"]))] += 1
        period_histograms[pk] = {str(s): pbins.get(s, 0) for s in range(hmin, hmax + 1)}

    # Top words
    top_positive = [{"word": w, "count": c} for w, c in all_pos_counter.most_common(20)]
    top_negative = [{"word": w, "count": c} for w, c in all_neg_counter.most_common(20)]
    print(f"\nTop 10 positive: {[w['word'] for w in top_positive[:10]]}")
    print(f"Top 10 negative: {[w['word'] for w in top_negative[:10]]}")

    # Most extreme / most engaged
    non_empty = [e for e in timeline if e["t"]]
    most_positive = sorted(non_empty, key=lambda e: (-e["s"], -e["f"]))[:5]
    most_negative = sorted(non_empty, key=lambda e: (e["s"], -e["f"]))[:5]
    most_engaged = sorted(non_empty, key=lambda e: -e["f"])[:5]

    # Example tweets (hand-picked, with full text)
    examples = []
    for row in rows:
        text = row.get("text", "") or ""
        for target_date, label, needle in EXAMPLE_TARGETS:
            if row["tweet_date"] == target_date and needle in text \
                    and not any(e["label"] == label for e in examples):
                tokens = tokenize(text)
                score, pm, nm, n_pos, n_neg = score_tweet(tokens, pos_set, neg_set)
                examples.append({
                    "label": label,
                    "date": row["tweet_date"],
                    "period": row["period3"],
                    "text": text,
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
        print(f"  {e['label']}: score={e['score']:.2f}, +{e['pos_count']}/-{e['neg_count']}")

    # Build final JSON
    data = {
        "total_tweets": sum(1 for e in timeline if e["t"]),
        "dict_sizes": {
            "positive": len(pos_set),
            "negative": len(neg_set),
        },
        "preprocessing": {
            "tokenizer": "wordpunct (NLTK / Orange default)",
            "dictionary": "Chen & Skiena 2014 (Korean)",
            "score_method": "100 * (pos_set - neg_set) / max(len(tokens), 1)",
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
