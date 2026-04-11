# Korean Sentiment Dictionaries

This folder contains Korean sentiment dictionaries for Week 9 (Sentiment Analysis). All dictionaries descend from the **KNU Korean Sentiment Lexicon** (Kunsan National University) — a standard reference dictionary built from the Standard Korean Dictionary (표준국어대사전) and validated by human annotators.

## Which file should I use?

**For Week 9 in Orange Data Mining → Use these:**

| File | Entries | Description |
|------|---------|-------------|
| [`positive_stems.txt`](positive_stems.txt) | ~700 | Positive stems (KNU scores +1 and +2). Load into the **Sentiment Analysis** widget as the positive word list. |
| [`negative_stems.txt`](negative_stems.txt) | ~1,400 | Negative stems (KNU scores −1 and −2). Load into the **Sentiment Analysis** widget as the negative word list. |

**For Week 9 in R → Use this:**

| File | Entries | Description |
|------|---------|-------------|
| [`SentiWord_Dict_stems.txt`](SentiWord_Dict_stems.txt) | ~2,100 | Full stem-indexed KNU with intensity scores (−2 to +2). Tab-separated: `stem⟨tab⟩score`. Load with `read_tsv()` and `left_join()` to your tokenized text. |

## Why "stems"?

Korean is agglutinative — one verb or adjective has dozens of inflected forms (e.g., `행복하다`, `행복합니다`, `행복했다`, `행복해`). You can't match all those forms against a dictionary entry unless both sides share a common *stem*.

Our preprocessing script ([`sentiment_preprocessing_mac-users.py`](../scripts/sentiment_preprocessing_mac-users.py)) tokenizes tweets with **Kiwi** and outputs content-word stems. The dictionary files in this folder were built by running every KNU entry through the same Kiwi pipeline and keeping the primary content stem.

The result: both sides of the lookup use the same form, so matching "just works."

## What about the other files?

These are **source files** — you normally don't need them:

| File | What it is |
|------|------------|
| `SentiWord_Dict.txt` | The original KNU dictionary (word + score). Unstemmed — contains mixed inflected and citation forms. Included for reference and R users who want to apply their own stemming. |
| `positive.txt`, `negative.txt` | The original KNU polarity lists, unstemmed. Included for reference. |
| `pos_pol_word.txt`, `neg_pol_word.txt`, `SentiWord_info.json`, `ReadMe.txt` | Original files from the KNU distribution. Included for provenance. |

**Unless you have a reason to use them, stick with the `*_stems.txt` files.**

## Source and citation

- **Original dictionary:** Park, S., Kim, E., Na, J., Yoon, H., & Lee, C. (2018). KNU Korean Sentiment Lexicon. Kunsan National University. [GitHub](https://github.com/park1200656/KnuSentiLex)
- **Stem versions** (files in this folder named `*_stems.txt`): built locally for this course by tokenizing KNU entries with [Kiwi](https://github.com/bab2min/Kiwi) via `kiwipiepy`.
