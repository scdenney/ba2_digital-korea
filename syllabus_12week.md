# Topical Reading: Digital Humanities
Course: BA3 Korean Studies, Leiden University
Instructor: Dr. Steven Denney
Time & Place: [To be determined]
Duration: 12 seminars (12 weeks of instruction + final project week)

---

## Expanded Course Description

This is the DH strand of the BA3 course **Contemporary Korea and Digital Humanities**. This course is meant to introduce students to digital humanities (DH) methods, focusing on text-as-data approaches. Using Orange Data Mining and pre-prepared Korean corpora, students will learn how to clean, analyze, and interpret textual data.

The DH strand complements the topical reading seminars by equipping students with methodological skills to support their undergraduate research and to introduce them to the DH side of research in the Humanities and Social Sciences. There are no programming requirements whatsoever in this course, although students will have the opportunity to explore ways to acquire such skills.

Students will learn how to prepare, analyze, and interpret text using **Orange Data Mining**. The aim is not technical mastery, but to understand how computational methods can support thesis research in the Korea Studies (BA) program at Leiden University.

**This 12-week version** provides a slower pace for learning foundational concepts, with more time for practice, reinforcement, and peer learning. It is designed for students who are completely new to computational text analysis.

---

## Tutorials

Each week lists required **Orange Data Mining Tutorials**.
- These tutorials are **required viewing before class**.
- They are short (≈5–10 minutes each) and introduce the widgets you will use hands-on.
- Watching them in advance will free up class time and have you better prepared for applying methods to Korean corpora.

