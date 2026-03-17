---
layout: default
title: "K-Means Clustering: Presidential Speeches"
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

.tutorial-meta span { display: inline-flex; align-items: center; gap: 0.3rem; }

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
  width: 28px; height: 28px;
  border-radius: 50%;
  background: var(--leiden-blue);
  color: #fff;
  font-size: 0.82rem;
  font-weight: 700;
  flex-shrink: 0;
}

.section-heading h2 { font-size: 1.25rem; color: var(--leiden-blue); margin: 0; }

/* ── Narrative ───────────────────────────────────────────────────── */
.narrative { font-size: 0.95rem; line-height: 1.7; color: #374151; margin: 1rem 0; }
.narrative strong { color: var(--leiden-blue); }

.callout { padding: 0.75rem 1rem; border-radius: 6px; margin: 1rem 0; font-size: 0.88rem; line-height: 1.6; }
.callout-info { background: #eff6ff; border-left: 3px solid #3b82f6; color: #1e40af; }
.callout-tip { background: #f0fdf4; border-left: 3px solid #22c55e; color: #166534; }

/* ── Output panels ───────────────────────────────────────────────── */
.output-panel { border: 1px solid #e2e8f0; border-radius: 8px; margin: 1.25rem 0; overflow: hidden; }
.output-panel-header { padding: 0.4rem 0.75rem; background: #fafafa; border-bottom: 1px solid #e2e8f0; font-size: 0.75rem; color: #64748b; font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em; }
.output-panel-body { padding: 1.25rem; background: #fff; }

/* ── Code ribbon ─────────────────────────────────────────────────── */
.code-ribbon { margin: 1rem 0; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; }
.code-ribbon summary { display: flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; background: linear-gradient(to right, #1e293b, #334155); color: #e2e8f0; font-size: 0.82rem; font-weight: 600; cursor: pointer; user-select: none; list-style: none; transition: background 0.2s; }
.code-ribbon summary::-webkit-details-marker { display: none; }
.code-ribbon summary::before { content: "\25B6"; font-size: 0.65rem; transition: transform 0.2s; flex-shrink: 0; }
.code-ribbon[open] summary::before { transform: rotate(90deg); }
.code-ribbon summary:hover { background: linear-gradient(to right, #0f172a, #1e293b); }
.code-ribbon summary .ribbon-label { flex: 1; }
.code-ribbon summary .ribbon-tag { padding: 0.12rem 0.45rem; border-radius: 4px; font-size: 0.68rem; font-weight: 700; background: rgba(255,255,255,0.12); color: #94a3b8; text-transform: uppercase; letter-spacing: 0.04em; }
.code-ribbon .code-ribbon-body { border-top: 1px solid #334155; }
.code-ribbon .code-block { margin: 0; border: none; border-radius: 0; }
.code-ribbon .callout { margin: 0; border-radius: 0; border-left-width: 3px; }

/* ── Code blocks ─────────────────────────────────────────────────── */
.code-block { position: relative; margin: 1rem 0; border-radius: 8px; overflow: hidden; border: 1px solid #e2e8f0; }
.code-block-header { display: flex; align-items: center; justify-content: space-between; padding: 0.4rem 0.75rem; background: #f1f5f9; border-bottom: 1px solid #e2e8f0; font-size: 0.75rem; color: #64748b; font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em; }
.copy-btn { padding: 0.2rem 0.5rem; border: 1px solid #cbd5e1; border-radius: 4px; background: #fff; font-size: 0.72rem; color: #64748b; cursor: pointer; font-family: inherit; transition: all 0.15s; }
.copy-btn:hover { background: #f8fafc; border-color: var(--leiden-blue); color: var(--leiden-blue); }
.copy-btn.copied { background: #ecfdf5; border-color: #6ee7b7; color: #059669; }
.code-block pre { margin: 0; padding: 1rem; background: #1e293b; color: #e2e8f0; font-size: 0.82rem; line-height: 1.55; overflow-x: auto; font-family: "SFMono-Regular", "Consolas", "Liberation Mono", monospace; }
.code-block pre code { background: none; color: inherit; padding: 0; font-size: inherit; }
.code-block .r-comment { color: #94a3b8; font-style: italic; }
.code-block .r-string { color: #86efac; }
.code-block .r-function { color: #93c5fd; }
.code-block .r-keyword { color: #c4b5fd; }
.code-block .r-number { color: #fde68a; }
.code-block .r-operator { color: #f9a8d4; }

/* ── Silhouette bar chart ────────────────────────────────────────── */
.sil-chart { display: flex; align-items: flex-end; gap: 0.5rem; justify-content: center; height: 180px; padding: 0.5rem 0; }
.sil-bar-wrap { display: flex; flex-direction: column; align-items: center; gap: 0.25rem; }
.sil-bar { width: 48px; border-radius: 4px 4px 0 0; transition: height 0.6s ease; position: relative; }
.sil-bar-label { font-size: 0.72rem; font-weight: 700; color: #64748b; }
.sil-bar-value { font-size: 0.68rem; font-weight: 600; color: #374151; margin-top: 0.15rem; }
.sil-bar.best { outline: 2px solid #059669; outline-offset: 1px; }
.sil-best-tag { font-size: 0.65rem; font-weight: 700; color: #059669; text-transform: uppercase; }

/* ── Cluster cards ───────────────────────────────────────────────── */
.cluster-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1rem; margin: 1rem 0; }
.cluster-card { border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; }
.cluster-card-header { padding: 0.6rem 1rem; font-weight: 700; font-size: 0.85rem; color: #fff; }
.cluster-card-body { padding: 0.75rem 1rem; }
.cluster-card-section { margin-bottom: 0.6rem; }
.cluster-card-section-title { font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; color: #9ca3af; margin-bottom: 0.25rem; }

/* ── Word cloud ──────────────────────────────────────────────────── */
.wc-word { display: inline-block; cursor: default; font-weight: 600; transition: opacity 0.15s; }
.wc-word:hover { opacity: 0.7; }

/* ── Mini bar ────────────────────────────────────────────────────── */
.mini-bar-row { display: flex; align-items: center; gap: 0.4rem; margin-bottom: 0.2rem; }
.mini-bar-label { width: 50px; font-size: 0.75rem; text-align: right; color: #374151; flex-shrink: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.mini-bar-track { flex: 1; height: 14px; background: #f1f5f9; border-radius: 3px; overflow: hidden; }
.mini-bar-fill { height: 100%; border-radius: 3px; }
.mini-bar-count { font-size: 0.68rem; color: #6b7280; width: 28px; text-align: right; flex-shrink: 0; }

/* ── Chart legend ────────────────────────────────────────────────── */
.chart-legend { display: flex; justify-content: center; gap: 1.5rem; margin: 0.75rem 0 0.5rem; font-size: 0.8rem; flex-wrap: wrap; }
.chart-legend-item { display: inline-flex; align-items: center; gap: 0.35rem; color: #4b5563; }
.chart-legend-dot { width: 10px; height: 10px; border-radius: 50%; }

/* ── Responsive ──────────────────────────────────────────────────── */
@media (max-width: 768px) { .cluster-grid { grid-template-columns: 1fr; } }
</style>

<div class="tutorial-page">

<div class="tutorial-header">
  <h1>K-Means Clustering: Presidential Speeches</h1>
  <p class="tutorial-subtitle">Letting silhouette scores choose <em>k</em>, then interpreting what the clusters found</p>
  <div class="tutorial-meta">
    <span>Week 7</span>
    <span>R + tidyverse + tidytext</span>
    <span>Democratic-Era Presidential Speeches (749 speeches, 7 presidents)</span>
  </div>
</div>

<p class="narrative">
  In the hierarchical clustering demo we let the dendrogram reveal structure. K-means works differently: you must choose <em>k</em> (the number of clusters) in advance. But how? We let the <strong>silhouette score</strong> guide us &mdash; the same approach you use in Orange's K-Means widget. We run k-means for k=2 through k=8, compare scores, and then explore what the best clustering found.
</p>

<p class="narrative">
  The corpus is the 749 democratic-era presidential speeches you have been using since Week 2 &mdash; speeches from 7 presidents (Roh Tae-woo through Moon Jae-in). The question: <strong>does k-means group speeches by president, or by something else?</strong>
</p>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">1</span>
  <h2>Choosing <em>k</em>: Silhouette Scores</h2>
</div>

<p class="narrative">
  Orange's K-Means widget does exactly this: it runs k-means for every value in a range (default 2&ndash;8), computes the <strong>average silhouette score</strong> for each, and highlights the best one. A higher silhouette score means documents fit their assigned cluster well and are far from neighboring clusters. Here are the results for our presidential speeches:
</p>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: run k-means for k=2..8 and compare silhouette scores</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── Packages ──────────────────────────────────────────────────────</span>
<span class="r-function">library</span>(tidyverse)
<span class="r-function">library</span>(tidytext)
<span class="r-function">library</span>(elbird)
<span class="r-function">library</span>(cluster)     <span class="r-comment"># for silhouette()</span>

<span class="r-comment"># ── Load and preprocess ───────────────────────────────────────────</span>
corpus <span class="r-operator">&lt;-</span> <span class="r-function">read_csv</span>(<span class="r-string">"data/president_speeches/president_speeches_democratic_era.csv"</span>)
stopwords_ko <span class="r-operator">&lt;-</span> <span class="r-function">read_lines</span>(<span class="r-string">"data/stopwords_ko.txt"</span>) <span class="r-operator">|&gt;</span> <span class="r-function">str_trim</span>() <span class="r-operator">|&gt;</span> <span class="r-function">discard</span>(<span class="r-operator">~</span> .x <span class="r-operator">==</span> <span class="r-string">""</span>)

<span class="r-comment"># Tokenize (same Kiwi pipeline as before)</span>
tokenize_kiwi <span class="r-operator">&lt;-</span> <span class="r-keyword">function</span>(text) {
  result <span class="r-operator">&lt;-</span> <span class="r-function">tokenize</span>(text, flatten <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>)
  <span class="r-function">tibble</span>(form <span class="r-operator">=</span> result<span class="r-operator">$</span>form, tag <span class="r-operator">=</span> result<span class="r-operator">$</span>tag)
}

tokens <span class="r-operator">&lt;-</span> corpus <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(doc_id <span class="r-operator">=</span> <span class="r-function">row_number</span>(), morphemes <span class="r-operator">=</span> <span class="r-function">map</span>(speech_text, tokenize_kiwi)) <span class="r-operator">|&gt;</span>
  <span class="r-function">unnest</span>(morphemes) <span class="r-operator">|&gt;</span>
  <span class="r-function">filter</span>(tag <span class="r-operator">%in%</span> <span class="r-function">c</span>(<span class="r-string">"NNG"</span>, <span class="r-string">"NNP"</span>), <span class="r-operator">!</span>form <span class="r-operator">%in%</span> stopwords_ko,
         <span class="r-function">str_length</span>(form) <span class="r-operator">&gt;=</span> <span class="r-number">2</span>, <span class="r-operator">!</span><span class="r-function">str_detect</span>(form, <span class="r-string">"^[0-9]+$"</span>)) <span class="r-operator">|&gt;</span>
  <span class="r-function">select</span>(doc_id, president, kind, word <span class="r-operator">=</span> form)

<span class="r-comment"># TF-IDF matrix</span>
tfidf <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span> <span class="r-function">count</span>(doc_id, word) <span class="r-operator">|&gt;</span> <span class="r-function">bind_tf_idf</span>(word, doc_id, n)
dtm <span class="r-operator">&lt;-</span> tfidf <span class="r-operator">|&gt;</span> <span class="r-function">select</span>(doc_id, word, tf_idf) <span class="r-operator">|&gt;</span>
  <span class="r-function">pivot_wider</span>(names_from <span class="r-operator">=</span> word, values_from <span class="r-operator">=</span> tf_idf, values_fill <span class="r-operator">=</span> <span class="r-number">0</span>)
mat <span class="r-operator">&lt;-</span> dtm <span class="r-operator">|&gt;</span> <span class="r-function">select</span>(<span class="r-operator">-</span>doc_id) <span class="r-operator">|&gt;</span> <span class="r-function">as.matrix</span>()

<span class="r-comment"># ── K-means for k=2..8 with silhouette scores ─────────────────────</span>
sil_results <span class="r-operator">&lt;-</span> <span class="r-function">tibble</span>(k <span class="r-operator">=</span> <span class="r-number">2</span>:<span class="r-number">8</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(
    km <span class="r-operator">=</span> <span class="r-function">map</span>(k, <span class="r-operator">~</span> <span class="r-function">kmeans</span>(mat, centers <span class="r-operator">=</span> .x, nstart <span class="r-operator">=</span> <span class="r-number">10</span>)),
    sil <span class="r-operator">=</span> <span class="r-function">map_dbl</span>(km, <span class="r-keyword">function</span>(m) {
      s <span class="r-operator">&lt;-</span> <span class="r-function">silhouette</span>(m<span class="r-operator">$</span>cluster, <span class="r-function">dist</span>(mat))
      <span class="r-function">mean</span>(s[, <span class="r-number">3</span>])
    })
  )

<span class="r-comment"># Which k is best?</span>
sil_results <span class="r-operator">|&gt;</span> <span class="r-function">arrange</span>(<span class="r-function">desc</span>(sil))
best_k <span class="r-operator">&lt;-</span> sil_results <span class="r-operator">|&gt;</span> <span class="r-function">slice_max</span>(sil) <span class="r-operator">|&gt;</span> <span class="r-function">pull</span>(k)</code></pre>
    </div>
    <div class="callout callout-info">
      <strong>About <code>nstart = 10</code>:</strong> K-means results depend on random initial centroid placement. Setting <code>nstart = 10</code> runs the algorithm 10 times with different starting points and keeps the best result &mdash; the same approach Orange uses by default.
    </div>
  </div>
</details>

<div class="output-panel">
  <div class="output-panel-header">Silhouette Scores by <em>k</em></div>
  <div class="output-panel-body">
    <div class="sil-chart" id="silChart"></div>
    <p style="text-align:center; font-size:0.82rem; color:#6b7280; margin-top:0.5rem;">Higher silhouette = better-defined clusters. The green bar is the best <em>k</em>.</p>
  </div>
</div>

<div class="callout callout-info">
  <strong>How to read silhouette scores:</strong> As a general guideline: <strong>0.70&ndash;1.0</strong> = strong structure, <strong>0.50&ndash;0.70</strong> = reasonable, <strong>0.25&ndash;0.50</strong> = weak but potentially useful, <strong>below 0.25</strong> = little meaningful structure. Our scores here (~0.01&ndash;0.02) are low even by text standards &mdash; this is honest. It means the cluster boundaries are fuzzy: speeches share a lot of overlapping vocabulary regardless of topic. The clusters still show <em>interpretable</em> thematic patterns (see below), but the separation is soft. This is a realistic result and worth acknowledging.
</div>

<div class="callout callout-tip">
  <strong>Low scores are common for text.</strong> TF-IDF document vectors are high-dimensional and sparse, which makes clean separation rare. What matters is (1) the <em>relative</em> comparison across k values and (2) whether the resulting clusters are <em>interpretable</em> when you look at the top words.
</div>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">2</span>
  <h2>What Did K-Means Find?</h2>
</div>

<p class="narrative">
  With 7 presidents in the corpus, you might expect k=7 to recover one cluster per president. But look at the cluster compositions below &mdash; <strong>every president appears in multiple clusters</strong>. K-means grouped speeches by <em>topic</em>, not by <em>speaker</em>. The algorithm found thematic structure: diplomacy, national addresses, commemorative events, education, economy.
</p>

<p class="narrative">
  This is an important lesson: <strong>clustering finds the dominant source of variation in the data</strong>. In this corpus, the biggest vocabulary differences are between speech <em>types</em> (a diplomatic welcome vs. an economic policy address), not between presidents.
</p>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: run k-means with best k and extract cluster words</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── Run k-means with the best k ───────────────────────────────────</span>
<span class="r-function">set.seed</span>(<span class="r-number">42</span>)   <span class="r-comment"># for reproducibility</span>
best_km <span class="r-operator">&lt;-</span> <span class="r-function">kmeans</span>(mat, centers <span class="r-operator">=</span> best_k, nstart <span class="r-operator">=</span> <span class="r-number">10</span>)

<span class="r-comment"># ── Attach cluster labels to each document ────────────────────────</span>
doc_clusters <span class="r-operator">&lt;-</span> <span class="r-function">tibble</span>(
  doc_id  <span class="r-operator">=</span> dtm<span class="r-operator">$</span>doc_id,
  cluster <span class="r-operator">=</span> <span class="r-function">as.character</span>(best_km<span class="r-operator">$</span>cluster)
)

<span class="r-comment"># ── Extract top TF-IDF words per cluster ──────────────────────────</span>
<span class="r-comment"># Treat all speeches in a cluster as one pseudo-document,</span>
<span class="r-comment"># then find the words with highest TF-IDF within that cluster.</span>
cluster_tfidf <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span>
  <span class="r-function">left_join</span>(doc_clusters, by <span class="r-operator">=</span> <span class="r-string">"doc_id"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(cluster, word) <span class="r-operator">|&gt;</span>
  <span class="r-function">bind_tf_idf</span>(word, cluster, n) <span class="r-operator">|&gt;</span>
  <span class="r-function">group_by</span>(cluster) <span class="r-operator">|&gt;</span>
  <span class="r-function">slice_max</span>(tf_idf, n <span class="r-operator">=</span> <span class="r-number">15</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">ungroup</span>()

<span class="r-comment"># View top words for each cluster</span>
cluster_tfidf <span class="r-operator">|&gt;</span>
  <span class="r-function">select</span>(cluster, word, tf_idf) <span class="r-operator">|&gt;</span>
  <span class="r-function">arrange</span>(cluster, <span class="r-function">desc</span>(tf_idf)) <span class="r-operator">|&gt;</span>
  <span class="r-function">print</span>(n <span class="r-operator">=</span> <span class="r-number">30</span>)

<span class="r-comment"># ── Plot: top words per cluster ───────────────────────────────────</span>
cluster_tfidf <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(word <span class="r-operator">=</span> <span class="r-function">reorder_within</span>(word, tf_idf, cluster)) <span class="r-operator">|&gt;</span>
  <span class="r-function">ggplot</span>(<span class="r-function">aes</span>(tf_idf, word, fill <span class="r-operator">=</span> cluster)) <span class="r-operator">+</span>
  <span class="r-function">geom_col</span>(show.legend <span class="r-operator">=</span> <span class="r-keyword">FALSE</span>) <span class="r-operator">+</span>
  <span class="r-function">facet_wrap</span>(<span class="r-operator">~</span> cluster, scales <span class="r-operator">=</span> <span class="r-string">"free"</span>) <span class="r-operator">+</span>
  <span class="r-function">scale_y_reordered</span>() <span class="r-operator">+</span>
  <span class="r-function">labs</span>(title <span class="r-operator">=</span> <span class="r-function">paste</span>(<span class="r-string">"Top words by cluster (k ="</span>, best_k, <span class="r-string">")"</span>),
       x <span class="r-operator">=</span> <span class="r-string">"TF-IDF"</span>, y <span class="r-operator">=</span> <span class="r-keyword">NULL</span>) <span class="r-operator">+</span>
  <span class="r-function">theme_minimal</span>()</code></pre>
    </div>
    <div class="callout callout-info">
      <strong>Why TF-IDF again here?</strong> We already used TF-IDF to build the document vectors. Now we re-apply it at the cluster level: treating all speeches in a cluster as one big pseudo-document reveals which words are <em>distinctive to that cluster</em> compared to the other clusters. This is the same logic as the cluster word analysis in the NIKH textbook demo.
    </div>
  </div>
</details>

<div class="output-panel">
  <div class="output-panel-header">Clusters: Top Words &amp; President Distribution</div>
  <div class="output-panel-body">
    <div id="clusterLegend" class="chart-legend"></div>
    <div class="cluster-grid" id="clusterGrid"></div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">3</span>
  <h2>Presidents Across Clusters</h2>
</div>

<p class="narrative">
  Another way to read the results: for each president, how are their speeches distributed across clusters? If k-means had found president-level clusters, each president would be concentrated in a single row. Instead, we see that most presidents' speeches spread across 4&ndash;6 clusters &mdash; because presidents give many <em>types</em> of speeches.
</p>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: summarize president distribution across clusters</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block">
      <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># ── President distribution per cluster ────────────────────────────</span>
<span class="r-comment"># For each president, count how many speeches landed in each cluster.</span>
pres_cluster <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span>
  <span class="r-function">distinct</span>(doc_id, president) <span class="r-operator">|&gt;</span>
  <span class="r-function">left_join</span>(doc_clusters, by <span class="r-operator">=</span> <span class="r-string">"doc_id"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(president, cluster)

<span class="r-comment"># ── Tabular view ──────────────────────────────────────────────────</span>
pres_order <span class="r-operator">&lt;-</span> <span class="r-function">c</span>(<span class="r-string">"노태우"</span>, <span class="r-string">"김영삼"</span>, <span class="r-string">"김대중"</span>, <span class="r-string">"노무현"</span>, <span class="r-string">"이명박"</span>, <span class="r-string">"박근혜"</span>, <span class="r-string">"문재인"</span>)

pres_cluster <span class="r-operator">|&gt;</span>
  <span class="r-function">pivot_wider</span>(names_from <span class="r-operator">=</span> cluster, values_from <span class="r-operator">=</span> n,
              values_fill <span class="r-operator">=</span> <span class="r-number">0</span>, names_sort <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">arrange</span>(<span class="r-function">match</span>(president, pres_order))

<span class="r-comment"># ── Stacked bar chart: proportional view ──────────────────────────</span>
pres_cluster <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(president <span class="r-operator">=</span> <span class="r-function">factor</span>(president, levels <span class="r-operator">=</span> pres_order)) <span class="r-operator">|&gt;</span>
  <span class="r-function">ggplot</span>(<span class="r-function">aes</span>(x <span class="r-operator">=</span> president, y <span class="r-operator">=</span> n, fill <span class="r-operator">=</span> cluster)) <span class="r-operator">+</span>
  <span class="r-function">geom_col</span>(position <span class="r-operator">=</span> <span class="r-string">"fill"</span>) <span class="r-operator">+</span>
  <span class="r-function">scale_y_continuous</span>(labels <span class="r-operator">=</span> scales<span class="r-operator">::</span><span class="r-function">percent</span>) <span class="r-operator">+</span>
  <span class="r-function">labs</span>(title <span class="r-operator">=</span> <span class="r-string">"How each president's speeches are distributed across clusters"</span>,
       x <span class="r-operator">=</span> <span class="r-keyword">NULL</span>, y <span class="r-operator">=</span> <span class="r-string">"Share of speeches"</span>, fill <span class="r-operator">=</span> <span class="r-string">"Cluster"</span>) <span class="r-operator">+</span>
  <span class="r-function">theme_minimal</span>() <span class="r-operator">+</span>
  <span class="r-function">theme</span>(axis.text.x <span class="r-operator">=</span> <span class="r-function">element_text</span>(angle <span class="r-operator">=</span> <span class="r-number">45</span>, hjust <span class="r-operator">=</span> <span class="r-number">1</span>))</code></pre>
    </div>
    <div class="callout callout-tip">
      <strong>What to look for:</strong> If k-means had clustered by president, each row would be one solid colour. Instead, every president's bar is split across multiple clusters &mdash; confirming that topic, not speaker identity, drives the clustering.
    </div>
  </div>
</details>

<div class="output-panel">
  <div class="output-panel-header">Speech Distribution by President</div>
  <div class="output-panel-body" id="presidentGrid"></div>
</div>

<div class="callout callout-info">
  <strong>Comparing methods:</strong> Hierarchical clustering on the NIKH textbooks found <em>era-based</em> clusters (Colonial, Authoritarian, Democratic) because each textbook has one era label and its entire vocabulary reflects that era. K-means on presidential speeches found <em>topic-based</em> clusters because each president gives speeches on many different topics. The method is the same &mdash; the structure it finds depends on the data.
</div>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">4</span>
  <h2>Key Takeaways</h2>
</div>

<p class="narrative">
  Three lessons from this exercise:
</p>

<p class="narrative">
  <strong>1. Silhouette scores guide, but you interpret.</strong> The silhouette score told us k=<span id="bestKInline"></span> produces the tightest clusters. But a different k might be more useful for your research question &mdash; maybe k=3 (progressive/conservative/neutral) is what you actually want to test.
</p>

<p class="narrative">
  <strong>2. Clustering finds the strongest signal.</strong> The biggest vocabulary differences in this corpus are between speech <em>types</em>, not between presidents. A diplomatic welcome speech uses different words than an economic policy address, regardless of who is speaking.
</p>

<p class="narrative">
  <strong>3. K-means and hierarchical clustering complement each other.</strong> Hierarchical clustering shows the full tree of relationships. K-means gives you a clean partition. Use both and compare.
</p>

</div><!-- /tutorial-page -->

<script>
(function () {
  "use strict";

  var DATA = null;
  var CLUSTER_COLORS = [
    "#2563eb", "#dc2626", "#059669", "#d97706",
    "#7c3aed", "#0891b2", "#be185d", "#4f46e5"
  ];

  var PRESIDENT_ORDER = ["노태우", "김영삼", "김대중", "노무현", "이명박", "박근혜", "문재인"];

  // Subjective labels based on top words in each cluster (0-indexed internally)
  var CLUSTER_LABELS = {
    "0": "Bilateral Diplomacy",
    "1": "International Summits",
    "2": "National Unity & Inter-Korean",
    "3": "Commemorative & Cultural",
    "4": "Security & Defense",
    "5": "Education & Youth",
    "6": "Economic Policy & Reform"
  };

  fetch("{{ '/interactive/kmeans_data.json' | relative_url }}")
    .then(function (r) { return r.json(); })
    .then(function (json) {
      DATA = json;
      document.getElementById("bestKInline").textContent = DATA.best_k;
      renderSilhouetteChart();
      renderClusterGrid();
      renderPresidentGrid();
    });

  // ── Silhouette bar chart ────────────────────────────────────────
  function renderSilhouetteChart() {
    var container = document.getElementById("silChart");
    var items = DATA.silhouette_comparison;
    var maxSil = Math.max.apply(null, items.map(function (d) { return d.silhouette; }));

    items.forEach(function (d) {
      var wrap = document.createElement("div");
      wrap.className = "sil-bar-wrap";

      var isBest = d.k === DATA.best_k;
      var pct = (d.silhouette / maxSil) * 140;

      var bar = document.createElement("div");
      bar.className = "sil-bar" + (isBest ? " best" : "");
      bar.style.height = pct + "px";
      bar.style.background = isBest ? "#059669" : "#94a3b8";

      var value = document.createElement("div");
      value.className = "sil-bar-value";
      value.textContent = d.silhouette.toFixed(4);

      var label = document.createElement("div");
      label.className = "sil-bar-label";
      label.textContent = "k=" + d.k;

      wrap.appendChild(value);
      wrap.appendChild(bar);
      wrap.appendChild(label);
      if (isBest) {
        var tag = document.createElement("div");
        tag.className = "sil-best-tag";
        tag.textContent = "best";
        wrap.appendChild(tag);
      }

      container.appendChild(wrap);
    });
  }

  // ── Cluster cards ───────────────────────────────────────────────
  function renderClusterGrid() {
    var grid = document.getElementById("clusterGrid");
    var legend = document.getElementById("clusterLegend");
    var nClusters = DATA.best_k;

    for (var c = 0; c < nClusters; c++) {
      var color = CLUSTER_COLORS[c % CLUSTER_COLORS.length];
      var words = DATA.cluster_words[String(c)];
      var presDist = DATA.cluster_president_dist[String(c)];

      // Legend
      var displayNum = c + 1;
      var clusterLabel = CLUSTER_LABELS[String(c)] || "";
      var legItem = document.createElement("span");
      legItem.className = "chart-legend-item";
      legItem.innerHTML = '<span class="chart-legend-dot" style="background:' + color + '"></span> ' + displayNum + '. ' + clusterLabel;
      legend.appendChild(legItem);

      // Card
      var card = document.createElement("div");
      card.className = "cluster-card";

      var header = document.createElement("div");
      header.className = "cluster-card-header";
      header.style.background = color;
      var totalSpeeches = Object.values(presDist).reduce(function (a, b) { return a + b; }, 0);
      header.textContent = "Cluster " + displayNum + ": " + clusterLabel + " (" + totalSpeeches + ")";
      card.appendChild(header);

      var body = document.createElement("div");
      body.className = "cluster-card-body";

      // Top words section
      var wordsSection = document.createElement("div");
      wordsSection.className = "cluster-card-section";
      var wordsTitle = document.createElement("div");
      wordsTitle.className = "cluster-card-section-title";
      wordsTitle.textContent = "Top Words";
      wordsSection.appendChild(wordsTitle);

      var wordContainer = document.createElement("div");
      wordContainer.style.lineHeight = "1.4";
      var maxTfidf = words[0].tfidf;
      words.slice(0, 15).forEach(function (w) {
        var span = document.createElement("span");
        span.className = "wc-word";
        var ratio = w.tfidf / maxTfidf;
        span.style.fontSize = (0.7 + ratio * 1.0) + "rem";
        span.style.color = color;
        span.style.opacity = 0.5 + ratio * 0.5;
        span.textContent = w.word;
        span.title = w.word + ": " + w.tfidf.toFixed(4);
        wordContainer.appendChild(span);
        wordContainer.appendChild(document.createTextNode(" "));
      });
      wordsSection.appendChild(wordContainer);
      body.appendChild(wordsSection);

      // President distribution section
      var presSection = document.createElement("div");
      presSection.className = "cluster-card-section";
      var presTitle = document.createElement("div");
      presTitle.className = "cluster-card-section-title";
      presTitle.textContent = "Presidents";
      presSection.appendChild(presTitle);

      var sorted = PRESIDENT_ORDER.filter(function (p) { return presDist[p]; });
      sorted.forEach(function (p) {
        var count = presDist[p];
        var pct = (count / totalSpeeches) * 100;
        var row = document.createElement("div");
        row.className = "mini-bar-row";
        row.innerHTML =
          '<div class="mini-bar-label">' + p + '</div>' +
          '<div class="mini-bar-track"><div class="mini-bar-fill" style="width:' + pct + '%;background:' + color + '"></div></div>' +
          '<div class="mini-bar-count">' + count + '</div>';
        presSection.appendChild(row);
      });
      body.appendChild(presSection);

      card.appendChild(body);
      grid.appendChild(card);
    }
  }

  // ── President distribution grid ─────────────────────────────────
  function renderPresidentGrid() {
    var container = document.getElementById("presidentGrid");

    // Add legend at top
    var legend = document.createElement("div");
    legend.className = "chart-legend";
    legend.style.marginBottom = "1rem";
    for (var i = 0; i < DATA.best_k; i++) {
      var item = document.createElement("span");
      item.className = "chart-legend-item";
      item.innerHTML = '<span class="chart-legend-dot" style="background:' + CLUSTER_COLORS[i] + '"></span> ' +
        (i + 1) + '. ' + (CLUSTER_LABELS[String(i)] || '');
      legend.appendChild(item);
    }
    container.appendChild(legend);

    PRESIDENT_ORDER.forEach(function (pres) {
      var summary = DATA.president_summary.find(function (p) { return p.president === pres; });
      if (!summary) return;

      var row = document.createElement("div");
      row.style.marginBottom = "0.75rem";

      var label = document.createElement("div");
      label.style.cssText = "font-weight:700; font-size:0.88rem; color:#374151; margin-bottom:0.3rem;";
      label.textContent = pres + " (" + summary.count + " speeches)";
      row.appendChild(label);

      var barRow = document.createElement("div");
      barRow.style.cssText = "display:flex; height:22px; border-radius:4px; overflow:hidden;";

      for (var c = 0; c < DATA.best_k; c++) {
        var count = summary.cluster_dist[String(c)] || 0;
        if (count === 0) continue;
        var pct = (count / summary.count) * 100;
        var seg = document.createElement("div");
        seg.style.cssText = "height:100%; display:flex; align-items:center; justify-content:center; cursor:default;";
        seg.style.width = pct + "%";
        seg.style.background = CLUSTER_COLORS[c % CLUSTER_COLORS.length];
        seg.title = "Cluster " + (c + 1) + ": " + (CLUSTER_LABELS[String(c)] || "") + " (" + count + ")";
        if (pct > 8) {
          var txt = document.createElement("span");
          txt.style.cssText = "font-size:0.65rem; font-weight:700; color:#fff;";
          txt.textContent = count;
          seg.appendChild(txt);
        }
        barRow.appendChild(seg);
      }

      row.appendChild(barRow);
      container.appendChild(row);
    });
  }

  // ── Copy button ─────────────────────────────────────────────────
  window.copyCode = function (btn) {
    var pre = btn.closest(".code-block").querySelector("pre code");
    var text = pre.textContent;
    navigator.clipboard.writeText(text).then(function () {
      btn.textContent = "Copied!";
      btn.classList.add("copied");
      setTimeout(function () { btn.textContent = "Copy"; btn.classList.remove("copied"); }, 2000);
    });
  };
})();
</script>
