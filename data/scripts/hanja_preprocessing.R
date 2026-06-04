# ============================================================
# Korean + Hanja + Hanmun Text Preprocessing in RStudio
# BA2 Digital Korea — Hanja-aware variant
#
# For mixed-script historical corpora (Colonial Magazines,
# Kaebyok, older newspapers). Each article is ROUTED by its
# Hanja density:
#
#   * KOREAN / mixed  (Hanja share < HANMUN_THRESHOLD)
#       Every Hanja is converted to its Korean READING
#       (學生 -> 학생) and tokenized with Kiwi, keeping nouns.
#       This is reading substitution, NOT translation of meaning.
#
#   * HANMUN / Classical Chinese  (Hanja share >= HANMUN_THRESHOLD)
#       Kiwi is a modern-Korean analyzer and cannot parse literary
#       Chinese, so these articles are tokenized at the CHARACTER
#       level — each Hanja is one token — with a Classical-Chinese
#       function-word stoplist applied. They are marked
#       text_type = "hanmun" so you can analyze them separately.
#
# It mirrors week03_preprocessing.R and adds `hanja` to the same
# reticulate -> Python bridge.
#
# Output columns added to the corpus:
#   hanja_ratio     Hanja share (0–1) of each article
#   text_type       "korean" or "hanmun"
#   processed_text  the tokens, space-joined
# ============================================================


# ── Step 1: Install packages (run once, then skip) ─────────────

install.packages(c("tidyverse", "reticulate"))
# Optional, only if you load the .parquet instead of a .csv:
# install.packages("arrow")


# ── Step 2: Set up Python + Kiwi + hanja (run once) ────────────
# After running this the FIRST time, RESTART RStudio before Step 3.

library(reticulate)

if (packageVersion("reticulate") >= "1.40") {
  py_require(c("kiwipiepy", "hanja"))      # declares both dependencies
} else {
  tryCatch(install_miniconda(), error = function(e)
    message("Miniconda already installed or not needed — continuing."))
  py_install(c("kiwipiepy", "hanja"), pip = TRUE)
}

cat("kiwipiepy:", py_module_available("kiwipiepy"),
    " hanja:", py_module_available("hanja"), "\n")
# Both should print TRUE. If either is FALSE, restart RStudio and
# re-run the two lines above.


# ── Step 3: Load libraries ─────────────────────────────────────

library(tidyverse)
library(reticulate)


# ── Step 4: Set your file paths + threshold (EDIT THESE) ───────
# Point these at where YOU saved the downloaded files.

corpus_file      <- "kaebyok.csv"        # any Colonial Magazines CSV
stopword_file    <- "stopwords_ko.txt"   # the Korean stopwords file you downloaded
TEXT_COLUMN      <- "text"               # the column holding the article text
HANMUN_THRESHOLD <- 0.60                 # Hanja share at/above which an article is Hanmun


# ── Step 5: Read the corpus ────────────────────────────────────

corpus <- read_csv(corpus_file, show_col_types = FALSE)
# For the full corpus instead, use the parquet (needs the arrow package):
#   corpus <- arrow::read_parquet("colonial_magazines.parquet")

cat("Loaded", nrow(corpus), "articles\n")


# ── Step 6: Define the Python preprocessing functions ──────────
# These run inside Python via reticulate. The Hanja conversion
# happens BEFORE tokenizing, so Kiwi sees ordinary Korean. Hanmun
# articles are routed to character-level tokenization instead.

py_run_string(sprintf("
from kiwipiepy import Kiwi
import hanja
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

# Classical-Chinese function words to drop in the Hanmun branch.
hanmun_stopwords = set('之 而 不 則 其 也 矣 乎 焉 者 以 於 于 所 乃 且 亦 即 既 故 哉 耳 歟 耶 邪 兮 諸 斯 蓋 凡 惟 唯'.split())

def _is_hanja(c):
    o = ord(c)
    return (0x3400 <= o <= 0x9fff) or (0xf900 <= o <= 0xfaff) or (0x20000 <= o <= 0x2fa1f)

def _is_hangul(c):
    return 0xac00 <= ord(c) <= 0xd7a3

def hanja_ratio(text):
    if not text or not isinstance(text, str):
        return 0.0
    h = sum(1 for c in text if _is_hanja(c))
    k = sum(1 for c in text if _is_hangul(c))
    return h / (h + k) if (h + k) else 0.0

def preprocess(text, pos_tags, hanmun_threshold):
    if not text or not isinstance(text, str):
        return []
    # HANMUN branch: Classical Chinese -> 1 Hanja = 1 token, drop particles
    if hanja_ratio(text) >= hanmun_threshold:
        return [c for c in text if _is_hanja(c) and c not in hanmun_stopwords]
    # KOREAN branch: Hanja -> reading, safety-strip residue, Kiwi nouns
    text = hanja.translate(text, 'substitution')
    text = ''.join(' ' if _is_hanja(c) else c for c in text)
    out = []
    for t in kiwi.tokenize(text):
        if t.tag.split('-')[0] in pos_tags and len(t.form) >= 2 and t.form not in stopwords:
            out.append(t.form)
    return out
", stopword_file))

cat("Kiwi + hanja ready\n")


# ── Step 7: Preprocess every article ───────────────────────────
# To also keep verbs/adjectives in the Korean branch:
#   pos_tags <- c("NNG","NNP","VV","VA")

pos_tags <- c("NNG", "NNP")

corpus <- corpus |>
  mutate(
    hanja_ratio    = map_dbl(.data[[TEXT_COLUMN]], ~ py$hanja_ratio(.x)),
    text_type      = if_else(hanja_ratio >= HANMUN_THRESHOLD, "hanmun", "korean"),
    tokens         = map(.data[[TEXT_COLUMN]],
                         ~ py$preprocess(.x, pos_tags, HANMUN_THRESHOLD),
                         .progress = "Tokenizing"),
    processed_text = map_chr(tokens, ~ paste(.x, collapse = " "))
  )

cat("text_type counts:\n")
print(count(corpus, text_type))


# ── Step 8: Use the results ────────────────────────────────────
# The two text types live in different vocabularies (Korean words
# vs Classical-Chinese characters), so analyze them separately:

corpus_korean <- corpus |> filter(text_type == "korean")
corpus_hanmun <- corpus |> filter(text_type == "hanmun")

cat("\nExample KOREAN article (readings + nouns):\n")
cat(substr(corpus_korean$processed_text[1], 1, 200), "\n")

cat("\nExample HANMUN article (Hanja characters):\n")
cat(substr(corpus_hanmun$processed_text[1], 1, 200), "\n")

# `corpus_korean$processed_text` -> word frequencies, TF-IDF, topic models.
# `corpus_hanmun$processed_text` -> character-level analysis of the
#   Classical-Chinese material, kept separate so it does not distort
#   the modern-Korean vocabulary.
