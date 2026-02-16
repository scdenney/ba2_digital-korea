# ============================================================
# Korean Text Preprocessing + Word Cloud
# BA2 Digital Korea — Week 3 Optional Assignment
#
# This script walks through the Korean text preprocessing
# pipeline: reading a corpus, tokenizing with Kiwi (a Korean
# morphological analyzer), filtering by POS tags, and removing
# stopwords. The word cloud at the end is a quick way to verify
# your preprocessing produced meaningful output.
#
# Before running, make sure you have the presidential speeches
# CSV in your data folder. Download it from the course Data page.
# ============================================================


# ── Step 1: Install required R packages (only needed once) ──────

install.packages(c("tidyverse", "ggwordcloud", "reticulate"))


# ── Step 2: Set up Python + Kiwi (only needed once) ────────────
# After running this step for the first time, RESTART RStudio
# before continuing to Step 3.

library(reticulate)

# If you don't already have Python, this gives you one.
# If you do, it will say so and move on. Say "yes" if prompted.
tryCatch(install_miniconda(), error = function(e) {
  message("Miniconda already installed or not needed — continuing.")
})

# Install the Kiwi Korean tokenizer.
# pip = TRUE is required — this package is not on conda-forge.
py_install("kiwipiepy", pip = TRUE)

# Verify it worked (should print TRUE).
# If it prints FALSE, restart RStudio and run only the two lines below:
#   library(reticulate)
#   cat("kiwipiepy installed:", py_module_available("kiwipiepy"), "\n")
cat("kiwipiepy installed:", py_module_available("kiwipiepy"), "\n")


# ── Step 3: Load libraries ─────────────────────────────────────

library(tidyverse)
library(ggwordcloud)
library(reticulate)


# ── Step 4: Set file paths ─────────────────────────────────────
# Automatically detect where this script lives so all paths work
# regardless of your working directory.

script_dir <- dirname(rstudioapi::getSourceEditorContext()$path)
data_dir   <- dirname(script_dir)   # data/scripts/ -> data/


# ── Step 5: Read the corpus ────────────────────────────────────

speeches <- read_csv(
  file.path(data_dir, "president_speeches",
            "president_speeches_democratic_era.csv"),
  show_col_types = FALSE
)

cat("Loaded", nrow(speeches), "speeches\n")


# ── Step 6: Set up Kiwi for Korean preprocessing ───────────────
# Kiwi is a Python package, so we call it from R using reticulate.
# The code below defines a preprocessing function in Python.

stopword_file <- file.path(data_dir, "stopwords_ko.txt")

py_run_string(sprintf("
from kiwipiepy import Kiwi
kiwi = Kiwi()

stopwords = set()
try:
    with open('%s', encoding='utf-8') as f:
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
    return [
        t.form for t in kiwi.tokenize(text)
        if t.tag.split('-')[0] in pos_tags
        and len(t.form) >= 2
        and t.form not in stopwords
    ]
", stopword_file))

cat("Kiwi ready\n")


# ── Step 7: Preprocess all speeches ────────────────────────────
# This may take a minute. We extract nouns (NNG + NNP) by default.
# To also include verbs and adjectives, change the line below to:
#   pos_tags <- c("NNG", "NNP", "VV", "VA")

pos_tags <- c("NNG", "NNP")

all_words <- speeches$speech_text |>
  map(~ py$preprocess(.x, pos_tags), .progress = "Tokenizing") |>
  list_c()

cat("Total words extracted:", length(all_words), "\n")


# ── Step 8: Count word frequencies ─────────────────────────────

word_freq <- tibble(word = all_words) |>
  count(word, sort = TRUE)

cat("Top 10 words:\n")
print(head(word_freq, 10))


# ── Step 9: Generate and save the word cloud ───────────────────

wc <- word_freq |>
  slice_max(n, n = 100) |>
  ggplot(aes(label = word, size = n, color = n)) +
  geom_text_wordcloud(seed = 42) +
  scale_size_area(max_size = 14) +
  scale_color_viridis_c() +
  theme_void()

ggsave(file.path(script_dir, "wordcloud.png"),
       plot = wc, width = 8, height = 6, dpi = 150)

cat("\nDone! Word cloud saved to the scripts folder.\n")
cat("Upload wordcloud.png to your GitHub repository.\n")
