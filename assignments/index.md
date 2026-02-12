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

Download the corpus from the [Data]({{ '/data/' | relative_url }}) page.

**Steps:**
1. Download the presidential speeches CSV from the Data page
2. Add it to a subfolder in your repo (e.g., `/data/president_speeches/`)
3. Commit and push via GitHub Desktop
4. Open Orange Data Mining
5. Add a **Corpus** widget and load the CSV from your data folder
6. Explore the corpus -- browse speeches, filter, search
7. Save your workflow (`.ows` file)

**Submission:** Upload your `.ows` file and a screenshot of your Orange workflow to your GitHub repository.

</div>
</details>

<details>
<summary>Week 3: Text Preprocessing &amp; Word Cloud</summary>
<div class="assignment-content" markdown="1">

**Assigned:** Feb. 16
**Due:** Feb. 23 (before class)

**Required — R Programming:**

Complete DataCamp: Introduction to Text Analysis in R — Chapter 1: Wrangling Text.

**Optional — Preprocessing Practice (choose one or both):**

Practice the full Korean text preprocessing pipeline on the presidential speeches corpus using Orange Data Mining, R, or both. To demonstrate your preprocessing, generate a word cloud from the result — this is a quick way to verify that your pipeline is working and producing meaningful output.

**Option A: Orange Data Mining**

1. Open Orange and create a new workflow
2. Load the presidential speeches corpus using the **Corpus** widget
3. Add a **Preprocess Text** widget — connect it to Corpus
4. Add the Korean preprocessing Python script (provided in class) using the **Python Script** widget
5. Add a **Word Cloud** widget — connect it to the output
6. Adjust settings until you have a meaningful word cloud
7. Save your deliverables (see below)

**Saving your ODM work:**
- **Screenshot:** Right-click the canvas background and select **Save As Image**, or use your system screenshot tool (`Cmd+Shift+4` on macOS, `Win+Shift+S` on Windows)
- **Workflow file:** Go to **File → Save As** and save with the `.ows` extension

**Option B: RStudio**

1. Download the R script: [week03_preprocessing.R]({{ '/data/scripts/week03_preprocessing.R' | relative_url }})
2. Open it in RStudio
3. Read the comments — the script walks you through each step
4. Run the script section by section (select lines and press `Ctrl+Enter` / `Cmd+Enter`)
5. The script will save `wordcloud.png` to your working directory

**Note:** The first run installs Python + Kiwi automatically (this takes a few minutes). After that, you can skip the installation steps.

**Submitting your work:**

1. Create a `week03/` folder inside `assignments/` in your repository
2. Add your deliverables to that folder:
   - **ODM:** screenshot (`.png`) + workflow file (`.ows`)
   - **R:** the saved word cloud image (`wordcloud.png`)
3. In GitHub Desktop: you will see the new files listed as changes
4. Write a short commit message (e.g., "Add week 3 word cloud")
5. Click **Commit to main**, then **Push origin**
6. Confirm your files appear on github.com in your repository

The instructor has access to your repository and will review your submission there.

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
