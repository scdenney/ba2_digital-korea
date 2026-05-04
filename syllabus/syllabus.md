---
layout: default
title: Syllabus
---

<div class="page-layout">
  <aside class="page-sidebar">
    <div class="page-sidebar-inner">
      <h2 class="page-sidebar-title">On this page</h2>
      <nav class="page-toc">
        <ul>
          <li><a href="#expanded-description">Expanded Description</a></li>
          <li>
            <a href="#course-policies">Course Policies</a>
            <ul>
              <li><a href="#academic-integrity">Academic Integrity</a></li>
              <li><a href="#collaboration">Collaboration</a></li>
              <li>
                <a href="#assessment">Assessment</a>
                <ul>
                  <li><a href="#participation">Participation</a></li>
                  <li><a href="#research-methods-project">Research Methods Project</a></li>
                  <li><a href="#final-paper">Final Paper</a></li>
                </ul>
              </li>
            </ul>
          </li>
          <li><a href="#on-data">On Data</a></li>
          <li>
            <a href="#schedule">Schedule</a>
            <ul>
              <li><a href="#week-1">Week 1 (Feb. 02)</a></li>
              <li><a href="#week-2">Week 2 (Feb. 09)</a></li>
              <li><a href="#week-3">Week 3 (Feb. 16)</a></li>
              <li><a href="#week-4">Week 4 (Feb. 23)</a></li>
              <li><a href="#week-5">Week 5 (Mar. 02)</a></li>
              <li><a href="#week-6">Week 6 (Mar. 09)</a></li>
              <li><a href="#week-7">Week 7 (Mar. 16)</a></li>
              <li><a href="#week-8">Week 8 (Mar. 30)</a></li>
              <li><a href="#week-9">Week 9 (Apr. 13)</a></li>
              <li><a href="#week-10">Week 10 (Apr. 20)</a></li>
              <li><a href="#week-11">Week 11 (May 4)</a></li>
              <li><a href="#week-12">Week 12 (May 11)</a></li>
            </ul>
          </li>
        </ul>
      </nav>
    </div>
  </aside>

  <div class="page-content" markdown="1">
# Syllabus

## Expanded Description {#expanded-description}

This course introduces students to computational text analysis as a research method in Korean (Area) Studies. Students will learn to treat text as data, transforming written sources into formats that can be analyzed using computational tools. The course covers the full text analysis pipeline: preprocessing (preparing text for analysis), descriptive analysis (finding patterns in word usage), clustering (discovering natural groupings in documents), classification (categorizing texts using both rule-based and machine learning approaches), and topic modeling (uncovering hidden themes across document collections).

Students work primarily with Orange Data Mining, a widget-based, drag-and-drop software tool that makes computational methods accessible without requiring (advanced) programming skills. In addition, students develop foundational R programming skills through tutorials, building some initial capacity for more advanced work. No prior programming or statistical experience is required. You only need curiosity and a willingness to learn by trial and error.

A central component of the course is the use of curated text corpora. Provided by the instructor, these corpora draw on Korean-language primary sources and span a range of historical, political, and social issues related to both North and South Korea. They are designed to support methods learning while also grounding computational analysis in content relevant to the study of Korea. Alongside hands-on analysis, class time will be spent on reading and discussing recent scholarship that applies digital tools and methods in the digital humanities and computational social sciences, with particular attention to research on Korea.

Throughout the course, students engage with the possibilities and limitations of computational approaches to cultural and textual analysis. They learn to work with data according to FAIR principles (Findable, Accessible, Interoperable, Reusable) and develop practical and transferable skills in documenting and sharing research workflows. The course culminates in a Research Methods Project in which students apply text analysis methods to Korean-language materials (or another primary source Asian language), generating data and analysis that will inform their final papers.

## Course Policies {#course-policies}

### Academic Integrity {#academic-integrity}
- All work must be your own
- Generative AI tools (ChatGPT, Claude, etc.) may be used for assistance
- Using AI to write analysis text or interpretations is not permitted
- Plagiarism will result in failing the course

### Collaboration {#collaboration}
- Assignments are individual work
- Discussing concepts and troubleshooting with peers is encouraged
- Sharing code/workflows directly is not permitted for individual assignments

### Assessment {#assessment}

- Participation (15%) — attendance, R programming assignments
- Research Methods Project (35%) — in-class assessments, Week 12 workshop
- Final Paper (50%)

