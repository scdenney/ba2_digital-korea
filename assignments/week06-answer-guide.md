---
layout: default
title: "Week 6 — Midterm Answer Guide"
permalink: /assignments/week06-answers/
---

# Midterm Assessment — Answer Guide

**For in-class review after the assessment**

---

## Version A

### Q1. Why can't Korean text be tokenized by simply splitting on spaces?

| | Option |
|---|--------|
| a | Korean uses a different alphabet |
| **b** | **Korean is agglutinative — grammatical information is attached to word stems via particles and endings** |
| c | Korean sentences don't contain spaces |
| d | Korean words are too long for simple splitting |

> Korean eojeols (space-separated units) contain stems plus attached particles/endings, so splitting on spaces doesn't isolate meaningful units.

---

### Q2. What is a morpheme?

| | Option |
|---|--------|
| a | The smallest unit of sound in a language |
| b | A complete sentence in Korean |
| **c** | **The smallest meaningful unit of language** |
| d | A type of Korean character |

> A morpheme is the smallest unit carrying meaning — distinct from phonemes (sound) and syllables (writing units).

---

### Q3. In the preprocessing pipeline, what is the purpose of POS filtering?

| | Option |
|---|--------|
| a | To correct spelling errors in the text |
| **b** | **To keep only content-bearing morphemes (like nouns) and discard grammatical particles and endings** |
| c | To translate Korean text into English |
| d | To count how many words are in each document |

> After Kiwi decomposes eojeols into morphemes, POS filtering keeps nouns (NNG, NNP) and removes grammatical morphemes like particles (JKS, JKO) and endings (EF).

---

### Q4. What is the difference between document frequency filtering and TF-IDF?

| | Option |
|---|--------|
| a | They are the same thing |
| **b** | **Document frequency filtering removes words entirely from the corpus; TF-IDF reweights words but keeps them** |
| c | TF-IDF removes words; document frequency filtering reweights them |
| d | Document frequency filtering only applies to proper nouns |

> This is a critical distinction. DF filtering (min/max thresholds) deletes words from the DTM. TF-IDF adjusts weights — common words get lower scores but remain in the matrix.

---

### Q5. What information does the Bag of Words model deliberately discard?

| | Option |
|---|--------|
| a | Word frequencies |
| b | Document metadata like author and date |
| **c** | **Word order, grammar, and context** |
| d | The number of documents in the corpus |

> BoW treats each document as an unordered collection of words, deliberately sacrificing syntax and context for computational tractability.

---

### Q6. In a Document-Term Matrix, what do the rows, columns, and cells represent?

| | Option |
|---|--------|
| a | Rows = words, columns = documents, cells = TF-IDF scores |
| **b** | **Rows = documents, columns = words, cells = counts or weights** |
| c | Rows = sentences, columns = paragraphs, cells = word counts |
| d | Rows = authors, columns = dates, cells = speech lengths |

> Each row is one document, each column is one unique term, and each cell contains either a raw count or a weighted value (like TF-IDF).

---

### Q7. A word appears in 748 out of 749 presidential speeches. What can you say about its IDF score?

| | Option |
|---|--------|
| a | Very high — it appears in almost every document |
| **b** | **Very low — appearing in almost every document makes it uninformative** |
| c | Exactly zero — it should be removed entirely |
| d | It depends entirely on the word's TF score |

> IDF = log(N/DF). When DF approaches N, the ratio approaches 1 and log(1) approaches 0. Words in nearly every document get very low IDF because they don't help distinguish documents.

---

### Q8. What does concordance analysis reveal that simple word frequency counts cannot?

| | Option |
|---|--------|
| a | How many times a word appears across the corpus |
| b | The TF-IDF score of a word |
| **c** | **How a word is actually used in context** |
| d | Which documents are the longest |

> Concordance (KWIC) shows every occurrence with surrounding text, revealing meaning, usage patterns, and collocations that raw counts miss.

