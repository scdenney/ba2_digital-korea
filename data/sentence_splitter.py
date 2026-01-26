# data/sentence_splitter.py
import pandas as pd
import nltk
from pathlib import Path

# Ensure NLTK tokenizer is available
nltk.download("punkt")

# --- Paths ---
base = Path(__file__).parent          # points to /data
nikh_dir = base / "nikh"
input_file = nikh_dir / "nikh_corpus.csv"
output_file = nikh_dir / "nikh_sentences.csv"

# --- Columns ---
TEXT_COLUMN = "full_text"           # the column with full text
META_COLUMNS = ["period_ordered", "book_id", "nikh_period",
"level"]  # adjust as needed; keeps cols

print(f"Reading corpus from {input_file}")
df = pd.read_csv(input_file)

rows = []
for _, row in df.iterrows():
    sentences = nltk.sent_tokenize(str(row[TEXT_COLUMN]))
    for sent in sentences:
        new_row = {col: row[col] for col in META_COLUMNS if col in df.columns}
        new_row["sentence"] = sent.strip()
        rows.append(new_row)

out_df = pd.DataFrame(rows)
out_df.to_csv(output_file, index=False)
print(f"Saved {len(out_df)} sentences to {output_file}")
