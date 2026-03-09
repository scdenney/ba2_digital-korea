---
layout: default
title: Midterm Assessment
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
.quiz-button {
  display: block;
  background: #002147;
  color: #fff !important;
  text-align: center;
  padding: 0.75rem 1.25rem;
  border-radius: 6px;
  font-weight: 600;
  font-size: 1rem;
  margin: 1rem 0;
  text-decoration: none !important;
}
.quiz-button:hover { background: #003366; }
.password-box {
  background: #fffbeb;
  border: 1px solid #f59e0b;
  border-radius: 6px;
  padding: 0.6rem 1rem;
  margin: 0.75rem 0;
  font-size: 0.95rem;
}
.password-box strong { color: #92400e; }
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

# Midterm Assessment

**Date:** Monday, March 9, 2026 · In class

<div class="schedule-card">
  <div class="row">
    <span class="time">15:15–15:20</span>
    <span class="label">Announcements</span>
  </div>
  <div class="row">
    <span class="time">15:20–16:00</span>
    <span class="label">Midterm assessment (40 minutes)</span>
  </div>
  <div class="row">
    <span class="time">16:00–16:10</span>
    <span class="label">Break</span>
  </div>
  <div class="row">
    <span class="time">16:10–17:00</span>
    <span class="label">Discussion: the rest of the term</span>
  </div>
</div>

<p class="clock-note">You have 40 minutes to complete both parts. The clock starts at 15:20.</p>

---

## Part 1: Concepts Quiz (10–15 min)

Complete the online multiple-choice quiz covering key concepts from Weeks 1–5: Korean morphological analysis, the preprocessing pipeline, Bag of Words and TF-IDF, and descriptive exploration in Orange Data Mining.

**Please take this on your laptop** (not your phone).

<a class="quiz-button" href="https://leidenuniv.eu.qualtrics.com/jfe/form/SV_e2LcUtDEfwYS7jg" target="_blank" rel="noopener">Take the Quiz</a>


- 10 multiple-choice questions, one per page
- Work independently
- Closed book, closed notes — you may **not** look up answers, use notes, or consult any outside resources
- Do **not** leave the survey page until you have completed the assessment

---

## Part 2: Preprocessing Task (20–25 min)

Download a small corpus of 15 presidential speeches that you have **not** worked with before. Build a complete preprocessing and visualization pipeline **from scratch** in Orange Data Mining.

<div class="warning-box">
  <strong>Start a fresh Orange session.</strong> Close any existing Orange windows and do <strong>not</strong> load a previously saved workflow — build the pipeline from scratch. This is part of the assessment.
</div>

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