---

### Q9. Why are word clouds considered imprecise for comparing groups?

| | Option |
|---|--------|
| a | Word clouds use incorrect font sizes |
| **b** | **Size differences are hard to judge visually, layout changes each rendering, and they can mislead when comparing groups** |
| c | Word clouds only work with English text |
| d | Bar charts always show more words than word clouds |

> Human perception is poor at comparing areas (word size), and random layout changes make side-by-side comparison unreliable. Bar charts with exact values are more precise.

---

### Q10. In the standard Orange workflow, why are two Corpus widgets needed?

| | Option |
|---|--------|
| a | One for training data and one for test data |
| **b** | **The first selects the raw text column; after the Python Script creates processed_text, the second tells Orange to use that new column** |
| c | One displays Korean text and the other displays English translations |
| d | It is a workaround for a bug in Orange |

> The Python Script widget adds a new column (processed_text) to the data. Orange needs to be told which column is "the text" — the second Corpus widget does this.

---

### Extra Credit (Version A)

**A researcher finds that 경제 has high TF but low TF-IDF, while 통상 has moderate TF but very high TF-IDF. Which word better distinguishes the speeches?**

| | Option |
|---|--------|
| a | 경제, because it appears more frequently |
| **b** | **통상, because its high TF-IDF means it is frequent here but rare across the corpus, making it distinctive** |
| c | Neither — you need concordance analysis to determine distinctiveness |
| d | 경제, because higher TF always means higher importance |

> TF-IDF captures distinctiveness. High TF + low TF-IDF means the word is common everywhere. High TF-IDF means the word is concentrated in specific documents — exactly what "distinctive" means.

---

## Version B

### Q1. Korean is described as an "agglutinative" language. What does this mean for text analysis?

| | Option |
|---|--------|
| a | Korean words cannot be broken into smaller parts |
| **b** | **Multiple grammatical elements attach to word stems, so space-separated units contain several morphemes that must be decomposed** |
| c | Korean has no grammar rules |
| d | Korean text must always be analyzed character by character |

> Agglutinative languages build complex words by attaching morphemes. Each eojeol must be decomposed by a morphological analyzer (like Kiwi) to extract meaningful units.

---

### Q2. Where does the morpheme sit in the hierarchy of linguistic units?

| | Option |
|---|--------|
| a | It is the largest unit, above discourse |
| **b** | **Between syllable and eojeol — it is the smallest meaningful unit** |
| c | Between sentence and discourse |
| d | It is the same as a phoneme |

> The hierarchy runs: Discourse > Sentence > Eojeol > Morpheme > Syllable > Phoneme. Morphemes are where meaning begins.

---

### Q3. Why do we remove stopwords like 있다, 하다, and 것 even though they may pass POS filtering?

| | Option |
|---|--------|
| a | They are misspelled |
| b | They are too short to analyze |
| **c** | **They are high-frequency words that carry little topical meaning** |
| d | They only appear in colonial-era texts |

