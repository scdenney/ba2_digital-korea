---
layout: default
title: Assignments
---

<style>
.assignment-accordion {
  margin: 1.5rem 0;
}

.assignment-accordion details {
  background: #fafafa;
  border-left: 4px solid #1e6bb8;
  border-radius: 4px;
  margin-bottom: 1rem;
  box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}

.assignment-accordion summary {
  padding: 1rem 1.25rem;
  cursor: pointer;
  font-weight: 600;
  color: #1e6bb8;
  list-style: none;
  display: flex;
  align-items: center;
}

.assignment-accordion summary::-webkit-details-marker {
  display: none;
}

.assignment-accordion summary::before {
  content: "+";
  margin-right: 0.75rem;
  font-size: 1.2rem;
  font-weight: 400;
  color: #1e6bb8;
}

.assignment-accordion details[open] summary::before {
  content: "−";
}

.assignment-accordion .assignment-content {
  padding: 0 1.25rem 1.25rem 1.25rem;
}
</style>

# Assignments

Assignments are posted here as they are assigned. Not every week has an assignment; some weeks involve only in-class work. Refer to the [Syllabus]({{ '/syllabus/syllabus.html' | relative_url }}) for the complete schedule.

**Standing policy:** All assignments are due by the beginning of the next class unless otherwise specified.

---

<div class="assignment-accordion">

<details>
<summary>Week 1: R Programming with Swirl</summary>
<div class="assignment-content" markdown="1">

**Assigned:** Feb. 02
**Due:** Feb. 09 (before class)

Complete the following Swirl R Programming lessons:

| Lesson | Topic |
|--------|-------|
| 1 | Basic Building Blocks |
| 2 | Workspace and Files |
| 4 | Vectors |
| 6 | Subsetting Vectors |
| 7 | Matrices and Data Frames |
| 12 | Looking at Data |

**How to complete:**
1. Open RStudio
2. Type `library(swirl)` then `swirl()` in the console
3. Select "R Programming" and work through each lesson listed above

**Submission:** You will confirm completion via an in-class poll at the start of Week 2. No screenshots or documentation required.

</div>
</details>

<details>
<summary>Week 2: R Programming &amp; Orange Data Mining</summary>
<div class="assignment-content" markdown="1">

**Assigned:** Feb. 09
**Due:** Feb. 16 (before class)

**R Programming:**

Complete DataCamp: Introduction to Text Analysis in R -- Chapter 1: Wrangling Text.

**Optional: Replicate the in-class Orange demo**

For extra practice, replicate the in-class demo by loading the presidential speeches corpus into Orange Data Mining and exploring it with the Corpus widget.

**Corpus file:** [Download presidential speeches (democratic era)]({{ '/data/president_speeches_democratic_era.csv' | relative_url }}) (~4.4 MB, 749 speeches)

This file contains a proportionally sampled subset of Korean presidential speeches from the democratic era (노태우 through 문재인). See the [data documentation]({{ '/data/README.md' | relative_url }}) for details on the sampling method and variables.

**Steps:**
1. Download the CSV file above
2. Add it to a `/data` folder in your GitHub repository
3. Open Orange Data Mining
4. Add a **Corpus** widget and load the CSV from your `/data` folder
5. Explore the corpus -- browse speeches, filter, search
6. Save your workflow (`.ows` file)

**Submission:** Upload your `.ows` file and a screenshot of your Orange workflow to your GitHub repository.

</div>
</details>

</div>

---

## Uploading Your Work

Unless otherwise noted, coursework must be documented with screenshots and relevant files, then uploaded to your individual GitHub repository. See the [Getting Started]({{ '/getting-started/' | relative_url }}) guide for repository setup and structure.

---

## Optional: Supplementary R Programming

For students interested in developing deeper R programming skills:

**Swirl R Programming:**
- Lesson 5: Missing Values
- Lesson 8: Logic
- Lesson 9: Functions

**Swirl Exploratory Data Analysis:**
- Lesson 13: Dimension Reduction

**DataCamp:**
- Data Manipulation & Visualization
- Intermediate R
- Text Mining with Bag-of-Words in R
