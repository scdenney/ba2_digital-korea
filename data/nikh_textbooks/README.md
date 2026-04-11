# NIKH Korean History Textbooks

Samples from the **NIKH corpus** (National Institute of Korean History, 국사편찬위원회) — a collection of 67 Korean history textbooks spanning 1895–2016. Originally used for studying how Korean history has been presented across political eras.

## Files in this folder

| File | Rows | Description |
|------|------|-------------|
| [`nikh_textbooks_demo.csv`](nikh_textbooks_demo.csv) | 9 | 9 textbooks across three eras (Colonial, Authoritarian, Democratic). Includes a `processed_text` column (pre-tokenized nouns) so you can start analysis without running preprocessing first. Used in **Week 5**. |
| [`nikh_clustering_demo.csv`](nikh_clustering_demo.csv) | 11 | 11 textbooks (3 Colonial, 4 Authoritarian, 4 Democratic). Contains raw `full_text` only — you preprocess it yourself as part of the exercise. Used in **Week 7 (Clustering)**. |

## Columns

| Column | Description |
|--------|-------------|
| `book_id` | Unique identifier |
| `title` | Book title (Korean) |
| `era` | `Colonial`, `Authoritarian`, or `Democratic` |
| `period` | More detailed period label |
| `level` | Elementary / Middle / High |
| `year` | Publication year |
| `full_text` | Complete textbook body (Korean) |
| `processed_text` | Pre-tokenized nouns (only in the Week 5 demo file) |

## Source

Full corpus and documentation: [nlp_corpora/nikh](https://github.com/scdenney/nlp_corpora/tree/main/data/nikh)
