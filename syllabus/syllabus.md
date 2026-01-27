# Course Syllabus: Digital Korea

## Expanded Description

This course introduces students to computational text analysis as a research method in Korean (Area) Studies. Students will learn to treat text as data, transforming written sources into formats that can be analyzed using computational tools. The course covers the full text analysis pipeline: preprocessing (preparing text for analysis), descriptive analysis (finding patterns in word usage), clustering (discovering natural groupings in documents), classification (categorizing texts using both rule-based and machine learning approaches), and topic modeling (uncovering hidden themes across document collections).

Students work primarily with Orange Data Mining, a widget-based, drag-and-drop software tool that makes computational methods accessible without requiring (advanced) programming skills. In addition, students develop foundational R programming skills through tutorials, building some initial capacity for more advanced work. No prior programming or statistical experience is required. You only need curiosity and a willingness to learn by trial and error.

Throughout the course, students engage with the possibilities and limitations of computational approaches to cultural and textual analysis. They learn to work with data according to FAIR principles (Findable, Accessible, Interoperable, Reusable) and develop practical and transferable skills in documenting and sharing research workflows. The course culminates in a Research Methods Project in which students apply text analysis methods to Korean-language materials (or another primary source Asian language), generating data and analysis that will inform their final papers.

## Course Policies

### Assessment
- Participation (15%) [attendance, R programming assigsnments]
- Research Methods Project (35%) [in-class assessments, Week 12 workshop]
- Final Paper (60%)

#### Participation
Each R Programming exercise or assignment listed below is assessed as complete (1) or incomplete (0). To receive credit, assignments must be submitted by the start of the next class. Late submissions receive no credit; partial credit is possible at the instructor's discretion.

Full attendance is not only expected but, for a hands-on class such as this, extremely important. Each class you are marked as present (1) or absent (0). If you miss a class, you must catch up immediately by reviewing lecture material and consulting your peers. With exceptions for extenuating circumstances, absences are not excused and no extensions for assignments will be granted.

The final participation grade is calculated as the proportion of completed items (assignments and attendance), scaled to 10.

#### Research Methods Project
The Research Methods Project (RMP) requires students to apply course methods to a research question of their choosing, generating data and analysis that will both constitute a grade ('Project on Research Methods') and inform their final papers. The RMP is due at the end of Week 12. It will be assessed out of 10. Information and guidelines are provided in class. Methods assessments (Week 6 and Week 11) also contribute to this grade. Each assessment is a multiple choice and/or short answer test administered in class, also out of 10 total points. The final grade is the average of the RMP and assesments.

#### Final Paper
The final paper is a ~5,000 word research report applying computational text analysis methods learned in this course to a research question of the student's choosing. The paper should include an introduction, literature review, methods section, results, and conclusion. Students are expected to use their Research Methods Project as the basis for the paper. More information and guidelines will be provided in class. The final paper is due two weeks after the end of the course.

### Academic Integrity
- All work must be your own
- Generative AI tools (ChatGPT, Claude, etc.) may be used for assistance
- Using AI to write analysis text or interpretations is not permitted
- Plagiarism will result in failing the course

### Collaboration
- Assignments are individual work
- Discussing concepts and troubleshooting with peers is encouraged
- Sharing code/workflows directly is not permitted for individual assignments

---

# Schedule

## **Week 1 (Feb. 02): Introduction & Getting Started**

This opening week establishes the foundation for the course. Students will ensure they have the right technical setup and understand course expectations. We'll configure essential tools including GitHub for version control and collaboration, R and RStudio for programming with Swirl, DataCamp for guided learning modules in R, and Orange Data Mining as our primary analysis tool.

**Topics:**
- Course overview and expectations
- Technical environment setup
- Introduction to course tools and platforms

**In-Class Assignments:**
- GitHub setup; clone course repository; share repository link with - instructor
- Confirm DataCamp enrollment
- Verify installations: RStudio, Swirl and Swirl courses, Orange Data Mining.
- *Note:* To continue in this class, these assignments must be completed.

**R Programming:**
- Complete Swirl R Programming lessons 1, 2, 4, 6, 7, 12: Basic Building Blocks, Workspace and Files, Vectors, Subsetting Vectors, Matrices and Data Frames, Looking at Data. Due by start of next class.

---

## **Week 2 (Feb. 09): Foundations of Computational Text Analysis**

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

## **Week 3 (Feb. 16): Text Preprocessing Basics**

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
- Getting Started 16: Text Preprocessing

**Orange Widgets to Master:**
- Corpus (loading text data)
- Preprocess Text (tokenization, normalization, filtering)
- Bag of Words (creating document-term matrix)

