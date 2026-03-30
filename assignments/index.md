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

Download the corpus from the [Data & Scripts]({{ '/data/' | relative_url }}) page.

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
<summary>Week 3: Text Preprocessing Basics</summary>
<div class="assignment-content" markdown="1">

**Assigned:** Feb. 16
**Due:** Feb. 23 (before class)

**Required — R Programming:**

Complete DataCamp: Introduction to R — Chapter 1 (Intro to Basics) and Chapter 2 (Vectors).

**Optional — Preprocessing Practice (choose one or both):**

Practice the full Korean text preprocessing pipeline on the presidential speeches corpus using Orange Data Mining, R, or both. To demonstrate your preprocessing, generate a word cloud from the result — this is a quick way to verify that your pipeline is working and producing meaningful output.

**Option A: Orange Data Mining**

Download the preprocessing script for your OS from the [Data & Scripts]({{ '/data/' | relative_url }}) page. Refer to the widget pipeline on the [Presentations]({{ '/presentations/' | relative_url }}) page (Orange column) for the full workflow.

1. Open Orange and create a new workflow
2. Load the presidential speeches corpus using the **Corpus** widget
3. Add a **Preprocess Text** widget — connect it to Corpus
4. Add a **Python Script** widget and paste the preprocessing script
5. Change `TEXT_COLUMN` to match your corpus column name
6. Add a **Word Cloud** widget — connect it to the output
7. Adjust settings until you have a meaningful word cloud
8. Save your deliverables (see below)

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

<details>
<summary>Week 4: From Words to Numbers — BoW &amp; TF-IDF</summary>
<div class="assignment-content" markdown="1">

**Assigned:** Feb. 23
**Due:** Mar. 02 (before class) | **R Programming extended deadline: Mar. 09, 15:15**

**Required — R Programming:**

Complete DataCamp: Introduction to R — Factors Chapter and Matrices Chapter.

**Orange Data Mining Workflow:**

Reproduce the in-class Orange workflow to practice building a complete text analysis pipeline from corpus to visualization.

1. **Corpus** widget: load the presidential speeches CSV
2. **Python Script** widget: paste the preprocessing script for your OS
3. **Corpus** widget (second): reload to pick up processed text
4. **Preprocess Text**: tokenize by whitespace, load stopword list
5. **Bag of Words**: select **TF-IDF** weighting
6. Connect at least **two visualization widgets** (Word Cloud, Bar Plot, Distributions, or Statistics)
7. Take a screenshot of your workflow

**Submitting your work:**

1. Create a `week04/` folder inside `assignments/` in your repository
2. Add your deliverables:
   - Workflow file (`.ows`)
   - Screenshot of your Orange workflow (`.png`)
   - Two visualization figures (`.png`): one from **raw counts** (BoW Count) and one from **TF-IDF** (e.g., Word Cloud, Bar Plot, or another widget for each)
