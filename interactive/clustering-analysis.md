---
layout: default
title: "Clustering Korean History Textbooks"
---

<style>
/* ── Page layout ─────────────────────────────────────────────────── */
.tutorial-page { max-width: 100%; }

.tutorial-header {
  margin-top: 1rem;
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 2px solid #e2e8f0;
}

.tutorial-header h1 {
  font-size: 1.6rem;
  color: var(--leiden-blue);
  margin: 0 0 0.5rem;
}

.tutorial-subtitle {
  font-size: 1rem;
  color: #6b7280;
  margin: 0 0 0.75rem;
}

.tutorial-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  font-size: 0.82rem;
  color: #9ca3af;
}

.tutorial-meta span {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
}

/* ── Section headings ────────────────────────────────────────────── */
.section-heading {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin: 2.5rem 0 1rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid #e2e8f0;
}

.section-number {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--leiden-blue);
  color: #fff;
  font-size: 0.82rem;
  font-weight: 700;
  flex-shrink: 0;
}

.section-heading h2 {
  font-size: 1.25rem;
  color: var(--leiden-blue);
  margin: 0;
}

/* ── Code blocks ─────────────────────────────────────────────────── */
.code-block {
  position: relative;
  margin: 1rem 0;
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid #e2e8f0;
}

.code-block-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.4rem 0.75rem;
  background: #f1f5f9;
  border-bottom: 1px solid #e2e8f0;
  font-size: 0.75rem;
  color: #64748b;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.copy-btn {
  padding: 0.2rem 0.5rem;
  border: 1px solid #cbd5e1;
  border-radius: 4px;
  background: #fff;
  font-size: 0.72rem;
  color: #64748b;
  cursor: pointer;
  font-family: inherit;
  transition: all 0.15s;
}

