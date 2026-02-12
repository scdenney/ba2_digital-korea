"""
Generate preprocessing demo data for the Interactive page.

Reads presidential speeches, splits into sentences with Kiwi,
samples ~150 balanced across presidents, runs the full preprocessing
pipeline capturing every intermediate step, and outputs JSON.

Usage:
    python generate_preprocessing_demo.py
"""

import csv
import json
import random
import re
from pathlib import Path

from kiwipiepy import Kiwi

# ── paths ────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
CORPUS_CSV = SCRIPT_DIR.parent / "president_speeches" / "president_speeches_democratic_era.csv"
OUTPUT_DIR = SCRIPT_DIR.parent.parent / "interactive"
OUTPUT_JSON = OUTPUT_DIR / "preprocessing_data.json"

# ── config ───────────────────────────────────────────────────────────
STOPWORDS_FILE = SCRIPT_DIR.parent / "stopwords_ko.txt"
SENTENCES_PER_PRESIDENT = 22          # ~154 total across 7 presidents
MIN_CHARS = 20
MAX_CHARS = 120
SEED = 42

# POS tags we keep as "content words"
CONTENT_TAGS = {"NNG", "NNP", "VV", "VA", "MAG"}


def load_stopwords() -> set[str]:
    """Load stopwords from stopwords_ko.txt.

    For morpheme-level matching we keep single-token entries as-is.
    For verb/adjective dictionary forms ending in 다, we also add the
    stem (without 다) since Kiwi splits stems from endings.
    """
    stopwords: set[str] = set()
    with open(STOPWORDS_FILE, encoding="utf-8") as f:
        for line in f:
            word = line.strip()
            if not word:
                continue
            # Skip multi-word phrases (contain spaces)
            if " " in word:
                continue
            stopwords.add(word)
            # Add verb/adj stems: 하다→하, 있다→있, etc.
            if len(word) > 1 and word.endswith("다"):
                stopwords.add(word[:-1])
    return stopwords


STOPWORDS = load_stopwords()

# Human-readable POS tag labels (Korean linguistic terms simplified)
TAG_LABELS = {
    "NNG": "General noun",
    "NNP": "Proper noun",
    "NNB": "Bound noun",
    "NR":  "Number (word)",
    "NP":  "Pronoun",
    "VV":  "Verb",
    "VA":  "Adjective",
    "VX":  "Auxiliary verb",
    "VCP": "Copula (이다)",
    "VCN": "Negative copula",
    "MAG": "Adverb",
    "MAJ": "Conjunctive adverb",
    "MM":  "Determiner",
    "IC":  "Interjection",
    "JKS": "Subject particle",
    "JKC": "Complement particle",
    "JKG": "Possessive particle",
    "JKO": "Object particle",
    "JKB": "Adverbial particle",
    "JKV": "Vocative particle",
    "JKQ": "Quotative particle",
    "JX":  "Auxiliary particle",
    "JC":  "Conjunctive particle",
    "EP":  "Pre-final ending",
    "EF":  "Final ending",
    "EC":  "Connective ending",
    "ETN": "Nominalizing ending",
    "ETM": "Adnominal ending",
    "XPN": "Prefix",
    "XSN": "Noun-deriv. suffix",
    "XSV": "Verb-deriv. suffix",
    "XSA": "Adj.-deriv. suffix",
    "XR":  "Root",
    "SF":  "Period/Question/Excl.",
    "SP":  "Comma/Colon/Dash",
    "SS":  "Quotes/Brackets",
    "SE":  "Ellipsis",
    "SO":  "Hyphen/Tilde",
    "SN":  "Number (digit)",
    "SL":  "Latin character",
    "SH":  "Chinese character",
    "SW":  "Other symbol",
    "UN":  "Unknown",
    "W_URL": "URL",
    "W_EMAIL": "Email",
    "W_HASHTAG": "Hashtag",
    "W_MENTION": "Mention",
}

# POS tag visual categories (for the frontend color coding)
TAG_CATEGORIES = {
    "noun":      {"NNG", "NNP", "NNB", "NR", "NP"},
    "verb":      {"VV", "VX", "VCP", "VCN"},
    "adjective": {"VA"},
    "adverb":    {"MAG", "MAJ"},
    "particle":  {"JKS", "JKC", "JKG", "JKO", "JKB", "JKV", "JKQ", "JX", "JC"},
    "ending":    {"EP", "EF", "EC", "ETN", "ETM"},
    "affix":     {"XPN", "XSN", "XSV", "XSA", "XR"},
    "symbol":    {"SF", "SP", "SS", "SE", "SO", "SN", "SL", "SH", "SW"},
    "other":     {"MM", "IC", "UN"},
}