3. In GitHub Desktop: write a short commit message (e.g., "Add week 4 workflow")
4. Click **Commit to main**, then **Push origin**
5. Confirm your files appear on github.com in your repository
6. Mark your completion on the [shared Google Sheet](https://docs.google.com/spreadsheets/d/1gYzaIKDgJ81MEp4xa3GYrV_oFpU1OSAw3YyaddeLfqk/edit?usp=sharing)

</div>
</details>

<details>
<summary>Week 5: Practice &amp; Deepen — Midterm Prep</summary>
<div class="assignment-content" markdown="1">

**Assigned:** Mar. 02
**Due:** Mar. 09 (before class)

**Required — R Programming:**

Complete DataCamp: Introduction to R — Factors Chapter and Matrices Chapter (extended deadline: **Mar. 09, 15:15**).

**Midterm Preparation:**

The **Week 6 midterm assessment** has two parts:

1. **Online quiz** (~20 min) — multiple-choice questions covering concepts from Weeks 1–5.
2. **Hands-on task** (~20 min) — download a small new corpus, preprocess it in Orange, and produce a clean Word Cloud. Upload your `.ows` file, a saved Word Cloud image, and a short `.md` file (research question + expected findings) to your GitHub repo.

Use the study guide to review all key concepts, the preprocessing pipeline, BoW/TF-IDF, and the Orange workflow.

**Study Guide:** [Week 6 Assessment Study Guide (PDF)]({{ '/presentations/week05-study-guide.pdf' | relative_url }})

**How to prepare:**
- Review the study guide — work through the self-check questions
- Practice building Orange workflows end-to-end (File → Corpus → Python Script → Corpus → BoW → Visualization)
- Make sure you understand *why* each preprocessing step exists, not just *how* to do it

</div>
</details>

<details>
<summary>Week 6: Midterm Review Week</summary>
<div class="assignment-content" markdown="1">

**Assigned:** Mar. 09
**Due:** Mar. 16 (before class)

**R Programming:**

Complete DataCamp: Introduction to R — Lists Chapter and Data Frames Chapter.

**Orange Data Mining Tutorials:**

Watch the following four tutorials before next class. These cover the clustering methods we will use in Week 7:

- [Hierarchical Clustering](https://www.youtube.com/watch?v=dJ5z2SRwzgs) (Getting Started #05)
- [k-Means](https://www.youtube.com/watch?v=vgmL808eSw4) (Getting Started #11)
- [k-Means Explained](https://www.youtube.com/watch?v=I0e0Qyev8Ac) (Getting Started #12)
- [Document Clustering and Cluster Exploration](https://www.youtube.com/watch?v=v5Kgoq6xn8A) (Text Mining #09)

</div>
</details>

<details>
<summary>Week 7: Clustering</summary>
<div class="assignment-content" markdown="1">

**Assigned:** Mar. 16
**Due:** Mar. 30 (before class)

**Orange Data Mining — Hierarchical Clustering:**

Replicate the in-class hierarchical clustering demo using the NIKH clustering demo corpus (11 textbooks). Download it from the [Data & Scripts]({{ '/data/' | relative_url }}) page.

1. Load the corpus in Orange using the **Corpus** widget
2. Preprocess the text (Python Script → Preprocess Text → Bag of Words with TF-IDF)
3. Compute **Distances** (Cosine)
4. Run **Hierarchical Clustering** (Ward linkage)
5. Select **two clusters** from the dendrogram
6. Explore each cluster using descriptive tools of your choice (e.g., Word Cloud, Bar Plot, Corpus Viewer) — try to understand what makes these clusters different

**Write-up:** Create a short Markdown file (`analysis.md`) describing:
- **What you did** — which settings you chose and how you set up your workflow
- **Why you did it** — your reasoning for the choices you made
- **What you found** — which books ended up in each cluster, and what vocabulary or themes distinguish them

This does not need to be long — a few clear paragraphs is adequate. The goal is to reflect on the process and interpret what the clustering reveals.

**Submitting your work:**

1. Create a `week07/` folder inside `assignments/` in your repository
2. Add the following to that folder:
   - Your Orange workflow file (`.ows`)
   - Visualization screenshots (`.png`) showing your two-cluster comparison
   - Your analysis write-up (`analysis.md`)
3. In GitHub Desktop: write a short commit message (e.g., "Add week 7 clustering")
4. Click **Commit to main**, then **Push origin**
5. Confirm your files appear on github.com in your repository
6. Mark your completion on the [shared Google Sheet](https://docs.google.com/spreadsheets/d/1gYzaIKDgJ81MEp4xa3GYrV_oFpU1OSAw3YyaddeLfqk/edit?gid=963967460#gid=963967460)

**R Programming — Swirl Tutorials:**

Complete two Swirl lessons from the **Exploratory Data Analysis** course. You will need to install this course first — it is separate from the R Programming course you have been using.

**Installing the course:**
1. Open RStudio
2. Run the following in the console:

```r
library(swirl)
install_course("Exploratory_Data_Analysis")
swirl()
```

3. Select **Exploratory Data Analysis** from the course list

For more details on installing Swirl courses, see the [Swirl student page](https://swirlstats.com/students.html).

**Complete these two lessons:**

| Lesson | Topic |
|--------|-------|
| 11 | Hierarchical Clustering |
| 12 | K-Means Clustering |

**Documenting completion:** Take a screenshot of the completion message for each lesson and save them as `.png` files in your `week07/` folder alongside your Orange deliverables.

**Optional — R Programming:**

Complete DataCamp: Intermediate R — The apply family Chapter and Utilities Chapter.

**Orange Data Mining Tutorials (preparation for Week 8):**

Watch the following tutorials before the next class. These cover the word embedding methods we will use in Week 8:

- [Word Embedding and Nearest Neighbors](https://www.youtube.com/watch?v=RIFwBbbbvbI) (Text Mining #01)
- [Semantic Word Search](https://www.youtube.com/watch?v=6Luj-nPZjJA) (Text Mining #02)
- [Document Embedding](https://www.youtube.com/watch?v=QQqaWZEdE58) (Text Mining #05)

</div>
</details>

<details>
<summary>Week 8: Word Embeddings</summary>
<div class="assignment-content" markdown="1">

**Assigned:** Mar. 30
**Due:** Apr. 06

**Orange Data Mining — Word Embeddings:**

Replicate the in-class word embeddings demo using the presidential speeches corpus. Explore the results and try to identify patterns — which speeches or presidents appear similar, and what that might tell us about the content.

**Submitting your work:**

Add the following to a `week08/` folder in your repository:
- Your Orange workflow file (`.ows`)
- A visualization (`.png`) — TBD as per instructions from Mr. Aron van de Pol
- A short write-up (`analysis.md`) describing what you see

Commit and push your changes, then confirm your files appear on github.com.

**Required — R Programming:**

Complete DataCamp: Introduction to the Tidyverse — Data Visualization Chapter and Data Wrangling Chapter.

**Optional — R Programming:**

Complete DataCamp: Introduction to Text Analysis in R — Sentiment Analysis Chapter and Intermediate R — Utilities Chapter.

**Orange Data Mining Tutorials (preparation for Week 9):**

Watch the following tutorial before the next class. This covers the sentiment analysis methods we will use in Week 9:

- [Sentiment Analysis](https://www.youtube.com/watch?v=CK_F1JktzHk&list=PLmNPvQr9Tf-Yirm1aN3kHGnhMofrLmEy7&index=10) (Text Mining #10)

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
- Intermediate R — Conditionals and Control Flow
- Intermediate R — Loops
- Data Manipulation & Visualization
- Text Mining with Bag-of-Words in R
