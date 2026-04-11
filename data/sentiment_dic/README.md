# Korean Sentiment Dictionaries

This folder contains Korean sentiment dictionaries for Week 9 (Sentiment Analysis).

## What we use in Week 9

**Chen & Skiena (2014) Korean sentiment lexicon** — this is what Orange's **Sentiment Analysis** widget uses internally when you pick Method = *Multilingual* and Language = *Korean*. It's built into Orange; you don't need to load anything manually. The files are shipped here so you can inspect them, use them in R, or back them up.

| File | Entries | Description |
|------|---------|-------------|
| [`positive_words_ko.txt`](positive_words_ko.txt) | 883 | Positive Korean words (one per line) |
| [`negative_words_ko.txt`](negative_words_ko.txt) | 1,235 | Negative Korean words (one per line) |

**Format**: plain text, one word per line. No header. Binary polarity (each word is either positive or negative, no intensity).

**How Orange uses them**: tokenize each tweet on whitespace and punctuation, take the unique tokens, count how many appear in the positive list (`n_pos`) and how many in the negative list (`n_neg`), output `100 × (n_pos − n_neg) / total_tokens`. This is also what the Week 9 interactive exercise does, so the numbers match.

**Provenance**: Chen, Y. and Skiena, S. (2014). *Building Sentiment Lexicons for All Major Languages*. Proceedings of ACL 2014. Built via knowledge-graph propagation from seed English sentiment words across 44 languages. The Korean lexicon is what Orange downloads at runtime from `http://file.biolab.si/files/sentiment/`.

**Limitations worth knowing**: the lexicon was built automatically, not hand-curated. It contains:
- Some genuine sentiment words (`감사합니다`, `좋은`, `따뜻한`, `어려운`)
- Some grammatical function words mislabeled (`한`, `의`, `다른`)
- Occasional non-Korean entries (Chinese characters, English words)

This is what "automatic broad-coverage lexicon" means in practice. For research work you'd clean it up or replace it with a hand-curated alternative (see below).

---

## Alternative dictionaries (included for reference)

These are not used in Week 9's main workflow, but they're included so you can compare approaches or use them if you continue working with Korean sentiment.

### KNU Korean Sentiment Lexicon (Park et al. 2018)

Hand-assisted dictionary with **intensity scoring** (−2 to +2). Built from the Standard Korean Dictionary (표준국어대사전) with Bi-LSTM classification and human validation.

| File | Entries | Description |
|------|---------|-------------|
| [`SentiWord_Dict.txt`](SentiWord_Dict.txt) | 14,854 | Full KNU, tab-separated `word⟨tab⟩score` with scores −2 to +2 |
| [`positive.txt`](positive.txt) | 4,868 | KNU entries with positive scores |
| [`negative.txt`](negative.txt) | 9,824 | KNU entries with negative scores |
| `pos_pol_word.txt`, `neg_pol_word.txt`, `ReadMe.txt` | — | Original KNU files from the upstream repository |

Stem-indexed variants (built by running KNU entries through Kiwi morphological analyzer):

| File | Entries | Description |
|------|---------|-------------|
| [`SentiWord_Dict_stems.txt`](SentiWord_Dict_stems.txt) | ~2,100 | KNU stems with −2 to +2 scores |
| [`positive_stems.txt`](positive_stems.txt) | ~700 | KNU positive stems |
| [`negative_stems.txt`](negative_stems.txt) | ~1,400 | KNU negative stems |

**When to use KNU**: you want intensity scoring (distinguish "worried" from "devastated"), you're doing research rather than intro teaching, or you want a more hand-curated dictionary than Chen & Skiena.

**How to use KNU in Orange**: drop a **Sentiment Analysis** widget, set Method = *Custom Dictionary*, upload `positive_stems.txt` and `negative_stems.txt`. You'll also want to preprocess tweets with Kiwi first (see `data/scripts/sentiment_preprocessing_mac-users.py`) so tokens match the stem format.

**How to use KNU in R**: `read_tsv("SentiWord_Dict_stems.txt", col_names = c("stem", "score"))`, then tokenize your text and join.

**Citation**: Park, S. et al. (2018). KNU Korean Sentiment Lexicon. [github.com/park1200656/KnuSentiLex](https://github.com/park1200656/KnuSentiLex)

### Other dictionaries worth knowing

- **KOSAC** (Jang et al. 2013) — ~11,275 sentiment expressions with 5-class polarity and intensity, manually annotated on Korean news. Research standard. [word.snu.ac.kr/kosac](http://word.snu.ac.kr/kosac/)
- **NRC Emotion Lexicon** — ~14,000 English words across 8 emotions plus positive/negative polarity. Machine-translated to 100+ languages including Korean. [saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm](https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm)
- **KSenticNet** — 5,465 Korean words with continuous sentic values. Neural/concept-level. [github.com/zzaebok/ksenticnet](https://github.com/zzaebok/ksenticnet)

## File organization

```
sentiment_dic/
├── README.md                      ← this file
├── positive_words_ko.txt          ← Chen & Skiena 2014 (what Week 9 uses)
├── negative_words_ko.txt          ← Chen & Skiena 2014 (what Week 9 uses)
│
├── SentiWord_Dict.txt             ← KNU full dictionary (reference)
├── SentiWord_Dict_stems.txt       ← KNU stems (reference)
├── positive.txt / negative.txt    ← KNU polarity lists (reference)
├── positive_stems.txt / negative_stems.txt  ← KNU stems by polarity (reference)
├── pos_pol_word.txt / neg_pol_word.txt      ← Original KNU source files
├── ReadMe.txt                     ← Original KNU readme
└── SentiWord_info.json            ← Original KNU metadata
```