#### Participation {#participation}

Each R Programming exercise or assignment listed below is assessed as complete (1) or incomplete (0). To receive credit, assignments must be submitted by the start of the next class. Late submissions receive no credit; partial credit is possible at the instructor's discretion.

Full attendance is not only expected but, for a hands-on class such as this, extremely important. Each class you are marked as present (1) or absent (0). If you miss a class, you must catch up immediately by reviewing lecture material and consulting your peers. With exceptions for extenuating circumstances, absences are not excused and no extensions for assignments will be granted.

The final participation grade is calculated as the proportion of completed items (assignments and attendance), scaled to 10.

#### Research Methods Project {#research-methods-project}

The Research Methods Project (RMP) requires students to apply course methods to a research question of their choosing, generating data and analysis that will both constitute a grade and inform their final papers. The RMP is due at the end of Week 12. It will be assessed out of 10.

Information and guidelines are provided in class. Methods assessments (Week 6 and Week 11) also contribute to this grade. Each assessment is a multiple choice and/or short answer test administered in class, also out of 10 total points. The final grade is the average of the RMP and assessments.

#### Final Paper {#final-paper}

The final paper is a short research report applying computational text analysis methods learned in this course to a research question of the student's choosing. The paper is **2,500–6,000 words** (excluding references, figures/tables, and appendix material; 2,500 is a hard minimum, with a 10% tolerance over 6,000), built around a corpus from the [Final Paper Dataset Menu](https://github.com/scdenney/ba2-final-paper-data) and supported by a public, FAIR-structured GitHub replication repository. The paper includes a research question, brief literature review, data and methods section, analysis and findings, and a summary and conclusion.

The full brief and rubric are on the [Final Paper page]({{ '/final-paper/' | relative_url }}). Students bring a chosen dataset and a draft research question to the **11 May (Week 12) workshop**, where the question and dataset are reviewed in conversation and students workshop their analysis plans with classmates. The paper is due **Friday 5 June 2026, 23:59** on Brightspace.

*A resit is possible for a failing grade on the final paper. However, a resit will only constitute a re-grade of the final paper's proportion of the overall grade and can only be attempted if an original final paper was submitted.*

---

## On Data {#on-data}