> These words pass POS filters (they're nouns/verbs) but are so common and general that they don't help distinguish topics or documents.

---

### Q4. What does Kiwi's morphological analyzer do to the eojeol 학생들이?

| | Option |
|---|--------|
| a | Translates it to "students" |
| **b** | **Decomposes it into morphemes: 학생/NNG + 들/XSN + 이/JKS** |
| c | Removes it as a stopword |
| d | Counts how many times it appears in the document |

> Kiwi breaks the eojeol into its constituent morphemes and tags each: 학생 (student, common noun), 들 (plural suffix), 이 (subject particle).

---

### Q5. Why is the Document-Term Matrix mostly zeros (sparse)?

| | Option |
|---|--------|
| a | The data is corrupted |
| b | Most preprocessing steps failed |
| **c** | **Any given document uses only a small fraction of all the words in the entire corpus** |
| d | Korean text naturally produces many zero values |

> With thousands of unique terms across the corpus, each individual document uses only a subset, leaving most cells at zero. This sparsity is normal and expected.

---

### Q6. What is the difference between a matrix, a DTM, and a dataframe?

| | Option |
|---|--------|
| a | They are all the same thing |
| **b** | **A matrix is a grid of numbers; a DTM is a specific matrix where rows are documents, columns are terms, and cells are counts/weights; a dataframe is a table with named columns of mixed types** |
| c | A DTM contains text; a matrix contains numbers; a dataframe contains images |
| d | Matrices are used in mathematics; DTMs and dataframes are not |

> These are related but distinct concepts. A DTM is a specialized matrix purpose-built for text analysis. A dataframe (like a CSV) can hold mixed data types with column names.

---

### Q7. If a word has high TF in a document but low TF-IDF, what does that tell you?

| | Option |
|---|--------|
| a | The word is important and distinctive for that document |
| **b** | **The word is frequent in this document but also common across the corpus, so it is not distinctive** |
| c | The preprocessing pipeline failed for that word |
| d | The word should be added to the stopword list |

> TF-IDF = TF x IDF. If TF is high but TF-IDF is low, IDF must be low — meaning the word appears in many documents and doesn't distinguish this one.

---

### Q8. If you place a Select Rows widget before the Bag of Words widget in Orange, how does this affect TF-IDF scores?

| | Option |
|---|--------|
| a | It has no effect |
| **b** | **TF-IDF scores are calculated relative to the filtered subset only, not the full corpus** |
| c | It removes all TF-IDF scores |
| d | It only affects word clouds, not TF-IDF values |

> TF-IDF depends on document frequency across the corpus being analyzed. Filtering first changes what counts as "the corpus," so IDF values change.

---

### Q9. What is one strength and one limitation of word clouds?

| | Option |
|---|--------|
| a | They show exact values well; limitation is they only work with nouns |
| **b** | **They give a quick visual overview of frequent terms; limitation is size differences are hard to judge precisely** |
| c | They show grammar structure well; limitation is they require English text |
| d | They show document length well; limitation is they cannot display Korean |

> Word clouds are good for first impressions and spotting preprocessing issues, but area-based comparisons are unreliable for precise analysis.

---

### Q10. What is the purpose of L2 normalization in the Bag of Words widget?

| | Option |
|---|--------|
| a | To translate text to a standard language |
| **b** | **To scale each document row to unit length, removing the effect of document length differences** |
| c | To remove stopwords from the DTM |
| d | To convert raw counts to percentages |

> Longer documents naturally have higher term frequencies. L2 normalization divides each row by its length, so documents of different sizes can be compared fairly.

---

### Extra Credit (Version B)

**A student sees 정부 as the largest word in both a "politics" and "economics" word cloud subset. They conclude it's equally important to both. What's wrong with this reasoning?**

| | Option |
|---|--------|
| a | Nothing is wrong — word clouds are always accurate |
| **b** | **Word cloud size reflects frequency, not meaning. Concordance analysis would show how 정부 is used differently in each subset** |
| c | The student should use a bar chart instead, which would completely solve the problem |
| d | The student needs to remove 정부 as a stopword |

> Same frequency doesn't mean same usage. In politics articles, 정부 might collocate with "policy" and "reform"; in economics, with "spending" and "regulation." Concordance reveals these contextual differences.

---

## Grading Formula

| Component | Scoring | Weight |
|---|---|---|
| Multiple Choice (10 questions) | 1 point each = 10 points raw | Weighted to **8 points**: (raw / 10) x 8 |
| Preprocessing Task | 0, 1, or 2 points | **2 points** |
| **Total** | | **out of 10** |
| Extra Credit | +1 bonus point (added on top) | |

**Preprocessing task rubric:**

- **0** — Did not preprocess or did not follow directions
- **1** — Attempted but incomplete or pipeline issues
- **2** — Successful preprocessing with clean output
