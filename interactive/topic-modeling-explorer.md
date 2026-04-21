---
layout: default
title: "Topic Modeling (LDA): Korean History Textbooks"
---

<style>
:root { --leiden-blue: #001158; }
.tutorial-page { max-width: 100%; }

.tutorial-header { margin-top: 1rem; margin-bottom: 2rem; padding-bottom: 1.5rem; border-bottom: 2px solid #e2e8f0; }
.tutorial-header h1 { font-size: 1.6rem; color: var(--leiden-blue); margin: 0 0 0.5rem; }
.tutorial-subtitle { font-size: 1rem; color: #6b7280; margin: 0 0 0.75rem; }
.tutorial-meta { display: flex; flex-wrap: wrap; gap: 1rem; font-size: 0.82rem; color: #9ca3af; }
.tutorial-meta span { display: inline-flex; align-items: center; gap: 0.3rem; }

.section-heading { display: flex; align-items: center; gap: 0.75rem; margin: 2.5rem 0 1rem; padding-bottom: 0.5rem; border-bottom: 1px solid #e2e8f0; }
.section-number { display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; background: var(--leiden-blue); color: #fff; font-size: 0.82rem; font-weight: 700; flex-shrink: 0; }
.section-heading h2 { font-size: 1.25rem; color: var(--leiden-blue); margin: 0; }

.narrative { font-size: 0.95rem; line-height: 1.7; color: #374151; margin: 1rem 0; }
.narrative strong { color: var(--leiden-blue); }

.callout { padding: 0.75rem 1rem; border-radius: 6px; margin: 1rem 0; font-size: 0.88rem; line-height: 1.6; }
.callout-info { background: #eff6ff; border-left: 3px solid #3b82f6; color: #1e40af; }
.callout-tip  { background: #f0fdf4; border-left: 3px solid #22c55e; color: #166534; }
.callout-note { background: #fefce8; border-left: 3px solid #eab308; color: #854d0e; }

/* ── Stats grid ──────────────────────────────────────────────────── */
.stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 0.75rem; margin: 1rem 0; }
.stat-card { border: 1px solid #e2e8f0; border-radius: 8px; padding: 0.75rem 1rem; background: #fff; }
.stat-label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.05em; color: #9ca3af; font-weight: 600; }
.stat-value { font-size: 1.3rem; color: var(--leiden-blue); font-weight: 700; margin-top: 0.15rem; }
.stat-sub   { font-size: 0.75rem; color: #6b7280; margin-top: 0.1rem; }

/* ── Era badges ──────────────────────────────────────────────────── */
.era-badge { display: inline-block; padding: 0.1rem 0.5rem; border-radius: 10px; font-size: 0.72rem; font-weight: 600; }
.era-badge-colonial      { background: #fef3c7; color: #92400e; }
.era-badge-authoritarian { background: #ede9fe; color: #5b21b6; }
.era-badge-democratic    { background: #cffafe; color: #155e75; }

/* ── Coherence chart ─────────────────────────────────────────────── */
.coherence-svg-wrap { border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem 0.75rem 0.5rem; background: #fafafa; }
.coherence-svg-wrap svg { display: block; width: 100%; max-width: 720px; height: auto; margin: 0 auto; }
.coherence-note { font-size: 0.82rem; color: #6b7280; margin-top: 0.6rem; }

/* ── Topic browser ───────────────────────────────────────────────── */
.topic-tabs { display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 1rem 0 0.75rem; }
.topic-tab {
  padding: 0.4rem 0.85rem; border-radius: 20px; border: 2px solid #e2e8f0;
  background: #fff; font-size: 0.82rem; font-weight: 600;
  cursor: pointer; transition: all 0.2s; font-family: inherit; color: #374151;
}
.topic-tab:hover { border-color: var(--leiden-blue); }
.topic-tab.active { background: var(--leiden-blue); color: #fff; border-color: var(--leiden-blue); }

.topic-panel { border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem; background: #fff; }
.topic-panel-title { font-size: 1rem; color: var(--leiden-blue); font-weight: 700; margin: 0 0 0.3rem; }
.topic-panel-sub   { font-size: 0.82rem; color: #6b7280; margin: 0 0 0.85rem; }

.topic-words-grid { display: grid; grid-template-columns: 1fr; gap: 0.25rem; }
.topic-word-row { display: flex; align-items: center; gap: 0.5rem; }
.topic-word      { min-width: 7.5rem; font-weight: 600; color: #1f2937; font-size: 0.9rem; }
.topic-word-bar-track { flex: 1; height: 14px; background: #f1f5f9; border-radius: 3px; overflow: hidden; }
.topic-word-bar-fill  { height: 100%; border-radius: 3px; transition: width 0.35s; }
.topic-word-weight { width: 4.5rem; text-align: right; font-size: 0.75rem; color: #6b7280; font-variant-numeric: tabular-nums; }

/* ── Document table ──────────────────────────────────────────────── */
.doc-controls { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0.75rem 0; font-size: 0.82rem; color: #4b5563; align-items: center; }
.doc-controls select { padding: 0.25rem 0.5rem; border: 1px solid #cbd5e1; border-radius: 4px; font-family: inherit; font-size: 0.82rem; }
.doc-table-wrap { border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; }
.doc-table { width: 100%; border-collapse: collapse; font-size: 0.82rem; }
.doc-table thead th { background: #f8fafc; text-align: left; padding: 0.5rem 0.75rem; font-weight: 600; color: #475569; border-bottom: 1px solid #e2e8f0; }
.doc-table tbody td { padding: 0.45rem 0.75rem; border-bottom: 1px solid #f1f5f9; vertical-align: middle; }
.doc-table tbody tr:last-child td { border-bottom: 0; }
.mix-bar { display: flex; height: 12px; border-radius: 3px; overflow: hidden; min-width: 180px; }
.mix-seg { height: 100%; }

.era-topic-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 0.75rem; margin: 1rem 0; }
.era-topic-card { border: 1px solid #e2e8f0; border-radius: 8px; padding: 0.75rem 1rem; background: #fff; }
.era-topic-card h4 { margin: 0 0 0.5rem; font-size: 0.95rem; color: var(--leiden-blue); }

/* ── LDAvis iframe ───────────────────────────────────────────────── */
.ldavis-wrap { border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; background: #fff; }
.ldavis-wrap iframe { display: block; width: 100%; height: 720px; border: 0; }

/* ── Code blocks ─────────────────────────────────────────────────── */
.code-block { position: relative; margin: 1rem 0; border-radius: 8px; overflow: hidden; border: 1px solid #e2e8f0; }
.code-block-header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 0.4rem 0.75rem; background: #f1f5f9; border-bottom: 1px solid #e2e8f0;
  font-size: 0.75rem; color: #64748b; font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em;
}
.copy-btn {
  padding: 0.2rem 0.5rem; border: 1px solid #cbd5e1; border-radius: 4px; background: #fff;
  font-size: 0.72rem; color: #64748b; cursor: pointer; font-family: inherit; transition: all 0.15s;
}
.copy-btn:hover { background: #f8fafc; border-color: var(--leiden-blue); color: var(--leiden-blue); }
.copy-btn.copied { background: #ecfdf5; border-color: #6ee7b7; color: #059669; }
.code-block pre {
  margin: 0; padding: 1rem; background: #1e293b; color: #e2e8f0;
  font-size: 0.82rem; line-height: 1.55; overflow-x: auto;
  font-family: "SFMono-Regular", "Consolas", "Liberation Mono", monospace;
}
.code-block pre code { background: none; color: inherit; padding: 0; font-size: inherit; }
.code-block .r-comment  { color: #94a3b8; font-style: italic; }
.code-block .r-string   { color: #86efac; }
.code-block .r-function { color: #93c5fd; }
.code-block .r-keyword  { color: #c4b5fd; }
.code-block .r-number   { color: #fde68a; }
.code-block .r-operator { color: #f9a8d4; }

/* ── R code ribbon (collapsible) ─────────────────────────────────── */
.code-ribbon { margin: 1rem 0; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; }
.code-ribbon summary {
  display: flex; align-items: center; gap: 0.5rem;
  padding: 0.5rem 1rem; background: linear-gradient(to right, #1e293b, #334155);
  color: #e2e8f0; font-size: 0.82rem; font-weight: 600;
  cursor: pointer; user-select: none; list-style: none; transition: background 0.2s;
}
.code-ribbon summary::-webkit-details-marker { display: none; }
.code-ribbon summary::before { content: "\25B6"; font-size: 0.65rem; transition: transform 0.2s; flex-shrink: 0; }
.code-ribbon[open] summary::before { transform: rotate(90deg); }
.code-ribbon summary:hover { background: linear-gradient(to right, #0f172a, #1e293b); }
.code-ribbon summary .ribbon-label { flex: 1; }
.code-ribbon summary .ribbon-tag {
  padding: 0.12rem 0.45rem; border-radius: 4px; font-size: 0.68rem; font-weight: 700;
  background: rgba(255,255,255,0.12); color: #94a3b8; text-transform: uppercase; letter-spacing: 0.04em;
}
.code-ribbon .code-ribbon-body { border-top: 1px solid #334155; }
.code-ribbon .code-block { margin: 0; border: none; border-radius: 0; }
.code-ribbon .callout    { margin: 0; border-radius: 0; border-left-width: 3px; }

@media (max-width: 700px) {
  .ldavis-wrap iframe { height: 560px; }
}
</style>

<div class="tutorial-page">

<div class="tutorial-header">
  <h1>Topic Modeling (LDA): Korean History Textbooks</h1>
  <p class="tutorial-subtitle">
    Fit LDA on the full 67-book NIKH corpus. Watch coherence scores guide the choice of <em>k</em>,
    read the discovered topics, and see how textbook themes shift across Colonial, Authoritarian, and Democratic eras.
  </p>
  <div class="tutorial-meta">
    <span>🗓 Week 10</span>
    <span>📚 NIKH · 67 books · 1895 – 2016</span>
    <span>🧮 LDA (gensim) · pyLDAvis</span>
  </div>
</div>

<!-- ====================================================================== -->
<div class="section-heading">
  <span class="section-number">1</span>
  <h2>What we're doing, and why</h2>
</div>

<div class="callout callout-note">
  <strong>New to LDA? Start here.</strong> LDA is a sorting tool for words. It reads a pile of books and notices which words tend to show up together. Words that keep co-occurring end up in the same group, and each group is called a <em>topic</em>. You read the top words in a topic and decide what theme they point to. No topic arrives with a name attached; the labels on this page are readings we wrote, and you are welcome to disagree.
</div>

<p class="narrative">
In lecture we ran LDA on an 11-book sample so the workflow would fit in a class session. Here we run it on the <strong>full 67-book Nick Korpis</strong> &mdash; Korean history textbooks curated by the National Institute of Korean History and supplemented with additional books from the instructor's library, covering 1895 through 2016. The method is the same: Kiwi tokenization on nouns, stopword removal, document-frequency filtering, LDA on the bag-of-words counts.
</p>

<p class="narrative">
Three things become visible on the full corpus that the 11-book demo couldn't show you:
</p>

<ul class="narrative">
  <li>How <strong>coherence scores</strong> can help you pick <em>k</em> (we'll explain what coherence is &mdash; Orange doesn't surface this metric).</li>
  <li>What the discovered topics look like when the model has enough data to separate themes it couldn't separate on 11 books.</li>
  <li>How the <strong>era-level topic mix</strong> shifts: colonial-era textbooks emphasize different things than post-1987 democratic-era ones.</li>
</ul>

<!-- ====================================================================== -->
<div class="section-heading">
  <span class="section-number">2</span>
  <h2>The corpus</h2>
</div>

<div id="corpusStats" class="stats-grid"></div>

<p class="narrative">
The periodization follows the course convention: <span class="era-badge era-badge-colonial">Colonial</span> for Japanese-colonial-era textbooks (roughly 1895&ndash;1945), <span class="era-badge era-badge-authoritarian">Authoritarian</span> for the developmental-state decades (1946&ndash;1987), and <span class="era-badge era-badge-democratic">Democratic</span> for the post-1987 period. The Authoritarian period dominates the corpus by book count because that is when the state published textbooks most intensively.
</p>

<p class="narrative">
The R walkthroughs below run the same pipeline the visuals on this page use: the <strong>full 67-book NIKH corpus</strong>, noun-only tokenization, a 5%&ndash;95% document-frequency filter, and LDA at <em>k</em> = 5. Download <code>nikh_corpus.csv</code> from the <a href="https://github.com/scdenney/nlp_corpora/tree/main/data/nikh">nlp_corpora repo</a> (or clone the repo) and save it to your <code>data/</code> folder before running the code.
</p>

<div class="callout callout-note">
  <strong>R vs. the interactive.</strong> The interactive uses gensim's variational-Bayes LDA in Python. R's <code>topicmodels</code> uses Gibbs sampling. Same algorithm family, different solver and different random stream, so the topics you get in R will look similar in <em>content</em> but will not be byte-identical to the ones shown above. If your 67-book fit is slow, swap in the 11-book clustering demo or the 9-book demo from the <a href="{{ '/data/' | relative_url }}">Data &amp; Scripts</a> page &mdash; the code works on any CSV with a <code>full_text</code> column.
</div>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: load the full 67-book NIKH corpus and stopwords</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── Packages ──────────────────────────────────────────────────────</span>
<span class="r-function">library</span>(tidyverse)
<span class="r-function">library</span>(tidytext)
<span class="r-function">library</span>(elbird)        <span class="r-comment"># Korean morphological analysis (Kiwi)</span>
<span class="r-function">library</span>(topicmodels)   <span class="r-comment"># LDA</span>
<span class="r-function">library</span>(LDAvis)        <span class="r-comment"># interactive topic visualization</span>

<span class="r-comment"># ── Load the full 67-book NIKH corpus ─────────────────────────────</span>
<span class="r-comment"># Download once from the nlp_corpora repo and save to your data/ folder:</span>
<span class="r-comment">#   https://github.com/scdenney/nlp_corpora/blob/main/data/nikh/nikh_corpus.csv</span>
corpus <span class="r-operator">&lt;-</span> <span class="r-function">read_csv</span>(<span class="r-string">"data/nikh_corpus.csv"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">drop_na</span>(full_text, book_id) <span class="r-operator">|&gt;</span>
  <span class="r-function">distinct</span>(book_id, .keep_all <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(era <span class="r-operator">=</span> <span class="r-function">case_when</span>(
    period <span class="r-operator">%in%</span> <span class="r-function">c</span>(<span class="r-string">"Colonial"</span>, <span class="r-string">"Late Choson"</span>) <span class="r-operator">~</span> <span class="r-string">"Colonial"</span>,
    period <span class="r-operator">==</span> <span class="r-string">"Democratic"</span>                        <span class="r-operator">~</span> <span class="r-string">"Democratic"</span>,
    <span class="r-keyword">TRUE</span>                                          <span class="r-operator">~</span> <span class="r-string">"Authoritarian"</span>
  ))

<span class="r-comment"># ── Korean stopwords ──────────────────────────────────────────────</span>
stopwords_ko <span class="r-operator">&lt;-</span> <span class="r-function">read_lines</span>(<span class="r-string">"data/stopwords_ko.txt"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">str_trim</span>() <span class="r-operator">|&gt;</span>
  <span class="r-function">discard</span>(<span class="r-operator">~</span> .x <span class="r-operator">==</span> <span class="r-string">""</span>)

corpus <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(era, name <span class="r-operator">=</span> <span class="r-string">"books"</span>)</code></pre>
    </div>
    <div class="callout callout-info">
      <strong>About the packages:</strong> <code>elbird</code> wraps <a href="https://github.com/bab2min/Kiwi">Kiwi</a>, the same tokenizer used in our Orange scripts. <code>topicmodels</code> is the standard R package for LDA. <code>LDAvis</code> is the R sibling of pyLDAvis. The era recoding collapses the five raw period labels into the three-era view used on this page.
    </div>
  </div>
</details>

<!-- ====================================================================== -->
<div class="section-heading">
  <span class="section-number">3</span>
  <h2>Preprocessing</h2>
</div>

<p class="narrative">
We apply the exact pipeline from the Orange demo, just scripted in Python instead:
</p>

<ol class="narrative">
  <li><strong>Tokenize</strong> each book with <a href="https://github.com/bab2min/kiwipiepy" target="_blank" rel="noopener">Kiwi</a>.</li>
  <li>Keep only <strong>nouns</strong> (<code>NNG</code>, <code>NNP</code>).</li>
  <li>Drop <strong>stopwords</strong> and tokens shorter than 2 characters.</li>
  <li>Drop terms that appear in <strong>very few books</strong> (likely OCR noise) or in <strong>almost every book</strong> (nearly-universal, uninformative).</li>
</ol>

<div id="preprocStats" class="stats-grid"></div>

<div class="callout callout-tip">
  LDA reads raw <em>counts</em>, not TF&ndash;IDF weights. The document-frequency filter replaces what TF&ndash;IDF's IDF step would do: it removes words that are too common or too rare to help separate topics.
</div>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: tokenize with Kiwi, filter, and build a document-term matrix</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── Helper: tokenize one text with Kiwi via elbird ────────────────</span>
tokenize_kiwi <span class="r-operator">&lt;-</span> <span class="r-keyword">function</span>(text) {
  result <span class="r-operator">&lt;-</span> <span class="r-function">tokenize</span>(text, flatten <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>)
  <span class="r-function">tibble</span>(form <span class="r-operator">=</span> result<span class="r-operator">$</span>form, tag <span class="r-operator">=</span> result<span class="r-operator">$</span>tag)
}

<span class="r-comment"># ── Tokenize and keep only nouns ──────────────────────────────────</span>
tokens <span class="r-operator">&lt;-</span> corpus <span class="r-operator">|&gt;</span>
  <span class="r-function">select</span>(book_id, era, full_text) <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(morphemes <span class="r-operator">=</span> <span class="r-function">map</span>(full_text, tokenize_kiwi)) <span class="r-operator">|&gt;</span>
  <span class="r-function">unnest</span>(morphemes) <span class="r-operator">|&gt;</span>
  <span class="r-function">filter</span>(
    tag <span class="r-operator">%in%</span> <span class="r-function">c</span>(<span class="r-string">"NNG"</span>, <span class="r-string">"NNP"</span>),
    <span class="r-operator">!</span>form <span class="r-operator">%in%</span> stopwords_ko,
    <span class="r-function">str_length</span>(form) <span class="r-operator">&gt;=</span> <span class="r-number">2</span>,
    <span class="r-operator">!</span><span class="r-function">str_detect</span>(form, <span class="r-string">"^[0-9]+$"</span>)
  ) <span class="r-operator">|&gt;</span>
  <span class="r-function">select</span>(book_id, era, word <span class="r-operator">=</span> form)

<span class="r-comment"># ── Count (book, word) ────────────────────────────────────────────</span>
counts <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(book_id, word)

<span class="r-comment"># ── Document-frequency filter ─────────────────────────────────────</span>
<span class="r-comment"># Same thresholds as the Python pipeline: in ≥ 5% of books and ≤ 95%.</span>
n_docs <span class="r-operator">&lt;-</span> <span class="r-function">n_distinct</span>(counts<span class="r-operator">$</span>book_id)
min_df <span class="r-operator">&lt;-</span> <span class="r-function">max</span>(<span class="r-number">2</span>, <span class="r-function">floor</span>(<span class="r-number">0.05</span> <span class="r-operator">*</span> n_docs))
max_df <span class="r-operator">&lt;-</span> <span class="r-function">floor</span>(<span class="r-number">0.95</span> <span class="r-operator">*</span> n_docs)

doc_freq <span class="r-operator">&lt;-</span> counts <span class="r-operator">|&gt;</span>
  <span class="r-function">distinct</span>(book_id, word) <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(word, name <span class="r-operator">=</span> <span class="r-string">"df"</span>)

keep_words <span class="r-operator">&lt;-</span> doc_freq <span class="r-operator">|&gt;</span>
  <span class="r-function">filter</span>(df <span class="r-operator">&gt;=</span> min_df, df <span class="r-operator">&lt;=</span> max_df) <span class="r-operator">|&gt;</span>
  <span class="r-function">pull</span>(word)

counts_filt <span class="r-operator">&lt;-</span> counts <span class="r-operator">|&gt;</span> <span class="r-function">filter</span>(word <span class="r-operator">%in%</span> keep_words)

<span class="r-comment"># ── Cast to a document-term matrix for topicmodels ────────────────</span>
dtm <span class="r-operator">&lt;-</span> counts_filt <span class="r-operator">|&gt;</span>
  <span class="r-function">cast_dtm</span>(document <span class="r-operator">=</span> book_id, term <span class="r-operator">=</span> word, value <span class="r-operator">=</span> n)

<span class="r-function">dim</span>(dtm)   <span class="r-comment"># books × vocabulary size</span></code></pre>
    </div>
    <div class="callout callout-tip">
      <strong>Why a DTM?</strong> <code>topicmodels::LDA()</code> expects a <code>DocumentTermMatrix</code>, which is just the raw count table in a shape it understands. <code>cast_dtm()</code> from tidytext does the conversion from a long tidy tibble.
    </div>
  </div>
</details>

<!-- ====================================================================== -->
<div class="section-heading">
  <span class="section-number">4</span>
  <h2>Choosing <em>k</em>: coherence scores</h2>
</div>

<div class="callout callout-note">
  <strong>What is <em>k</em>?</strong> It is the number of topics you ask LDA to find. If you set <em>k</em> = 5, the model splits the vocabulary across 5 groups. Pick <em>k</em> too small and unrelated themes get mashed together. Pick <em>k</em> too large and one theme ends up split into look-alike pieces. There is no single right answer, which is why we use measures like coherence to help us pick.
</div>

<p class="narrative">
In class we said <em>k</em> is a research choice with no universal rule. One tool that can help &mdash; but that Orange's Topic Modeling widget does not surface &mdash; is a <strong>coherence score</strong>.
</p>

<div class="callout callout-note">
  <strong>What is coherence?</strong> A topic is <em>coherent</em> when its top words tend to co-occur in short windows of text across the corpus. A human who reads them together should recognize them as belonging to the same theme. The <code>c_v</code> coherence score formalizes this intuition: it measures how often each pair of top words from a topic appears together (relative to chance), averaged across topics. Higher is usually better. See <a href="https://aclanthology.org/E14-1056/" target="_blank" rel="noopener">Röder et al. (2015)</a> for the full definition.
</div>

<p class="narrative">
We fit LDA at several values of <em>k</em> and compute <code>c_v</code> for each:
</p>

<div class="coherence-svg-wrap">
  <svg id="coherenceChart" viewBox="0 0 680 340" aria-label="Coherence (c_v) by number of topics"></svg>
</div>

<p class="coherence-note" id="coherenceNote"></p>

<p class="narrative">
Coherence isn't the last word. Two topics can look equally &ldquo;coherent&rdquo; to the algorithm but not equally useful for your research question. And coherence rewards models that use a narrower vocabulary, which can hide real variety. Read it as one signal, together with reading the topics themselves.
</p>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: compare several values of <em>k</em> with ldatuning</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── Package for k-selection metrics ───────────────────────────────</span>
<span class="r-function">library</span>(ldatuning)

<span class="r-comment"># ── Fit LDA at several k values and score each fit ────────────────</span>
tune <span class="r-operator">&lt;-</span> <span class="r-function">FindTopicsNumber</span>(
  dtm,
  topics  <span class="r-operator">=</span> <span class="r-function">c</span>(<span class="r-number">3</span>, <span class="r-number">4</span>, <span class="r-number">5</span>, <span class="r-number">6</span>, <span class="r-number">7</span>, <span class="r-number">8</span>, <span class="r-number">10</span>, <span class="r-number">12</span>),
  metrics <span class="r-operator">=</span> <span class="r-function">c</span>(<span class="r-string">"Arun2010"</span>, <span class="r-string">"CaoJuan2009"</span>, <span class="r-string">"Deveaud2014"</span>),
  method  <span class="r-operator">=</span> <span class="r-string">"Gibbs"</span>,
  control <span class="r-operator">=</span> <span class="r-function">list</span>(seed <span class="r-operator">=</span> <span class="r-number">42</span>),
  mc.cores <span class="r-operator">=</span> <span class="r-number">2</span>,
  verbose <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>
)

<span class="r-function">FindTopicsNumber_plot</span>(tune)</code></pre>
    </div>
    <div class="callout callout-info">
      <strong>How to read the plot:</strong> <code>Deveaud2014</code> should be high (maximize), while <code>Arun2010</code> and <code>CaoJuan2009</code> should be low (minimize). The best <em>k</em> is a compromise. These are not identical to the <code>c_v</code> score we plot above, but they answer the same question: which <em>k</em> gives the cleanest topics.
    </div>
  </div>
</details>

<!-- ====================================================================== -->
<div class="section-heading">
  <span class="section-number">5</span>
  <h2>The topics</h2>
</div>

<p class="narrative">
Below are the topics from <strong>k = <span id="kDefault">6</span></strong>, each with its top 15 words and a suggested label (the label is ours, not the algorithm's &mdash; you can disagree with it and propose your own).
</p>

<div class="callout callout-note">
  <strong>How to read a topic.</strong> Each tab below is one topic. The list of words inside is what LDA judged most central to it. The bar next to each word shows how strongly that word belongs to the topic. The title at the top of the tab is our reading of those words. Try it yourself: read the words and ask what theme they point to before you look at our label.
</div>

<div id="topicTabs" class="topic-tabs"></div>
<div id="topicPanel"></div>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: fit LDA and inspect the top words per topic</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── Fit the model (k = 5 matches the interactive's default) ───────</span>
<span class="r-function">set.seed</span>(<span class="r-number">20260420</span>)
k <span class="r-operator">&lt;-</span> <span class="r-number">5</span>

lda_fit <span class="r-operator">&lt;-</span> <span class="r-function">LDA</span>(
  dtm,
  k       <span class="r-operator">=</span> k,
  method  <span class="r-operator">=</span> <span class="r-string">"Gibbs"</span>,
  control <span class="r-operator">=</span> <span class="r-function">list</span>(iter <span class="r-operator">=</span> <span class="r-number">500</span>, burnin <span class="r-operator">=</span> <span class="r-number">200</span>, seed <span class="r-operator">=</span> <span class="r-number">20260420</span>)
)

<span class="r-comment"># ── β: topic–word probabilities (ϕ_k(w)) ──────────────────────────</span>
beta <span class="r-operator">&lt;-</span> <span class="r-function">tidy</span>(lda_fit, matrix <span class="r-operator">=</span> <span class="r-string">"beta"</span>)

<span class="r-comment"># Top 15 words per topic</span>
top_words <span class="r-operator">&lt;-</span> beta <span class="r-operator">|&gt;</span>
  <span class="r-function">group_by</span>(topic) <span class="r-operator">|&gt;</span>
  <span class="r-function">slice_max</span>(beta, n <span class="r-operator">=</span> <span class="r-number">15</span>, with_ties <span class="r-operator">=</span> <span class="r-keyword">FALSE</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">ungroup</span>() <span class="r-operator">|&gt;</span>
  <span class="r-function">arrange</span>(topic, <span class="r-function">desc</span>(beta))

<span class="r-function">print</span>(top_words, n <span class="r-operator">=</span> k <span class="r-operator">*</span> <span class="r-number">15</span>)</code></pre>
    </div>
    <div class="callout callout-tip">
      <strong>What is β (beta)?</strong> It is the <em>topic–word</em> matrix: for each topic, the probability of each word. In lecture we called this ϕ<sub>k</sub>(w). The tidytext <code>tidy()</code> function pulls it out of a fitted model in long format so you can pipe and plot it.
    </div>
  </div>
</details>

<!-- ====================================================================== -->
<div class="section-heading">
  <span class="section-number">6</span>
  <h2>Documents and their topic mixtures</h2>
</div>

<p class="narrative">
LDA hands each document a mixture over topics &mdash; the <em>θ<sub>d</sub>(k)</em> row from lecture. The bar on each row below shows that mixture. The color of each segment matches the topic color above.
</p>

<div class="callout callout-note">
  <strong>What is a topic mixture?</strong> LDA does not sort each book into one topic. It treats every book as a blend. A single textbook might be, say, 40% ancient history, 30% colonial resistance, and smaller shares of the other topics. The colored bar on each row shows that blend for one book.
</div>

<div class="doc-controls">
  <label>Filter by era:
    <select id="eraFilter">
      <option value="all">All eras</option>
      <option value="Colonial">Colonial</option>
      <option value="Authoritarian">Authoritarian</option>
      <option value="Democratic">Democratic</option>
    </select>
  </label>
  <label>Sort by:
    <select id="sortBy">
      <option value="year">Year (oldest first)</option>
      <option value="year_desc">Year (newest first)</option>
      <option value="dominant">Dominant topic</option>
      <option value="tokens">Token count</option>
    </select>
  </label>
</div>

<div class="doc-table-wrap">
  <table class="doc-table">
    <thead>
      <tr>
        <th>Book</th>
        <th>Era</th>
        <th>Year</th>
        <th>Tokens</th>
        <th>Mixture</th>
        <th>Dominant</th>
      </tr>
    </thead>
    <tbody id="docTableBody"></tbody>
  </table>
</div>

<h3 style="margin-top:1.5rem;font-size:1rem;color:var(--leiden-blue)">Average mixture by era</h3>
<p class="narrative">
Averaging each era's topic mixtures gives you a sense of which themes each period concentrated on.
</p>
<div id="eraTopicCards" class="era-topic-grid"></div>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: document–topic mixtures and era averages</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── γ: document–topic proportions (θ_d(k)) ────────────────────────</span>
gamma <span class="r-operator">&lt;-</span> <span class="r-function">tidy</span>(lda_fit, matrix <span class="r-operator">=</span> <span class="r-string">"gamma"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">rename</span>(book_id <span class="r-operator">=</span> document)

<span class="r-comment"># Dominant topic per book</span>
dominant <span class="r-operator">&lt;-</span> gamma <span class="r-operator">|&gt;</span>
  <span class="r-function">group_by</span>(book_id) <span class="r-operator">|&gt;</span>
  <span class="r-function">slice_max</span>(gamma, n <span class="r-operator">=</span> <span class="r-number">1</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">ungroup</span>() <span class="r-operator">|&gt;</span>
  <span class="r-function">left_join</span>(corpus <span class="r-operator">|&gt;</span> <span class="r-function">select</span>(book_id, title, era, year),
            by <span class="r-operator">=</span> <span class="r-string">"book_id"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">arrange</span>(year)

<span class="r-function">print</span>(dominant, n <span class="r-operator">=</span> <span class="r-function">nrow</span>(dominant))

<span class="r-comment"># ── Era-level topic mix ───────────────────────────────────────────</span>
era_mix <span class="r-operator">&lt;-</span> gamma <span class="r-operator">|&gt;</span>
  <span class="r-function">left_join</span>(corpus <span class="r-operator">|&gt;</span> <span class="r-function">select</span>(book_id, era), by <span class="r-operator">=</span> <span class="r-string">"book_id"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">group_by</span>(era, topic) <span class="r-operator">|&gt;</span>
  <span class="r-function">summarise</span>(share <span class="r-operator">=</span> <span class="r-function">mean</span>(gamma), .groups <span class="r-operator">=</span> <span class="r-string">"drop"</span>)

era_mix <span class="r-operator">|&gt;</span>
  <span class="r-function">pivot_wider</span>(names_from <span class="r-operator">=</span> topic, values_from <span class="r-operator">=</span> share,
              names_prefix <span class="r-operator">=</span> <span class="r-string">"T"</span>)</code></pre>
    </div>
    <div class="callout callout-tip">
      <strong>What is γ (gamma)?</strong> The <em>document–topic</em> matrix: for each book, the proportion of each topic. In lecture we called this θ<sub>d</sub>(k). Averaging γ within an era gives you the era-level topic mix shown in the cards above.
    </div>
  </div>
</details>

<!-- ====================================================================== -->
<div class="section-heading">
  <span class="section-number">7</span>
  <h2>LDAvis</h2>
</div>

<p class="narrative">
LDAvis is an interactive map of the LDA model. The left-hand circles are topics (size = prevalence, distance = dissimilarity). The right-hand bar chart shows the words that define the topic you click on. The <em>λ</em> slider blends raw frequency (λ = 1) with distinctiveness (λ = 0) &mdash; start at around 0.3 to see which words make a topic <em>specific</em>.
</p>

<div class="ldavis-wrap">
  <iframe src="{{ '/interactive/topic_modeling_ldavis.html' | relative_url }}" title="LDAvis for the NIKH 67-book corpus" loading="lazy"></iframe>
</div>

<p class="narrative" style="margin-top:0.75rem;font-size:0.85rem;color:#6b7280">
  Opens in an iframe. If it feels cramped, <a id="ldavisLink" href="{{ '/interactive/topic_modeling_ldavis.html' | relative_url }}" target="_blank" rel="noopener">open it in a new tab</a>.
</p>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: build the same LDAvis view from your fitted model</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── Extract the pieces LDAvis expects ─────────────────────────────</span>
phi   <span class="r-operator">&lt;-</span> <span class="r-function">posterior</span>(lda_fit)<span class="r-operator">$</span>terms     <span class="r-comment"># K × V, rows sum to 1</span>
theta <span class="r-operator">&lt;-</span> <span class="r-function">posterior</span>(lda_fit)<span class="r-operator">$</span>topics    <span class="r-comment"># D × K, rows sum to 1</span>
vocab <span class="r-operator">&lt;-</span> <span class="r-function">colnames</span>(phi)

doc_lengths <span class="r-operator">&lt;-</span> <span class="r-function">as.matrix</span>(dtm) <span class="r-operator">|&gt;</span> <span class="r-function">rowSums</span>()
term_freqs  <span class="r-operator">&lt;-</span> <span class="r-function">as.matrix</span>(dtm) <span class="r-operator">|&gt;</span> <span class="r-function">colSums</span>()

<span class="r-comment"># ── Build the JSON and open it in a browser ───────────────────────</span>
json <span class="r-operator">&lt;-</span> <span class="r-function">createJSON</span>(
  phi            <span class="r-operator">=</span> phi,
  theta          <span class="r-operator">=</span> theta,
  doc.length     <span class="r-operator">=</span> doc_lengths,
  vocab          <span class="r-operator">=</span> vocab,
  term.frequency <span class="r-operator">=</span> term_freqs
)

<span class="r-function">serVis</span>(json, out.dir <span class="r-operator">=</span> <span class="r-string">"lda_view"</span>, open.browser <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>)</code></pre>
    </div>
    <div class="callout callout-info">
      <strong>What <code>serVis()</code> does:</strong> writes the LDAvis HTML to <code>lda_view/</code> and opens it in your browser. The λ slider, circle map, and bar chart work the same as the iframe above. Share the folder with a classmate and they can open <code>index.html</code> to see your model.
    </div>
  </div>
</details>

<!-- ====================================================================== -->
<div class="section-heading">
  <span class="section-number">8</span>
  <h2>What to take away</h2>
</div>

<ul class="narrative">
  <li><strong>LDA is a reading aid.</strong> The model finds co-occurring words; you read them and decide what they mean. Every topic label on this page is an interpretation.</li>
  <li><strong>Coherence is one signal, not the answer.</strong> It's useful to rule out obviously bad <em>k</em> values. It is <em>not</em> a replacement for actually reading the topics.</li>
  <li><strong>Era effects come from the mixture, not the clustering.</strong> A textbook can be mostly ancient-history and partly colonial-resistance. Clustering would have put it in one bucket; LDA keeps the mix.</li>
  <li><strong>Orange uses the same algorithm.</strong> When you run the final assignment in Orange, you'll get topics in the same shape as these &mdash; the gensim library under the hood is the same.</li>
</ul>

</div>

<script>
(function () {
  "use strict";

  var DATA = null;
  var TOPIC_COLORS = ["#2563eb", "#b45309", "#22c55e", "#7c3aed", "#db2777", "#0891b2", "#f59e0b", "#0f766e", "#65a30d", "#9333ea", "#ea580c", "#14b8a6"];
  var ERA_ORDER = ["Colonial", "Authoritarian", "Democratic"];
  var SUGGESTED_LABELS = null;  // computed after data loads

  var activeTopic = 0;

  fetch("{{ '/interactive/topic_modeling_data.json' | relative_url }}")
    .then(function (r) { return r.json(); })
    .then(function (json) {
      DATA = json;
      SUGGESTED_LABELS = guessLabels(DATA.topics);
      renderCorpusStats();
      renderPreprocStats();
      renderCoherence();
      renderTopicTabs();
      renderTopicPanel();
      renderDocTable();
      renderEraTopicCards();
      document.getElementById("kDefault").textContent = DATA.lda.default_k;
    })
    .catch(function (err) {
      document.querySelector(".tutorial-page").innerHTML +=
        '<div class="callout callout-note"><strong>Data failed to load.</strong> ' +
        'Check that <code>topic_modeling_data.json</code> exists in <code>/interactive/</code>. ' +
        '(' + err + ')</div>';
    });

  // ── 2. Corpus stats ─────────────────────────────────────────────────
  function renderCorpusStats() {
    var c = DATA.corpus;
    var grid = document.getElementById("corpusStats");
    var cards = [
      { label: "Books", value: c.n_books },
      { label: "Year range", value: c.year_min + "&ndash;" + c.year_max },
      { label: "Colonial",      value: c.era_counts.Colonial      || 0, sub: "pre-1945" },
      { label: "Authoritarian", value: c.era_counts.Authoritarian || 0, sub: "1946&ndash;1991" },
      { label: "Democratic",    value: c.era_counts.Democratic    || 0, sub: "post-1987" },
    ];
    grid.innerHTML = cards.map(function (x) {
      return '<div class="stat-card"><div class="stat-label">' + x.label + '</div>' +
             '<div class="stat-value">' + x.value + '</div>' +
             (x.sub ? '<div class="stat-sub">' + x.sub + '</div>' : '') +
             '</div>';
    }).join("");
  }

  // ── 3. Preprocessing stats ──────────────────────────────────────────
  function renderPreprocStats() {
    var p = DATA.preprocessing;
    var grid = document.getElementById("preprocStats");
    var cards = [
      { label: "Tokenizer",          value: "Kiwi", sub: "POS: " + p.pos_tags_kept.join(", ") },
      { label: "Stopwords",          value: p.stopwords_count.toLocaleString() },
      { label: "Vocab (after)",      value: p.vocabulary_size_after_filter.toLocaleString(),
        sub: "from " + p.vocabulary_size_before_filter.toLocaleString() },
      { label: "Tokens in model",    value: p.total_tokens_after_filter.toLocaleString() },
      { label: "Doc-freq filter",    value: "≥ " + p.min_doc_freq_books + " books · ≤ " + Math.round(p.max_doc_freq_prop * 100) + "%" },
    ];
    grid.innerHTML = cards.map(function (x) {
      return '<div class="stat-card"><div class="stat-label">' + x.label + '</div>' +
             '<div class="stat-value" style="font-size:1.05rem">' + x.value + '</div>' +
             (x.sub ? '<div class="stat-sub">' + x.sub + '</div>' : '') +
             '</div>';
    }).join("");
  }

  // ── 4. Coherence line chart (SVG) ───────────────────────────────────
  function renderCoherence() {
    var pts = DATA.coherence;
    if (!pts || !pts.length) return;
    var svg = document.getElementById("coherenceChart");
    // Layout
    var W = 680, H = 340, m = { t: 46, r: 28, b: 58, l: 62 };
    var xs = pts.map(function (p) { return p.k; });
    var ys = pts.map(function (p) { return p.coherence_cv; });
    var xMin = Math.min.apply(null, xs), xMax = Math.max.apply(null, xs);
    var yMin = Math.min.apply(null, ys), yMax = Math.max.apply(null, ys);
    var yPad = (yMax - yMin) * 0.25 || 0.05;
    yMin -= yPad; yMax += yPad;

    function sx(x) { return m.l + (x - xMin) / (xMax - xMin) * (W - m.l - m.r); }
    function sy(y) { return H - m.b - (y - yMin) / (yMax - yMin) * (H - m.t - m.b); }

    var parts = [];
    // gridlines (y)
    var yTicks = 4;
    for (var i = 0; i <= yTicks; i++) {
      var v = yMin + (yMax - yMin) * i / yTicks;
      parts.push('<line x1="' + m.l + '" x2="' + (W - m.r) + '" y1="' + sy(v) + '" y2="' + sy(v) + '" stroke="#e2e8f0"/>');
      parts.push('<text x="' + (m.l - 10) + '" y="' + (sy(v) + 4) + '" text-anchor="end" font-size="11" fill="#94a3b8">' + v.toFixed(2) + '</text>');
    }
    // x ticks
    pts.forEach(function (p) {
      parts.push('<text x="' + sx(p.k) + '" y="' + (H - m.b + 18) + '" text-anchor="middle" font-size="11" fill="#64748b">' + p.k + '</text>');
    });
    parts.push('<text x="' + (m.l + (W - m.l - m.r) / 2) + '" y="' + (H - 14) + '" text-anchor="middle" font-size="12" fill="#475569" font-weight="600">number of topics (k)</text>');
    parts.push('<text transform="rotate(-90) translate(' + (-(H / 2)) + ',18)" font-size="12" fill="#475569" font-weight="600" text-anchor="middle">coherence (c_v)</text>');

    // line
    var d = pts.map(function (p, i) { return (i === 0 ? "M" : "L") + sx(p.k) + "," + sy(p.coherence_cv); }).join(" ");
    parts.push('<path d="' + d + '" fill="none" stroke="#001158" stroke-width="2"/>');

    // best point + default point
    var best = pts.reduce(function (a, b) { return b.coherence_cv > a.coherence_cv ? b : a; });

    // Edge-aware label placement: keep labels off the y-axis labels at left
    // and off the chart's right edge. Tick line hidden when label sits
    // alongside the dot (left/right edges) since they'd be on top of each other.
    function placeLabel(px, py, text, color, below) {
      var nearLeft  = (px - m.l) < 50;
      var nearRight = ((W - m.r) - px) < 50;
      if (nearLeft || nearRight) {
        var lx     = nearLeft ? px + 11 : px - 11;
        var anchor = nearLeft ? "start" : "end";
        var ly     = py + (below ? 4 : -2);
        parts.push('<text x="' + lx + '" y="' + ly +
                   '" text-anchor="' + anchor + '" font-size="11" fill="' + color + '" font-weight="700">' + text + '</text>');
      } else {
        var tickY1 = below ? py + 10 : py - 10;
        var tickY2 = below ? py + 22 : py - 22;
        var textY  = below ? py + 34 : py - 26;
        parts.push('<line x1="' + px + '" x2="' + px + '" y1="' + tickY1 + '" y2="' + tickY2 + '" stroke="' + color + '" stroke-width="1.2"/>');
        parts.push('<text x="' + px + '" y="' + textY +
                   '" text-anchor="middle" font-size="11" fill="' + color + '" font-weight="700">' + text + '</text>');
      }
    }

    pts.forEach(function (p) {
      var isBest = p.k === best.k;
      var isDefault = p.k === DATA.lda.default_k;
      parts.push('<circle cx="' + sx(p.k) + '" cy="' + sy(p.coherence_cv) + '" r="' + (isBest ? 6 : (isDefault ? 6 : 4)) +
                 '" fill="' + (isBest ? "#22c55e" : (isDefault ? "#ea580c" : "#001158")) + '"/>');
      if (isBest) {
        placeLabel(sx(p.k), sy(p.coherence_cv), "best · k=" + p.k, "#166534", false);
      } else if (isDefault) {
        placeLabel(sx(p.k), sy(p.coherence_cv), "shown below · k=" + p.k, "#9a3412", true);
      }
    });

    svg.innerHTML = parts.join("");

    var note = document.getElementById("coherenceNote");
    var relation = "";
    if (DATA.lda.default_k === best.k) {
      relation = "&mdash; the coherence peak.";
    } else if (DATA.lda.default_k > best.k) {
      relation = "&mdash; a little higher than the peak, to trade coherence for slightly finer-grained themes.";
    } else {
      relation = "&mdash; a little lower than the peak.";
    }
    note.innerHTML = "<strong>" + best.coherence_cv.toFixed(4) + "</strong> is the highest c_v, at <strong>k = " + best.k +
      "</strong>. For the topic browser and LDAvis below we show <strong>k = " + DATA.lda.default_k +
      "</strong> " + relation;
  }

  // ── 5. Topic tabs ───────────────────────────────────────────────────
  function renderTopicTabs() {
    var container = document.getElementById("topicTabs");
    container.innerHTML = DATA.topics.map(function (t, i) {
      return '<button class="topic-tab' + (i === activeTopic ? " active" : "") +
             '" data-topic="' + i + '" style="' +
             (i === activeTopic ? "" : "border-color:" + TOPIC_COLORS[i] + ";color:" + TOPIC_COLORS[i]) +
             '">T' + (t.topic_id + 1) + " · " + SUGGESTED_LABELS[i] + '</button>';
    }).join("");
    container.querySelectorAll(".topic-tab").forEach(function (btn) {
      btn.addEventListener("click", function () {
        activeTopic = parseInt(btn.getAttribute("data-topic"), 10);
        renderTopicTabs();
        renderTopicPanel();
      });
    });
  }

  function renderTopicPanel() {
    var t = DATA.topics[activeTopic];
    var panel = document.getElementById("topicPanel");
    var color = TOPIC_COLORS[activeTopic];
    var maxW = Math.max.apply(null, t.top_words.map(function (w) { return w.weight; }));
    var rows = t.top_words.map(function (w) {
      var pct = (w.weight / maxW) * 100;
      return '<div class="topic-word-row">' +
        '<div class="topic-word">' + escapeHTML(w.word) + '</div>' +
        '<div class="topic-word-bar-track"><div class="topic-word-bar-fill" style="width:' + pct.toFixed(1) + '%;background:' + color + '"></div></div>' +
        '<div class="topic-word-weight">' + w.weight.toFixed(4) + '</div>' +
        '</div>';
    }).join("");

    panel.innerHTML =
      '<div class="topic-panel" style="border-top:3px solid ' + color + '">' +
      '<div class="topic-panel-title">Topic ' + (t.topic_id + 1) + ' &mdash; ' + SUGGESTED_LABELS[activeTopic] + '</div>' +
      '<div class="topic-panel-sub">Top ' + t.top_words.length + ' words with their topic&ndash;word weights (&#981;<sub>k</sub>(w)).</div>' +
      '<div class="topic-words-grid">' + rows + '</div>' +
      '</div>';
  }

  // ── 6. Document table & mixtures ────────────────────────────────────
  function renderDocTable() {
    var eraSelect = document.getElementById("eraFilter");
    var sortSelect = document.getElementById("sortBy");
    var tbody = document.getElementById("docTableBody");

    function repaint() {
      var era = eraSelect.value;
      var sortKey = sortSelect.value;
      var docs = DATA.documents.slice();
      if (era !== "all") docs = docs.filter(function (d) { return d.era === era; });
      docs.sort(function (a, b) {
        if (sortKey === "year")      return (a.year || 0) - (b.year || 0);
        if (sortKey === "year_desc") return (b.year || 0) - (a.year || 0);
        if (sortKey === "tokens")    return b.n_tokens - a.n_tokens;
        if (sortKey === "dominant")  return a.dominant_topic - b.dominant_topic ||
                                            (a.year || 0) - (b.year || 0);
        return 0;
      });
      tbody.innerHTML = docs.map(function (d) {
        var eraClass = "era-badge era-badge-" + d.era.toLowerCase();
        var mix = d.weights.map(function (w, i) {
          return w > 0 ? '<div class="mix-seg" style="width:' + (w * 100).toFixed(2) + '%;background:' + TOPIC_COLORS[i] + '" title="T' + (i + 1) + ' · ' + SUGGESTED_LABELS[i] + ' · ' + (w * 100).toFixed(1) + '%"></div>' : "";
        }).join("");
        return '<tr>' +
          '<td title="' + escapeHTML(d.full_title) + '">' + escapeHTML(d.title) + '</td>' +
          '<td><span class="' + eraClass + '">' + d.era + '</span></td>' +
          '<td>' + (d.year || "") + '</td>' +
          '<td>' + d.n_tokens.toLocaleString() + '</td>' +
          '<td><div class="mix-bar">' + mix + '</div></td>' +
          '<td style="color:' + TOPIC_COLORS[d.dominant_topic] + ';font-weight:700">T' + (d.dominant_topic + 1) + '</td>' +
          '</tr>';
      }).join("");
    }
    eraSelect.addEventListener("change", repaint);
    sortSelect.addEventListener("change", repaint);
    repaint();
  }

  function renderEraTopicCards() {
    var grid = document.getElementById("eraTopicCards");
    var html = ERA_ORDER.filter(function (e) { return DATA.era_topic_mix[e]; }).map(function (era) {
      var mix = DATA.era_topic_mix[era];
      var bars = mix.map(function (w, i) {
        return '<div class="topic-word-row">' +
          '<div class="topic-word" style="font-size:0.78rem;min-width:7rem">T' + (i + 1) + ' · ' + SUGGESTED_LABELS[i] + '</div>' +
          '<div class="topic-word-bar-track"><div class="topic-word-bar-fill" style="width:' + (w * 100).toFixed(1) + '%;background:' + TOPIC_COLORS[i] + '"></div></div>' +
          '<div class="topic-word-weight">' + (w * 100).toFixed(1) + '%</div>' +
          '</div>';
      }).join("");
      return '<div class="era-topic-card"><h4><span class="era-badge era-badge-' + era.toLowerCase() + '">' + era + '</span></h4>' + bars + '</div>';
    }).join("");
    grid.innerHTML = html;
  }

  // ── Label inference: quick heuristic from top words ─────────────────
  function guessLabels(topics) {
    // Match top words against a small hint table and pick the label
    // with the highest overlap. If nothing scores ≥ 2, show top words.
    var HINTS = [
      { words: ["고구려", "백제", "신라", "삼국", "기원전", "기원후", "원년", "즉위"], label: "Ancient Korea (Three Kingdoms)" },
      { words: ["일제", "독립", "저항", "항일", "식민"],                  label: "Colonial era & resistance" },
      { words: ["중국", "세기", "세계", "러시아", "영국", "일본", "유럽"], label: "World history & foreign relations" },
      { words: ["문화", "사회", "생활", "전통", "시대"],                  label: "Culture & society" },
      { words: ["산업화", "경제", "발전", "수출", "성장"],                label: "Industrialization & growth" },
      { words: ["민주", "시민", "참여", "투표", "선거"],                  label: "Democracy & civic life" },
      { words: ["농민", "생산", "토지", "노동", "농업"],                  label: "Peasants, production, society" },
      { words: ["조선", "왕", "성리학"],                                  label: "Joseon dynasty" },
      { words: ["민족", "정체성", "통일", "한민족"],                      label: "Nation & identity" },
    ];
    return topics.map(function (t) {
      var top = t.top_words.slice(0, 10).map(function (w) { return w.word; });
      var best = { label: null, count: 0 };
      HINTS.forEach(function (h) {
        var overlap = h.words.filter(function (w) { return top.indexOf(w) !== -1; }).length;
        if (overlap > best.count) { best = { label: h.label, count: overlap }; }
      });
      if (best.count >= 2) return best.label;
      return top.slice(0, 3).join(" · ");
    });
  }

  function escapeHTML(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c];
    });
  }

  // ── Copy button ─────────────────────────────────────────────────
  window.copyCode = function (btn) {
    var pre = btn.closest(".code-block").querySelector("pre code");
    navigator.clipboard.writeText(pre.textContent).then(function () {
      btn.textContent = "Copied!";
      btn.classList.add("copied");
      setTimeout(function () {
        btn.textContent = "Copy";
        btn.classList.remove("copied");
      }, 1500);
    });
  };
})();
</script>
