---
layout: default
title: Final Assessment — Data Dictionary
---

# Data Dictionary — Week 11 Datasets

Quick reference for the two CSVs used in the [Final Assessment]({{ '/final-assessment/' | relative_url }}). Use this if a Korean label slows you down.

---

## `dataset1_kjyg_sample.csv` — KJYG (NK economics journal)

360 articles, balanced **120 per leader era**.

### Columns

| Column | What it is |
|---|---|
| `text` | Article body (truncated to 3,500 chars) |
| `era` | Leader era — three values, see below |
| `year` | Publication year (1987–2017) |
| `issue` | Issue number within year (1–4) |
| `title`, `author`, `doc_id` | Identifiers |

### `era` values

| Value (as in the CSV) | Period |
|---|---|
| `Kim Il-sung (1987-1994)` | Late Kim Il-sung |
| `Kim Jong-il (1995-2011)` | Full Kim Jong-il |
| `Kim Jong-un (2012-2017)` | Early Kim Jong-un |

---

## `dataset2_bluehouse_petitions_sample.csv` — Cheong Wa Dae petitions

360 petitions, balanced **60 per category**.

### Columns

| Column | What it is |
|---|---|
| `text` | Petition body |
| `category` | One of six categories — see below |
| `year` | 2017 or 2018 |
| `votes` | Number of signatures |
| `title`, `doc_id` | Identifiers |

### `category` values (Korean → English)

| Value (Korean) | English |
|---|---|
| `정치개혁` | Political reform |
| `인권/성평등` | Human rights / gender equality |
| `외교/통일/국방` | Foreign affairs / unification / defense |
| `육아/교육` | Childcare / education |
| `보건복지` | Health and welfare |
| `일자리` | Jobs / employment |

> **Heads-up:** the `answered_label` column is *Not answered* for every petition in this sample, so don't use it as a grouping variable.