def base_tag(tag: str) -> str:
    """Strip Kiwi's -R (regular) / -I (irregular) conjugation suffixes."""
    if tag.endswith("-R") or tag.endswith("-I"):
        return tag.rsplit("-", 1)[0]
    return tag


def tag_to_category(tag: str) -> str:
    bt = base_tag(tag)
    for cat, tags in TAG_CATEGORIES.items():
        if bt in tags:
            return cat
    return "other"


# ── text cleaning (mirrors Orange script) ────────────────────────────
def clean_text(text: str) -> str:
    text = re.sub(r"http[s]?://\S+", "", text)
    text = re.sub(r"\S+@\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    # Remove non-word chars except Korean and whitespace
    text = re.sub(r"[^\w\s\u3131-\u3163\uac00-\ud7a3\u1100-\u11ff]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def process_sentence(kiwi_instance: Kiwi, raw: str) -> dict | None:
    """Run the full pipeline on one sentence, capturing every step."""

    # Step 1: raw text (as-is)
    # Step 2: cleaned text
    cleaned = clean_text(raw)
    if not cleaned or len(cleaned) < 5:
        return None

    # Step 3+4: tokenize and POS-tag (Kiwi does both at once)
    kiwi_tokens = kiwi_instance.tokenize(cleaned)

    tokens = []
    for t in kiwi_tokens:
        raw_tag = t.tag
        bt = base_tag(raw_tag)
        is_content = bt in CONTENT_TAGS
        is_stopword = t.form in STOPWORDS
        tokens.append({
            "form": t.form,
            "tag": bt,              # normalized (no -R/-I suffix)
            "tag_raw": raw_tag,     # original Kiwi tag for reference
            "tag_label": TAG_LABELS.get(bt, bt),
            "category": tag_to_category(raw_tag),
            "is_content": is_content,
            "is_stopword": is_stopword,
        })

    # Step 5-6: filter → result
    kept = [
        t["form"] for t in tokens
        if t["is_content"] and not t["is_stopword"] and len(t["form"]) >= 2 and not t["form"].isdigit()
    ]
    result = " ".join(kept)

    if not result:
        return None

    return {
        "raw": raw,
        "cleaned": cleaned,
        "tokens": tokens,
        "result": result,
    }


def main():
    random.seed(SEED)
    kiwi = Kiwi()

    # ── read corpus ──────────────────────────────────────────────────
    print(f"Reading corpus from {CORPUS_CSV} ...")
    speeches_by_president: dict[str, list[dict]] = {}
    with open(CORPUS_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pres = row["president"]
            speeches_by_president.setdefault(pres, []).append(row)

    print(f"  Presidents: {sorted(speeches_by_president.keys())}")
    for p, rows in speeches_by_president.items():
        print(f"    {p}: {len(rows)} speeches")

    # ── sentence-split and sample ────────────────────────────────────
    print("Splitting sentences and sampling ...")
    demo_entries = []

    for president, speeches in speeches_by_president.items():
        candidates = []
        for sp in speeches:
            text = sp.get("speech_text", "")
            if not text:
                continue
            title = sp.get("title", "")
            # Use Kiwi's sentence splitter
            sentences = kiwi.split_into_sents(text)
            for sent in sentences:
                s = sent.text.strip()
                if MIN_CHARS <= len(s) <= MAX_CHARS:
                    candidates.append((s, title))

        print(f"  {president}: {len(candidates)} candidate sentences")

        # Sample up to SENTENCES_PER_PRESIDENT
        n = min(SENTENCES_PER_PRESIDENT, len(candidates))
        sampled = random.sample(candidates, n)

        for raw, title in sampled:
            entry = process_sentence(kiwi, raw)
            if entry is None:
                continue
            entry["president"] = president
            entry["source_title"] = title
            demo_entries.append(entry)

    print(f"\nTotal demo entries: {len(demo_entries)}")

    # ── write JSON ───────────────────────────────────────────────────
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(demo_entries, f, ensure_ascii=False, indent=2)

    print(f"Wrote {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
