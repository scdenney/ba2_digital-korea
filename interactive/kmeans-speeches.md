---
layout: default
title: "K-Means Clustering: Presidential Speeches"
---

<style>
/* ── Page layout ──────────────────────────────────────────────────── */
.demo-app { max-width: 100%; }

.demo-header { margin-bottom: 1.5rem; margin-top: 1rem; }
.demo-header h1 { margin: 0 0 0.5rem; font-size: 1.6rem; color: var(--leiden-blue); }
.demo-intro { color: #4a4a4a; font-size: 0.95rem; line-height: 1.6; margin: 0 0 0.75rem; }

.tutorial-meta {
  display: flex; flex-wrap: wrap; gap: 1rem;
  font-size: 0.82rem; color: #9ca3af;
}
.tutorial-meta span { display: inline-flex; align-items: center; gap: 0.3rem; }

/* ── Pipeline step buttons ────────────────────────────────────────── */
.pipeline-steps { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 1rem; }

.step-btn {
  padding: 0.45rem 0.9rem; border: 2px solid #dfe3ee; border-radius: 20px;
  background: #fff; font-size: 0.85rem; cursor: pointer; color: #4a4a4a;
  font-weight: 600; transition: all 0.2s; font-family: inherit;
}
.step-btn:hover { border-color: var(--leiden-blue); color: var(--leiden-blue); }
.step-btn.active { background: var(--leiden-blue); color: #fff; border-color: var(--leiden-blue); }
.step-btn.completed { border-color: #10b981; color: #10b981; }
.step-btn.completed.active { background: var(--leiden-blue); color: #fff; border-color: var(--leiden-blue); }

/* ── Buttons ──────────────────────────────────────────────────────── */
.btn {
  display: inline-block; padding: 0.5rem 1rem; border: 1px solid #dfe3ee;
  border-radius: 6px; background: #fff; font-size: 0.9rem; line-height: 1.2;
  cursor: pointer; color: var(--leiden-blue); font-weight: 600;
  font-family: inherit; transition: background 0.15s, border-color 0.15s;
}
.btn:hover { background: #f5f7fb; border-color: var(--leiden-blue); }
.btn:disabled { opacity: 0.4; cursor: default; }
.btn-sm { padding: 0.35rem 0.75rem; font-size: 0.82rem; }
.btn-primary { background: var(--leiden-blue); color: #fff; border-color: var(--leiden-blue); }
.btn-primary:hover { background: #003366; }
.btn-primary:disabled { background: #94a3b8; border-color: #94a3b8; }

/* ── Scatter plot ─────────────────────────────────────────────────── */
.scatter-wrap { margin: 0.5rem 0 1rem; }

.scatter-container {
  position: relative; border: 1px solid #e2e8f0; border-radius: 8px;
  overflow: hidden; background: #fafbfc; max-width: 760px; margin: 0 auto;
}

#scatterCanvas { display: block; width: 100%; cursor: crosshair; }

.scatter-tooltip {
  display: none; position: absolute; background: rgba(15,23,42,0.92);
  color: #f1f5f9; padding: 0.4rem 0.65rem; border-radius: 5px;
  font-size: 0.75rem; line-height: 1.45; pointer-events: none;
  z-index: 10; max-width: 280px; white-space: nowrap;
}

/* ── Navigation ───────────────────────────────────────────────────── */
.nav-row {
  display: flex; justify-content: space-between; align-items: center; margin: 0.5rem 0;
}
.step-description {
  font-size: 0.88rem; color: #6b7280; text-align: center; flex: 1;
  padding: 0 1rem; line-height: 1.4;
}

/* ── Detail panel ─────────────────────────────────────────────────── */
.detail-panel { margin: 1rem 0; min-height: 60px; }
.step-info { animation: fadeIn 0.3s ease; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
.step-info p { font-size: 0.92rem; line-height: 1.65; color: #374151; margin: 0.5rem 0; }
.step-info strong { color: var(--leiden-blue); }

/* ── K selector / silhouette chart ────────────────────────────────── */
.sil-chart-row {
  display: flex; align-items: flex-end; gap: 0.6rem; justify-content: center;
  height: 170px; padding: 0.5rem 0; margin: 0.75rem 0;
}

.sil-bar-group {
  display: flex; flex-direction: column; align-items: center; gap: 0.25rem;
  cursor: pointer; transition: transform 0.15s;
}
.sil-bar-group:hover { transform: translateY(-2px); }

.sil-bar {
  width: 48px; border-radius: 4px 4px 0 0; transition: height 0.4s ease, background 0.2s;
}
.sil-bar-value { font-size: 0.68rem; font-weight: 600; color: #374151; }
.sil-bar-label { font-size: 0.78rem; font-weight: 700; color: #64748b; transition: color 0.2s; }
.sil-bar-group.selected .sil-bar-label { color: var(--leiden-blue); }
.sil-best-tag { font-size: 0.62rem; font-weight: 700; color: #059669; text-transform: uppercase; }

/* ── Animation controls ───────────────────────────────────────────── */
.anim-controls { display: flex; align-items: center; gap: 0.5rem; margin: 0.75rem 0; flex-wrap: wrap; }
.anim-status {
  font-size: 0.85rem; color: #4b5563; padding: 0.5rem 0.75rem;
  background: #f1f5f9; border-radius: 6px; margin: 0.5rem 0; min-height: 2rem;
  line-height: 1.4;
}

/* ── Cluster legend (clickable) ───────────────────────────────────── */
.cluster-legend-row { display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.75rem 0; }

.cluster-legend-btn {
  display: inline-flex; align-items: center; gap: 0.35rem;
  padding: 0.35rem 0.7rem; border-radius: 20px; border: 2px solid #e2e8f0;
  background: #f8fafc; font-size: 0.8rem; font-weight: 600;
  cursor: pointer; transition: all 0.2s; font-family: inherit; color: #374151;
}
.cluster-legend-btn:hover { border-color: currentColor; }
.cluster-legend-btn.active { background: #fff; box-shadow: 0 1px 4px rgba(0,0,0,0.1); }
.cluster-legend-dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }

/* ── Cluster detail card ──────────────────────────────────────────── */
.cluster-detail {
  border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden;
  margin: 0.75rem 0; animation: fadeIn 0.3s ease;
}
.cluster-detail-header {
  padding: 0.6rem 1rem; font-weight: 700; font-size: 0.85rem; color: #fff;
}
.cluster-detail-body { padding: 0.75rem 1rem; }
.cluster-card-section { margin-bottom: 0.6rem; }
.cluster-card-section-title {
  font-size: 0.72rem; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.04em; color: #9ca3af; margin-bottom: 0.25rem;
}

/* ── Word cloud ───────────────────────────────────────────────────── */
.wc-word {
  display: inline-block; cursor: default; font-weight: 600;
  transition: opacity 0.15s;
}
.wc-word:hover { opacity: 0.7; }

/* ── Mini bars ────────────────────────────────────────────────────── */
.mini-bar-row { display: flex; align-items: center; gap: 0.4rem; margin-bottom: 0.2rem; }
.mini-bar-label {
  width: 50px; font-size: 0.75rem; text-align: right; color: #374151;
  flex-shrink: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}
.mini-bar-track { flex: 1; height: 14px; background: #f1f5f9; border-radius: 3px; overflow: hidden; }
.mini-bar-fill { height: 100%; border-radius: 3px; }
.mini-bar-count { font-size: 0.68rem; color: #6b7280; width: 28px; text-align: right; flex-shrink: 0; }

/* ── Color toggle ─────────────────────────────────────────────────── */
.color-toggle {
  display: inline-flex; border: 2px solid #e2e8f0; border-radius: 8px;
  overflow: hidden; margin: 0.5rem 0;
}
.color-toggle button {
  padding: 0.5rem 1.25rem; border: none; background: #fff;
  font-size: 0.85rem; font-weight: 600; color: #64748b;
  cursor: pointer; transition: all 0.2s; font-family: inherit;
}
.color-toggle button.active { background: var(--leiden-blue); color: #fff; }
.color-toggle button:hover:not(.active) { background: #f8fafc; }

/* ── Color legend ─────────────────────────────────────────────────── */
.color-legend {
  display: flex; flex-wrap: wrap; gap: 0.75rem; margin: 0.75rem 0;
  padding: 0.6rem 0.75rem; background: #f9fafb; border-radius: 6px;
  border: 1px solid #e5e7eb;
}
.color-legend-item {
  display: inline-flex; align-items: center; gap: 0.3rem;
  font-size: 0.78rem; color: #4a4a4a;
}
.color-legend-dot { width: 10px; height: 10px; border-radius: 50%; }

/* ── Callouts ─────────────────────────────────────────────────────── */
.callout {
  padding: 0.75rem 1rem; border-radius: 6px; margin: 0.75rem 0;
  font-size: 0.85rem; line-height: 1.6;
}
.callout-info { background: #eff6ff; border-left: 3px solid #3b82f6; color: #1e40af; }
.callout-tip { background: #f0fdf4; border-left: 3px solid #22c55e; color: #166534; }

/* ── Code ribbons ─────────────────────────────────────────────────── */
.code-ribbon { margin: 0.75rem 0; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; }
.code-ribbon summary {
  display: flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem;
  background: linear-gradient(to right, #1e293b, #334155); color: #e2e8f0;
  font-size: 0.82rem; font-weight: 600; cursor: pointer; user-select: none;
  list-style: none; transition: background 0.2s;
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
.code-ribbon .callout { margin: 0; border-radius: 0; border-left-width: 3px; }

/* ── Code blocks ──────────────────────────────────────────────────── */
.code-block { position: relative; margin: 0.75rem 0; border-radius: 8px; overflow: hidden; border: 1px solid #e2e8f0; }
.code-block-header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 0.4rem 0.75rem; background: #f1f5f9; border-bottom: 1px solid #e2e8f0;
  font-size: 0.75rem; color: #64748b; font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em;
}
.copy-btn {
  padding: 0.2rem 0.5rem; border: 1px solid #cbd5e1; border-radius: 4px;
  background: #fff; font-size: 0.72rem; color: #64748b; cursor: pointer;
  font-family: inherit; transition: all 0.15s;
}
.copy-btn:hover { background: #f8fafc; border-color: var(--leiden-blue); color: var(--leiden-blue); }
.copy-btn.copied { background: #ecfdf5; border-color: #6ee7b7; color: #059669; }
.code-block pre {
  margin: 0; padding: 1rem; background: #1e293b; color: #e2e8f0;
  font-size: 0.82rem; line-height: 1.55; overflow-x: auto;
  font-family: "SFMono-Regular","Consolas","Liberation Mono",monospace;
}
.code-block pre code { background: none; color: inherit; padding: 0; font-size: inherit; }
.r-comment { color: #94a3b8; font-style: italic; }
.r-string { color: #86efac; }
.r-function { color: #93c5fd; }
.r-keyword { color: #c4b5fd; }
.r-number { color: #fde68a; }
.r-operator { color: #f9a8d4; }

/* ── Responsive ───────────────────────────────────────────────────── */
@media (max-width: 600px) {
  .demo-header h1 { font-size: 1.3rem; }
  .pipeline-steps { gap: 0.3rem; }
  .step-btn { font-size: 0.75rem; padding: 0.35rem 0.6rem; }
  .sil-chart-row { height: 140px; gap: 0.35rem; }
  .sil-bar { width: 36px; }
  .color-toggle button { padding: 0.4rem 0.75rem; font-size: 0.8rem; }
}
</style>

<div class="demo-app" id="app">
  <div class="demo-header">
    <h1>K-Means Clustering: Presidential Speeches</h1>
    <p class="demo-intro">Step through a k-means clustering of 648 presidential speeches. Each step shows how the algorithm finds structure in the data and what that structure means.</p>
    <div class="tutorial-meta">
      <span>Week 7</span>
      <span>648 speeches, 7 presidents</span>
      <span>Democratic era (1988&ndash;2022)</span>
    </div>
  </div>

  <div class="pipeline-steps" id="pipelineSteps"></div>

  <div class="scatter-wrap">
    <div class="scatter-container" id="scatterContainer">
      <canvas id="scatterCanvas"></canvas>
      <div id="tooltip" class="scatter-tooltip"></div>
    </div>
  </div>

  <div class="nav-row">
    <button class="btn" id="prevBtn" disabled>Previous</button>
    <span class="step-description" id="stepDesc"></span>
    <button class="btn" id="nextBtn">Next</button>
  </div>

  <div id="detailPanel" class="detail-panel"><p style="color:#6b7280;font-size:0.9rem;">Loading speech data...</p></div>

  <div id="detailPanel2" class="detail-panel"></div>

  <!-- Hidden R code — pulled into the detail panel by Step 6 -->
  <div id="rCodeContent" style="display:none;">

    <p><strong>Step A. Load packages and data</strong><br>We need four packages. <code>elbird</code> wraps the Kiwi Korean morphological analyzer &mdash; install it with <code>install.packages("elbird")</code>. First run downloads the model automatically.</p>
    <details class="code-ribbon">
      <summary><span class="ribbon-label">Show code</span><span class="ribbon-tag">R</span></summary>
      <div class="code-ribbon-body"><div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
        <pre><code><span class="r-function">library</span>(tidyverse)
<span class="r-function">library</span>(tidytext)
<span class="r-function">library</span>(elbird)       <span class="r-comment"># Korean morphological analysis (wraps Kiwi)</span>
<span class="r-function">library</span>(cluster)      <span class="r-comment"># for silhouette()</span>

corpus <span class="r-operator">&lt;-</span> <span class="r-function">read_csv</span>(<span class="r-string">"data/president_speeches/president_speeches_democratic_era.csv"</span>)
stopwords_ko <span class="r-operator">&lt;-</span> <span class="r-function">read_lines</span>(<span class="r-string">"data/stopwords_ko.txt"</span>) <span class="r-operator">|&gt;</span> <span class="r-function">str_trim</span>() <span class="r-operator">|&gt;</span> <span class="r-function">discard</span>(<span class="r-operator">~</span> .x <span class="r-operator">==</span> <span class="r-string">""</span>)</code></pre>
      </div></div>
    </details>

    <p style="margin-top:1rem;"><strong>Step B. Filter by genre</strong><br>We keep all speech types except <span style="font-family:inherit">회의</span> (meeting transcripts). Those 49 transcripts exist only for one president (문재인), so including them would introduce a genre confound: the algorithm could cluster them together simply because they are meetings, not because of their topic content.</p>
    <details class="code-ribbon">
      <summary><span class="ribbon-label">Show code</span><span class="ribbon-tag">R</span></summary>
      <div class="code-ribbon-body"><div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
        <pre><code>corpus <span class="r-operator">&lt;-</span> corpus <span class="r-operator">|&gt;</span> <span class="r-function">filter</span>(kind <span class="r-operator">!=</span> <span class="r-string">"회의"</span>)</code></pre>
      </div></div>
    </details>

    <p style="margin-top:1rem;"><strong>Step C. Tokenize and filter</strong><br>We tokenize each speech with Kiwi, keep only nouns (<code>NNG</code>, <code>NNP</code>), remove stopwords and single-character tokens. Then we drop speeches with fewer than 75 noun tokens &mdash; short documents produce sparse vectors that add noise to the clustering.</p>
    <details class="code-ribbon">
      <summary><span class="ribbon-label">Show code</span><span class="ribbon-tag">R</span></summary>
      <div class="code-ribbon-body"><div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
        <pre><code>tokenize_kiwi <span class="r-operator">&lt;-</span> <span class="r-keyword">function</span>(text) {
  result <span class="r-operator">&lt;-</span> <span class="r-function">tokenize</span>(text, flatten <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>)
  <span class="r-function">tibble</span>(form <span class="r-operator">=</span> result<span class="r-operator">$</span>form, tag <span class="r-operator">=</span> result<span class="r-operator">$</span>tag)
}

tokens <span class="r-operator">&lt;-</span> corpus <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(doc_id <span class="r-operator">=</span> <span class="r-function">row_number</span>(), morphemes <span class="r-operator">=</span> <span class="r-function">map</span>(speech_text, tokenize_kiwi)) <span class="r-operator">|&gt;</span>
  <span class="r-function">unnest</span>(morphemes) <span class="r-operator">|&gt;</span>
  <span class="r-function">filter</span>(tag <span class="r-operator">%in%</span> <span class="r-function">c</span>(<span class="r-string">"NNG"</span>, <span class="r-string">"NNP"</span>), <span class="r-operator">!</span>form <span class="r-operator">%in%</span> stopwords_ko,
         <span class="r-function">str_length</span>(form) <span class="r-operator">&gt;=</span> <span class="r-number">2</span>, <span class="r-operator">!</span><span class="r-function">str_detect</span>(form, <span class="r-string">"^[0-9]+$"</span>)) <span class="r-operator">|&gt;</span>
  <span class="r-function">select</span>(doc_id, president, kind, word <span class="r-operator">=</span> form)

<span class="r-comment"># Drop short speeches</span>
token_counts <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span> <span class="r-function">count</span>(doc_id, name <span class="r-operator">=</span> <span class="r-string">"n_tokens"</span>)
keep_docs <span class="r-operator">&lt;-</span> token_counts <span class="r-operator">|&gt;</span> <span class="r-function">filter</span>(n_tokens <span class="r-operator">&gt;=</span> <span class="r-number">75</span>) <span class="r-operator">|&gt;</span> <span class="r-function">pull</span>(doc_id)
tokens <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span> <span class="r-function">filter</span>(doc_id <span class="r-operator">%in%</span> keep_docs)

<span class="r-comment"># Check per-president counts (intentionally unbalanced)</span>
tokens <span class="r-operator">|&gt;</span> <span class="r-function">distinct</span>(doc_id, president) <span class="r-operator">|&gt;</span> <span class="r-function">count</span>(president)</code></pre>
      </div></div>
    </details>

    <p style="margin-top:1rem;"><strong>Step D. Build TF-IDF matrix</strong><br>We weight word counts with TF-IDF (same technique from Week 4), but first we filter the vocabulary: words must appear in at least 5 speeches (not too rare) and no more than 60% of speeches (not too common &mdash; effectively stopwords). This keeps the feature space focused on words that actually differentiate speeches.</p>
    <details class="code-ribbon">
      <summary><span class="ribbon-label">Show code</span><span class="ribbon-tag">R</span></summary>
      <div class="code-ribbon-body"><div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
        <pre><code>n_docs <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span> <span class="r-function">distinct</span>(doc_id) <span class="r-operator">|&gt;</span> <span class="r-function">nrow</span>()
word_doc_freq <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span>
  <span class="r-function">distinct</span>(doc_id, word) <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(word, name <span class="r-operator">=</span> <span class="r-string">"doc_freq"</span>)

keep_words <span class="r-operator">&lt;-</span> word_doc_freq <span class="r-operator">|&gt;</span>
  <span class="r-function">filter</span>(doc_freq <span class="r-operator">&gt;=</span> <span class="r-number">5</span>, doc_freq <span class="r-operator">&lt;=</span> <span class="r-number">0.6</span> <span class="r-operator">*</span> n_docs) <span class="r-operator">|&gt;</span>
  <span class="r-function">pull</span>(word)

tokens_filtered <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span> <span class="r-function">filter</span>(word <span class="r-operator">%in%</span> keep_words)

tfidf <span class="r-operator">&lt;-</span> tokens_filtered <span class="r-operator">|&gt;</span> <span class="r-function">count</span>(doc_id, word) <span class="r-operator">|&gt;</span> <span class="r-function">bind_tf_idf</span>(word, doc_id, n)
dtm <span class="r-operator">&lt;-</span> tfidf <span class="r-operator">|&gt;</span> <span class="r-function">select</span>(doc_id, word, tf_idf) <span class="r-operator">|&gt;</span>
  <span class="r-function">pivot_wider</span>(names_from <span class="r-operator">=</span> word, values_from <span class="r-operator">=</span> tf_idf, values_fill <span class="r-operator">=</span> <span class="r-number">0</span>)
mat <span class="r-operator">&lt;-</span> dtm <span class="r-operator">|&gt;</span> <span class="r-function">select</span>(<span class="r-operator">-</span>doc_id) <span class="r-operator">|&gt;</span> <span class="r-function">as.matrix</span>()</code></pre>
      </div></div>
    </details>

    <p style="margin-top:1rem;"><strong>Step E. Choose k with silhouette scores</strong><br>We run k-means on the TF-IDF matrix for k = 2 through 8 and compute the average silhouette score for each. The silhouette measures how well each speech fits its assigned cluster vs. the next-best cluster. Higher is better. We pick the k with the highest score. This is the same as selecting k in Orange's k-Means widget.</p>
    <details class="code-ribbon">
      <summary><span class="ribbon-label">Show code</span><span class="ribbon-tag">R</span></summary>
      <div class="code-ribbon-body"><div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
        <pre><code>sil_results <span class="r-operator">&lt;-</span> <span class="r-function">tibble</span>(k <span class="r-operator">=</span> <span class="r-number">2</span>:<span class="r-number">8</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(
    km <span class="r-operator">=</span> <span class="r-function">map</span>(k, <span class="r-operator">~</span> <span class="r-function">kmeans</span>(mat, centers <span class="r-operator">=</span> .x, nstart <span class="r-operator">=</span> <span class="r-number">10</span>)),
    sil <span class="r-operator">=</span> <span class="r-function">map_dbl</span>(km, <span class="r-keyword">function</span>(m) {
      s <span class="r-operator">&lt;-</span> <span class="r-function">silhouette</span>(m<span class="r-operator">$</span>cluster, <span class="r-function">dist</span>(mat))
      <span class="r-function">mean</span>(s[, <span class="r-number">3</span>])
    })
  )

best_k <span class="r-operator">&lt;-</span> sil_results <span class="r-operator">|&gt;</span> <span class="r-function">slice_max</span>(sil) <span class="r-operator">|&gt;</span> <span class="r-function">pull</span>(k)
best_k  <span class="r-comment"># print it</span></code></pre>
      </div></div>
    </details>

    <p style="margin-top:1rem;"><strong>Step F. Run k-means and inspect clusters</strong><br>Now we run k-means one final time with the best k. To understand what each cluster is "about," we re-apply TF-IDF at the cluster level &mdash; treating all speeches in a cluster as one big document &mdash; and extract the top distinctive words.</p>
    <details class="code-ribbon">
      <summary><span class="ribbon-label">Show code</span><span class="ribbon-tag">R</span></summary>
      <div class="code-ribbon-body"><div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
        <pre><code><span class="r-function">set.seed</span>(<span class="r-number">42</span>)
best_km <span class="r-operator">&lt;-</span> <span class="r-function">kmeans</span>(mat, centers <span class="r-operator">=</span> best_k, nstart <span class="r-operator">=</span> <span class="r-number">10</span>)

doc_clusters <span class="r-operator">&lt;-</span> <span class="r-function">tibble</span>(doc_id <span class="r-operator">=</span> dtm<span class="r-operator">$</span>doc_id, cluster <span class="r-operator">=</span> <span class="r-function">as.character</span>(best_km<span class="r-operator">$</span>cluster))

<span class="r-comment"># Top TF-IDF words per cluster</span>
cluster_tfidf <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span>
  <span class="r-function">left_join</span>(doc_clusters, by <span class="r-operator">=</span> <span class="r-string">"doc_id"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(cluster, word) <span class="r-operator">|&gt;</span>
  <span class="r-function">bind_tf_idf</span>(word, cluster, n) <span class="r-operator">|&gt;</span>
  <span class="r-function">group_by</span>(cluster) <span class="r-operator">|&gt;</span>
  <span class="r-function">slice_max</span>(tf_idf, n <span class="r-operator">=</span> <span class="r-number">15</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">ungroup</span>()

<span class="r-comment"># Plot</span>
cluster_tfidf <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(word <span class="r-operator">=</span> <span class="r-function">reorder_within</span>(word, tf_idf, cluster)) <span class="r-operator">|&gt;</span>
  <span class="r-function">ggplot</span>(<span class="r-function">aes</span>(tf_idf, word, fill <span class="r-operator">=</span> cluster)) <span class="r-operator">+</span>
  <span class="r-function">geom_col</span>(show.legend <span class="r-operator">=</span> <span class="r-keyword">FALSE</span>) <span class="r-operator">+</span>
  <span class="r-function">facet_wrap</span>(<span class="r-operator">~</span> cluster, scales <span class="r-operator">=</span> <span class="r-string">"free"</span>) <span class="r-operator">+</span>
  <span class="r-function">scale_y_reordered</span>() <span class="r-operator">+</span>
  <span class="r-function">labs</span>(x <span class="r-operator">=</span> <span class="r-string">"TF-IDF"</span>, y <span class="r-operator">=</span> <span class="r-keyword">NULL</span>) <span class="r-operator">+</span>
  <span class="r-function">theme_minimal</span>()</code></pre>
      </div></div>
    </details>

    <p style="margin-top:1rem;"><strong>Step G. President distribution across clusters</strong><br>Finally, we check whether clusters track presidents or topics. If each president's speeches scatter across multiple clusters, it confirms that topic &mdash; not speaker identity &mdash; drives the grouping.</p>
    <details class="code-ribbon">
      <summary><span class="ribbon-label">Show code</span><span class="ribbon-tag">R</span></summary>
      <div class="code-ribbon-body"><div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
        <pre><code>pres_order <span class="r-operator">&lt;-</span> <span class="r-function">c</span>(<span class="r-string">"노태우"</span>, <span class="r-string">"김영삼"</span>, <span class="r-string">"김대중"</span>, <span class="r-string">"노무현"</span>, <span class="r-string">"이명박"</span>, <span class="r-string">"박근혜"</span>, <span class="r-string">"문재인"</span>)

pres_cluster <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span>
  <span class="r-function">distinct</span>(doc_id, president) <span class="r-operator">|&gt;</span>
  <span class="r-function">left_join</span>(doc_clusters, by <span class="r-operator">=</span> <span class="r-string">"doc_id"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(president, cluster)

pres_cluster <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(president <span class="r-operator">=</span> <span class="r-function">factor</span>(president, levels <span class="r-operator">=</span> pres_order)) <span class="r-operator">|&gt;</span>
  <span class="r-function">ggplot</span>(<span class="r-function">aes</span>(x <span class="r-operator">=</span> president, y <span class="r-operator">=</span> n, fill <span class="r-operator">=</span> cluster)) <span class="r-operator">+</span>
  <span class="r-function">geom_col</span>(position <span class="r-operator">=</span> <span class="r-string">"fill"</span>) <span class="r-operator">+</span>
  <span class="r-function">scale_y_continuous</span>(labels <span class="r-operator">=</span> scales<span class="r-operator">::</span><span class="r-function">percent</span>) <span class="r-operator">+</span>
  <span class="r-function">labs</span>(x <span class="r-operator">=</span> <span class="r-keyword">NULL</span>, y <span class="r-operator">=</span> <span class="r-string">"Share of speeches"</span>, fill <span class="r-operator">=</span> <span class="r-string">"Cluster"</span>) <span class="r-operator">+</span>
  <span class="r-function">theme_minimal</span>() <span class="r-operator">+</span>
  <span class="r-function">theme</span>(axis.text.x <span class="r-operator">=</span> <span class="r-function">element_text</span>(angle <span class="r-operator">=</span> <span class="r-number">45</span>, hjust <span class="r-operator">=</span> <span class="r-number">1</span>))</code></pre>
      </div></div>
    </details>

  </div>
</div>

<script>
(function () {
  "use strict";

  // ── CONSTANTS ─────────────────────────────────────────────────────
  var STEPS = [
    { id: "corpus",  label: "1. The Corpus",       desc: "648 speeches from 7 presidents. Each dot is one speech. Hover to see its title." },
    { id: "choosek", label: "2. Choose k",          desc: "Click a k value to preview that clustering. Higher silhouette = better separation." },
    { id: "animate", label: "3. K-Means in Action", desc: "Watch k-means iterate: assign to nearest centroid, then update centroids. Click Run or Step." },
    { id: "explore", label: "4. Explore Clusters",  desc: "Click a cluster to see its top words and president composition." },
    { id: "insight", label: "5. The Insight",        desc: "Toggle coloring. Notice: presidents spread across all clusters. Topic drives the clustering." },
    { id: "code",    label: "6. Replicate in R",    desc: "The full R code to reproduce this analysis yourself. More advanced \u2014 here if you want it." }
  ];

  var PALETTE = ["#3b82f6","#ef4444","#10b981","#f59e0b","#8b5cf6","#06b6d4","#ec4899","#84cc16"];

  var CLUSTER_LABELS = [
    "Women's Movement & Rural Dev", "Foreign Relations & Unification",
    "State Visits & Diplomacy", "Police & Public Safety",
    "Economy, Industry & Technology", "Security & Veterans",
    "Culture, Diaspora & Events", "Democracy & Human Rights"
  ];

  var PRESIDENT_ORDER = ["\ub178\ud0dc\uc6b0","\uae40\uc601\uc0bc","\uae40\ub300\uc911","\ub178\ubb34\ud604","\uc774\uba85\ubc15","\ubc15\uadfc\ud61c","\ubb38\uc7ac\uc778"];

  var PRESIDENT_COLORS = {};
  var PRES_PAL = ["#a855f7","#f97316","#14b8a6","#f43f5e","#6366f1","#eab308","#22c55e"];
  PRESIDENT_ORDER.forEach(function (p, i) { PRESIDENT_COLORS[p] = PRES_PAL[i]; });

  var DOT_R = 3.5;
  var PAD = 28;

  // ── STATE ─────────────────────────────────────────────────────────
  var DATA = null;
  var currentStep = 0;
  var canvasW = 0, canvasH = 0;

  // Drawing state
  var colorState = "gray";        // gray | kmeans | cluster | president
  var currentAssignments = null;   // per-speech cluster index
  var showCentroids = false;
  var currentCentroids = null;     // [[x,y], ...]
  var highlightCluster = null;     // null or cluster index
  var selectedK = 8;
  var hoveredIdx = -1;

  // Animation state
  var animFrames = [];
  var animFrameIdx = -1;
  var isAutoPlaying = false;
  var animTimers = [];

  // K-means cache
  var kmeansCache = {};

  // Seeded PRNG for reproducible k-selection
  var _seed = 42;
  function seededRandom() {
    _seed |= 0; _seed = _seed + 0x6D2B79F5 | 0;
    var t = Math.imul(_seed ^ _seed >>> 15, 1 | _seed);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  }

  // ── DOM REFS ──────────────────────────────────────────────────────
  var canvas = document.getElementById("scatterCanvas");
  var ctx = canvas.getContext("2d");
  var tooltipEl = document.getElementById("tooltip");
  var stepsEl = document.getElementById("pipelineSteps");
  var prevBtn = document.getElementById("prevBtn");
  var nextBtn = document.getElementById("nextBtn");
  var stepDesc = document.getElementById("stepDesc");
  var detailPanel = document.getElementById("detailPanel");

  // ── CANVAS SETUP ──────────────────────────────────────────────────
  function setupCanvas() {
    var container = document.getElementById("scatterContainer");
    var w = container.clientWidth;
    var h = Math.round(Math.min(w * 0.6, 460));
    var dpr = window.devicePixelRatio || 1;
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    canvas.style.width = w + "px";
    canvas.style.height = h + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    canvasW = w;
    canvasH = h;
  }

  function tx(dataX) { return PAD + dataX * (canvasW - 2 * PAD); }
  function ty(dataY) { return PAD + (1 - dataY) * (canvasH - 2 * PAD); }

  // ── DRAWING ───────────────────────────────────────────────────────
  function draw() {
    ctx.clearRect(0, 0, canvasW, canvasH);
    if (!DATA) return;

    var speeches = DATA.speeches;
    var n = speeches.length;

    // Draw dots
    for (var i = 0; i < n; i++) {
      var s = speeches[i];
      var x = tx(s.x), y = ty(s.y);
      var r = (i === hoveredIdx) ? DOT_R + 2 : DOT_R;
      var color, alpha;

      if (colorState === "gray") {
        color = "#94a3b8"; alpha = 0.5;
      } else if (colorState === "kmeans") {
        var c = currentAssignments ? currentAssignments[i] : 0;
        color = PALETTE[c % PALETTE.length]; alpha = 0.65;
      } else if (colorState === "cluster") {
        color = PALETTE[s.cluster % PALETTE.length];
        alpha = (highlightCluster === null || highlightCluster === s.cluster) ? 0.7 : 0.07;
      } else if (colorState === "president") {
        color = PRESIDENT_COLORS[s.president] || "#94a3b8"; alpha = 0.7;
      } else {
        color = "#94a3b8"; alpha = 0.5;
      }

      if (i === hoveredIdx) alpha = 1;

      ctx.globalAlpha = alpha;
      ctx.fillStyle = color;
      ctx.beginPath();
      ctx.arc(x, y, r, 0, Math.PI * 2);
      ctx.fill();
    }

    ctx.globalAlpha = 1;

    // Draw centroids
    if (showCentroids && currentCentroids) {
      for (var j = 0; j < currentCentroids.length; j++) {
        drawCentroid(tx(currentCentroids[j][0]), ty(currentCentroids[j][1]),
                     PALETTE[j % PALETTE.length]);
      }
    }

    // Hovered dot ring
    if (hoveredIdx >= 0) {
      var hs = speeches[hoveredIdx];
      ctx.beginPath();
      ctx.arc(tx(hs.x), ty(hs.y), DOT_R + 5, 0, Math.PI * 2);
      ctx.strokeStyle = "#1e293b";
      ctx.lineWidth = 1.5;
      ctx.stroke();
    }

    // Watermark
    ctx.globalAlpha = 0.35;
    ctx.fillStyle = "#94a3b8";
    ctx.font = "10px -apple-system, sans-serif";
    ctx.textAlign = "right";
    ctx.fillText("2D projection of TF-IDF vectors", canvasW - PAD, canvasH - 8);
    ctx.globalAlpha = 1;
    ctx.textAlign = "start";
  }

  function drawCentroid(cx, cy, color) {
    var r = 7;
    ctx.beginPath();
    ctx.moveTo(cx, cy - r); ctx.lineTo(cx + r, cy);
    ctx.lineTo(cx, cy + r); ctx.lineTo(cx - r, cy);
    ctx.closePath();
    ctx.fillStyle = color; ctx.fill();
    ctx.strokeStyle = "#fff"; ctx.lineWidth = 2.5; ctx.stroke();
    ctx.strokeStyle = "rgba(0,0,0,0.2)"; ctx.lineWidth = 0.5; ctx.stroke();
  }

  // ── K-MEANS ALGORITHM ─────────────────────────────────────────────
  function runKMeans(points, k, rng) {
    var n = points.length;
    rng = rng || seededRandom;

    // k-means++ init
    var centroids = [points[Math.floor(rng() * n)].slice()];
    for (var c = 1; c < k; c++) {
      var dists = [];
      for (var i = 0; i < n; i++) {
        var minD = Infinity;
        for (var j = 0; j < centroids.length; j++) {
          var dx = points[i][0] - centroids[j][0], dy = points[i][1] - centroids[j][1];
          var d = dx * dx + dy * dy;
          if (d < minD) minD = d;
        }
        dists.push(minD);
      }
      var total = 0;
      for (var i = 0; i < n; i++) total += dists[i];
      var r = rng() * total, cum = 0;
      for (var i = 0; i < n; i++) {
        cum += dists[i];
        if (cum >= r) { centroids.push(points[i].slice()); break; }
      }
    }

    // Iterate
    var assignments = new Array(n);
    for (var iter = 0; iter < 40; iter++) {
      var changed = false;
      for (var i = 0; i < n; i++) {
        var minD = Infinity, best = 0;
        for (var j = 0; j < k; j++) {
          var dx = points[i][0] - centroids[j][0], dy = points[i][1] - centroids[j][1];
          var d = dx * dx + dy * dy;
          if (d < minD) { minD = d; best = j; }
        }
        if (assignments[i] !== best) { assignments[i] = best; changed = true; }
      }
      if (!changed) break;

      for (var j = 0; j < k; j++) {
        var sx = 0, sy = 0, cnt = 0;
        for (var i = 0; i < n; i++) {
          if (assignments[i] === j) { sx += points[i][0]; sy += points[i][1]; cnt++; }
        }
        if (cnt > 0) centroids[j] = [sx / cnt, sy / cnt];
      }
    }
    return { assignments: assignments, centroids: centroids };
  }

  function getKResult(k) {
    if (k === DATA.best_k) {
      return {
        assignments: DATA.speeches.map(function (s) { return s.cluster; }),
        centroids: DATA.centroids_2d.map(function (c) { return c.slice(); })
      };
    }
    if (!kmeansCache[k]) {
      var pts = DATA.speeches.map(function (s) { return [s.x, s.y]; });
      var best = null;
      for (var run = 0; run < 5; run++) {
        var res = runKMeans(pts, k);
        var inertia = 0;
        for (var i = 0; i < pts.length; i++) {
          var c = res.centroids[res.assignments[i]];
          inertia += (pts[i][0] - c[0]) * (pts[i][0] - c[0]) + (pts[i][1] - c[1]) * (pts[i][1] - c[1]);
        }
        if (!best || inertia < best.inertia) best = { result: res, inertia: inertia };
      }
      kmeansCache[k] = best.result;
    }
    return kmeansCache[k];
  }

  // ── ANIMATION (Step 3) ────────────────────────────────────────────
  function buildAnimFrames() {
    var pts = DATA.speeches.map(function (s) { return [s.x, s.y]; });
    var n = pts.length, k = DATA.best_k;

    // Random initial centroids (use Math.random for variety)
    var indices = [];
    while (indices.length < k) {
      var idx = Math.floor(Math.random() * n);
      if (indices.indexOf(idx) === -1) indices.push(idx);
    }
    var centroids = indices.map(function (i) { return pts[i].slice(); });

    var frames = [];
    frames.push({ type: "init", centroids: centroids.map(function (c) { return c.slice(); }), assignments: null, label: "Placed " + k + " random centroids" });

    for (var iter = 0; iter < 5; iter++) {
      // Assign
      var assignments = [];
      for (var i = 0; i < n; i++) {
        var minD = Infinity, best = 0;
        for (var j = 0; j < k; j++) {
          var dx = pts[i][0] - centroids[j][0], dy = pts[i][1] - centroids[j][1];
          if (dx * dx + dy * dy < minD) { minD = dx * dx + dy * dy; best = j; }
        }
        assignments.push(best);
      }
      frames.push({ type: "assign", centroids: centroids.map(function (c) { return c.slice(); }), assignments: assignments.slice(), label: "Iteration " + (iter + 1) + ": assigned to nearest centroid" });

      // Update
      var newC = [];
      for (var j = 0; j < k; j++) {
        var sx = 0, sy = 0, cnt = 0;
        for (var i = 0; i < n; i++) {
          if (assignments[i] === j) { sx += pts[i][0]; sy += pts[i][1]; cnt++; }
        }
        newC.push(cnt > 0 ? [sx / cnt, sy / cnt] : centroids[j].slice());
      }
      centroids = newC;
      frames.push({ type: "update", centroids: centroids.map(function (c) { return c.slice(); }), assignments: assignments.slice(), label: "Iteration " + (iter + 1) + ": moved centroids to cluster centers" });
    }

    // Final: snap to actual
    frames.push({
      type: "final",
      centroids: DATA.centroids_2d.map(function (c) { return c.slice(); }),
      assignments: DATA.speeches.map(function (s) { return s.cluster; }),
      label: "Converged! Final k=" + k + " clustering"
    });

    return frames;
  }

  function scheduleNext(ms) {
    animTimers.push(setTimeout(function () { if (isAutoPlaying) playNextFrame(); }, ms));
  }

  function clearAnimTimers() {
    animTimers.forEach(function (t) { clearTimeout(t); });
    animTimers = [];
  }

  function playNextFrame() {
    if (!isAutoPlaying) return;
    animFrameIdx++;
    if (animFrameIdx >= animFrames.length) { isAutoPlaying = false; updateAnimUI(); return; }

    var frame = animFrames[animFrameIdx];
    var prev = animFrameIdx > 0 ? animFrames[animFrameIdx - 1] : null;

    if (frame.type === "init") {
      showCentroids = true;
      currentCentroids = frame.centroids.map(function (c) { return c.slice(); });
      currentAssignments = null;
      colorState = "gray";
      draw();
      updateAnimUI();
      if (isAutoPlaying) scheduleNext(1000);
    } else if (frame.type === "assign") {
      currentAssignments = frame.assignments;
      colorState = "kmeans";
      draw();
      updateAnimUI();
      if (isAutoPlaying) scheduleNext(900);
    } else if (frame.type === "update") {
      var from = prev ? prev.centroids : frame.centroids;
      var to = frame.centroids;
      animateCentroids(from, to, 600, function () {
        updateAnimUI();
        if (isAutoPlaying) scheduleNext(400);
      });
    } else if (frame.type === "final") {
      var from2 = currentCentroids ? currentCentroids.map(function (c) { return c.slice(); }) : frame.centroids;
      currentAssignments = frame.assignments;
      colorState = "kmeans";
      animateCentroids(from2, frame.centroids, 700, function () {
        isAutoPlaying = false;
        updateAnimUI();
      });
    }
  }

  function animateCentroids(from, to, duration, callback) {
    var start = performance.now();
    function tick(now) {
      var t = Math.min(1, (now - start) / duration);
      t = t * t * (3 - 2 * t); // smoothstep
      if (!currentCentroids) currentCentroids = from.map(function (c) { return c.slice(); });
      for (var i = 0; i < from.length; i++) {
        currentCentroids[i] = [
          from[i][0] + (to[i][0] - from[i][0]) * t,
          from[i][1] + (to[i][1] - from[i][1]) * t
        ];
      }
      draw();
      if (t < 1) requestAnimationFrame(tick);
      else callback();
    }
    requestAnimationFrame(tick);
  }

  function startAutoPlay() {
    if (isAutoPlaying) return;
    animFrames = buildAnimFrames();
    animFrameIdx = -1;
    isAutoPlaying = true;
    playNextFrame();
  }

  function stepForward() {
    if (isAutoPlaying) return;
    if (animFrameIdx < 0 || animFrames.length === 0) animFrames = buildAnimFrames();
    if (animFrameIdx >= animFrames.length - 1) return;
    // For step-by-step, skip centroid animation and snap
    animFrameIdx++;
    var frame = animFrames[animFrameIdx];
    showCentroids = true;
    currentCentroids = frame.centroids.map(function (c) { return c.slice(); });
    if (frame.assignments) { currentAssignments = frame.assignments; colorState = "kmeans"; }
    else { currentAssignments = null; colorState = "gray"; }
    draw();
    updateAnimUI();
  }

  function resetAnim() {
    isAutoPlaying = false;
    clearAnimTimers();
    animFrames = [];
    animFrameIdx = -1;
    showCentroids = false;
    currentCentroids = null;
    currentAssignments = null;
    colorState = "gray";
    draw();
    updateAnimUI();
  }

  function updateAnimUI() {
    var statusEl = document.getElementById("animStatus");
    var runBtn = document.getElementById("animRunBtn");
    var stepBtn = document.getElementById("animStepBtn");
    if (!statusEl) return;

    if (animFrameIdx >= 0 && animFrameIdx < animFrames.length) {
      statusEl.textContent = animFrames[animFrameIdx].label;
    } else {
      statusEl.textContent = "Click Run to watch the full animation, or Step to advance one phase at a time.";
    }
    if (runBtn) runBtn.disabled = isAutoPlaying;
    if (stepBtn) stepBtn.disabled = isAutoPlaying;
  }

  // ── PRECOMPUTE ────────────────────────────────────────────────────
  function precomputeAllK() {
    var pts = DATA.speeches.map(function (s) { return [s.x, s.y]; });
    for (var k = 2; k <= 8; k++) {
      if (k === DATA.best_k) {
        kmeansCache[k] = {
          assignments: DATA.speeches.map(function (s) { return s.cluster; }),
          centroids: DATA.centroids_2d.map(function (c) { return c.slice(); })
        };
      } else {
        var best = null;
        for (var run = 0; run < 5; run++) {
          var res = runKMeans(pts, k);
          var inertia = 0;
          for (var i = 0; i < pts.length; i++) {
            var c = res.centroids[res.assignments[i]];
            inertia += (pts[i][0] - c[0]) * (pts[i][0] - c[0]) + (pts[i][1] - c[1]) * (pts[i][1] - c[1]);
          }
          if (!best || inertia < best.inertia) best = { result: res, inertia: inertia };
        }
        kmeansCache[k] = best.result;
      }
    }
  }

  // ── STEP MANAGEMENT ───────────────────────────────────────────────
  function goToStep(n) {
    if (n < 0 || n >= STEPS.length) return;
    isAutoPlaying = false;
    clearAnimTimers();
    currentStep = n;
    highlightCluster = null;
    hoveredIdx = -1;
    tooltipEl.style.display = "none";

    switch (STEPS[n].id) {
      case "corpus":
        colorState = "gray"; showCentroids = false;
        currentCentroids = null; currentAssignments = null;
        break;
      case "choosek":
        selectedK = DATA.best_k;
        var res = getKResult(selectedK);
        currentAssignments = res.assignments;
        currentCentroids = res.centroids;
        colorState = "kmeans"; showCentroids = true;
        break;
      case "animate":
        colorState = "gray"; showCentroids = false;
        currentCentroids = null; currentAssignments = null;
        animFrames = []; animFrameIdx = -1; isAutoPlaying = false;
        break;
      case "explore":
        colorState = "cluster"; showCentroids = false;
        currentAssignments = null; currentCentroids = null;
        break;
      case "insight":
        colorState = "cluster"; showCentroids = false;
        currentAssignments = null; currentCentroids = null;
        break;
      case "code":
        colorState = "cluster"; showCentroids = false;
        currentAssignments = null; currentCentroids = null;
        break;
    }

    draw();
    renderDetail();
    updateStepBtns();
    updateNav();
  }

  function renderDetail() {
    var id = STEPS[currentStep].id;
    if (id === "corpus") renderCorpus();
    else if (id === "choosek") renderChooseK();
    else if (id === "animate") renderAnimate();
    else if (id === "explore") renderExplore();
    else if (id === "insight") renderInsight();
    else if (id === "code") renderCode();
  }

  function updateStepBtns() {
    var btns = stepsEl.querySelectorAll(".step-btn");
    btns.forEach(function (btn, i) {
      btn.classList.remove("active", "completed");
      if (i === currentStep) btn.classList.add("active");
      else if (i < currentStep) btn.classList.add("completed");
    });
  }

  function updateNav() {
    prevBtn.disabled = (currentStep === 0);
    nextBtn.disabled = (currentStep === STEPS.length - 1);
    stepDesc.textContent = STEPS[currentStep].desc;
  }

  // ── STEP 1: CORPUS ────────────────────────────────────────────────
  function renderCorpus() {
    var counts = {};
    DATA.speeches.forEach(function (s) { counts[s.president] = (counts[s.president] || 0) + 1; });

    var html = '<div class="step-info">';
    html += '<p>Each dot represents one of <strong>648 presidential speeches</strong> from the democratic era. The only exclusion is 회의 (meeting transcripts), which exist for only one president and would introduce a genre confound. Speeches with fewer than 75 noun tokens are also removed. Right now they are all gray because we have not clustered them yet. The goal: see if k-means can find meaningful groups.</p>';
    html += '<div style="display:flex;flex-wrap:wrap;gap:0.4rem;margin-top:0.5rem;">';
    PRESIDENT_ORDER.forEach(function (p) {
      if (counts[p]) {
        html += '<span style="background:#f1f5f9;padding:0.3rem 0.6rem;border-radius:4px;font-size:0.82rem;color:#374151;">';
        html += '<strong>' + esc(p) + '</strong> ' + counts[p];
        html += '</span>';
      }
    });
    html += '</div></div>';
    detailPanel.innerHTML = html;
  }

  // ── STEP 2: CHOOSE K ──────────────────────────────────────────────
  function renderChooseK() {
    var items = DATA.silhouette_comparison;
    var maxSil = Math.max.apply(null, items.map(function (d) { return d.silhouette; }));

    var html = '<div class="step-info">';
    html += '<p>K-means requires you to choose <em>k</em> (the number of clusters) in advance. The <strong>silhouette score</strong> compares options. Click each bar to see its clustering.</p>';

    // Silhouette chart
    html += '<div class="sil-chart-row">';
    items.forEach(function (d) {
      var isBest = d.k === DATA.best_k;
      var isSel = d.k === selectedK;
      var pct = (d.silhouette / maxSil) * 130;
      var color = isSel ? PALETTE[0] : (isBest ? "#059669" : "#cbd5e1");

      html += '<div class="sil-bar-group' + (isSel ? ' selected' : '') + '" data-k="' + d.k + '">';
      html += '<div class="sil-bar-value">' + d.silhouette.toFixed(4) + '</div>';
      html += '<div class="sil-bar" style="height:' + pct + 'px;background:' + color + ';';
      if (isSel) html += 'outline:2px solid ' + PALETTE[0] + ';outline-offset:2px;';
      html += '"></div>';
      html += '<div class="sil-bar-label">k=' + d.k + '</div>';
      if (isBest) html += '<div class="sil-best-tag">best</div>';
      html += '</div>';
    });
    html += '</div>';

    html += '<div class="callout callout-info" style="margin-top:0.5rem;"><strong>Low scores are common for text.</strong> These silhouette scores (~0.01&ndash;0.02) reflect the high-dimensional, sparse nature of TF-IDF vectors. Cluster boundaries are fuzzy, but what matters is the <em>relative</em> comparison across k values and whether the resulting clusters are interpretable.</div>';
    html += '</div>';

    detailPanel.innerHTML = html;
  }

  function selectK(k) {
    selectedK = k;
    var res = getKResult(k);
    currentAssignments = res.assignments;
    currentCentroids = res.centroids;
    colorState = "kmeans";
    showCentroids = true;
    draw();
    renderChooseK();
  }

  // ── STEP 3: ANIMATE ───────────────────────────────────────────────
  function renderAnimate() {
    var html = '<div class="step-info">';
    html += '<p>The k-means algorithm: <strong>(1)</strong> place <em>k</em> centroids at random, <strong>(2)</strong> assign each speech to its nearest centroid, <strong>(3)</strong> move centroids to the center of their cluster, <strong>(4)</strong> repeat until stable.</p>';
    html += '<div class="anim-controls">';
    html += '<button class="btn btn-primary btn-sm" id="animRunBtn">Run</button>';
    html += '<button class="btn btn-sm" id="animStepBtn">Step</button>';
    html += '<button class="btn btn-sm" id="animResetBtn">Reset</button>';
    html += '</div>';
    html += '<div class="anim-status" id="animStatus">Click Run to watch the full animation, or Step to advance one phase at a time.</div>';
    html += '<div class="callout callout-tip" style="margin-top:0.5rem;">The diamond markers are centroids. Click <strong>Reset + Run</strong> again to see a different random start. K-means may converge to slightly different results each time.</div>';
    html += '</div>';

    detailPanel.innerHTML = html;
    updateAnimUI();
  }

  // ── STEP 4: EXPLORE ───────────────────────────────────────────────
  function renderExplore() {
    var html = '<div class="step-info">';

    // Cluster legend
    html += '<div class="cluster-legend-row">';
    for (var c = 0; c < DATA.best_k; c++) {
      var active = highlightCluster === c ? ' active' : '';
      html += '<button class="cluster-legend-btn' + active + '" data-cluster="' + c + '" style="color:' + PALETTE[c] + ';border-color:' + (highlightCluster === c ? PALETTE[c] : '#e2e8f0') + ';">';
      html += '<span class="cluster-legend-dot" style="background:' + PALETTE[c] + ';"></span>';
      html += (c + 1) + '. ' + CLUSTER_LABELS[c];
      html += '</button>';
    }
    html += '</div>';

    // Detail card for selected cluster
    if (highlightCluster !== null) {
      html += buildClusterCard(highlightCluster);
    } else {
      html += '<p style="color:#6b7280;font-style:italic;font-size:0.88rem;">Click a cluster above (or click a dot on the scatter plot) to see its details.</p>';
    }

    html += '</div>';
    detailPanel.innerHTML = html;
  }

  function buildClusterCard(c) {
    var color = PALETTE[c % PALETTE.length];
    var words = DATA.cluster_words[String(c)];
    var presDist = DATA.cluster_president_dist[String(c)];
    var total = 0;
    PRESIDENT_ORDER.forEach(function (p) { total += (presDist[p] || 0); });

    var html = '<div class="cluster-detail">';
    html += '<div class="cluster-detail-header" style="background:' + color + ';">Cluster ' + (c + 1) + ': ' + CLUSTER_LABELS[c] + ' (' + total + ' speeches)</div>';
    html += '<div class="cluster-detail-body">';

    // Top words
    html += '<div class="cluster-card-section">';
    html += '<div class="cluster-card-section-title">Top Words (by TF-IDF)</div>';
    html += '<div style="line-height:1.5;">';
    var maxTf = words[0].tfidf;
    words.slice(0, 15).forEach(function (w) {
      var ratio = w.tfidf / maxTf;
      html += '<span class="wc-word" style="font-size:' + (0.7 + ratio * 1.0) + 'rem;color:' + color + ';opacity:' + (0.5 + ratio * 0.5) + ';" title="' + esc(w.word) + ': ' + w.tfidf.toFixed(4) + '">' + esc(w.word) + '</span> ';
    });
    html += '</div></div>';

    // President distribution
    html += '<div class="cluster-card-section">';
    html += '<div class="cluster-card-section-title">President Distribution</div>';
    PRESIDENT_ORDER.forEach(function (p) {
      var count = presDist[p] || 0;
      var pct = total > 0 ? (count / total) * 100 : 0;
      html += '<div class="mini-bar-row">';
      html += '<div class="mini-bar-label">' + esc(p) + '</div>';
      html += '<div class="mini-bar-track"><div class="mini-bar-fill" style="width:' + pct + '%;background:' + color + ';"></div></div>';
      html += '<div class="mini-bar-count">' + count + '</div>';
      html += '</div>';
    });
    html += '</div>';

    html += '</div></div>';
    return html;
  }

  function toggleClusterHighlight(c) {
    highlightCluster = (highlightCluster === c) ? null : c;
    draw();
    renderExplore();
  }

  // ── STEP 5: INSIGHT ───────────────────────────────────────────────
  function renderInsight() {
    var mode = colorState === "president" ? "president" : "cluster";
    var html = '<div class="step-info">';

    // Toggle
    html += '<div class="color-toggle">';
    html += '<button data-colormode="cluster"' + (mode === "cluster" ? ' class="active"' : '') + '>By Cluster</button>';
    html += '<button data-colormode="president"' + (mode === "president" ? ' class="active"' : '') + '>By President</button>';
    html += '</div>';

    // Legend
    html += '<div class="color-legend">';
    if (mode === "cluster") {
      for (var c = 0; c < DATA.best_k; c++) {
        html += '<span class="color-legend-item"><span class="color-legend-dot" style="background:' + PALETTE[c] + ';"></span>' + (c + 1) + '. ' + CLUSTER_LABELS[c] + '</span>';
      }
    } else {
      PRESIDENT_ORDER.forEach(function (p) {
        html += '<span class="color-legend-item"><span class="color-legend-dot" style="background:' + PRESIDENT_COLORS[p] + ';"></span>' + esc(p) + '</span>';
      });
    }
    html += '</div>';

    if (mode === "cluster") {
      html += '<p><strong>By cluster:</strong> dots are colored by the thematic cluster k-means assigned them to. The spatial grouping is clear because each cluster has its own topic vocabulary.</p>';
    } else {
      html += '<p><strong>By president:</strong> now each dot shows <em>who</em> gave that speech. Notice how every spatial cluster contains dots of many colors. <strong>K-means grouped speeches by topic, not by speaker.</strong> Presidents give many types of speeches, so their dots scatter across all clusters.</p>';
    }

    html += '<div class="callout callout-info"><strong>Key takeaway:</strong> clustering finds the dominant source of variation. In this corpus, the biggest vocabulary differences are between speech <em>types</em> (diplomatic welcome vs. economic policy), not between presidents. Hierarchical clustering on textbooks found <em>era-based</em> structure because each textbook reflects one era. The method is the same; what it finds depends on the data.</div>';
    html += '</div>';

    detailPanel.innerHTML = html;
  }

  function renderCode() {
    var codeHTML = document.getElementById("rCodeContent").innerHTML;
    var html = '<div class="step-info">';
    html += '<p style="margin-bottom:0.75rem;">This section is <strong>more advanced</strong> and completely optional. It walks through the full analysis in R, step by step. Click each ribbon to see the code, then copy and run it in RStudio. Each step builds on the previous one.</p>';
    html += codeHTML;
    html += '</div>';
    detailPanel.innerHTML = html;
  }

  function setColorMode(mode) {
    colorState = mode;
    draw();
    renderInsight();
  }

  // ── HOVER / TOOLTIP ───────────────────────────────────────────────
  function handleHover(mx, my) {
    if (!DATA) return;
    var nearest = -1, nearestD = Infinity;
    for (var i = 0; i < DATA.speeches.length; i++) {
      var s = DATA.speeches[i];
      var dx = mx - tx(s.x), dy = my - ty(s.y);
      var d = dx * dx + dy * dy;
      if (d < nearestD) { nearestD = d; nearest = i; }
    }

    if (nearestD < 225 && nearest >= 0) {
      hoveredIdx = nearest;
      var s = DATA.speeches[nearest];
      var px = tx(s.x), py = ty(s.y);
      var left = px + 14, top = py - 10;
      if (left + 220 > canvasW) left = px - 220;
      if (top < 0) top = py + 20;
      tooltipEl.style.display = "block";
      tooltipEl.style.left = left + "px";
      tooltipEl.style.top = top + "px";
      tooltipEl.innerHTML = "<strong>" + esc(s.title) + "</strong><br>" +
        esc(s.president) + " &middot; " + CLUSTER_LABELS[s.cluster];
    } else {
      hoveredIdx = -1;
      tooltipEl.style.display = "none";
    }
    draw();
  }

  // ── EVENT DELEGATION ──────────────────────────────────────────────
  detailPanel.addEventListener("click", function (e) {
    // K-value selection
    var kEl = e.target.closest("[data-k]");
    if (kEl && STEPS[currentStep].id === "choosek") {
      selectK(parseInt(kEl.dataset.k));
      return;
    }
    // Cluster selection
    var clEl = e.target.closest("[data-cluster]");
    if (clEl && STEPS[currentStep].id === "explore") {
      toggleClusterHighlight(parseInt(clEl.dataset.cluster));
      return;
    }
    // Color mode toggle
    var togEl = e.target.closest("[data-colormode]");
    if (togEl && STEPS[currentStep].id === "insight") {
      setColorMode(togEl.dataset.colormode);
      return;
    }
    // Animation controls
    if (e.target.id === "animRunBtn") startAutoPlay();
    if (e.target.id === "animStepBtn") stepForward();
    if (e.target.id === "animResetBtn") resetAnim();
  });

  canvas.addEventListener("mousemove", function (e) {
    var r = canvas.getBoundingClientRect();
    handleHover(e.clientX - r.left, e.clientY - r.top);
  });

  canvas.addEventListener("mouseleave", function () {
    hoveredIdx = -1;
    tooltipEl.style.display = "none";
    draw();
  });

  canvas.addEventListener("click", function () {
    if (STEPS[currentStep].id === "explore" && hoveredIdx >= 0) {
      toggleClusterHighlight(DATA.speeches[hoveredIdx].cluster);
    }
  });

  // Touch support
  canvas.addEventListener("touchstart", function (e) {
    e.preventDefault();
    var t = e.touches[0], r = canvas.getBoundingClientRect();
    handleHover(t.clientX - r.left, t.clientY - r.top);
  }, { passive: false });

  canvas.addEventListener("touchmove", function (e) {
    e.preventDefault();
    var t = e.touches[0], r = canvas.getBoundingClientRect();
    handleHover(t.clientX - r.left, t.clientY - r.top);
  }, { passive: false });

  canvas.addEventListener("touchend", function () {
    if (STEPS[currentStep].id === "explore" && hoveredIdx >= 0) {
      toggleClusterHighlight(DATA.speeches[hoveredIdx].cluster);
    }
    hoveredIdx = -1;
    tooltipEl.style.display = "none";
    draw();
  });

  prevBtn.addEventListener("click", function () { goToStep(currentStep - 1); });
  nextBtn.addEventListener("click", function () { goToStep(currentStep + 1); });

  document.addEventListener("keydown", function (e) {
    if (e.target.tagName === "INPUT" || e.target.tagName === "SELECT" || e.target.tagName === "TEXTAREA") return;
    if (e.key === "ArrowRight" || e.key === "l") goToStep(currentStep + 1);
    if (e.key === "ArrowLeft" || e.key === "h") goToStep(currentStep - 1);
    if (e.key === " " && STEPS[currentStep].id === "animate") { e.preventDefault(); startAutoPlay(); }
    if (e.key === "r" && STEPS[currentStep].id === "animate") resetAnim();
  });

  var resizeTimer;
  window.addEventListener("resize", function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () { setupCanvas(); draw(); }, 100);
  });

  // ── HELPERS ───────────────────────────────────────────────────────
  function esc(s) {
    var d = document.createElement("div");
    d.appendChild(document.createTextNode(s));
    return d.innerHTML;
  }

  window.copyCode = function (btn) {
    var pre = btn.closest(".code-block").querySelector("pre code");
    navigator.clipboard.writeText(pre.textContent).then(function () {
      btn.textContent = "Copied!";
      btn.classList.add("copied");
      setTimeout(function () { btn.textContent = "Copy"; btn.classList.remove("copied"); }, 2000);
    });
  };

  // ── BUILD STEP BUTTONS ────────────────────────────────────────────
  function buildStepButtons() {
    stepsEl.innerHTML = "";
    STEPS.forEach(function (s, i) {
      var btn = document.createElement("button");
      btn.className = "step-btn";
      btn.textContent = s.label;
      btn.addEventListener("click", function () { goToStep(i); });
      stepsEl.appendChild(btn);
    });
  }

  // ── INIT ──────────────────────────────────────────────────────────
  function init() {
    buildStepButtons();
    setupCanvas();
    goToStep(0);
  }

  fetch("{{ '/interactive/kmeans_data.json' | relative_url }}")
    .then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    })
    .then(function (json) {
      DATA = json;
      try { init(); }
      catch (e) {
        detailPanel.innerHTML = '<p style="color:#ef4444;">Init error: ' + e.message + '</p>';
        console.error("Init error:", e);
      }
    })
    .catch(function (err) {
      detailPanel.innerHTML = '<p style="color:#ef4444;">Failed to load data: ' + err.message + '. Try refreshing.</p>';
      console.error("Fetch error:", err);
    });
})();
</script>