**R Programming:**
- Complete DataCamp: Introduction to Text Analysis in R - Chapter 1: Wrangling Text.

---

## **Week 4 (Feb. 23): Text Preprocessing Practice**

Building on Week 3, this week provides hands-on practice with preprocessing workflows. We'll explore morphological analysis (word structure and formation), deepen our understanding of the bag-of-words approach, specifically, how text gets transformed into a document-term matrix (DTM), the table of word counts that makes computational analysis possible. We introduce term frequency (TF) as our first measurement approach and preview term frequency-inverse document frequency (TF-IDF). Students will work through complete preprocessing pipelines from raw text to analysis-ready data.

**Topics:**
- Review and reinforcement of Week 3 concepts
- Morphological preparation and analysis
- Bag-of-words representation
- Term frequency measurements

**Hands-On:**
- Complete preprocessing workflows
- Build document-term matrices
- Calculate and interpret term frequencies

**Assignment:**
- Reproduce class demo; upload .ows file and screenshot of ODM whiteboard/workflow.

**Optional R Programming:**
- Complete DataCamp: Text Mining with Bag-of-Words in R - Chapter 1: Jumping into Text Mining with Bag-of-Words

---

## **Week 5 (Mar. 02): Descriptive Patterns in Text**

This week introduces methods for describing and visualizing patterns in text data. Students review how to calculate term frequency (TF) and frequency-inverse document frequency (TF-IDF) measures. Visualization techniques including word clouds, frequency distributions, and bar charts for exploring and communicating patterns in corpora.

**Topics:**
- Term frequency (TF) and TF-IDF weighting
- Measuring word importance across documents
- Visualization techniques for text data
- Interpreting descriptive patterns

**Recommended Reading:**
- Grimmer, Roberts, and Stewart - Chapters 6-7: The Multinomial Language Model; The Vector Space Model and Similarity Metrics
- Bollen, J., et al. (2021). Historical language records reveal a surge of cognitive distortions in recent decades. *Proceedings of the National Academy of Sciences*, 118(30)

**Orange Data Mining Tutorials:**
- Getting Started 19: How to Import Text Documents (optional)

**Orange Widgets to Master:**
- Word Cloud (visual representation of word frequencies)
- Statistics (frequency analysis)
- Distributions (exploring data patterns)
- Bar Plot (comparative visualization)

**R Programming:**
- Complete DataCamp: Introduction to Text Analysis in R - Chapter 2: Visualizing Text.

**Optional R Programming:**
- Complete DataCamp: Text Mining with Bag-of-Words in R - Chapter 2: Word Clouds and More Interesting Visuals

---

## **Week 6 (Mar. 09): Midterm Review & Assessment**

This week consolidates learning from Weeks 1-5, covering setup and tools, foundational concepts, preprocessing workflows, and descriptive analysis. The midterm assessment, administered in class, evaluates understanding of core concepts and practical skills developed thus far. More information about this assessment will be provided in class. Weeks 7-10 require your complete understanding of everything to this point.

**Topics:**
- Comprehensive review of Weeks 1-5
- Midterm assessment

---

## **Week 7 (Mar. 16): Clustering**

Clustering introduces "unsupervised" learning, where algorithms discover patterns in data without human-provided assistance. We explore how documents can be represented as vectors and words analyzed as numbers, then learn two clustering approaches: hierarchical clustering, which builds a tree of nested clusters, and k-means clustering, which partitions documents into groups.

**Topics:**
- Introduction to unsupervised learning
- Vectorization with TF-IDF as foundation for clustering
- Hierarchical clustering (agglomerative methods)
- K-means clustering (partition-based methods)
- Choosing appropriate number of clusters

> **Special Lecture:** Brief introduction to word embeddings and distributed representations (TBD and conditional on sufficient demand)

**Recommended Reading:**
- Grimmer, Roberts, and Stewart - Chapter 12: Clustering

**Orange Data Mining Tutorials:**
- Getting Started 05: Hierarchical Clustering
- Getting Started 11: k-Means
- Getting Started 12: k-Means Explained

**Orange Widgets to Master:**
- Hierarchical Clustering (tree-based grouping)
- k-Means (partition-based grouping)
- Distance Matrix (calculating document similarities)
- Distances (choosing distance metrics)

**Hands-On:**
- Complete workflow from corpus through preprocessing to clustering
- Apply hierarchical clustering; interpret the dendrogram
- Apply k-means clustering

**R Programming:**
- Complete Swirl Exploratory Data Analysis: Lessons 11 and 12 (Hierarchical Clustering, K-Means Clustering)

**Optional R Programming:**
- Complete DataCamp: Text Mining with Bag-of-Words in R - Chapter 3: Adding to Your TM Skills

