# Week 11 Final Assessment — Curated Korean Text Datasets

These two CSVs are prepared for the **Week 11 final assessment** of BA2 Digital Korea (4 May 2026). Students load one (or both) into Orange Data Mining via the **File** widget and apply at least two of the four methods covered in the course:

- Hierarchical / k-means clustering
- Word embeddings (KLUE BERT)
- Sentiment analysis (KNU dictionary)
- LDA topic modeling

Both files are UTF-8 encoded, comma-separated, one document per row, with a header row. They were sub-sampled with a fixed random seed (`42`) for reproducibility from larger source corpora maintained at <https://github.com/scdenney/nlp_corpora> and in `ba3_text_as_data/data/`.

The two corpora are deliberately **thematically distinct** so the assessment offers a real choice:

- Dataset 1 is **state-academic prose from North Korea** (the journal *Kyongje Yongu* / Economic Research, published by the Academy of Social Sciences in Pyongyang).
- Dataset 2 is **citizen-vernacular political writing from South Korea** (Cheong Wa Dae Blue House online petitions during the Moon administration).

Both are post-1987 contemporary Korean, both deal heavily with politics and the economy, but they sit at opposite ends of the register spectrum: regime-mediated academic argumentation vs. unmediated grass-roots petitioning.

---

## Dataset 1 — Kyongje Yongu (Economic Research, NK)

**File:** `dataset1_kjyg_sample.csv`
**Rows:** 360 articles
**Size:** ~3.06 MB
**Source:** `ba3_text_as_data/data/kjyg/kjyg_corpus.csv` (2,583-article original, 1987-2017)

*Kyongje Yongu* (경제연구, *Economic Research*) is the flagship economics journal of the DPRK Academy of Social Sciences. Articles offer regime-aligned theoretical and applied economic argumentation — frequently citing the words of the supreme leader and articulating the ideological framing of the planned economy. The corpus spans three decades and three leadership eras, so it is excellent for tracking shifts in NK economic discourse over time.

The sample is **stratified at 120 articles per supreme-leader era**, so every era is equally represented in Box Plot comparisons. Each article is **truncated to 3,500 characters** (about half a typical full article) to keep the file under the 5 MB cap; this is more than enough text for clustering, sentiment, and LDA in Orange.

### Columns

| Column | Type | Description |
|---|---|---|
| `doc_id` | string | Synthetic ID, `kjyg_0000` – `kjyg_0359` |
| `text` | string | Cleaned article body, truncated to 3,500 characters |
| `year` | integer | Publication year (1987–2017) |
| `era` | categorical | NK leader era — `Kim Il-sung (1987-1994)`, `Kim Jong-il (1995-2011)`, `Kim Jong-un (2012-2017)` (120 each) |
| `issue` | string | Issue number within the year (1, 2, 3, 4) |
| `year_issue` | string | `YYYY-N` raw label, e.g. `2015-2` |
| `title` | string | Original Korean article title |
| `author` | string | Article author (or `Unknown` for the few cases where it was missing) |

### Suggested research questions

1. **Did NK economic discourse become more or less positive after Kim Jong-un took power?** Apply the KNU sentiment dictionary to each article, then use the Box Plot widget grouped by `era`. The Kim Jong-un era introduced market-tolerant rhetoric (e.g. "our-style economic management methods") — does that show up as a measurable sentiment shift? (sentiment + Box Plot grouping)
2. **What topics dominate each NK leadership era?** Fit a 6- to 8-topic LDA, then chart topic prevalence by `era`. Expectation: Kim Il-sung articles emphasise Juche / heavy industry; Kim Jong-il articles dwell on the Arduous March / military-first; Kim Jong-un articles introduce science-and-technology and finance themes. (LDA + grouping)
3. **Are early-era and late-era articles linguistically distinct enough to cluster on their own?** Embed articles with KLUE BERT, run hierarchical clustering, then compare the dendrogram to the `era` labels. If the clusters align with leadership eras, that's evidence of measurable diachronic discourse change. (embeddings + clustering)

---

## Dataset 2 — Blue House (Cheong Wa Dae) Citizen Petitions

**File:** `dataset2_bluehouse_petitions_sample.csv`
**Rows:** 360 petitions
**Size:** ~0.60 MB
**Source:** `nlp_corpora/data/bluehouse_petitions/bluehouse_petitions.csv` (18,077-petition original, 2017-2018)

The Cheong Wa Dae online-petitions platform was launched by the Moon Jae-in administration in August 2017. Citizens could post a petition on any topic; petitions reaching 200,000 signatures within 30 days received an official government response. The corpus is a window into what ordinary South Koreans wanted to push onto the national agenda — written in their own voice, not in the register of journalism or academia.

The sample is **stratified at 60 petitions per category** across six thematically distinct categories. Petitions are filtered to 200–4,000 characters so each row is substantive but legible.

### Columns

| Column | Type | Description |
|---|---|---|
| `doc_id` | string | Synthetic ID, `petition_0000` – `petition_0359` |
| `text` | string | Cleaned petition body (Korean) |
| `category` | categorical | Petition category — `정치개혁`, `인권/성평등`, `외교/통일/국방`, `육아/교육`, `보건복지`, `일자리` (60 each) |
| `year` | string | Petition start year (`2017` or `2018`) |
| `start` | string (YYYY-MM-DD) | Petition start date |
| `votes` | integer | Number of signatures the petition received (proxy for resonance) |
| `answered_label` | categorical | `Answered` / `Not answered` (whether the petition met the 200K-signature threshold) |
| `title` | string | Petition title |

### Suggested research questions

1. **Which petition categories carry the most negative emotional tone?** Apply the KNU sentiment dictionary, then use the Box Plot widget grouped by `category`. Hypothesis: human-rights and political-reform petitions (often complaints about specific cases or officials) skew more negative than education or welfare petitions. (sentiment + grouping)
2. **What latent topics cut across the official categories?** Fit an 8- to 10-topic LDA. Use the Box Plot to chart topic prevalence by `category`. Some topics will line up neatly with categories; others will reveal cross-cutting concerns (e.g. a "perceived government inaction" topic appearing across multiple categories). (LDA + grouping)
3. **Do high-signature petitions cluster together stylistically?** Embed petitions with KLUE BERT, run k-means with k=4–6, then check whether `votes` (or a high/low-engagement binning of it) is concentrated in particular clusters. Are the most resonant petitions written in a recognisably distinct rhetorical style? (embeddings + clustering)

---

## Reproducibility

Both files were generated by `build_week11_datasets.py` (this folder) with `random_state=42`. Light cleaning was applied — NFC Unicode normalisation, whitespace collapse, removal of zero-width and BOM characters, removal of URLs and HTML entities, removal of literal `\n`/`\r`/`\t` artefacts that survive JSON-to-CSV pipelines. **No Korean morphological tokenisation** was done; students will do that in Orange via the Python Script widget.

To rebuild from the upstream sources:

```bash
cd private/week11_datasets
python3 build_week11_datasets.py
```

## Verified file sizes

| File | Rows | Size |
|---|---:|---:|
| `dataset1_kjyg_sample.csv` | 360 | 3.06 MB |
| `dataset2_bluehouse_petitions_sample.csv` | 360 | 0.60 MB |

Both are within the 5 MB hard cap. The petitions file is comfortably under the 2 MB ideal target; the KJYG file is larger because *Kyongje Yongu* articles are long state-academic prose even after truncation.