This course uses primary source corpora curated by the instructor. These corpora are maintained in a dedicated repository: [NLP Corpora for Korean Studies](https://github.com/scdenney/nlp_corpora). The repository includes datasets spanning historical texts, periodicals, political speeches, social media, and interview data relevant to the study of Korea.

The focus is on Korean-language corpora. For students who do not read Korean, accommodations will be made using English-language materials or primary sources in another Asian language.

In many cases, we will work with truncated versions of the corpora to facilitate in-class exercises and manage processing requirements. Additional supporting files for preprocessing and other tasks will be provided in due course and documented for reference and reuse.

---

## Schedule {#schedule}

### Week 1 (Feb. 02): Introduction & Getting Started {#week-1}

This opening week establishes the foundation for the course. Students will ensure they have the right technical setup and understand course expectations. We'll configure essential tools including GitHub for version control and collaboration, R and RStudio for programming with Swirl, DataCamp for guided learning modules in R, and Orange Data Mining as our primary analysis tool.

**Topics:**
- Course overview and expectations
- Technical environment setup
- Introduction to course tools and platforms

**In-Class Assignments:**
- GitHub setup; clone course repository; share repository link with instructor
- Confirm DataCamp enrollment
- Verify installations: RStudio, Swirl and Swirl courses, Orange Data Mining.
- *Note:* To continue in this class, these assignments must be completed.

**R Programming:**
- Complete Swirl R Programming lessons 1, 2, 4, 6, 7, 12: Basic Building Blocks, Workspace and Files, Vectors, Subsetting Vectors, Matrices and Data Frames, Looking at Data. Due by start of next class.

---

### Week 2 (Feb. 09): Foundations of Computational Text Analysis {#week-2}

This week introduces the conceptual foundations of computational text analysis and its role across computational social science and digital humanities. Students will learn what makes text analysis "computational," understand the concept of a corpus, and explore available text data sources. Practical skills include GitHub workflow management and an introduction to writing in Markdown.

**Topics:**
- Computational text analysis, computational social science, and digital humanities
- Defining and working with text corpora
- Data sources and corpus availability
- GitHub management and Markdown syntax

**Required Reading:**
- Grimmer, Roberts, and Stewart - Chapter 2: Social Science Research and Text Analysis (provided by instructor)
- Markdown explainer

**Orange Data Mining Tutorials:**
- Getting Started 01: Welcome to Orange
- Getting Started 02: Data Workflows
- Getting Started 03: Widgets and Channels
- Getting Started 04: Loading Your Data

**Recommended Reading:**
- Wilkerson, J., & Casas, A. (2017). Large-scale computerized text analysis in political science: Opportunities and challenges. *Annual Review of Political Science*, 20, 529-544
- Macanovic, A. (2022). Text mining for social science–The state and the future of computational text analysis in sociology. *Social Science Research*, 108, 102784

**Hands-On:**
- Load a corpus into Orange Data Mining
- Practice GitHub workflows
- Create Markdown documentation

---

### Week 3 (Feb. 16): Text Preprocessing Basics {#week-3}

Preprocessing transforms raw text into a format suitable for computational analysis. This week covers fundamental concepts including tokenization (breaking text into meaningful units), part-of-speech (POS) tagging, and the preprocessing pipeline. Students will learn to use custom Python scripts within Orange Data Mining on both Mac and Windows platforms, addressing platform-specific considerations and limitations with Korean-language morphemes.

**Topics:**
- Tokenization and token types
- Part-of-speech (POS) tagging
- Introduction to preprocessing workflows
- Custom Python scripts in Orange Data Mining (Mac and Windows)

**Recommended Reading:**
- Grimmer, Roberts, and Stewart - Chapter 5: Bag of Words
- Denny, M. J., & Spirling, A. (2018). Text preprocessing for unsupervised learning: Why it matters, when it misleads, and what to do about it. *Political Analysis*, 26(2), 168-189

**Orange Data Mining Tutorials:**
- [Text Preprocessing](https://www.youtube.com/watch?v=nAIqoCxvIqc) (Text Mining #06)
- Getting Started 16: Text Preprocessing (supplementary — older but still useful)

**Orange Widgets to Master:**
- Corpus (loading text data)
- Preprocess Text (tokenization, normalization, filtering)
- Bag of Words (creating document-term matrix)

**R Programming:**
- Complete DataCamp: Introduction to R - Chapter 1: Intro to Basics and Chapter 2: Vectors. Due by start of next class.

---

### Week 4 (Feb. 23): From Words to Numbers: Bag of Words, TF-IDF, and Visualization {#week-4}

This week covers the full arc from preprocessing to quantitative text representation. We begin with a brief review of Week 3's preprocessing pipeline, then introduce the bag-of-words (BoW) model and its assumptions, term frequency (TF), document frequency (DF), and the document-term matrix (DTM). We then develop TF-IDF weighting as a method for identifying distinctive words. The session concludes with a live Orange demo showing how to build a complete workflow from corpus to visualization.

**Topics:**
- Bag-of-words assumptions and trade-offs
- Term frequency (TF): raw counts and normalization
- Document frequency (DF) and word rarity
- The document-term matrix (DTM) and sparsity
- TF-IDF weighting: identifying distinctive words
- Visualization: word clouds, frequency distributions, bar charts

**Recommended Reading:**
- Grimmer, Roberts, and Stewart - Chapters 6-7: The Multinomial Language Model; The Vector Space Model and Similarity Metrics
- Bollen, J., et al. (2021). Historical language records reveal a surge of cognitive distortions in recent decades. *Proceedings of the National Academy of Sciences*, 118(30) (optional)

**Orange Data Mining Tutorials:**
- [Bag of Words](https://www.youtube.com/watch?v=eCdYyaDtjjQ) (Text Mining #07)

**Orange Widgets to Master:**
- Bag of Words (Count, Binary, Sublinear, TF-IDF)
- Word Cloud (visual representation of word frequencies)
- Statistics (frequency analysis and TF-IDF sorting)
- Distributions (exploring patterns across presidents)
- Bar Plot (comparative visualization)

**Assignment:**
- Reproduce the in-class Orange workflow (corpus → preprocessing → Bag of Words with TF-IDF → at least two visualization widgets). Upload .ows file and screenshot to `week04/` folder.

**R Programming:**
- Complete DataCamp: Introduction to R — Factors Chapter and Matrices Chapter.
- **Extended deadline: March 09, 15:15 (start of Week 6).**

---

### Week 5 (Mar. 02): Practice & Deepen: Hands-On Lab {#week-5}

A practice week to consolidate everything from Weeks 3-4 before the midterm. Students work through extended BoW/TF-IDF workflows, compare presidential speech patterns using multiple visualization widgets, and practice interpreting results. No new readings — focus is on deepening practical skills and preparing for the Week 6 assessment.

**Topics:**
- Extended practice with BoW and TF-IDF workflows
- Comparing presidents using word clouds, bar plots, and distributions
- Interpreting TF vs TF-IDF rankings
- Midterm preparation and review

---

### Week 6 (Mar. 09): Midterm Review & Assessment {#week-6}

This week consolidates learning from Weeks 1-5, covering setup and tools, foundational concepts, preprocessing workflows, and descriptive analysis. The midterm assessment, administered in class, evaluates understanding of core concepts and practical skills developed thus far. More information about this assessment will be provided in class. Weeks 7-10 require your complete understanding of everything to this point.

**Topics:**
- Comprehensive review of Weeks 1-5
- Midterm assessment

**R Programming:**
- Complete DataCamp: Introduction to R — Lists Chapter and Data Frames Chapter. Due by start of next class.
- *Optional:* DataCamp: Intermediate R — Conditionals and Control Flow, Loops.

**Orange Data Mining Tutorials:**
- [Hierarchical Clustering](https://www.youtube.com/watch?v=dJ5z2SRwzgs) (Getting Started #05)
- [k-Means](https://www.youtube.com/watch?v=vgmL808eSw4) (Getting Started #11)
- [k-Means Explained](https://www.youtube.com/watch?v=I0e0Qyev8Ac) (Getting Started #12)
- [Document Clustering and Cluster Exploration](https://www.youtube.com/watch?v=v5Kgoq6xn8A) (Text Mining #09)

---

### Week 7 (Mar. 16): Clustering {#week-7}

Clustering introduces "unsupervised" learning, where algorithms discover patterns in data without human-provided assistance. We explore how documents can be represented as vectors and words analyzed as numbers, then learn two clustering approaches: hierarchical clustering, which builds a tree of nested clusters, and k-means clustering, which partitions documents into groups.

**Topics:**
- Introduction to unsupervised learning
- Vectorization with TF-IDF as foundation for clustering
- Hierarchical clustering (agglomerative methods)
- K-means clustering (partition-based methods)
- Choosing appropriate number of clusters

**Recommended Reading:**
- Grimmer, Roberts, and Stewart - Chapter 12: Clustering

**Orange Data Mining Tutorials:**
- [Hierarchical Clustering](https://www.youtube.com/watch?v=dJ5z2SRwzgs) (Getting Started #05)
- [k-Means](https://www.youtube.com/watch?v=vgmL808eSw4) (Getting Started #11)
- [k-Means Explained](https://www.youtube.com/watch?v=I0e0Qyev8Ac) (Getting Started #12)
- [Document Clustering and Cluster Exploration](https://www.youtube.com/watch?v=v5Kgoq6xn8A) (Text Mining #09)

**Orange Widgets to Master:**
- Hierarchical Clustering (tree-based grouping)
- k-Means (partition-based grouping)
- Distances (choosing distance metrics)

**Hands-On:**
- Complete workflow from corpus through preprocessing to clustering
- Apply hierarchical clustering; interpret the dendrogram
- Apply k-means clustering

---

### Week 8 (Mar. 30): Word Embeddings {#week-8}

Word embeddings represent words as dense vectors in a continuous space, capturing semantic relationships that bag-of-words models miss. This week introduces the concept of distributed representations: words with similar meanings appear near each other in vector space. Students learn how embeddings enable semantic search, analogy tasks, and document-level representations that can improve downstream analysis like clustering and classification.

**Topics:**
- From sparse vectors (BoW) to dense vectors (embeddings)
- Word embedding concepts and nearest neighbors
- Semantic search and word similarity
- Document embeddings: representing entire documents as vectors

**Orange Data Mining Tutorials:**
- [Word Embedding and Nearest Neighbors](https://www.youtube.com/watch?v=RIFwBbbbvbI) (Text Mining #01)
- [Semantic Word Search](https://www.youtube.com/watch?v=6Luj-nPZjJA) (Text Mining #02)
- [Document Embedding](https://www.youtube.com/watch?v=QQqaWZEdE58) (Text Mining #05)

**Orange Widgets to Master:**
- Document Embedding (creating document vectors)
- Nearest Neighbors (finding similar words/documents)
- Corpus Viewer (examining results)

---

### Week 9 (Apr. 13): Sentiment Analysis – Dictionary and Rule-Based Approaches {#week-9}

Sentiment analysis assigns valence (positive, negative, neutral) to texts using predefined dictionaries or rules. This week focuses on dictionary-based methods, where humans define rules (like lists of positive and negative words) and the computer applies them. These interpretable, transparent methods are widely used in computational social science and digital humanities research. Students learn to apply sentiment dictionaries, build custom scoring rules, and critically evaluate the strengths and limitations of dictionary-based approaches.

**Topics:**
- Dictionary-based sentiment analysis
- Rule-based text classification
- Building and applying custom dictionaries
- Advantages and limitations of dictionary methods

**Recommended Reading:**
- Grimmer, Roberts, and Stewart - Chapter 16: Word Counting
- Young, L., & Soroka, S. (2012). Affective news: The automated coding of sentiment in political texts. *Political Communication*, 29(2), 205-231

**Orange Data Mining Tutorials:**
- [Sentiment Analysis](https://www.youtube.com/watch?v=CK_F1JktzHk) (Text Mining #10)

**Orange Widgets to Master:**
- Sentiment Analysis (applying sentiment dictionaries)
- Corpus Viewer (examining classified documents)
- Score Documents (custom dictionary scoring)

---

### Week 10 (Apr. 20): Topic Modeling with Latent Dirichlet Allocation {#week-10}

Topic modeling finds hidden thematic structure in document collections. Latent Dirichlet Allocation (LDA) assumes documents are mixtures of topics, and topics are mixtures of words. Unlike clustering, which assigns each document to one group, topic modeling allows documents to belong partially to multiple topics. Students learn to fit topic models, choose appropriate numbers of topics, and interpret results using visualization tools.

**Topics:**
- Introduction to topic modeling concepts
- Latent Dirichlet Allocation (LDA)
- Choosing the number of topics
- Interpreting and validating topic models
- Topic-document and topic-word distributions
- Using LDAvis for interactive exploration

**Recommended Reading:**
- Grimmer, Roberts, and Stewart - Chapter 13: Topic Models
- Roberts, M. E., et al. (2014). Structural topic models for open-ended survey responses. *American Journal of Political Science*, 58(4), 1064-1082

**Orange Data Mining Tutorials:**
- [Topic Modeling](https://www.youtube.com/watch?v=RRhGlSi2Dio) (Text Mining #11)
- [Exploring Topics](https://www.youtube.com/watch?v=jFabEv8JalE) (Text Mining #12)

**Orange Widgets to Master:**
- Topic Modelling (fitting LDA models)
- LDAvis (interactive topic visualization and interpretation)
- Corpus Viewer (examining documents by topic)

---

### Week 11 (May 4): Final Review & Assessment {#week-11}

This second assessment, administered in class, evaluates understanding of core concepts and practical skills developed from Week 7.

Following the assessment, we will review our learning across the entire course, from preprocessing through clustering, word embeddings, sentiment analysis, and topic modeling. It will focus more on content learned in the second half of the class. It will also prepare students for the week 12 Workshop. 

**Topics:**
- Second assessment
- Comprehensive review
- Overview of Week 12 Workshop

---

### Week 12 (May 11): Research Methods Workshop & Final Paper Planning {#week-12}

The Week 12 workshop is built around the [final paper]({{ '/final-paper/' | relative_url }}). Arrive with a corpus picked from the [Final Paper Dataset Menu](https://github.com/scdenney/ba2-final-paper-data) and a draft research question phrased as a single sentence. We will review your dataset choice and research question together in conversation, and you will workshop your analysis plan with classmates who are working on different corpora and will see issues you miss.

**Bring to class:**
- Your chosen dataset (one of the eleven on the menu; off-menu corpora from `scdenney/nlp_corpora` or elsewhere are possible by prior email approval)
- A draft research question, phrased as a single sentence

**Format:**
- Brief one-on-one review of dataset choice and research question
- "Hackathon" style collaborative workshop with peer consultation
- Instructor and peer support for planning the analysis

**Orange Data Mining:**
- Review and apply relevant tutorials from throughout the semester as needed for your project

**Final paper due:** Friday 5 June 2026, 23:59 (Brightspace).


*Note: This schedule is subject to adjustment based on class progress and needs. Any changes will be communicated in advance.*

  </div>
</div>
