---
layout: default
title: Final Paper — Research Report with Replication Repository
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
  width: 160px;
  flex-shrink: 0;
  font-weight: 600;
  color: #002147;
}
.schedule-card .label { color: #374151; }
.menu-button {
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
.menu-button:hover { background: #003366; }
</style>

# Final Paper

**Released** 4 May 2026 (in class) · **Workshop** 11 May 2026 · **Due** Friday 5 June 2026, 23:59 (Brightspace)
**Length** 2,000–5,000 words (excluding references, figures, appendix) · **Format** PDF + public GitHub replication repository

<div class="schedule-card">
  <div class="row">
    <span class="time">Mon 4 May</span>
    <span class="label">Brief released in class</span>
  </div>
  <div class="row">
    <span class="time">Mon 11 May</span>
    <span class="label">Workshop — bring dataset choice + draft RQ; we'll review together and you'll workshop your plan with classmates</span>
  </div>
  <div class="row">
    <span class="time">11 May – 5 Jun</span>
    <span class="label">Write the paper, build the replication repository</span>
  </div>
  <div class="row">
    <span class="time">Fri 5 Jun, 23:59</span>
    <span class="label"><strong>PDF + repo URL due on Brightspace</strong></span>
  </div>
</div>

<a class="menu-button" href="{{ '/presentations/week12-final-paper-brief.pdf' | relative_url }}" target="_blank" rel="noopener">Download the Brief (PDF)</a>

<a class="menu-button" href="https://github.com/scdenney/ba2-final-paper-data" target="_blank" rel="noopener">Open the Dataset Menu</a>

**Writing style:** follow the [BAKS Style Guide](https://scdenney.github.io/thesis-supervision/) for citation, formatting, and prose conventions.

---

## Overview

The final paper is a short research report. You generate a research question, answer it with computational text analysis methods learned in this course, and publish a public replication repository so any reader can re-run your analysis and confirm your findings. The paper is the headline product; the replication repository is what makes the work count as research.

Pick one corpus from the [curated dataset menu](https://github.com/scdenney/ba2-final-paper-data). The menu deliberately excludes everything you have already worked with this term, so you will be exposed to a corpus you have not yet handled. Use that corpus to answer one research question of your own.

## The Week 12 workshop (11 May)

The workshop session is for two things. First, I will review your draft research question and dataset choice with you in conversation; this is the moment to surface scoping or feasibility issues before you commit. Second, you will workshop your analysis plan with classmates, who are working on different corpora and will see issues you miss. Arrive with a corpus picked from the menu and a draft research question phrased as a single sentence.

## Required structure

Suggested word allocations are guidance; the **2,000–5,000-word total** is what counts.

### Research question (~150–250 words)

State your research question clearly in one sentence. Briefly motivate it: why does the question matter, and what kind of answer would count as informative? Specify the kind of answer you expect (e.g., "three to five distinct topical clusters whose prevalence varies across leader era").

### Brief literature review (~250–400 words; 3–5 sources)

Anchor your question in scholarly conversation; do not survey the field. At least one source must be a methods source (e.g., a chapter from Grimmer, Roberts & Stewart, or a journal article using the same method). The remainder should be substantive Korea-area scholarship that your question engages.

### Data and methods (~400–600 words)

Describe *before* you show results: the corpus, the slice you analyse, your preprocessing decisions, and the methods you apply with reasons. A reader of this section should be able to predict roughly what your findings will contain.

### Analysis and findings (~600–1,500 words; 1–3 figures or tables)

Apply your methods. Each figure or table is labelled clearly and referred to in the text. Figures are exported from Orange or generated in R, embedded inline in the PDF, and also placed in the `figures/` folder of your replication repository.

### Summary and conclusion (~250–400 words)

Summarise your headline finding. Reflect briefly on the limitations of your analysis and what a follow-up project might do next. Mention anything that surprised you or that you couldn't fully explain.

## Replication and FAIR

Create a *new*, *public* GitHub repository — separate from your weekly-coursework repository — that anyone can clone to reproduce your analysis. Structure it per the [FAIR principles](https://www.go-fair.org/fair-principles/) (Findable, Accessible, Interoperable, Reusable). Required contents:

| File / folder | Purpose | FAIR |
|---|---|---|
| `README.md` | Project description, RQ, headline finding, instructions to reproduce | F, A |
| `data/` *or* `data/SOURCE.md` | The CSV directly, or a `SOURCE.md` pointing to the menu repo URL + commit hash | F, A |
| `data/data_dictionary.md` | Column-by-column with types, units, examples | R |
| `analysis/` | Your Orange `.ows` workflow file and/or R script(s) | R, I |
| `figures/` | PNG exports of every figure that appears in your paper | F, A |
| `LICENSE` | MIT for code, CC-BY-4.0 for any data you produced | R |
| `CITATION.cff` | Author, paper title, course, date | F, R |
| `requirements.md` | Orange version, R version, non-default packages | I |

A worked example is in the [`examples/`](https://github.com/scdenney/ba2-final-paper-data/tree/main/examples) folder of the menu repo. Spot-checks: I will clone two or three replication repositories per cohort on a fresh machine and re-run the analysis; reproducibility failures count against this component of the grade.

## Submission

Submit two items on Brightspace by 23:59 on **Friday 5 June 2026**: the paper as a single PDF, and the URL of your public replication repository pasted into the Brightspace text box.

## Assessment

| Component | Weight | What I am looking for |
|---|---:|---|
| Research question | 15% | Clear, well-scoped, answerable with the chosen corpus and methods |
| Methods application & interpretation | **40%** | Methods applied correctly; output interpreted, not just reported; findings connect back to the question |
| Replication repository (FAIR) | **20%** | All required files present; README explains the project; a fresh clone reproduces the figures |
| Writing quality & structure | 15% | Reads as a scholarly research report; consistent citations; sections do what their headings promise |
| Brief literature review | 10% | 3–5 sources including one methods source; situates the question rather than surveying the field |

A failing grade qualifies for a re-sit per the standing course policy (see [syllabus]({{ '/syllabus/syllabus.html#final-paper' | relative_url }})).

## Tips

- The hard part is the research question, not the methods. A focused, well-scoped RQ makes everything else easier.
- Keep the lit review brief. Three to five sources is the spec; a long lit review eats the word count you need for findings.
- Build the replication repository as you go, not at the end. Commit the workflow file every time you make progress; commit figures as soon as you export them.
- Read the data first. The Corpus Viewer and Word Cloud widgets in Orange catch tokenisation and encoding problems in 30 seconds.
- Combinations of methods are encouraged — clustering with sentiment, LDA with grouping by metadata, embeddings with clustering. Explain the combination in your data and methods section.
- Pre-modern or Hanmun-mixed corpora (colonial magazines, *Kaebyok*) give the morphological analyser more trouble than contemporary Korean. If you choose one, plan for extra preprocessing time and acknowledge the limitation in your data and methods section.
