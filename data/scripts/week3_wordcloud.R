# ============================================================
# Korean Word Cloud Generator
# BA2 Digital Korea — Week 3 Optional Assignment
#
# This script:
#   1. Reads the presidential speeches corpus
#   2. Preprocesses Korean text using Kiwi (via Python)
#   3. Generates a word cloud
#   4. Saves it as a PNG image
#
# Before running, make sure you have the presidential speeches
# CSV in your data folder. Download it from the course Data page.
# ============================================================


# ── Step 1: Install required R packages (only needed once) ──────

install.packages(c("reticulate", "wordcloud", "RColorBrewer"))


# ── Step 2: Set up Python + Kiwi (only needed once) ────────────

library(reticulate)

# This installs a small Python environment managed by R.
# Say "yes" if prompted.
install_miniconda()

# Install the Kiwi Korean tokenizer
py_install("kiwipiepy")


# ── Step 3: Load libraries ─────────────────────────────────────

library(wordcloud)
library(RColorBrewer)


# ── Step 4: Read the corpus ────────────────────────────────────
# IMPORTANT: Change this path to match where YOUR CSV file is.

speeches <- read.csv(
  "data/president_speeches/president_speeches_democratic_era.csv",
  stringsAsFactors = FALSE
)

cat("Loaded", nrow(speeches), "speeches\n")


# ── Step 5: Set up Kiwi for Korean preprocessing ───────────────
# Kiwi is a Python package, so we call it from R using reticulate.
# The code below defines a preprocessing function in Python.

py_run_string("
from kiwipiepy import Kiwi
kiwi = Kiwi()

# Stopwords: common words that don't carry meaning for analysis
stopwords = set()
try:
    with open('data/stopwords_ko.txt', encoding='utf-8') as f:
        for line in f:
            w = line.strip()
            if w and ' ' not in w:
                stopwords.add(w)
                if len(w) > 1 and w.endswith('다'):
                    stopwords.add(w[:-1])
except FileNotFoundError:
    pass

def preprocess(text, pos_tags=['NNG', 'NNP']):
    \"\"\"Tokenize Korean text and keep only selected POS tags.\"\"\"
    if not text or not isinstance(text, str):
        return []
    tokens = kiwi.tokenize(text)
    result = []
    for t in tokens:
        tag = t.tag.split('-')[0]  # normalize VV-R -> VV, etc.
        if tag in pos_tags and len(t.form) >= 2 and t.form not in stopwords:
            result.append(t.form)
    return result
")

cat("Kiwi ready\n")


# ── Step 6: Preprocess all speeches ────────────────────────────
# This may take a minute. We extract nouns (NNG + NNP) by default.
# To also include verbs and adjectives, change the line below to:
#   pos_tags <- c("NNG", "NNP", "VV", "VA")

pos_tags <- c("NNG", "NNP")

all_words <- c()
for (i in seq_len(nrow(speeches))) {
  text <- speeches$speech_text[i]
  words <- py$preprocess(text, pos_tags)
  all_words <- c(all_words, unlist(words))

  if (i %% 100 == 0) cat("  Processed", i, "of", nrow(speeches), "\n")
}

cat("Total words extracted:", length(all_words), "\n")


# ── Step 7: Count word frequencies ─────────────────────────────

word_freq <- as.data.frame(table(all_words), stringsAsFactors = FALSE)
colnames(word_freq) <- c("word", "freq")
word_freq <- word_freq[order(-word_freq$freq), ]

cat("Top 10 words:\n")
print(head(word_freq, 10))


# ── Step 8: Generate and save the word cloud ───────────────────

png("wordcloud.png", width = 800, height = 600, res = 150)

wordcloud(
  words = word_freq$word,
  freq  = word_freq$freq,
  max.words = 100,
  random.order = FALSE,
  colors = brewer.pal(8, "Dark2"),
  scale = c(3, 0.5)
)

dev.off()

cat("\nDone! Word cloud saved as 'wordcloud.png'\n")
cat("Upload this file to your GitHub repository.\n")
