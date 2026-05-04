---
layout: default
title: Final Assessment
---

<style>
.schedule-card {
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 1rem 1.25rem;
  margin: 1rem 0 1.25rem;
}
.schedule-card .row {
  display: flex;
  align-items: baseline;
  padding: 0.35rem 0;
  border-bottom: 1px solid #f3f4f6;
  font-size: 0.95rem;
}
.schedule-card .row:last-child { border-bottom: none; }
.schedule-card .time {
  width: 130px;
  flex-shrink: 0;
  font-weight: 600;
  color: #002147;
}
.schedule-card .label { color: #374151; }
.clock-note {
  font-size: 0.95rem;
  color: #002147;
  font-weight: 600;
  margin-top: 0.5rem;
}
.quiz-placeholder {
  display: block;
  background: #f3f4f6;
  color: #4b586b;
  text-align: center;
  padding: 0.75rem 1.25rem;
  border-radius: 6px;
  font-weight: 600;
  font-size: 1rem;
  margin: 1rem 0;
  border: 1px dashed #c8ccd3;
}
.warning-box {
  background: #fef2f2;
  border-left: 3px solid #ef4444;
  padding: 0.6rem 1rem;
  border-radius: 0 4px 4px 0;
  font-size: 0.9rem;
  color: #991b1b;
  margin: 1rem 0;
}
</style>

# Final Assessment

**Date:** Monday, 4 May 2026 · In class

<div class="schedule-card">
  <div class="row">
    <span class="time">15:15–15:20</span>
    <span class="label">Announcements</span>
  </div>
  <div class="row">
    <span class="time">15:20–16:20</span>
    <span class="label">Final assessment (60 minutes — quiz + application exercise)</span>
  </div>
  <div class="row">
    <span class="time">16:20–16:30</span>
    <span class="label">Break</span>
  </div>
  <div class="row">
    <span class="time">16:30–17:00</span>
    <span class="label">Discussion · introduction to the final paper</span>
  </div>
</div>

<p class="clock-note">You have 60 minutes to complete both parts. The clock starts at 15:20.</p>

The assessment has two parts, both completed during class on your laptop. The quiz covers the second-half methods from Weeks 7–10 (clustering, word embeddings, sentiment analysis, LDA / topic modeling). The application exercise asks you to build an Orange Data Mining pipeline that answers a research question on a new corpus.

---

## Part 1 — Online Quiz (~15 min)

Ten multiple-choice questions covering Weeks 7–10. Auto-graded, one point per correct answer.

<div class="quiz-placeholder">The Qualtrics link will be provided in class on 4 May.</div>

- 10 multiple-choice questions, one per page
- Work independently
- Closed book, closed notes — you may **not** look up answers, use notes, or consult any outside resources
- Do **not** leave the survey page until you have completed the quiz

---

## Part 2 — Application Exercise (~45 min)

Build pipelines in Orange Data Mining to answer **two of the three sub-tasks** below. You may either do both sub-tasks on a single dataset or do one sub-task on each — your choice.

For each sub-task, your answer rests on a visualization. **Box Plot, violin plot, dendrogram, LDAvis view, t-SNE scatter, Word Cloud, and bar plot** are all fair game — pick whichever best supports the claim you want to make.

<div class="warning-box">
  <strong>Start a fresh Orange session.</strong> Do not load a previously saved workflow — build the pipeline from scratch. This is part of the assessment.
</div>

### Datasets

Two CSVs and a short Korean→English data-dictionary key for the petition category values are linked from the [Data & Scripts]({{ '/data/' | relative_url }}) page (Week 11 row). Pick one or both:

- **`dataset1_kjyg_sample.csv`** — 360 articles from *Kyongje Yongu* (경제연구), the DPRK economics journal, 1987–2017. Balanced 120 articles per leader era (Kim Il-sung, Kim Jong-il, Kim Jong-un). Useful columns: `era`, `year`, `issue`, `title`, `text`.
- **`dataset2_bluehouse_petitions_sample.csv`** — 360 citizen petitions from the Cheong Wa Dae online platform, 2017–2018, balanced 60 per category. Useful columns: `category`, `year`, `votes`, `title`, `text`.

### The three sub-tasks

**Task A — Did NK economic discourse shift tone across leader eras?**
Dataset: `dataset1_kjyg_sample.csv`. Research question: is the sentiment of *Kyongje Yongu* articles measurably different across the three NK leader eras?
A good answer names the direction and rough size of the shift across eras and supports the claim with a visualization.

**Task B — What latent topics cut across the petition categories?**
Dataset: `dataset2_bluehouse_petitions_sample.csv`. Research question: identify the latent topics in the petitions and look at how they map onto the six official categories. Some topics will line up neatly with one category; others will cross-cut several.
A good answer labels two or three of the topics in plain language and identifies at least one category where one of those topics is clearly more or less prevalent than the others.

**Task C — What makes each cluster distinctive? (either dataset)**
Dataset: your choice — either CSV. Research question: cluster the documents into 3–5 groups and characterize what makes each cluster distinctive in vocabulary or tone.
A good answer gives each cluster a short label of your own and points to the vocabulary or sentiment evidence behind the label.

### What to submit

Push the following to a **`week11/` folder** in your GitHub repository:

| File | Description |
|---|---|
| `workflow.ows` | Your Orange workflow |
| Exported figures (`.png`) | Use each widget's built-in export option (right-click → Save Image, or the disk/camera icon). Label each clearly, e.g., `figure1_sentiment_by_era.png` |
| `analysis.md` | Short write-up — see below |

`analysis.md` should, for each of your two sub-tasks: state which sub-task and on which dataset; refer to your figures by their labels (embedding the figures directly in the markdown is encouraged); answer the research question in 2–4 sentences citing the figure(s); and reflect on the figures themselves — what they show, what stood out, anything surprising or hard to interpret.

**Steps:**

1. Add all files to the `week11/` folder in your repo
2. In GitHub Desktop: write a short commit message
3. Click **Commit to main**, then **Push origin**
4. Confirm your files appear on github.com in your repository

### Tips

- The preprocessing scripts on the [Data & Scripts]({{ '/data/' | relative_url }}) page are heavily annotated. By now you should be comfortable making at least light modifications — at minimum set `TEXT_COLUMN = 'text'` (both Week 11 CSVs use that column).
- Save your workflow as you go (`File → Save As`, `.ows`). If Orange crashes you don't want to start over.
- Look at the data once before you trust the model (Corpus Viewer or Word Cloud after preprocessing). Bad tokenization is easy to spot in 30 seconds.
- Pick the sub-task you can finish, not the one that sounds most impressive. A complete Task A beats an abandoned Task B.

---

## Grading

| Component | Scoring | Weight |
|---|---|---|
| Concepts Quiz (10 questions) | 1 point each | Weighted to **8 points**: (raw / 10) × 8 |
| Application Exercise | 0, 1, or 2 points (see rubric) | **2 points** |
| **Total** | | **out of 10** |

**Application-exercise rubric:**

| Score | Criteria |
|---|---|
| **0** | Did not complete, or did not follow directions (e.g., loaded a previous workflow) |
| **1** | Attempted but incomplete — missing steps, pipeline errors, or write-up does not answer the question |
| **2** | Successful end-to-end pipeline; clear answer to the research question with a labeled figure cited from the write-up |

---

## Study Guide

The Week 11 study guide PDF is on the [Presentations]({{ '/presentations/' | relative_url }}) page: [Week 11 Assessment Study Guide]({{ '/presentations/week11-study-guide.pdf' | relative_url }}). It covers the four second-half methods (clustering, word embeddings, sentiment, LDA), the workflows for each, and the key terms.