**Assignment:**
- Reproduce class demo; upload .ows file and screenshot of ODM whiteboard/workflow. Also upload screenshots showing completion of Swirl exercises.

---

## **Week 8 (Mar. 30): Classification I – Dictionary and Rule-Based Approaches**

Classification assigns documents to predefined categories. This week focuses on dictionary-based methods, where humans define rules (like lists of positive and negative words for sentiment analysis) and the computer applies them. These interpretable, transparent methods serve as foundation for understanding more complex machine learning approaches in Week 9. We will use sentiment analysis in this week.

**Topics:**
- Dictionary-based sentiment analysis
- Rule-based text classification
- Building and applying custom dictionaries
- Advantages and limitations of dictionary methods

**Recommended Reading:**
- Grimmer, Roberts, and Stewart - Chapter 16: Word Counting
- Young, L., & Soroka, S. (2012). Affective news: The automated coding of sentiment in political texts. *Political Communication*, 29(2), 205-231

**Orange Data Mining Tutorials:**
- Getting Started 17: Text Clustering (for workflow understanding)

**Orange Widgets to Master:**
- Sentiment Analysis (applying sentiment dictionaries)
- Corpus Viewer (examining classified documents)
- Score Documents (custom dictionary scoring)

**R Programming:**
- Complete DataCamp: Introduction to Text Analysis in R - Chapter 3: Sentiment Analysis

**Assignment:**
- Reproduce class demo; upload .ows file and screenshot of ODM whiteboard/workflow.

---

## **Week 9 (Apr. 13): Classification II – Machine Learning with Support Vector Machines**

This week introduces supervised machine learning for classification. Unlike dictionary methods where we write the rules, supervised learning involves providing labeled examples and letting algorithms learn classification patterns. We focus on Support Vector Machines (SVM), a powerful classification algorithm. Students learn to split data into training and testing sets, train classifiers, and evaluate performance using appropriate metrics. This is the most challenging thing leanred in this class. 

**Topics:**
- Introduction to supervised learning
- Support Vector Machines (SVM) for text classification
- Training and testing workflows
- Evaluation metrics
- Comparing dictionary and machine learning approaches

**Recommended Reading:**
- Grimmer, Roberts, and Stewart - Chapters 17-19: Overview of Supervised Classification; Coding a Training Set; Classifying Documents with Supervised Learning
- Barberá, P., et al. (2021). Automated text classification of news articles: A practical guide. *Political Analysis*, 29(1), 19-42

**Orange Data Mining Tutorials:**
- Getting Started 18: Text Classification
- Getting Started 06: Making Predictions
- Getting Started 07: Model Evaluation and Scoring

**Orange Widgets to Master:**
- SVM (training support vector machine classifier)
- Test and Score (evaluating model performance)
- Predictions (applying trained models to new data)
- Select Columns (preparing train/test splits)

---

## **Week 10 (Apr. 20): Topic Modeling with Latent Dirichlet Allocation**

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
- Getting Started 09: Principal Component Analysis (not totally related; for conceptual background)

**Orange Widgets to Master:**
- Topic Modelling (fitting LDA models)
- LDAvis (interactive topic visualization and interpretation)
- Corpus Viewer (examining documents by topic)

**R Programming:**
- Complete DataCamp: Introduction to Text Analysis in R - Chapter 4: Topic Modeling

**Assignment:**
- Reproduce class demo; upload .ows file and screenshot of ODM whiteboard/workflow.

---

## **Week 11 (May 11): Final Review & Assessment**

This second assessment, administered in class, evaluates understanding of core concepts and practical skills developed from Week 7.

Following the assessment, we will review our learning across the entire course, from preprocessing through clustering, classification, and topic modeling. It will focus more on content learned in the second half of the class. It will also prepare students for the week 12 Workshop. 

**Topics:**
- Second assessment
- Comprehensive review
- Overvivew of Week 12 Workshop

---

## **Week 12 (May 18): Research Methods Project Workshop**

This intensive workshop session provides dedicated time for students to work on their Research Methods Projects in a supportive environment. The RMP requires students to apply course methods to a research question, generating data and analysis that will both constitute a grade ('Project on Research Methods') and inform their final papers. 

More information aobut this workshop will be provided in class.

**Topics:**
- Hands-on project development
- Troubleshooting technical challenges
- Interpreting results
- Preparing analysis for final paper

**Format:**
- "Hackathon" style collaborative workshop
- Instructor and peer consultation
- Technical support and guidance

**Orange Data Mining:**
- Review and apply relevant tutorials from throughout the semester as needed for project requirements

**Assignment:**
- The project is due at the end of the working day (17:00).


*Note: This schedule is subject to adjustment based on class progress and needs. Any changes will be communicated in advance.*