👉 You can download the Orange Data Mining application **[HERE](https://orangedatamining.com/)**
👉 Tutorials (to watch before class) are available here: [Orange Data Mining Tutorials (YouTube Playlist)](https://www.youtube.com/playlist?list=PLmNPvQr9Tf-ZSDLwOzxpvY-HrE0yv-8Fy)

---

## Assignments

In addition to attending weekly sessions, you are required to complete **weekly assignments ("deliverables")**. These tasks reinforce the skills introduced in tutorials and class exercises. Assignments can be found in the folder marked with the same name ([Assignments](https://github.com/scdenney/ba3_text_as_data/tree/main/assignments)).

### Format
- Each deliverable consists of:
  1. One or more screenshots of your Orange workflow/output
  2. A short written reflection (≈1–2 paragraphs)
  3. Your `.ows` workflow file (where applicable)

### Submission
- Commit your deliverables to your GitHub repository in the appropriate weekly folder (e.g., `week01/`, `week02/`, etc.)
- **Deadline:** 17:00 on the Monday following class unless otherwise specified.
- **Grading:**
  - `2` = fully complete and accurate
  - `1` = attempted but not fully complete/accurate
  - `0` = incomplete, late, or not attempted
- **Note:** You do *not* need to upload assignments to Brightspace. The instructor will review your GitHub repo and record grades.

### Examples
- *Week 1:* Reflection on DH and thesis research
- *Week 2:* Set up your GitHub repo + README
- *Week 3:* Screenshot and reflection on text preprocessing (raw vs. cleaned text)
- Later weeks: continue the same format — apply tutorials, document results, and reflect on significance

👉 **Weekly deliverables, together with attendance, make up 30% of your DH strand grade** (see Assessment section).

---

## Optional: R Programming Extensions

Students interested in developing foundational R programming skills alongside the DH strand are encouraged to explore the **R Programming Extensions**. These optional activities complement our work with Orange Data Mining and offer pathways to begin coding and analyzing text directly in R.

We will make use of two platforms:
- **Swirl** — interactive, in-R tutorials for learning R at your own pace
  👉 [https://swirlstats.com/students.html](https://swirlstats.com/students.html)
- **DataCamp** — an online learning platform with a dedicated class account

All enrolled students have access to the shared **DataCamp classroom**. The primary course to complete there is:
👉 [Introduction to Text Analysis in R](https://app.datacamp.com/learn/courses/introduction-to-text-analysis-in-r)

Additional short modules may be assigned later, depending on time and fit.

**Assessment policy for the optional R Programming track:**
- **Extra credit** will be awarded upon satisfactory completion of the designated lessons or modules (up to .5 points added to the final DH strand grade).
- Students who opt in but do not complete required lessons may receive a **minor penalty** to their DH strand grade.
  Opt in only if you plan to finish.

---

## GitHub Repository Requirement

See the ["how-to" guide](repo_how-to.md) (located in the syllabus folder) on how to get started with GitHub and repo management.

You are required to maintain a **private GitHub repository** for this course:

1. Create a new private repo named: `DH-TopicalReading-<Surname>`.
2. Add the instructor (**username: scdenney**) as a collaborator.
3. Keep the repo private, unless you explicitly choose to share it.
4. Organize the repo with the following structure:

📂 Student Repository Structure
<pre>
DH-TopicalReading-<Surname>/
  ├── assignments/    # where you commit your assignments
│   ├── week01/
│   │   ├── week01-deliverable.md
│   │   └── screenshots/
│   ├── week02/
│   │   └── ...
│   ├── week12/
│   └── final-project/
└── README.md          # use the README to introduce yourself and what your repo will do for you
</pre>

5. Each week's deliverable (markdown file + screenshots) must be committed to the correct subfolder.
6. At the start of the course, submit the **URL of your repo** to the instructor at [this Google Sheet](https://docs.google.com/spreadsheets/d/1iVdwLTfmVkMn2cQGXPxCC4YIxADawSKAWltZIxD5WMs/edit?usp=sharing) (click to open).

This organization mirrors best practices for **research data management** and is part of the course's learning objectives.

---

## Corpus Overview

The primary dataset for this course is the 국사편찬위원회 (Kuksap'yŏnch'an Wiwŏnhoe; National Institute of Korean History, NIKH) history textbook corpus. This collection brings together Korean history textbooks produced under successive national curricula, spanning from the late 조선 (Chosŏn; Joseon) and 대한제국 (Taehan Cheguk; Korean Empire) through the 일제강점기 (Ilche Kangjŏmgi; Japanese colonial period), liberation, and the postwar 교육과정 (kyoyuk kwajŏng; national curricula) up to the present. These textbooks, published and authorized by the state, offer an authoritative view of how the Korean nation, state, and people have been represented by state-sanctioned education across different political eras.

You may peruse an online-navigable version of the history textbooks through the National Institute of Korean History's official website: [contents.history.go.kr](https://contents.history.go.kr/front/ta/main.do)

Because textbooks are central to the formation of collective memory and national identity, this corpus is especially well suited for exploring questions of modern Korean identity: how ideas of 민족 (minjok; nation/people), 국민 (kungmin; citizens), 시민 (simin; civic belonging), and 통일 (t'ongil; unification) have been framed, contested, and transmitted to generations of (South) Korean students. In this way, the corpus links directly to broader themes in modern political sociology in Korea, which you are also examining in the topical reading strand of this course.

For **supplementary purposes**, additional pre-prepared corpora are available:
- **개벽 (Kaebyŏk, 1920–1935):** An interwar magazine reflecting cultural, intellectual, and political debates in colonial Korea. *Kaebyŏk* has been used extensively in scholarship on cultural nationalism and modern identity, including Michael Robinson's *Cultural Nationalism in Colonial Korea, 1920–1925* (1988), Andre Schmid's *Korea Between Empires, 1895–1919* (2002), and Henry Em's "Minjok as a Modern and Democratic Construct: Sin Ch'aeho's Historiography" (1999).
- **경제연구 (Kyŏngje Yŏngu, 1987–2017):** A North Korean economics journal, useful for examining how policy and ideology interact in the DPRK. Read more about this at [38 North](https://www.38north.org/2025/05/in-memoriam-kyongje-yongu/).

👉 Other corpora will be introduced during the course to support student exploration. For the final project, students will be required to use one of the pre-prepared corpora, except the NIKH practice corpora, or to have approved the use of one of their own. We will discuss how to design a mini text-as-data project throughout the course and especially in Weeks 11–12.

---

## Weekly Outline (subject to change)

### Week 1: Introduction to Digital Humanities
- **Lecture:** What is DH? Why text-as-data matters for Korean Studies. FAIR data principles. Overview of the course.
- **Hands-On:** Orange Data Mining installation and interface orientation. Basic navigation.
- **Tutorials:** *Welcome to Orange, Data Workflows*.
- **Deliverable:** Install Orange (screenshot) + written reflection on what you hope to learn and how DH might support your thesis research.

---

### Week 2: GitHub & Data Management
- **Lecture:** Version control for humanities research. GitHub fundamentals. Repository organization best practices. Introduction to Markdown.
- **Hands-On:** Create and organize GitHub repository. Clone course repository. Practice commits and pushes. Introduction to the NIKH corpus.
- **Tutorials:** *Widgets & Channels*.
- **Deliverable:** GitHub repo setup complete with proper structure. README.md file. Successfully cloned course data.

---

### Week 3: Text Preprocessing Basics
- **Lecture:** What makes text data different? Introduction to tokenization. Understanding stopwords. Korean-specific preprocessing challenges (morphological analysis).
- **Hands-On:** Import first corpus into Orange. Explore raw text. Apply basic preprocessing pipeline. Compare raw vs. preprocessed text.
- **Tutorials:** *Text Preprocessing, Importing Text Documents*.
- **Deliverable:** Screenshot of preprocessing workflow. Brief comparison of raw vs. cleaned text (1–2 paragraphs).

---

### Week 4: Text Preprocessing Practice
- **Lecture:** Deep dive into Bag-of-Words representation. Korean morphological analysis (nouns, verbs, adjectives). Preprocessing parameters and their effects. Introduction to the Python preprocessing script.
- **Hands-On:** Apply multiple preprocessing approaches. Create and compare different BOW representations. Experiment with preprocessing parameters. Test custom Python script (optional).
- **Tutorials:** Review previous tutorials as needed.
- **Deliverable:** Preprocessing workflow (.ows file). Word frequency bar chart. Reflection on preprocessing choices and their impact (1–2 paragraphs).

---

### Week 5: Descriptive Patterns - Word Frequency
- **Lecture:** Term Frequency (TF) explained. What frequency tells us (and what it doesn't). Introduction to word clouds and frequency visualizations. From descriptive observations to interpretive claims.
- **Hands-On:** Create word clouds with different parameters. Generate frequency bar charts. Explore most common terms in the corpus. Practice using the Corpus Viewer.
- **Tutorials:** *Word Cloud widget*.
- **Deliverable:** Two word clouds (with different parameters/settings). Bar chart of top terms. Short analysis: What do these visualizations reveal about the corpus? (1–2 paragraphs).

---

### Week 6: Descriptive Patterns - TF-IDF and Keywords
- **Lecture:** Document Frequency (DF) explained. Inverse Document Frequency (IDF) explained. Deep dive into TF-IDF: why distinctiveness matters. Keyword extraction techniques. Comparing groups and time periods.
- **Hands-On:** Create visualizations using TF-IDF weights. Extract keywords from different document groups. Compare keywords across time periods or document categories. Contrast raw counts vs. TF-IDF representations.
- **Tutorials:** Review as needed.
- **Deliverable:** Word cloud or bar chart comparison (raw frequency vs. TF-IDF). Keyword comparison across two time periods or document types. Reflection: What patterns emerge? What's the difference between the two approaches? (2–3 paragraphs). .ows workflow file.

---

### Week 7: Mid-Term Review & Assessment
- **Lecture:** Review of Weeks 1–6 concepts. Q&A session addressing common challenges and questions. Preview of clustering (Weeks 8–9). Peer learning session.
- **Hands-On:** Peer review of workflows. Troubleshooting common issues. Practice building complete workflow from scratch. Group discussion of findings so far.
- **Tutorials:** None (review week).
- **Mid-Term Assignment (take-home):** Import a provided corpus. Build a complete preprocessing → analysis workflow. Create 2–3 visualizations. Write 500–750 word interpretation discussing findings, limitations, and potential research questions. Submit .ows file and PDF report.
  - **Due:** One week from class session.
  - **Weight:** 15% of DH strand grade.

---

### Week 8: Introduction to Clustering
- **Lecture:** What is clustering? Supervised vs. unsupervised learning. Document similarity and distance metrics. Introduction to hierarchical clustering. How to interpret dendrograms.
- **Hands-On:** Create first hierarchical clustering. Explore cluster compositions. Generate word clouds for individual clusters. Connect to Corpus Viewer for qualitative verification. Practice reading dendrogram structures.
- **Tutorials:** *Text Clustering, Hierarchical Clustering*.
- **Deliverable:** Dendrogram screenshot. Word clouds for 2–3 selected clusters. Analysis: What themes do these clusters represent? What documents are grouped together? (2–3 paragraphs). .ows file.

---

### Week 9: Advanced Clustering & Comparison
- **Lecture:** k-means clustering explained. Comparing hierarchical vs. k-means approaches. When to use which method. Introduction to multivariate projection techniques (FreeViz). Cluster validation and interpretation strategies.
- **Hands-On:** Apply k-means clustering. Compare k-means results with hierarchical clustering from Week 8. Use projection widgets for visualization. Practice qualitative verification by reading sample documents from clusters.
- **Tutorials:** *k-Means Clustering, Multivariate Projection (FreeViz)*.
- **Deliverable:** Comparison report (PDF): hierarchical vs. k-means results. Screenshots of both clustering approaches and at least one projection visualization. Reflection: Which method works better for this corpus? Why? What are the trade-offs? (2–3 paragraphs). .ows file.

---

### Week 10: Classification & Sentiment Analysis
- **Lecture:** Introduction to supervised learning and classification. What is sentiment analysis? Classification models and evaluation metrics. Working with sentiment scores: normalization and interpretation. Limitations of computational sentiment analysis for Korean texts. Connecting quantitative scores to qualitative reading.
- **Hands-On:** Filter corpus by keyword. Apply sentiment analysis. Normalize scores and filter zeros. Create visualizations (box plots, violin plots). Connect sentiment scores back to actual sentences using Corpus Viewer or Data Table. Interpret results with contextual understanding.
- **Tutorials:** *Text Classification, Making Predictions, Model Evaluation*.
- **Deliverable:** Sentiment analysis report (PDF). Choose one keyword of interest, analyze sentiment patterns across time periods or document types. Include example sentences with their scores. Include at least one visualization. Reflection on process, findings, and limitations (2–3 paragraphs).

---

### Week 11: Topic Modeling
- **Lecture:** What is topic modeling? Introduction to LDA (Latent Dirichlet Allocation). How LDA works (simplified explanation). Topics vs. Clusters: understanding the key differences. Using LDAvis for interpretation. Understanding the lambda (λ) parameter and word relevance metrics. Topic-document mixtures and probability distributions.
- **Hands-On:** Build LDA model in Orange. Choose appropriate number of topics. Explore topics with LDAvis widget. Experiment with lambda slider for interpretation. Analyze topic-document mixtures in Data Table. Connect topics to actual documents for verification.
- **Tutorials:** *Topic Modeling widget, LDAvis widget*.
- **Deliverable:** LDA workflow screenshot. LDAvis visualizations for 2–3 topics (showing different λ values). Topic interpretation report (PDF): What themes do the topics represent? Analysis of 3 documents showing their topic mixtures. Reflection: What are the strengths and limitations of topic modeling? How does it differ from clustering? (2–3 paragraphs). .ows file.

---

### Week 12: Project Preparation & Course Wrap-Up
- **Lecture:** Review of all methods learned (Weeks 1–11). How to formulate good research questions for text analysis. Designing a complete analytical workflow. Qualitative verification strategies and why they matter. Writing up computational text analysis results for academic audiences. Ethical considerations in text-as-data research.
- **Hands-On:** Final project group formation. Explore available corpora for final project. Brainstorm research questions in groups. Draft workflow plans. Peer feedback on project ideas. Practice presentation of preliminary findings.
- **Tutorials:** None (project preparation week).
- **Deliverable:** Project proposal (submitted by group): Research question, corpus choice, proposed analytical methods, brief justification (300–500 words). Individual reflection on course learning: What has been most valuable? What remains challenging? How will you apply these skills? (1–2 paragraphs).

---

### Final Project (Week 13 or Weeks 13–14)

The final project will take the form of an **in-person text-as-data analysis project** completed in small groups. Working collaboratively, students will complete a full text-as-data analysis that draws directly on the skills developed throughout the 12-week course.

**Format Options:**
- **Option A:** One-day extended hackathon (6–8 hours in DH Lab)
- **Option B:** Two-week project with work session (Week 13) and presentations (Week 14)

Each group will:
- Select from a pre-prepared corpus (or use an approved corpus of your own)
- Formulate a specific, answerable research question
- Design and execute a workflow in Orange Data Mining
- Apply at least 3 different analytical methods (e.g., TF-IDF, clustering, sentiment analysis, topic modeling)
- Include qualitative verification (close reading of selected documents)
- Generate and interpret findings with appropriate visualizations
- Write up results in a structured report (2,000–3,000 words)
- Submit workflow file (.ows) and PDF report

**Deliverables:**
1. **PDF Report** (required): Research question, motivation, corpus description, workflow overview, key results, interpretation, limitations, and reflection
2. **`.ows` Orange workflow file** (required): Must run cleanly
3. **Appendix** (optional): Additional visualizations or supplementary analysis
4. **`.R` file** (if using R for any part of analysis)

**Assessment Criteria:**
- Research Question (15%): Clear, specific, feasible, and aligned with corpus
- Workflow Quality (30%): Logical structure, correct widget use, reproducibility
- Interpretation of Results (40%): Accuracy, depth, qualitative verification
- Report Quality (15%): Structure, clarity, writing, presentation

This is a **timed assignment** (not a take-home project, unless Option B Week 13–14 format is used). Further details, including corpus descriptions and assessment rubric, will be provided 48 hours before the project begins.

---

## Assessment

The DH strand of the course is worth 25% of the full course grade. That 25% is broken down as follows:

- **Weekly Deliverables & Attendance** (Weeks 1–6, 8–12): 30%
  - 11 weekly assignments at ~2.7% each
  - Graded on 0–2 scale (see Assignments section)
  - Attendance required; absences affect this component

- **Mid-Term Assessment** (Week 7): 15%
  - Take-home analysis assignment
  - Graded on 0–10 scale
  - Tests understanding of preprocessing, visualization, and interpretation

- **Final Project** (Week 13): 55%
  - Group project with individual accountability
  - Graded on 0–10 scale using detailed rubric
  - Four weighted criteria: Research Question (15%), Workflow Quality (30%), Interpretation (40%), Report Quality (15%)

**Total:** 100% of DH strand grade

**Optional R Programming Track:**
- Extra credit: up to +0.5 points on final DH strand grade
- Penalty for opt-in without completion: -0.25 points

---

## Attendance

Full attendance is expected. This 12-week course builds skills cumulatively, and missing sessions will significantly impact your ability to complete later assignments and the final project.

If you cannot attend a session, you must:
1. Notify the instructor in advance
2. Review the materials and tutorials independently
3. Complete the weekly assignment on time
4. Attend office hours to catch up

**More than two unexcused absences may result in failing the DH strand.**

---

## Course Policies

### Late Submissions
- Weekly deliverables submitted late (after Monday 17:00 deadline) receive maximum score of 1/2
- Deliverables more than one week late receive 0
- Mid-term and final project deadlines are firm; late submissions lose 1 point per day

### Academic Integrity
- All work must be your own (or your group's for collaborative assignments)
- Generative AI tools (ChatGPT, Claude, etc.) may be used for R programming assistance ONLY if:
  - You are transparent about their use
  - You submit chat history/logs
  - You understand and can explain all code
- Using AI to write analysis text or interpretations is not permitted
- Plagiarism will result in failing the course

### Collaboration
- Weekly deliverables are individual work
- Discussing concepts and troubleshooting with peers is encouraged
- Sharing code/workflows directly is not permitted for individual assignments
- Final project is collaborative; all group members must contribute equally

---

## Learning Objectives

By the end of this 12-week DH strand, students will be able to:

1. **Understand** the role and value of Digital Humanities methods in Korean Studies research
2. **Apply** appropriate text preprocessing techniques to prepare Korean-language corpora for analysis
3. **Execute** core text analysis methods including frequency analysis, TF-IDF, clustering, classification, and topic modeling
4. **Interpret** computational text analysis results with appropriate caution and contextual knowledge
5. **Combine** computational methods with qualitative close reading for verification and interpretation
6. **Document** analytical workflows using version control (GitHub) and research data management best practices
7. **Communicate** text-as-data findings clearly in written reports with appropriate visualizations
8. **Reflect** critically on the possibilities and limitations of computational text analysis for humanities research

---

## Required Materials

- **Personal computer** (Mac, Windows, or Linux) capable of running Orange Data Mining
- **Orange Data Mining software** (free download from [orangedatamining.com](https://orangedatamining.com/))
- **GitHub account** (free)
- **GitHub Desktop application** (recommended, free)
- **Markdown editor** (recommended: VS Code, Typora, or any text editor)

All course materials (corpora, tutorials, assignment instructions) are provided via the course GitHub repository.

---

## Support & Resources

- **Office Hours:** [To be determined]
- **Course Repository:** [https://github.com/scdenney/ba3_text_as_data](https://github.com/scdenney/ba3_text_as_data)
- **Orange Tutorials:** [YouTube Playlist](https://www.youtube.com/playlist?list=PLmNPvQr9Tf-ZSDLwOzxpvY-HrE0yv-8Fy)
- **Orange Documentation:** [https://orangedatamining.com/docs/](https://orangedatamining.com/docs/)
- **GitHub Guide:** See `repo_how-to.md` in syllabus folder
- **Markdown Guide:** See `markdown_how-to.md` in syllabus folder

For technical issues with Orange or GitHub, consult documentation first, then bring questions to class or office hours.

---

## Acknowledgments

This course draws on materials and pedagogical approaches from the digital humanities community, including the Orange Data Mining team, practitioners in Korean Studies DH, and open educational resources. Special thanks to Aron van der Pol for contributions to preprocessing instruction.

---

*This syllabus is subject to change. Any modifications will be announced in class and updated in the course repository.*
