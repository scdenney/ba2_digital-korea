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
  transition: transform 0.2s;
}

.assignment-accordion details[open] summary::before {
  content: "−";
}

.assignment-accordion .assignment-content {
  padding: 0 1.25rem 1.25rem 2.5rem;
  color: #333;
}

.assignment-accordion .assignment-meta {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 1rem;
}

.assignment-accordion table {
  margin: 1rem 0;
  font-size: 0.95rem;
}

.assignment-accordion th,
.assignment-accordion td {
  padding: 0.5rem 1rem;
}
</style>

# Assignments

Assignments are posted here as they are assigned. Not every week has an assignment; some weeks involve only in-class work. Refer to the [Syllabus]({{ '/syllabus/syllabus.html' | relative_url }}) for the complete schedule.

**Standing policy:** All assignments are due by the beginning of the next class unless otherwise specified.

---

<div class="assignment-accordion">

<details open>
<summary>Week 1: R Programming with Swirl</summary>
<div class="assignment-content">
<div class="assignment-meta">
<strong>Assigned:</strong> Feb. 02 · <strong>Due:</strong> Feb. 09 (before class)
</div>

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
