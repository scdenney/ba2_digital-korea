---
layout: default
title: Data
---

# Data

This page provides truncated corpora used in class demonstrations and assignments. These are sampled subsets of larger corpora maintained in the [NLP Corpora for Korean Studies](https://github.com/scdenney/nlp_corpora) repository.

**Organizing your data folder:** We recommend creating subfolders within your `/data` directory organized by file type or corpus name -- for example, `/data/president_speeches/`, `/data/newspapers/`, etc. This will keep things tidy as we work with more datasets throughout the semester.

---

| Week(s) | Corpus | Description | Truncation | Full Corpus | Download |
|------|--------|-------------|------------|-------------|----------|
| 2, 3 | Presidential Speeches (Democratic Era) | 749 Korean presidential speeches from the democratic era (6th Republic onward): Roh Tae-woo through Moon Jae-in. Variables include president, title, date, location, speech type, and full text. | Proportionally sampled from 5,840 speeches (random seed 42), with representation across all 7 democratic-era presidents. | [Full corpus](https://github.com/scdenney/nlp_corpora/tree/main/data/president_speeches) | [CSV](president_speeches/president_speeches_democratic_era.csv) (~4.4 MB) |

---

## How to Use These Files

1. Download the CSV file from the link above
2. Add it to a subfolder in your GitHub repository (e.g., `/data/president_speeches/`)
3. Commit and push via GitHub Desktop
4. Load the file in Orange Data Mining using the Corpus widget

For details on sampling methods and variable descriptions, see the [data documentation](president_speeches/README.md).