.copy-btn:hover { background: #f8fafc; border-color: var(--leiden-blue); color: var(--leiden-blue); }
.copy-btn.copied { background: #ecfdf5; border-color: #6ee7b7; color: #059669; }

.code-block pre {
  margin: 0;
  padding: 1rem;
  background: #1e293b;
  color: #e2e8f0;
  font-size: 0.82rem;
  line-height: 1.55;
  overflow-x: auto;
  font-family: "SFMono-Regular", "Consolas", "Liberation Mono", monospace;
}

.code-block pre code { background: none; color: inherit; padding: 0; font-size: inherit; }

/* Syntax highlighting */
.code-block .r-comment { color: #94a3b8; font-style: italic; }
.code-block .r-string { color: #86efac; }
.code-block .r-function { color: #93c5fd; }
.code-block .r-keyword { color: #c4b5fd; }
.code-block .r-number { color: #fde68a; }
.code-block .r-operator { color: #f9a8d4; }

/* ── Narrative text ──────────────────────────────────────────────── */
.narrative {
  font-size: 0.95rem;
  line-height: 1.7;
  color: #374151;
  margin: 1rem 0;
}

.narrative strong { color: var(--leiden-blue); }

.callout {
  padding: 0.75rem 1rem;
  border-radius: 6px;
  margin: 1rem 0;
  font-size: 0.88rem;
  line-height: 1.6;
}

.callout-info {
  background: #eff6ff;
  border-left: 3px solid #3b82f6;
  color: #1e40af;
}

.callout-tip {
  background: #f0fdf4;
  border-left: 3px solid #22c55e;
  color: #166534;
}

/* ── Output panels ───────────────────────────────────────────────── */
.output-panel {
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  margin: 1.25rem 0;
  overflow: hidden;
}

.output-panel-header {
  padding: 0.4rem 0.75rem;
  background: #fafafa;
  border-bottom: 1px solid #e2e8f0;
  font-size: 0.75rem;
  color: #64748b;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.output-panel-body {
  padding: 1.25rem;
  background: #fff;
}

/* ── Data table ──────────────────────────────────────────────────── */
.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85rem;
}

.data-table th {
  background: #f8fafc;
  padding: 0.5rem 0.75rem;
  text-align: left;
  font-weight: 700;
  color: var(--leiden-blue);
  border-bottom: 2px solid #e2e8f0;
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}

.data-table td {
  padding: 0.5rem 0.75rem;
  border-bottom: 1px solid #f1f5f9;
  color: #374151;
}

.data-table tr:hover td { background: #f8fafc; }

.era-badge {
  display: inline-block;
  padding: 0.1rem 0.5rem;
  border-radius: 10px;
  font-size: 0.72rem;
  font-weight: 700;
  color: #fff;
}

.era-badge-colonial { background: #b45309; }
.era-badge-authoritarian { background: #7c3aed; }
.era-badge-democratic { background: #0891b2; }

/* ── Word cloud grid ─────────────────────────────────────────────── */
.wordcloud-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.wordcloud-card {
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  overflow: hidden;
}

.wordcloud-card-header {
  padding: 0.5rem 0.75rem;
  font-weight: 700;
  font-size: 0.85rem;
  text-align: center;
  color: #fff;
}

.wordcloud-card-header.era-colonial { background: #b45309; }
.wordcloud-card-header.era-authoritarian { background: #7c3aed; }
.wordcloud-card-header.era-democratic { background: #0891b2; }

.wordcloud-card-body {
  padding: 0.75rem;
  min-height: 220px;
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  justify-content: center;
  gap: 0.2rem 0.4rem;
  line-height: 1.3;
}

.wc-word {
  display: inline-block;
  cursor: default;
  font-weight: 600;
  transition: opacity 0.15s;
}

.wc-word:hover { opacity: 0.7; }

/* ── Chart legend ────────────────────────────────────────────────── */
.chart-legend {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  margin: 0.75rem 0 0.5rem;
  font-size: 0.8rem;
}

.chart-legend-item {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  color: #4b5563;
}

.chart-legend-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}

/* ── R code ribbon (collapsible) ─────────────────────────────────── */
.code-ribbon {
  margin: 1rem 0;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  overflow: hidden;
}

.code-ribbon summary {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: linear-gradient(to right, #1e293b, #334155);
  color: #e2e8f0;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  user-select: none;
  list-style: none;
  transition: background 0.2s;
}

.code-ribbon summary::-webkit-details-marker { display: none; }

.code-ribbon summary::before {
  content: "\25B6";
  font-size: 0.65rem;
  transition: transform 0.2s;
  flex-shrink: 0;
}

.code-ribbon[open] summary::before {
  transform: rotate(90deg);
}

.code-ribbon summary:hover {
  background: linear-gradient(to right, #0f172a, #1e293b);
}

.code-ribbon summary .ribbon-label {
  flex: 1;
}

.code-ribbon summary .ribbon-tag {
  padding: 0.12rem 0.45rem;
  border-radius: 4px;
  font-size: 0.68rem;
  font-weight: 700;
  background: rgba(255,255,255,0.12);
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.code-ribbon .code-ribbon-body {
  border-top: 1px solid #334155;
}

.code-ribbon .code-block {
  margin: 0;
  border: none;
  border-radius: 0;
}

.code-ribbon .callout {
  margin: 0;
  border-radius: 0;
  border-left-width: 3px;
}

/* ── Dendrogram SVG ──────────────────────────────────────────────── */
.dendro-container {
  width: 100%;
  overflow-x: auto;
  padding: 0.5rem 0;
}

.dendro-container svg {
  display: block;
  margin: 0 auto;
}

.dendro-link {
  fill: none;
  stroke: #94a3b8;
  stroke-width: 1.5;
}

.dendro-cut-line {
  stroke: #dc2626;
  stroke-width: 1.5;
  stroke-dasharray: 6 4;
}

.dendro-cut-label {
  font-size: 11px;
  fill: #dc2626;
  font-weight: 600;
}

.dendro-leaf-label {
  font-size: 11px;
  font-weight: 600;
}

.dendro-height-label {
  font-size: 10px;
  fill: #9ca3af;
}

/* ── Cluster comparison grid ─────────────────────────────────────── */
.cluster-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}

.cluster-card {
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  overflow: hidden;
}

.cluster-card-header {
  padding: 0.6rem 1rem;
  font-weight: 700;
  font-size: 0.85rem;
  color: #fff;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.cluster-card-body {
  padding: 0.75rem 1rem;
}

.cluster-book {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.3rem 0;
  font-size: 0.82rem;
  color: #374151;
}

.cluster-book-era {
  font-size: 0.68rem;
  font-weight: 700;
  padding: 0.1rem 0.4rem;
  border-radius: 8px;
  color: #fff;
  flex-shrink: 0;
}

.cluster-match {
  font-size: 0.75rem;
  opacity: 0.9;
}

/* ── Bar chart ───────────────────────────────────────────────────── */
.bar-chart-container {
  padding: 0.5rem 0;
}

.bar-row {
  display: flex;
  align-items: center;
  margin-bottom: 0.35rem;
  gap: 0.5rem;
}

.bar-label {
  width: 80px;
  font-size: 0.82rem;
  text-align: right;
  color: #374151;
  font-weight: 600;
  flex-shrink: 0;
}

.bar-track {
  flex: 1;
  height: 22px;
  background: #f1f5f9;
  border-radius: 4px;
  overflow: hidden;
  position: relative;
}

.bar-fill {
  height: 100%;
  border-radius: 4px;
  transition: width 0.6s ease;
  display: flex;
  align-items: center;
  padding-left: 6px;
}

.bar-value {
  font-size: 0.72rem;
  font-weight: 700;
  color: #fff;
  white-space: nowrap;
}

.bar-value-outside {
  font-size: 0.72rem;
  font-weight: 600;
  color: #6b7280;
  margin-left: 0.4rem;
  white-space: nowrap;
}

/* ── Responsive ──────────────────────────────────────────────────── */
@media (max-width: 768px) {
  .wordcloud-grid { grid-template-columns: 1fr; }
  .cluster-grid { grid-template-columns: 1fr; }
}
</style>

<div class="tutorial-page">

<div class="tutorial-header">
  <h1>Clustering Korean History Textbooks</h1>
  <p class="tutorial-subtitle">Hierarchical clustering, dendrogram visualization, and distinctive words by cluster</p>
  <div class="tutorial-meta">
    <span>Week 7</span>
    <span>R + tidyverse + tidytext</span>
    <span>NIKH History Textbook Corpus (11-book demo from 67-book corpus, 1895&ndash;2016)</span>
  </div>
</div>

<p class="narrative">
  In Weeks 3&ndash;5 we learned to preprocess text and measure word frequencies. This week we ask a different question: can an algorithm group texts by <em>similarity</em> without knowing anything about their labels? We use <strong>hierarchical clustering</strong> on TF-IDF vectors from 11 Korean history textbooks spanning three political eras &mdash; Colonial, Authoritarian, and Democratic &mdash; and see whether the clusters the algorithm discovers correspond to the eras we know.
</p>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">1</span>
  <h2>The Data: 11 History Textbooks</h2>
</div>

<p class="narrative">
  Our demo corpus is an 11-book subset of the 67-book NIKH (National Institute of Korean History) textbook corpus. The books span three political eras: 3 colonial-era textbooks (1940), 4 authoritarian-era textbooks (1973&ndash;1987), and 4 democratic-era textbooks (1995&ndash;2002). Each has been tokenized with Kiwi (NNG/NNP nouns, stopwords removed, min 2 characters).
</p>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: load the clustering demo corpus</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── Packages ──────────────────────────────────────────────────────</span>
<span class="r-function">library</span>(tidyverse)
<span class="r-function">library</span>(tidytext)

<span class="r-comment"># ── Load the clustering demo corpus ───────────────────────────────</span>
corpus <span class="r-operator">&lt;-</span> <span class="r-function">read_csv</span>(<span class="r-string">"data/nikh_textbooks/nikh_clustering_demo.csv"</span>)

<span class="r-comment"># Quick look at the data</span>
corpus <span class="r-operator">|&gt;</span>
  <span class="r-function">select</span>(book_id, title, era, year) <span class="r-operator">|&gt;</span>
  <span class="r-function">print</span>(n <span class="r-operator">=</span> <span class="r-number">11</span>)</code></pre>
    </div>
  </div>
</details>

<div class="output-panel">
  <div class="output-panel-header">Corpus Overview</div>
  <div class="output-panel-body" style="overflow-x: auto;">
    <table class="data-table" id="bookTable">
      <thead>
        <tr><th>Title</th><th>Era</th><th>Level</th><th>Year</th><th>Tokens</th></tr>
      </thead>
      <tbody></tbody>
    </table>
  </div>
</div>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">2</span>
  <h2>Preprocessing</h2>
</div>

<p class="narrative">
  The demo CSV includes a <code>processed_text</code> column with pre-tokenized nouns &mdash; the same Kiwi preprocessing pipeline from Weeks 3&ndash;5 (NNG/NNP nouns, stopwords removed, min 2 characters, no numbers). We split that column into one word per row and count how often each word appears in each book. No words are filtered out by document frequency &mdash; every word is kept, just like in the Week 5 demo.
</p>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: tokenize and count words per book</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── Tokenize from processed_text ──────────────────────────────────</span>
<span class="r-comment"># processed_text = space-separated nouns (Kiwi NNG/NNP),</span>
<span class="r-comment"># stopwords already removed, min 2 chars, no numbers.</span>
<span class="r-comment"># Same preprocessing as Weeks 3–5.</span>
tokens <span class="r-operator">&lt;-</span> corpus <span class="r-operator">|&gt;</span>
  <span class="r-function">select</span>(book_id, era, processed_text) <span class="r-operator">|&gt;</span>
  <span class="r-function">unnest_tokens</span>(word, processed_text)

<span class="r-comment"># ── Count words per book (raw frequencies) ────────────────────────</span>
<span class="r-comment"># No document-frequency filter: every word is kept.</span>
word_counts <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(book_id, word)

<span class="r-comment"># How many unique words per book?</span>
word_counts <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(book_id, name <span class="r-operator">=</span> <span class="r-string">"unique_words"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">left_join</span>(corpus <span class="r-operator">|&gt;</span> <span class="r-function">select</span>(book_id, title, era), by <span class="r-operator">=</span> <span class="r-string">"book_id"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">select</span>(book_id, title, era, unique_words)

<span class="r-comment"># Top 10 most frequent words across all books</span>
tokens <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(word, sort <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">slice_head</span>(n <span class="r-operator">=</span> <span class="r-number">10</span>)</code></pre>
    </div>
    <div class="callout callout-tip">
      <strong>Why no document-frequency filtering?</strong> With only 11 books, removing words that appear in too many or too few documents would discard useful signal. TF-IDF weighting (next step) already down-weights words that appear everywhere &mdash; no need to remove them outright.
    </div>
  </div>
</details>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">3</span>
  <h2>TF-IDF Vectorization &amp; Cosine Distance</h2>
</div>

<p class="narrative">
  Now we weight those raw word counts using <strong>TF-IDF</strong> (Term Frequency&ndash;Inverse Document Frequency) &mdash; the same technique from Week 4. TF-IDF down-weights common words that appear in every book (like <span style="font-family:inherit">나라</span>) and highlights words that are distinctive to particular books. We then compute <strong>cosine distance</strong> between every pair of books &mdash; the same metric you select in Orange's Distances widget.
</p>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: TF-IDF weighting and cosine distance matrix</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── TF-IDF weighting ──────────────────────────────────────────────</span>
<span class="r-comment"># tf  = word count / total words in book</span>
<span class="r-comment"># idf = ln(n_books / n_books_containing_word)</span>
<span class="r-comment"># tf_idf = tf * idf</span>
<span class="r-comment"># All words are kept — no minimum document-frequency cutoff.</span>
tfidf <span class="r-operator">&lt;-</span> word_counts <span class="r-operator">|&gt;</span>
  <span class="r-function">bind_tf_idf</span>(word, book_id, n)

<span class="r-comment"># ── Build document-term matrix ────────────────────────────────────</span>
<span class="r-comment"># Rows = books, columns = words, values = TF-IDF weights</span>
dtm <span class="r-operator">&lt;-</span> tfidf <span class="r-operator">|&gt;</span>
  <span class="r-function">select</span>(book_id, word, tf_idf) <span class="r-operator">|&gt;</span>
  <span class="r-function">pivot_wider</span>(names_from <span class="r-operator">=</span> word, values_from <span class="r-operator">=</span> tf_idf, values_fill <span class="r-operator">=</span> <span class="r-number">0</span>)

<span class="r-comment"># Convert to a matrix for clustering</span>
mat <span class="r-operator">&lt;-</span> dtm <span class="r-operator">|&gt;</span> <span class="r-function">select</span>(<span class="r-operator">-</span>book_id) <span class="r-operator">|&gt;</span> <span class="r-function">as.matrix</span>()
<span class="r-function">rownames</span>(mat) <span class="r-operator">&lt;-</span> dtm<span class="r-operator">$</span>book_id

<span class="r-comment"># ── Cosine distance ───────────────────────────────────────────────</span>
<span class="r-comment"># Cosine measures the angle between two vectors, ignoring length.</span>
<span class="r-comment"># cosine similarity = (a · b) / (||a|| * ||b||)</span>
<span class="r-comment"># cosine distance   = 1 - cosine similarity</span>
<span class="r-comment"># Same metric as Orange → Distances → Cosine.</span>
cosine_dist <span class="r-operator">&lt;-</span> <span class="r-keyword">function</span>(m) {
  sim <span class="r-operator">&lt;-</span> m <span class="r-operator">%*%</span> <span class="r-function">t</span>(m) <span class="r-operator">/</span>
    (<span class="r-function">sqrt</span>(<span class="r-function">rowSums</span>(m<span class="r-operator">^</span><span class="r-number">2</span>)) <span class="r-operator">%o%</span> <span class="r-function">sqrt</span>(<span class="r-function">rowSums</span>(m<span class="r-operator">^</span><span class="r-number">2</span>)))
  <span class="r-function">as.dist</span>(<span class="r-number">1</span> <span class="r-operator">-</span> sim)
}

d <span class="r-operator">&lt;-</span> <span class="r-function">cosine_dist</span>(mat)

<span class="r-comment"># Quick sanity check: which two books are most similar?</span>
<span class="r-function">round</span>(<span class="r-function">as.matrix</span>(d)[<span class="r-number">1</span>:<span class="r-number">5</span>, <span class="r-number">1</span>:<span class="r-number">5</span>], <span class="r-number">3</span>)</code></pre>
    </div>
    <div class="callout callout-info">
      <strong>Why cosine distance?</strong> Cosine distance measures the <em>angle</em> between two TF-IDF vectors, ignoring their magnitude. A short colonial textbook with 1,700 tokens and a long one with 9,000 tokens can still end up close together &mdash; what matters is the <em>mix</em> of words, not how many total words there are.
    </div>
  </div>
</details>

<div class="callout callout-tip">
  <strong>From Week 4 to Week 7:</strong> In Week 4, TF-IDF helped us find distinctive words in a single document. Now we use the same TF-IDF vectors to measure how <em>similar</em> entire documents are to each other via cosine distance. Clustering groups documents whose TF-IDF vectors point in similar directions.
</div>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">4</span>
  <h2>Dendrogram: Hierarchical Clustering</h2>
</div>

<p class="narrative">
  Using the cosine distances from Step 3, Ward's method builds a hierarchy by repeatedly merging the two most similar groups, minimizing within-cluster variance at each step. The result is a <strong>dendrogram</strong> &mdash; a tree that shows which textbooks are most similar and when groups merge. The height of each merge indicates how different the merged groups are. The dashed red line marks the cut at <em>k</em>&nbsp;=&nbsp;3 clusters.
</p>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: hierarchical clustering and dendrogram</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── Hierarchical clustering (Ward's method on cosine distances) ───</span>
hc <span class="r-operator">&lt;-</span> <span class="r-function">hclust</span>(d, method <span class="r-operator">=</span> <span class="r-string">"ward.D2"</span>)

<span class="r-comment"># ── Plot dendrogram ───────────────────────────────────────────────</span>
<span class="r-function">plot</span>(hc, labels <span class="r-operator">=</span> dtm<span class="r-operator">$</span>book_id, main <span class="r-operator">=</span> <span class="r-string">"Hierarchical Clustering of NIKH Textbooks"</span>,
     xlab <span class="r-operator">=</span> <span class="r-string">""</span>, sub <span class="r-operator">=</span> <span class="r-string">""</span>, cex <span class="r-operator">=</span> <span class="r-number">0.8</span>)

<span class="r-comment"># ── Cut into 3 clusters ───────────────────────────────────────────</span>
clusters <span class="r-operator">&lt;-</span> <span class="r-function">cutree</span>(hc, k <span class="r-operator">=</span> <span class="r-number">3</span>)
<span class="r-function">rect.hclust</span>(hc, k <span class="r-operator">=</span> <span class="r-number">3</span>, border <span class="r-operator">=</span> <span class="r-function">c</span>(<span class="r-string">"#b45309"</span>, <span class="r-string">"#7c3aed"</span>, <span class="r-string">"#0891b2"</span>))

<span class="r-comment"># ── View assignments ──────────────────────────────────────────────</span>
corpus <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(cluster <span class="r-operator">=</span> clusters) <span class="r-operator">|&gt;</span>
  <span class="r-function">select</span>(book_id, title, era, cluster) <span class="r-operator">|&gt;</span>
  <span class="r-function">arrange</span>(cluster) <span class="r-operator">|&gt;</span>
  <span class="r-function">print</span>(n <span class="r-operator">=</span> <span class="r-number">11</span>)</code></pre>
    </div>
  </div>
</details>

<div class="output-panel">
  <div class="output-panel-header">Dendrogram</div>
  <div class="output-panel-body">
    <div class="chart-legend">
      <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#b45309"></span> Colonial</span>
      <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#7c3aed"></span> Authoritarian</span>
      <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#0891b2"></span> Democratic</span>
    </div>
    <div class="dendro-container" id="dendrogramContainer"></div>
  </div>
</div>

<div class="callout callout-info">
  <strong>Reading the dendrogram:</strong> Textbooks that merge at low heights are very similar; merges at the top indicate large differences. The colonial-era texts (amber) form a tight, distinct cluster. The authoritarian and democratic texts merge with each other before joining the colonial branch &mdash; they share more vocabulary because they cover overlapping historical periods with a modern Korean lens.
</div>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">5</span>
  <h2>Cluster vs. Era: Do Clusters Match?</h2>
</div>

<p class="narrative">
  The algorithm had <em>no access</em> to the era labels &mdash; it worked only from the TF-IDF word vectors. Yet it recovered groupings that largely correspond to the historical eras. Below, each card shows one cluster and the books it contains. The era labels confirm: <strong>the language of history textbooks reflects the political era in which they were written</strong>.
</p>

<div class="cluster-grid" id="clusterGrid"></div>

<div class="callout callout-tip">
  <strong>The crossovers are interesting too.</strong> If a book is placed in a "wrong" cluster, it might mean the textbook's language is transitional &mdash; written in one era but using vocabulary more typical of another. This is exactly the kind of finding that makes clustering valuable: it surfaces patterns that simple labeling would miss.
</div>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">6</span>
  <h2>Distinctive Words by Cluster</h2>
</div>

<p class="narrative">
  What makes each cluster distinctive? We re-run TF-IDF treating each cluster as a single pseudo-document and extract the top-weighted words. This connects back to the word analysis from Weeks 3&ndash;5, but now the grouping comes from the clustering algorithm rather than our own labels.
</p>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: extract top TF-IDF words per cluster</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── Add cluster assignments to tokens ─────────────────────────────</span>
cluster_labels <span class="r-operator">&lt;-</span> <span class="r-function">tibble</span>(
  book_id <span class="r-operator">=</span> <span class="r-function">names</span>(clusters),
  cluster <span class="r-operator">=</span> <span class="r-function">as.character</span>(clusters)
)

<span class="r-comment"># ── TF-IDF by cluster (pseudo-documents) ──────────────────────────</span>
cluster_tfidf <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span>
  <span class="r-function">left_join</span>(cluster_labels, by <span class="r-operator">=</span> <span class="r-string">"book_id"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(cluster, word) <span class="r-operator">|&gt;</span>
  <span class="r-function">bind_tf_idf</span>(word, cluster, n) <span class="r-operator">|&gt;</span>
  <span class="r-function">group_by</span>(cluster) <span class="r-operator">|&gt;</span>
  <span class="r-function">slice_max</span>(tf_idf, n <span class="r-operator">=</span> <span class="r-number">20</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">ungroup</span>()

<span class="r-comment"># ── Plot ──────────────────────────────────────────────────────────</span>
cluster_tfidf <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(word <span class="r-operator">=</span> <span class="r-function">reorder_within</span>(word, tf_idf, cluster)) <span class="r-operator">|&gt;</span>
  <span class="r-function">ggplot</span>(<span class="r-function">aes</span>(tf_idf, word, fill <span class="r-operator">=</span> cluster)) <span class="r-operator">+</span>
  <span class="r-function">geom_col</span>(show.legend <span class="r-operator">=</span> <span class="r-keyword">FALSE</span>) <span class="r-operator">+</span>
  <span class="r-function">facet_wrap</span>(<span class="r-operator">~</span> cluster, scales <span class="r-operator">=</span> <span class="r-string">"free"</span>) <span class="r-operator">+</span>
  <span class="r-function">scale_y_reordered</span>() <span class="r-operator">+</span>
  <span class="r-function">labs</span>(x <span class="r-operator">=</span> <span class="r-string">"TF-IDF"</span>, y <span class="r-operator">=</span> <span class="r-keyword">NULL</span>) <span class="r-operator">+</span>
  <span class="r-function">theme_minimal</span>()</code></pre>
    </div>
  </div>
</details>

<div class="output-panel">
  <div class="output-panel-header">Top Words by Cluster (TF-IDF)</div>
  <div class="output-panel-body">
    <div class="wordcloud-grid" id="clusterWordGrid"></div>
  </div>
</div>

<p class="narrative">
  The distinctive words tell a clear story. The colonial-era cluster features <strong>천황</strong> (emperor), <strong>일본</strong> (Japan), <strong>고구려</strong> (Goguryeo), and <strong>군대</strong> (army) &mdash; reflecting Japanese imperial framing of Korean history. The authoritarian cluster foregrounds <strong>문화</strong> (culture), <strong>사회</strong> (society), and <strong>발전</strong> (development) &mdash; nation-building narratives. The democratic cluster highlights <strong>운동</strong> (movement), <strong>민족</strong> (nation/people), and <strong>독립</strong> (independence) &mdash; a shift toward social movements and self-determination.
</p>

<p class="narrative">
  This is the power of combining clustering with word analysis: the algorithm groups texts by vocabulary similarity, and distinctive words explain <em>why</em> each group is different. The method confirms what domain experts know &mdash; Korean history textbooks are products of their political moment &mdash; but does so from the text alone, without relying on metadata.
</p>

</div><!-- /tutorial-page -->

<script>
(function () {
  "use strict";

  var DATA = null;
  var ERA_COLORS = {
    Colonial: "#b45309",
    Authoritarian: "#7c3aed",
    Democratic: "#0891b2"
  };

  fetch("{{ '/interactive/clustering_data.json' | relative_url }}")
    .then(function (r) { return r.json(); })
    .then(function (json) {
      DATA = json;
      renderBookTable();
      renderDendrogram();
      renderClusterCards();
      renderClusterWords();
    });

  // ── Book table ──────────────────────────────────────────────────
  function renderBookTable() {
    var tbody = document.querySelector("#bookTable tbody");
    DATA.books.forEach(function (b) {
      var tr = document.createElement("tr");
      var eraClass = "era-badge era-badge-" + b.era.toLowerCase();
      tr.innerHTML =
        '<td>' + b.title + '</td>' +
        '<td><span class="' + eraClass + '">' + b.era + '</span></td>' +
        '<td>' + b.level + '</td>' +
        '<td>' + b.year + '</td>' +
        '<td>' + b.total_tokens.toLocaleString() + '</td>';
      tbody.appendChild(tr);
    });
  }

  // ── Dendrogram ──────────────────────────────────────────────────
  function renderDendrogram() {
    var container = document.getElementById("dendrogramContainer");
    var Z = DATA.dendrogram.linkage;
    var labels = DATA.dendrogram.labels;
    var n = labels.length;

    // Build dendrogram layout from linkage matrix
    // Each node: {x, y, left, right, label, isLeaf}
    var nodes = [];
    // Leaf nodes first
    for (var i = 0; i < n; i++) {
      nodes.push({ id: i, isLeaf: true, label: labels[i], height: 0, leaves: [i] });
    }

    // Compute leaf order using dendrogram ordering
    var leafOrder = computeLeafOrder(Z, n);

    // Assign x positions based on leaf order
    var leafX = {};
    for (var i = 0; i < leafOrder.length; i++) {
      leafX[leafOrder[i]] = i;
    }

    // Merge nodes
    for (var i = 0; i < Z.length; i++) {
      var left = Math.round(Z[i][0]);
      var right = Math.round(Z[i][1]);
      var dist = Z[i][2];
      var leftLeaves = nodes[left].leaves;
      var rightLeaves = nodes[right].leaves;
      nodes.push({
        id: n + i,
        isLeaf: false,
        height: dist,
        left: left,
        right: right,
        leaves: leftLeaves.concat(rightLeaves)
      });
    }

    // Compute x position for each node
    function getX(nodeIdx) {
      var node = nodes[nodeIdx];
      if (node.isLeaf) {
        return leafX[nodeIdx];
      }
      if (node._x !== undefined) return node._x;
      node._x = (getX(node.left) + getX(node.right)) / 2;
      return node._x;
    }

    // SVG dimensions
    var margin = { top: 30, right: 40, bottom: 100, left: 50 };
    var width = Math.max(600, n * 70);
    var height = 320;
    var plotW = width - margin.left - margin.right;
    var plotH = height - margin.top - margin.bottom;

    var maxHeight = nodes[nodes.length - 1].height;

    function scaleX(x) { return margin.left + (x / (n - 1)) * plotW; }
    function scaleY(h) { return margin.top + plotH - (h / maxHeight) * plotH; }

    var svg = '<svg width="' + width + '" height="' + height + '" xmlns="http://www.w3.org/2000/svg">';

    // Find cut height for k=3 (between 2nd and 3rd highest merge)
    var sortedHeights = Z.map(function (z) { return z[2]; }).sort(function (a, b) { return b - a; });
    var cutHeight = (sortedHeights[1] + sortedHeights[2]) / 2;

    // Draw cut line
    svg += '<line x1="' + margin.left + '" y1="' + scaleY(cutHeight) + '" x2="' + (width - margin.right) + '" y2="' + scaleY(cutHeight) + '" class="dendro-cut-line"/>';
    svg += '<text x="' + (width - margin.right + 5) + '" y="' + (scaleY(cutHeight) + 4) + '" class="dendro-cut-label">k = 3</text>';

    // Height axis labels
    var nTicks = 5;
    for (var i = 0; i <= nTicks; i++) {
      var h = (maxHeight * i) / nTicks;
      var y = scaleY(h);
      svg += '<text x="' + (margin.left - 8) + '" y="' + (y + 3) + '" class="dendro-height-label" text-anchor="end">' + h.toFixed(1) + '</text>';
      svg += '<line x1="' + margin.left + '" y1="' + y + '" x2="' + (margin.left - 4) + '" y2="' + y + '" stroke="#cbd5e1" stroke-width="1"/>';
    }

    // Draw links (U-shaped connections)
    for (var i = 0; i < Z.length; i++) {
      var nodeIdx = n + i;
      var node = nodes[nodeIdx];
      var lx = scaleX(getX(node.left));
      var rx = scaleX(getX(node.right));
      var ly = scaleY(nodes[node.left].height);
      var ry = scaleY(nodes[node.right].height);
      var my = scaleY(node.height);

      // Left vertical, horizontal, right vertical
      svg += '<path d="M' + lx + ',' + ly + ' V' + my + ' H' + rx + ' V' + ry + '" class="dendro-link"/>';
    }

    // Draw leaf labels
    for (var i = 0; i < n; i++) {
      var x = scaleX(leafX[i]);
      var y = scaleY(0) + 12;
      var book = DATA.books.find(function (b) { return b.book_id === labels[i]; });
      var color = book ? ERA_COLORS[book.era] : "#374151";
      var displayLabel = book ? book.short_title : labels[i];

      svg += '<text x="' + x + '" y="' + y + '" class="dendro-leaf-label" ' +
             'fill="' + color + '" text-anchor="end" ' +
             'transform="rotate(-40,' + x + ',' + y + ')">' +
             escapeHtml(displayLabel) + '</text>';
    }

    svg += '</svg>';
    container.innerHTML = svg;
  }

  // Compute leaf order from linkage matrix (same as scipy's dendrogram)
  function computeLeafOrder(Z, n) {
    var order = [];
    var root = n + Z.length - 1;
    function traverse(idx) {
      if (idx < n) {
        order.push(idx);
      } else {
        var row = Z[idx - n];
        traverse(Math.round(row[0]));
        traverse(Math.round(row[1]));
      }
    }
    traverse(root);
    return order;
  }

  // ── Cluster comparison cards ────────────────────────────────────
  function renderClusterCards() {
    var grid = document.getElementById("clusterGrid");
    var mapping = DATA.cluster_era_mapping;
    var clusters = Object.keys(mapping).sort();

    clusters.forEach(function (c) {
      var era = mapping[c];
      var color = ERA_COLORS[era];
      var books = DATA.books.filter(function (b) { return b.cluster === parseInt(c); });
      var matchCount = books.filter(function (b) { return b.era === era; }).length;

      var card = document.createElement("div");
      card.className = "cluster-card";

      var header = document.createElement("div");
      header.className = "cluster-card-header";
      header.style.background = color;
      header.innerHTML = '<span>Cluster ' + c + ' (' + era + ')</span>' +
                         '<span class="cluster-match">' + matchCount + '/' + books.length + ' match</span>';
      card.appendChild(header);

      var body = document.createElement("div");
      body.className = "cluster-card-body";

      books.forEach(function (b) {
        var bookDiv = document.createElement("div");
        bookDiv.className = "cluster-book";
        var badgeColor = ERA_COLORS[b.era];
        bookDiv.innerHTML =
          '<span class="cluster-book-era" style="background:' + badgeColor + '">' + b.era.substring(0, 3) + '</span>' +
          '<span>' + escapeHtml(b.short_title) + ' (' + b.year + ')</span>';
        body.appendChild(bookDiv);
      });

      card.appendChild(body);
      grid.appendChild(card);
    });
  }

  // ── Cluster word clouds ─────────────────────────────────────────
  function renderClusterWords() {
    var grid = document.getElementById("clusterWordGrid");
    var mapping = DATA.cluster_era_mapping;
    var clusters = Object.keys(mapping).sort();

    clusters.forEach(function (c) {
      var era = mapping[c];
      var words = DATA.cluster_words[c].slice(0, 25);
      var maxTfidf = words[0].tfidf;

      var card = document.createElement("div");
      card.className = "wordcloud-card";

      var header = document.createElement("div");
      header.className = "wordcloud-card-header era-" + era.toLowerCase();
      header.textContent = "Cluster " + c + ": " + era;
      card.appendChild(header);

      var body = document.createElement("div");
      body.className = "wordcloud-card-body";

      words.forEach(function (w) {
        var span = document.createElement("span");
        span.className = "wc-word";
        var ratio = w.tfidf / maxTfidf;
        var size = 0.65 + ratio * 1.6;
        var alpha = 0.4 + ratio * 0.6;
        span.style.fontSize = size + "rem";
        span.style.color = ERA_COLORS[era];
        span.style.opacity = alpha;
        span.textContent = w.word;
        span.title = w.word + ": " + w.tfidf.toFixed(4);
        body.appendChild(span);
        body.appendChild(document.createTextNode(" "));
      });

      card.appendChild(body);
      grid.appendChild(card);
    });
  }

  // ── Utility ─────────────────────────────────────────────────────
  function escapeHtml(str) {
    var div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
  }

  // ── Copy button ─────────────────────────────────────────────────
  window.copyCode = function (btn) {
    var pre = btn.closest(".code-block").querySelector("pre code");
    var text = pre.textContent;
    navigator.clipboard.writeText(text).then(function () {
      btn.textContent = "Copied!";
      btn.classList.add("copied");
      setTimeout(function () {
        btn.textContent = "Copy";
        btn.classList.remove("copied");
      }, 2000);
    });
  };
})();
</script>
