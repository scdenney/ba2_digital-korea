---
layout: default
title: "Exploring Korean History Textbooks in R"
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

/* ── Bar chart ───────────────────────────────────────────────────── */
.bar-chart-container {
  padding: 0.5rem 0;
}

.bar-row {
  display: flex;
  align-items: center;
  margin-bottom: 0.4rem;
  gap: 0.5rem;
}

.bar-label {
  width: 180px;
  font-size: 0.78rem;
  text-align: right;
  color: #374151;
  line-height: 1.3;
  flex-shrink: 0;
}

.bar-label .bar-label-era {
  font-size: 0.68rem;
  color: #9ca3af;
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

.era-colonial-bg { background: #b45309; }
.era-authoritarian-bg { background: #7c3aed; }
.era-democratic-bg { background: #0891b2; }

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

/* ── Toggle controls ─────────────────────────────────────────────── */
.toggle-group {
  display: flex;
  gap: 0.35rem;
  margin-bottom: 0.75rem;
  justify-content: center;
}

.toggle-btn {
  padding: 0.35rem 0.9rem;
  border: 2px solid #e2e8f0;
  border-radius: 20px;
  background: #fff;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  color: #64748b;
  transition: all 0.2s;
  font-family: inherit;
}

.toggle-btn:hover { border-color: var(--leiden-blue); color: var(--leiden-blue); }
.toggle-btn.active { background: var(--leiden-blue); color: #fff; border-color: var(--leiden-blue); }

/* ── Concordance cards ───────────────────────────────────────────── */
.concordance-intro {
  text-align: center;
  margin-bottom: 1.5rem;
}

.concordance-keyword {
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--leiden-blue);
  margin-bottom: 0.15rem;
}

.concordance-keyword-sub {
  font-size: 0.88rem;
  color: #6b7280;
  font-style: italic;
}

.concordance-card {
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 1.25rem 1.5rem;
  margin-bottom: 1rem;
  position: relative;
  transition: box-shadow 0.2s;
}

.concordance-card:hover {
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
}

.concordance-era-tag {
  display: inline-block;
  padding: 0.15rem 0.6rem;
  border-radius: 12px;
  font-size: 0.72rem;
  font-weight: 700;
  color: #fff;
  margin-bottom: 0.6rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.concordance-korean {
  font-size: 1.05rem;
  line-height: 1.8;
  color: #1f2937;
  margin-bottom: 0.5rem;
  word-break: keep-all;
}

.concordance-korean .kw-highlight {
  background: linear-gradient(to bottom, transparent 60%, #fde68a 60%);
  font-weight: 700;
  padding: 0 2px;
}

.concordance-english {
  font-size: 0.88rem;
  line-height: 1.6;
  color: #6b7280;
  font-style: italic;
  padding-left: 0.75rem;
  border-left: 2px solid #e2e8f0;
}

.concordance-english .kw-highlight-en {
  font-weight: 600;
  color: #4b5563;
  font-style: normal;
}

.concordance-source {
  font-size: 0.75rem;
  color: #9ca3af;
  margin-top: 0.5rem;
  text-align: right;
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

/* ── Responsive ──────────────────────────────────────────────────── */
@media (max-width: 768px) {
  .wordcloud-grid { grid-template-columns: 1fr; }
  .bar-label { width: 140px; font-size: 0.72rem; }
}
</style>

<div class="tutorial-page">

<div class="tutorial-header">
  <h1>Exploring Korean History Textbooks in R</h1>
  <p class="tutorial-subtitle">Word clouds, frequency analysis, and concordance with the NIKH corpus</p>
  <div class="tutorial-meta">
    <span>Week 5</span>
    <span>R + tidyverse + tidytext</span>
    <span>NIKH History Textbook Corpus (demo subset)</span>
  </div>
</div>

<p class="narrative">
  This walkthrough replicates part of the Week 5 hands-on lesson in R. We load 9 Korean history textbooks from three political eras, preprocess the text, and explore how language differs across eras using word clouds and concordance analysis. All code runs top to bottom in RStudio.
</p>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">1</span>
  <h2>Setup &amp; Load Data</h2>
</div>

<p class="narrative">
  We use <strong>tidyverse</strong> for data wrangling, <strong>tidytext</strong> for text analysis structure, <strong>elbird</strong> for Korean morphological analysis (it wraps the same Kiwi engine used in our Orange preprocessing scripts), and <strong>ggwordcloud</strong> for word clouds.
</p>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: load packages, corpus, and stopwords</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── Packages ──────────────────────────────────────────────────────</span>
<span class="r-function">library</span>(tidyverse)
<span class="r-function">library</span>(tidytext)
<span class="r-function">library</span>(elbird)
<span class="r-function">library</span>(ggwordcloud)

<span class="r-comment"># ── Load the NIKH demo corpus ─────────────────────────────────────</span>
corpus <span class="r-operator">&lt;-</span> <span class="r-function">read_csv</span>(<span class="r-string">"data/nikh_textbooks/nikh_textbooks_demo.csv"</span>)

<span class="r-comment"># ── Load Korean stopwords ─────────────────────────────────────────</span>
stopwords_ko <span class="r-operator">&lt;-</span> <span class="r-function">read_lines</span>(<span class="r-string">"data/stopwords_ko.txt"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">str_trim</span>() <span class="r-operator">|&gt;</span>
  <span class="r-function">discard</span>(<span class="r-operator">~</span> .x <span class="r-operator">==</span> <span class="r-string">""</span>)

<span class="r-comment"># Quick look at the data</span>
corpus <span class="r-operator">|&gt;</span> <span class="r-function">select</span>(book_id, title, era, period) <span class="r-operator">|&gt;</span> <span class="r-function">print</span>(n <span class="r-operator">=</span> <span class="r-number">9</span>)</code></pre>
    </div>
    <div class="callout callout-info">
      <strong>About elbird:</strong> Install it with <code>install.packages("elbird")</code>. It wraps <a href="https://github.com/bab2min/Kiwi">Kiwi</a>, the same Korean morphological analyzer used in our Orange preprocessing scripts. First run downloads the model automatically.
    </div>
  </div>
</details>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">2</span>
  <h2>Preprocessing</h2>
</div>

<p class="narrative">
  We tokenize each book with Kiwi's morphological analyzer, keep only common nouns (<code>NNG</code>) and proper nouns (<code>NNP</code>), remove stopwords, and filter out single-character tokens. This is the same pipeline as our Orange workflow.
</p>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: tokenize, filter nouns, remove stopwords</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── Helper: tokenize one text with Kiwi via elbird ────────────────</span>
tokenize_kiwi <span class="r-operator">&lt;-</span> <span class="r-keyword">function</span>(text) {
  result <span class="r-operator">&lt;-</span> <span class="r-function">tokenize</span>(text, flatten <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>)
  <span class="r-function">tibble</span>(form <span class="r-operator">=</span> result<span class="r-operator">$</span>form, tag <span class="r-operator">=</span> result<span class="r-operator">$</span>tag)
}

<span class="r-comment"># ── Tokenize and filter ───────────────────────────────────────────</span>
tokens <span class="r-operator">&lt;-</span> corpus <span class="r-operator">|&gt;</span>
  <span class="r-function">select</span>(book_id, era, full_text) <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(
    morphemes <span class="r-operator">=</span> <span class="r-function">map</span>(full_text, tokenize_kiwi)
  ) <span class="r-operator">|&gt;</span>
  <span class="r-function">unnest</span>(morphemes) <span class="r-operator">|&gt;</span>
  <span class="r-function">filter</span>(
    tag <span class="r-operator">%in%</span> <span class="r-function">c</span>(<span class="r-string">"NNG"</span>, <span class="r-string">"NNP"</span>),       <span class="r-comment"># keep nouns</span>
    <span class="r-operator">!</span>form <span class="r-operator">%in%</span> stopwords_ko,           <span class="r-comment"># remove stopwords</span>
    <span class="r-function">str_length</span>(form) <span class="r-operator">&gt;=</span> <span class="r-number">2</span>,           <span class="r-comment"># drop single characters</span>
    <span class="r-operator">!</span><span class="r-function">str_detect</span>(form, <span class="r-string">"^[0-9]+$"</span>)   <span class="r-comment"># drop pure numbers</span>
  ) <span class="r-operator">|&gt;</span>
  <span class="r-function">select</span>(book_id, era, word <span class="r-operator">=</span> form)

<span class="r-comment"># ── Count words per era ───────────────────────────────────────────</span>
era_counts <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(era, word, sort <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>)

<span class="r-comment"># Top 10 per era</span>
era_counts <span class="r-operator">|&gt;</span>
  <span class="r-function">group_by</span>(era) <span class="r-operator">|&gt;</span>
  <span class="r-function">slice_max</span>(n, n <span class="r-operator">=</span> <span class="r-number">10</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">print</span>(n <span class="r-operator">=</span> <span class="r-number">30</span>)</code></pre>
    </div>
    <div class="callout callout-tip">
      <strong>Note on <code>tokenize_kiwi()</code>:</strong> This helper wraps elbird's <code>tokenize()</code> function and returns a tidy tibble with <code>form</code> (the surface word) and <code>tag</code> (the POS tag). The <code>flatten = TRUE</code> argument returns all tokens in a single flat structure.
    </div>
  </div>
</details>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">3</span>
  <h2>Word Clouds by Era</h2>
</div>

<p class="narrative">
  Word clouds give a quick visual sense of what each era's textbooks emphasize. The colonial-era texts (written under Japanese rule) feature terms about kingdoms and military conflict. The authoritarian-era texts foreground <strong>nation</strong>, <strong>society</strong>, and <strong>culture</strong>. The democratic-era texts add <strong>movements</strong>, <strong>independence</strong>, and <strong>development</strong>.
</p>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: generate word clouds with ggwordcloud</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── Word clouds by era ────────────────────────────────────────────</span>
<span class="r-comment"># Colorblind-friendly palette (Okabe-Ito inspired)</span>
era_colors <span class="r-operator">&lt;-</span> <span class="r-function">c</span>(
  Colonial      <span class="r-operator">=</span> <span class="r-string">"#b45309"</span>,  <span class="r-comment"># amber</span>
  Authoritarian <span class="r-operator">=</span> <span class="r-string">"#7c3aed"</span>,  <span class="r-comment"># violet</span>
  Democratic    <span class="r-operator">=</span> <span class="r-string">"#0891b2"</span>   <span class="r-comment"># cyan</span>
)

era_counts <span class="r-operator">|&gt;</span>
  <span class="r-function">group_by</span>(era) <span class="r-operator">|&gt;</span>
  <span class="r-function">slice_max</span>(n, n <span class="r-operator">=</span> <span class="r-number">50</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">ungroup</span>() <span class="r-operator">|&gt;</span>
  <span class="r-function">ggplot</span>(<span class="r-function">aes</span>(label <span class="r-operator">=</span> word, size <span class="r-operator">=</span> n, color <span class="r-operator">=</span> era)) <span class="r-operator">+</span>
  <span class="r-function">geom_text_wordcloud</span>(area_corr <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>) <span class="r-operator">+</span>
  <span class="r-function">scale_color_manual</span>(values <span class="r-operator">=</span> era_colors) <span class="r-operator">+</span>
  <span class="r-function">scale_size_area</span>(max_size <span class="r-operator">=</span> <span class="r-number">14</span>) <span class="r-operator">+</span>
  <span class="r-function">facet_wrap</span>(<span class="r-operator">~</span> era) <span class="r-operator">+</span>
  <span class="r-function">theme_minimal</span>() <span class="r-operator">+</span>
  <span class="r-function">theme</span>(strip.text <span class="r-operator">=</span> <span class="r-function">element_text</span>(face <span class="r-operator">=</span> <span class="r-string">"bold"</span>, size <span class="r-operator">=</span> <span class="r-number">12</span>))</code></pre>
    </div>
  </div>
</details>

<div class="output-panel">
  <div class="output-panel-header">Output</div>
  <div class="output-panel-body">
    <div class="wordcloud-grid" id="wordcloudGrid"></div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">4</span>
  <h2>Tracking <span style="font-family: inherit;">통일</span> (Unification) Across Eras</h2>
</div>

<p class="narrative">
  The word <strong>통일</strong> (<em>tongil</em>, unification) appears in all three eras, but its meaning shifts dramatically. In colonial-era textbooks, it refers to ancient territorial unification of kingdoms. In authoritarian-era texts, it takes on nationalist overtones. In democratic-era texts, it centers on North-South reunification and peace.
</p>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: count and plot 통일 frequency per textbook</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── Count 통일 per document ───────────────────────────────────────</span>
tongil_counts <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span>
  <span class="r-function">filter</span>(word <span class="r-operator">==</span> <span class="r-string">"통일"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(book_id, era, name <span class="r-operator">=</span> <span class="r-string">"tongil_n"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">left_join</span>(
    tokens <span class="r-operator">|&gt;</span> <span class="r-function">count</span>(book_id, name <span class="r-operator">=</span> <span class="r-string">"total_n"</span>),
    by <span class="r-operator">=</span> <span class="r-string">"book_id"</span>
  ) <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(per_1k <span class="r-operator">=</span> tongil_n <span class="r-operator">/</span> total_n <span class="r-operator">*</span> <span class="r-number">1000</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">left_join</span>(corpus <span class="r-operator">|&gt;</span> <span class="r-function">select</span>(book_id, title), by <span class="r-operator">=</span> <span class="r-string">"book_id"</span>)

<span class="r-comment"># ── Plot ──────────────────────────────────────────────────────────</span>
tongil_counts <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(title <span class="r-operator">=</span> <span class="r-function">str_trunc</span>(title, <span class="r-number">25</span>)) <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(title <span class="r-operator">=</span> <span class="r-function">fct_reorder</span>(title, per_1k)) <span class="r-operator">|&gt;</span>
  <span class="r-function">ggplot</span>(<span class="r-function">aes</span>(x <span class="r-operator">=</span> per_1k, y <span class="r-operator">=</span> title, fill <span class="r-operator">=</span> era)) <span class="r-operator">+</span>
  <span class="r-function">geom_col</span>() <span class="r-operator">+</span>
  <span class="r-function">scale_fill_manual</span>(values <span class="r-operator">=</span> era_colors) <span class="r-operator">+</span>
  <span class="r-function">labs</span>(
    x <span class="r-operator">=</span> <span class="r-string">"Occurrences per 1,000 tokens"</span>,
    y <span class="r-operator">=</span> <span class="r-keyword">NULL</span>,
    fill <span class="r-operator">=</span> <span class="r-string">"Era"</span>,
    title <span class="r-operator">=</span> <span class="r-string">"통일 (unification) across textbooks"</span>
  ) <span class="r-operator">+</span>
  <span class="r-function">theme_minimal</span>(base_size <span class="r-operator">=</span> <span class="r-number">12</span>)</code></pre>
    </div>
  </div>
</details>

<div class="output-panel">
  <div class="output-panel-header">Output</div>
  <div class="output-panel-body">
    <div class="toggle-group" id="barToggle">
      <button class="toggle-btn active" data-mode="per1k">Per 1,000 tokens</button>
      <button class="toggle-btn" data-mode="raw">Raw count</button>
    </div>
    <div class="chart-legend">
      <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#b45309"></span> Colonial</span>
      <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#7c3aed"></span> Authoritarian</span>
      <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#0891b2"></span> Democratic</span>
    </div>
    <div class="bar-chart-container" id="barChart"></div>
  </div>
</div>

<div class="callout callout-info">
  <strong>Reading the chart:</strong> <em>Raw count</em> is simply how many times 통일 appears in each textbook. But longer books naturally contain more of every word, so raw counts can be misleading. <em>Per 1,000 tokens</em> adjusts for document length: divide the raw count by the total number of tokens in that book, then multiply by 1,000. This gives you a rate &mdash; "out of every 1,000 words, how many are 통일?" &mdash; so you can fairly compare books of different lengths.
</div>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">5</span>
  <h2>Concordance: 통일 in Context</h2>
</div>

<p class="narrative">
  A word count tells you <em>how often</em>. Concordance tells you <em>how</em>. Below are five sentences containing 통일, one or two from each era. Notice how the same word carries entirely different meanings depending on the political context in which the textbook was written.
</p>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: KWIC concordance search for 통일</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── KWIC concordance for 통일 ─────────────────────────────────────</span>
kwic_results <span class="r-operator">&lt;-</span> corpus <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(
    sentences <span class="r-operator">=</span> <span class="r-function">map</span>(full_text, <span class="r-operator">~</span> <span class="r-function">str_split</span>(.x, <span class="r-string">"(?&lt;=[다요])\\s+"</span>) <span class="r-operator">|&gt;</span> <span class="r-function">pluck</span>(<span class="r-number">1</span>))
  ) <span class="r-operator">|&gt;</span>
  <span class="r-function">unnest</span>(sentences) <span class="r-operator">|&gt;</span>
  <span class="r-function">filter</span>(<span class="r-function">str_detect</span>(sentences, <span class="r-string">"통일"</span>)) <span class="r-operator">|&gt;</span>
  <span class="r-function">select</span>(book_id, era, title, sentence <span class="r-operator">=</span> sentences)

<span class="r-comment"># Browse the results</span>
kwic_results <span class="r-operator">|&gt;</span> <span class="r-function">print</span>(n <span class="r-operator">=</span> <span class="r-number">20</span>)</code></pre>
    </div>
  </div>
</details>

<div class="output-panel">
  <div class="output-panel-header">Curated Concordance</div>
  <div class="output-panel-body" style="background: #f9fafb;">

    <div class="concordance-intro">
      <div class="concordance-keyword">통일</div>
      <div class="concordance-keyword-sub">tongil &mdash; unification</div>
    </div>

    <!-- Sentence 1: Colonial — ancient kingdom unification -->
    <div class="concordance-card">
      <span class="concordance-era-tag" style="background:#b45309;">Colonial</span>
      <p class="concordance-korean">태조는 즉위한 지 19년 만에 신라와 후백제를 병합하고 반도를 <span class="kw-highlight">통일</span>했다.</p>
      <p class="concordance-english">King Taejo annexed Silla and Later Baekje, <span class="kw-highlight-en">unifying</span> the peninsula within nineteen years of ascending the throne.</p>
      <p class="concordance-source">심상소학국사보충아동용 &middot; Colonial Period</p>
    </div>

    <!-- Sentence 2: Authoritarian — nationalist framing of ancient history -->
    <div class="concordance-card">
      <span class="concordance-era-tag" style="background:#7c3aed;">Authoritarian</span>
      <p class="concordance-korean">신라는 우리 땅을 지배하려는 당을 몰아 내고 마침내 삼국 <span class="kw-highlight">통일</span>을 이룩하여, 민족의 굳건한 기백을 보여 주었다.</p>
      <p class="concordance-english">Silla drove out Tang, which sought to dominate our land, and finally achieved the Three Kingdoms <span class="kw-highlight-en">unification</span>, demonstrating the unyielding spirit of the nation.</p>
      <p class="concordance-source">중학교 국사 4차(상) &middot; Chun/Roh Transitional &middot; 1981</p>
    </div>

    <!-- Sentence 3: Authoritarian — Cold War aspiration for unification -->
    <div class="concordance-card">
      <span class="concordance-era-tag" style="background:#7c3aed;">Authoritarian</span>
      <p class="concordance-korean">우리는 바라던 독립을 차지하였으나, 아직도 <span class="kw-highlight">통일</span>을 이루지 못하고 있으니, 앞으로 더욱 뭉쳐서 <span class="kw-highlight">통일</span>과 발전을 위하여 노력하여야 하겠다.</p>
      <p class="concordance-english">We have achieved the independence we longed for, but have still not achieved <span class="kw-highlight-en">unification</span>; we must unite further and strive for <span class="kw-highlight-en">unification</span> and national development.</p>
      <p class="concordance-source">초등학교 사회생활 6-1(1차) &middot; Postwar Authoritarian &middot; 1954</p>
    </div>

    <!-- Sentence 4: Democratic — inter-Korean peace process -->
    <div class="concordance-card">
      <span class="concordance-era-tag" style="background:#0891b2;">Democratic</span>
      <p class="concordance-korean">이러한 평화 <span class="kw-highlight">통일</span>을 위한 노력은 남북 대화가 중단된 후에도 계속되어 우리 정부는 북한에 상호 불가침 협정을 제안하기도 하였다.</p>
      <p class="concordance-english">These efforts for peaceful <span class="kw-highlight-en">unification</span> continued even after inter-Korean dialogue was suspended, and our government proposed a mutual non-aggression pact to North Korea.</p>
      <p class="concordance-source">중학교 국사 6차(하) &middot; Early Democratic &middot; 1995</p>
    </div>

    <!-- Sentence 5: Democratic — democratic nation-building vision -->
    <div class="concordance-card">
      <span class="concordance-era-tag" style="background:#0891b2;">Democratic</span>
      <p class="concordance-korean">광복 후 분단을 딛고 일어선 대한 민국은 민주 정치의 발전, 경제적 번영, 그리고 복지 사회 건설과 민족 <span class="kw-highlight">통일</span>을 목표로 성장해 왔다.</p>
      <p class="concordance-english">Since liberation, the Republic of Korea has risen above division and grown with the goals of democratic development, economic prosperity, welfare society, and national <span class="kw-highlight-en">unification</span>.</p>
      <p class="concordance-source">초등학교 사회 6-1(7차) &middot; Democratic Consolidation &middot; 2002</p>
    </div>

  </div>
</div>

<p class="narrative">
  The same word, 통일, carries the weight of its era. Colonial textbooks use it as a neutral historical term for ancient territorial consolidation. Authoritarian-era texts frame it through nationalist ideology — unification as proof of the Korean people's spirit, and as an urgent Cold War imperative. Democratic-era texts reframe it around <strong>peace</strong>, <strong>diplomacy</strong>, and <strong>democratic values</strong>. This is what concordance analysis reveals: not just <em>how often</em> a word appears, but <em>how it means</em>.
</p>

</div><!-- /tutorial-page -->

<script>
(function () {
  "use strict";

  // ── Data loading ─────────────────────────────────────────────────
  var DATA = null;
  var ERA_COLORS = {
    Colonial: "#b45309",
    Authoritarian: "#7c3aed",
    Democratic: "#0891b2"
  };

  fetch("{{ '/interactive/nikh_data.json' | relative_url }}")
    .then(function (r) { return r.json(); })
    .then(function (json) {
      DATA = json;
      renderWordClouds();
      renderBarChart("per1k");
    });

  // ── Word clouds ──────────────────────────────────────────────────
  function renderWordClouds() {
    var grid = document.getElementById("wordcloudGrid");
    grid.innerHTML = "";
    var eras = ["Colonial", "Authoritarian", "Democratic"];
    eras.forEach(function (era) {
      var card = document.createElement("div");
      card.className = "wordcloud-card";

      var header = document.createElement("div");
      header.className = "wordcloud-card-header era-" + era.toLowerCase();
      header.textContent = era;
      card.appendChild(header);

      var body = document.createElement("div");
      body.className = "wordcloud-card-body";

      var words = DATA.era_top_words[era].slice(0, 50);
      var maxCount = words[0].count;

      words.forEach(function (w) {
        var span = document.createElement("span");
        span.className = "wc-word";
        var ratio = w.count / maxCount;
        var size = 0.65 + ratio * 1.6;
        var alpha = 0.4 + ratio * 0.6;
        span.style.fontSize = size + "rem";
        span.style.color = ERA_COLORS[era];
        span.style.opacity = alpha;
        span.textContent = w.word;
        span.title = w.word + ": " + w.count;
        body.appendChild(span);
        body.appendChild(document.createTextNode(" "));
      });

      card.appendChild(body);
      grid.appendChild(card);
    });
  }

  // ── Bar chart ────────────────────────────────────────────────────
  function renderBarChart(mode) {
    var container = document.getElementById("barChart");
    container.innerHTML = "";

    var books = DATA.book_tongil_counts.slice().sort(function (a, b) {
      var valA = mode === "per1k" ? (a.tongil_count / a.total_tokens * 1000) : a.tongil_count;
      var valB = mode === "per1k" ? (b.tongil_count / b.total_tokens * 1000) : b.tongil_count;
      return valB - valA;
    });

    var maxVal = 0;
    books.forEach(function (b) {
      var val = mode === "per1k" ? (b.tongil_count / b.total_tokens * 1000) : b.tongil_count;
      if (val > maxVal) maxVal = val;
    });

    books.forEach(function (b) {
      var val = mode === "per1k" ? (b.tongil_count / b.total_tokens * 1000) : b.tongil_count;
      var pct = maxVal > 0 ? (val / maxVal * 100) : 0;
      var displayVal = mode === "per1k" ? val.toFixed(1) : val;

      var row = document.createElement("div");
      row.className = "bar-row";

      var label = document.createElement("div");
      label.className = "bar-label";
      label.innerHTML = b.title + '<br><span class="bar-label-era">' + b.era + (b.year ? " · " + Math.round(parseFloat(b.year)) : "") + '</span>';

      var track = document.createElement("div");
      track.className = "bar-track";

      var fill = document.createElement("div");
      fill.className = "bar-fill era-" + b.era.toLowerCase() + "-bg";
      fill.style.width = pct + "%";

      if (pct > 15) {
        var valSpan = document.createElement("span");
        valSpan.className = "bar-value";
        valSpan.textContent = displayVal;
        fill.appendChild(valSpan);
      }

      track.appendChild(fill);

      row.appendChild(label);
      row.appendChild(track);

      if (pct <= 15) {
        var valOut = document.createElement("span");
        valOut.className = "bar-value-outside";
        valOut.textContent = displayVal;
        row.appendChild(valOut);
      }

      container.appendChild(row);
    });
  }

  // ── Toggle buttons ───────────────────────────────────────────────
  document.getElementById("barToggle").addEventListener("click", function (e) {
    if (!e.target.classList.contains("toggle-btn")) return;
    var mode = e.target.getAttribute("data-mode");
    document.querySelectorAll("#barToggle .toggle-btn").forEach(function (btn) {
      btn.classList.remove("active");
    });
    e.target.classList.add("active");
    renderBarChart(mode);
  });

  // ── Copy button ──────────────────────────────────────────────────
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
