---
layout: default
title: Midterm Assessment
---

# Midterm Assessment

**Date:** Monday, March 9, 2026 · In class

**15:15–15:20** — Announcements
**15:20–16:00** — Midterm assessment (40 minutes)
**16:00–16:10** — Break
**16:10–17:00** — Discussion: the rest of the term

You have **40 minutes** to complete both parts of the assessment. The clock starts at 15:20.

---

## Part 1: Concepts Quiz (10–15 min)

Complete the online multiple-choice quiz covering key concepts from Weeks 1–5: Korean morphological analysis, the preprocessing pipeline, Bag of Words and TF-IDF, and descriptive exploration in Orange Data Mining.

**Please take this on your laptop** (not your phone).

**Survey link:** [https://leidenuniv.eu.qualtrics.com/jfe/form/SV_e2LcUtDEfwYS7jg](https://leidenuniv.eu.qualtrics.com/jfe/form/SV_e2LcUtDEfwYS7jg)

**Password:** `ba2`

- 10 multiple-choice questions, one per page
- Work independently
- Closed book, closed notes — you may **not** look up answers, use notes, or consult any outside resources
- Do **not** leave the survey page until you have completed the assessment

---

## Part 2: Preprocessing Task (20–25 min)

Download a small corpus of 15 presidential speeches that you have **not** worked with before. Build a complete preprocessing and visualization pipeline **from scratch** in Orange Data Mining.

### Before you begin

**Start a fresh Orange session.** Close any existing Orange windows and do **not** load a previously saved workflow — build the pipeline from scratch. This is part of the assessment.

### Corpus

**[president_speeches_assessment.csv]({{ '/data/president_speeches/president_speeches_assessment.csv' | relative_url }})**

A small corpus of 15 presidential speeches that you have not worked with before.

### What you need to do

Using Orange Data Mining, build a complete preprocessing and visualization pipeline for this corpus — from raw text to a clean Word Cloud. You should be able to do this based on what we have covered in Weeks 2–5.

Then write a short reflection (e.g., `midterm_reflection.md`) containing:

- One research question you could investigate using this corpus and the methods we've learned
- 2–3 sentences explaining what you would expect to find and why — connect your expectation to what you know about the speeches (presidents, time periods, speech types)

### What to submit

Create a `midterm/` folder inside `assignments/` in your repository containing:

| File | Description |
|---|---|
| `president_speeches_assessment.csv` | The corpus data file |
| workflow file (`.ows`) | Your Orange Data Mining workflow |
| Word Cloud screenshot (`.png`) | Screenshot of your Word Cloud output |
| reflection file (`.md`) | Your research question and expected findings |

**Steps:**

1. Add all four files to the `midterm/` folder
2. In GitHub Desktop: write a short commit message (e.g., "Add midterm assessment")
3. Click **Commit to main**, then **Push origin**
4. Confirm your files appear on github.com in your repository
5. Mark your completion on the [shared Google Sheet](https://docs.google.com/spreadsheets/d/1gYzaIKDgJ81MEp4xa3GYrV_oFpU1OSAw3YyaddeLfqk/edit?usp=sharing) in the **Midterm** column

---

## Grading

| Component | Scoring | Weight |
|---|---|---|
| Concepts Quiz (10 questions) | 1 point each | Weighted to **8 points**: (raw / 10) &times; 8 |
| Preprocessing Task | 0, 1, or 2 points (see rubric) | **2 points** |
| **Total** | | **out of 10** |

**Preprocessing task rubric:**

| Score | Criteria |
|---|---|
| **0** | Did not preprocess, or did not follow directions (e.g., loaded a previous workflow) |
| **1** | Attempted but incomplete — missing steps, pipeline errors, or output not clean |
| **2** | Successful end-to-end preprocessing with clean Word Cloud output and thoughtful reflection |
