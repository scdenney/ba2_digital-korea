# Korean Sentiment Dictionaries

This folder contains Korean sentiment dictionaries for Week 9 (Sentiment Analysis).

## What we use in Week 9

**KNU Korean Sentiment Lexicon** (Park et al. 2018) — a widely-cited Korean sentiment dictionary. We use the binary positive/negative word lists with Orange's Sentiment Analysis widget (Custom Dictionary option).

| File | Entries | Description |
|------|---------|-------------|
| [`positive.txt`](positive.txt) | 4,868 | Positive Korean words (one per line). Load into Sentiment Analysis as the positive list. |
| [`negative.txt`](negative.txt) | 9,824 | Negative Korean words (one per line). Load into Sentiment Analysis as the negative list. |

**Format**: plain text, one word per line, no header. Contains a mix of single words (`감사`, `희망`, `위기`), inflected forms (`행복하다`, `가난하다`), and some multi-word phrases. When combined with Kiwi morphological preprocessing on the tweet side, most single-word entries match cleanly.

**Citation**: Park, S. et al. (2018). KNU Korean Sentiment Lexicon. [github.com/park1200656/KnuSentiLex](https://github.com/park1200656/KnuSentiLex)

## Orange workflow

```
File → Corpus → Python Script (Kiwi preprocessing)
     → Corpus (re-map text feature to processed_text)
     → Sentiment Analysis (Method = Custom Dictionary,
                           load positive.txt + negative.txt)
     → Box Plot (subgroup by period3)
```

The Python Script tokenizes each tweet with [Kiwi](https://github.com/bab2min/Kiwi), a standard Korean morphological analyzer, and keeps content-word morphemes (nouns, verbs, adjectives) of length ≥ 2. The script is in [`data/scripts/sentiment_preprocessing_*.py`](../scripts/sentiment_preprocessing_mac-users.py).

## Scoring formula

Orange's Sentiment Analysis widget with Custom Dictionary computes:

    sentiment = 100 × (pos_hits − neg_hits) / num_tokens

Where `pos_hits` is the number of unique tokens in the document that match the positive list, and `neg_hits` is the same for the negative list. The score is a length-normalized percentage — a tweet with 2 positive matches in 20 tokens gets +10, a tweet with the same matches in 10 tokens gets +20.

The interactive exercise on the course website pre-computes these scores using the exact same formula, so your Orange Box Plot will match the interactive's distribution.

## Advanced / reference files

These files are not required for Week 9 but are kept for deeper analysis:

### Full KNU with intensity scores

| File | Description |
|------|-------------|
| [`SentiWord_Dict.txt`](SentiWord_Dict.txt) | Full KNU, tab-separated `word⟨tab⟩score` with scores from −2 to +2. Load in R with `read_tsv()` for weighted intensity analysis. |
| `pos_pol_word.txt`, `neg_pol_word.txt`, `ReadMe.txt`, `SentiWord_info.json` | Original files from the upstream KNU repository, kept for provenance. |

### Stem-indexed KNU (for Kiwi-tokenized R analysis)

| File | Description |
|------|-------------|
| [`SentiWord_Dict_stems.txt`](SentiWord_Dict_stems.txt) | KNU with content stems extracted via Kiwi, with scores −2 to +2 |
| [`positive_stems.txt`](positive_stems.txt), [`negative_stems.txt`](negative_stems.txt) | Stem-indexed polarity lists |

### Chen & Skiena (2014) Korean lexicon

| File | Description |
|------|-------------|
| [`positive_words_ko.txt`](positive_words_ko.txt), [`negative_words_ko.txt`](negative_words_ko.txt) | Chen & Skiena's Korean sentiment lists. This is what Orange's Sentiment Analysis widget uses internally if you pick Method = *Multilingual* and Language = *Korean*. Different dictionary, same set-intersection formula. |

## Other Korean sentiment dictionaries worth knowing

- **KOSAC** (Jang et al. 2013) — ~11,275 sentiment expressions with 5-class polarity and intensity, manually annotated on Korean news. [word.snu.ac.kr/kosac](http://word.snu.ac.kr/kosac/)
- **NRC Emotion Lexicon** — ~14,000 English words across 8 emotions plus positive/negative, machine-translated to 100+ languages including Korean. [saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm](https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm)
- **KSenticNet** — 5,465 Korean words with continuous sentic values. [github.com/zzaebok/ksenticnet](https://github.com/zzaebok/ksenticnet)
