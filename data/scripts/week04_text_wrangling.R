# ============================================================
# From Words to Numbers: Text Wrangling with Presidential Speeches
# BA2 Digital Korea — Week 4
#
# This script applies what you learned in DataCamp
# (Introduction to R Ch. 1-2 and Text Analysis in R Ch. 1)
# to our presidential speeches corpus.
#
# You'll practice: loading data, exploring with tidyverse,
# tokenizing text, removing stopwords, and counting words.
# ============================================================


# ── Step 1: Install packages (run once, then skip) ───────────

install.packages(c("tidyverse", "tidytext"))


# ── Step 2: Load libraries ───────────────────────────────────

library(tidyverse)
library(tidytext)


# ── Step 3: Load the presidential speeches ───────────────────
# Change this path to match where YOUR CSV file is.

speeches <- read.csv(
  "data/president_speeches/president_speeches_democratic_era.csv",
  stringsAsFactors = FALSE
)

# How big is our corpus?
nrow(speeches)

# What columns do we have?
colnames(speeches)

# Look at the first few rows
head(speeches)


# ── Step 4: Explore the corpus with tidyverse ────────────────
# These are the same skills from DataCamp Ch. 1 (Wrangling Text):
# filter(), group_by(), summarize(), count(), arrange()

# How many speeches per president?
speeches %>%
  count(president, sort = TRUE)

# What's the date range for each president?
speeches %>%
  group_by(president) %>%
  summarize(
    n_speeches = n(),
    earliest = min(date),
    latest = max(date)
  )


# ── Step 5: Tokenize the text ───────────────────────────────
# unnest_tokens() splits text into one-word-per-row,
# just like you did with tweets in DataCamp.

words <- speeches %>%
  unnest_tokens(word, speech_text)

# How many total word tokens?
nrow(words)

# Look at what happened: each row is now one word
head(words, 10)


# ── Step 6: Count the most frequent words ────────────────────

word_counts <- words %>%
  count(word, sort = TRUE)

# Top 20 words
head(word_counts, 20)

# Notice: the top words are mostly grammatical particles
# (을, 를, 의, 이, 에, 등) — not very informative!
# This is like the English stopwords problem from DataCamp.


# ── Step 7: Remove stopwords ────────────────────────────────
# In DataCamp you used anti_join(stop_words) for English.
# For Korean, we build our own stopword list using c() — vectors!
# (Remember DataCamp Intro to R Ch. 2?)

korean_stopwords <- c(
  # Particles and suffixes (split off by tokenizer)
  "의", "에", "를", "을", "이", "가", "은", "는", "로", "으로",
  "에서", "와", "과", "도", "만", "까지", "부터", "에게",
  # Common but uninformative words
  "것", "수", "등", "중", "및", "위", "때", "더", "또", "그",
  "이런", "저", "매우", "잘", "큰", "좋은", "많은", "새로운",
  # Common verbs/endings (appear after tokenization)
  "하다", "되다", "있다", "없다", "하고", "하는", "하여",
  "위한", "대한", "통한", "있는", "되는", "한다"
)

# Turn it into a data frame so we can use anti_join()
korean_stop_df <- data.frame(word = korean_stopwords)

# Remove Korean stopwords — same pattern as DataCamp!
words_clean <- words %>%
  anti_join(korean_stop_df, by = "word")

# Count again
clean_counts <- words_clean %>%
  count(word, sort = TRUE)

# Top 20 after removing stopwords
head(clean_counts, 20)

# Much better — now we see content words like
# 국민, 경제, 사회, 국가, 대통령, etc.


# ── Step 8: Compare presidents ───────────────────────────────
# filter() + count() — just like filtering tweets in DataCamp

# Top words for one president
words_clean %>%
  filter(president == "노무현") %>%
  count(word, sort = TRUE) %>%
  head(15)

# Compare: top words for a different president
words_clean %>%
  filter(president == "이명박") %>%
  count(word, sort = TRUE) %>%
  head(15)

# Are the top words the same or different?
# Words like 국민 appear for everyone — not very distinctive.
# This is the problem that TF-IDF solves! (We'll cover this in class.)


# ── Step 9: Track a word across presidents ───────────────────
# How often does 경제 appear per president?

words_clean %>%
  filter(word == "경제") %>%
  count(president, sort = TRUE)

# Try other words: 민주, 통일, 평화, 북한
words_clean %>%
  filter(word == "민주") %>%
  count(president, sort = TRUE)


# ── Recap ────────────────────────────────────────────────────
# What you practiced:
#   - read.csv() to load data
#   - Vectors with c() for our stopword list
#   - Pipes %>% to chain operations
#   - unnest_tokens() to tokenize text
#   - anti_join() to remove stopwords
#   - count() and arrange() for word frequencies
#   - filter() to compare subsets
#
# Next question: how do we find words that are *distinctive*
# to one president, not just *frequent*? → TF-IDF (in class!)
# ============================================================
