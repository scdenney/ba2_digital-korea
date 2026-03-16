---
layout: default
title: "Quick Start: Tidyverse & the Pipe Operator"
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

/* ── Comparison panels ───────────────────────────────────────────── */
.compare-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin: 1rem 0;
}

.compare-panel {
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  overflow: hidden;
}

.compare-panel-header {
  padding: 0.5rem 0.75rem;
  font-weight: 700;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  text-align: center;
}

.compare-panel-header.style-base { background: #f1f5f9; color: #64748b; }
.compare-panel-header.style-tidy { background: var(--leiden-blue); color: #fff; }

.compare-panel pre {
  margin: 0;
  padding: 0.75rem 1rem;
  background: #1e293b;
  color: #e2e8f0;
  font-size: 0.8rem;
  line-height: 1.55;
  overflow-x: auto;
  font-family: "SFMono-Regular", "Consolas", "Liberation Mono", monospace;
}

.compare-panel pre code { background: none; color: inherit; padding: 0; font-size: inherit; }

/* ── Pipe diagram ────────────────────────────────────────────────── */
.pipe-diagram {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin: 1.5rem 0;
  padding: 1.25rem;
  background: #f8fafc;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
}

.pipe-step {
  display: inline-flex;
  align-items: center;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  font-size: 0.82rem;
  font-weight: 600;
  font-family: "SFMono-Regular", "Consolas", "Liberation Mono", monospace;
}

.pipe-step-data { background: #dbeafe; color: #1e40af; }
.pipe-step-fn { background: #f0fdf4; color: #166534; }
.pipe-step-result { background: #fef3c7; color: #92400e; }

.pipe-arrow {
  font-size: 1.1rem;
  color: #9ca3af;
  font-weight: 700;
}

/* ── Package grid ────────────────────────────────────────────────── */
.pkg-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 0.75rem;
  margin: 1rem 0;
}

.pkg-card {
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 0.75rem 1rem;
  background: #fff;
}

.pkg-card-name {
  font-weight: 700;
  font-size: 0.9rem;
  color: var(--leiden-blue);
  font-family: "SFMono-Regular", "Consolas", "Liberation Mono", monospace;
  margin-bottom: 0.25rem;
}

.pkg-card-desc {
  font-size: 0.78rem;
  color: #6b7280;
  line-height: 1.5;
}

/* ── Responsive ──────────────────────────────────────────────────── */
@media (max-width: 768px) {
  .compare-grid { grid-template-columns: 1fr; }
  .pipe-diagram { flex-direction: column; }
}
</style>

<div class="tutorial-page">

<div class="tutorial-header">
  <h1>Quick Start: Tidyverse &amp; the Pipe Operator</h1>
  <p class="tutorial-subtitle">A short primer on the R packages and syntax used in this course</p>
  <div class="tutorial-meta">
    <span>Pre-requisite</span>
    <span>R + RStudio</span>
    <span>Read before the weekly exercises</span>
  </div>
</div>

<p class="narrative">
  The interactive exercises on this site use <strong>tidyverse</strong> &mdash; a collection of R packages designed for data science. If you have been learning base R through Swirl and DataCamp, the tidyverse code might look a little different. This page covers the essentials: what tidyverse is, how to install it, and the one piece of syntax you really need to know &mdash; the <strong>pipe operator</strong>.
</p>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">1</span>
  <h2>What Is Tidyverse?</h2>
</div>

<p class="narrative">
  Tidyverse is a bundle of R packages that work together. When you run <code>library(tidyverse)</code>, you load all of them at once. Here are the ones we use most:
</p>

<div class="pkg-grid">
  <div class="pkg-card">
    <div class="pkg-card-name">dplyr</div>
    <div class="pkg-card-desc">Filter rows, select columns, count, group, summarize</div>
  </div>
  <div class="pkg-card">
    <div class="pkg-card-name">tidyr</div>
    <div class="pkg-card-desc">Reshape data &mdash; pivot wider/longer, nest/unnest</div>
  </div>
  <div class="pkg-card">
    <div class="pkg-card-name">readr</div>
    <div class="pkg-card-desc">Fast CSV reading with <code>read_csv()</code></div>
  </div>
  <div class="pkg-card">
    <div class="pkg-card-name">ggplot2</div>
    <div class="pkg-card-desc">Plots and charts &mdash; bar plots, word clouds, etc.</div>
  </div>
  <div class="pkg-card">
    <div class="pkg-card-name">stringr</div>
    <div class="pkg-card-desc">String manipulation &mdash; detect, replace, trim text</div>
  </div>
  <div class="pkg-card">
    <div class="pkg-card-name">purrr</div>
    <div class="pkg-card-desc">Apply functions across lists and columns with <code>map()</code></div>
  </div>
</div>

<div class="code-block">
  <div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
  <pre><code><span class="r-comment"># Install tidyverse (only need to do this once)</span>
<span class="r-function">install.packages</span>(<span class="r-string">"tidyverse"</span>)

<span class="r-comment"># Load it at the start of every script</span>
<span class="r-function">library</span>(tidyverse)</code></pre>
</div>

<div class="callout callout-info">
  <strong>Tidyverse vs. base R:</strong> You are not replacing what you learned in Swirl &mdash; base R functions like <code>hclust()</code>, <code>dist()</code>, and <code>as.matrix()</code> work exactly the same. Tidyverse just adds convenient tools for reading data, wrangling tables, and making plots.
</div>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">2</span>
  <h2>The Pipe Operator</h2>
</div>

<p class="narrative">
  The pipe takes the result on the left and feeds it as the first argument to the function on the right. Instead of nesting functions inside each other, you read the code <strong>left to right, top to bottom</strong> &mdash; like a recipe.
</p>

<div class="pipe-diagram">
  <span class="pipe-step pipe-step-data">data</span>
  <span class="pipe-arrow">|&gt;</span>
  <span class="pipe-step pipe-step-fn">step_1()</span>
  <span class="pipe-arrow">|&gt;</span>
  <span class="pipe-step pipe-step-fn">step_2()</span>
  <span class="pipe-arrow">|&gt;</span>
  <span class="pipe-step pipe-step-fn">step_3()</span>
  <span class="pipe-arrow">&rarr;</span>
  <span class="pipe-step pipe-step-result">result</span>
</div>

<p class="narrative">
  R has two pipe operators. They do the same thing &mdash; you will see both in examples online:
</p>

<div class="compare-grid">
  <div class="compare-panel">
    <div class="compare-panel-header style-tidy">|&gt; &nbsp; (base R pipe, R 4.1+)</div>
    <pre><code>corpus <span class="r-operator">|&gt;</span>
  <span class="r-function">filter</span>(era <span class="r-operator">==</span> <span class="r-string">"Colonial"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">select</span>(title, year)</code></pre>
  </div>
  <div class="compare-panel">
    <div class="compare-panel-header style-base">%&gt;% &nbsp; (tidyverse/magrittr pipe)</div>
    <pre><code>corpus <span class="r-operator">%&gt;%</span>
  <span class="r-function">filter</span>(era <span class="r-operator">==</span> <span class="r-string">"Colonial"</span>) <span class="r-operator">%&gt;%</span>
  <span class="r-function">select</span>(title, year)</code></pre>
  </div>
</div>

<div class="callout callout-tip">
  <strong>Which one to use?</strong> We use <code>|&gt;</code> (the base R pipe) throughout this course. It is built into R &mdash; no extra packages needed. If you see <code>%&gt;%</code> in online examples or tutorials, it works the same way.
</div>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">3</span>
  <h2>Base R vs. Tidyverse: Side by Side</h2>
</div>

<p class="narrative">
  Here are three common tasks written both ways. Neither is wrong &mdash; tidyverse just reads more like plain English when you chain multiple steps together.
</p>

<p class="narrative"><strong>Read a CSV and look at it:</strong></p>

<div class="compare-grid">
  <div class="compare-panel">
    <div class="compare-panel-header style-base">Base R</div>
    <pre><code>corpus <span class="r-operator">&lt;-</span> <span class="r-function">read.csv</span>(<span class="r-string">"data.csv"</span>)
<span class="r-function">head</span>(corpus)</code></pre>
  </div>
  <div class="compare-panel">
    <div class="compare-panel-header style-tidy">Tidyverse</div>
    <pre><code>corpus <span class="r-operator">&lt;-</span> <span class="r-function">read_csv</span>(<span class="r-string">"data.csv"</span>)
corpus <span class="r-operator">|&gt;</span> <span class="r-function">glimpse</span>()</code></pre>
  </div>
</div>

<p class="narrative"><strong>Filter rows and select columns:</strong></p>

<div class="compare-grid">
  <div class="compare-panel">
    <div class="compare-panel-header style-base">Base R</div>
    <pre><code>sub <span class="r-operator">&lt;-</span> corpus[corpus<span class="r-operator">$</span>era <span class="r-operator">==</span> <span class="r-string">"Colonial"</span>, ]
sub <span class="r-operator">&lt;-</span> sub[, <span class="r-function">c</span>(<span class="r-string">"title"</span>, <span class="r-string">"year"</span>)]</code></pre>
  </div>
  <div class="compare-panel">
    <div class="compare-panel-header style-tidy">Tidyverse</div>
    <pre><code>corpus <span class="r-operator">|&gt;</span>
  <span class="r-function">filter</span>(era <span class="r-operator">==</span> <span class="r-string">"Colonial"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">select</span>(title, year)</code></pre>
  </div>
</div>

<p class="narrative"><strong>Count words and get the top 10:</strong></p>

<div class="compare-grid">
  <div class="compare-panel">
    <div class="compare-panel-header style-base">Base R</div>
    <pre><code>counts <span class="r-operator">&lt;-</span> <span class="r-function">table</span>(tokens<span class="r-operator">$</span>word)
counts <span class="r-operator">&lt;-</span> <span class="r-function">sort</span>(counts, decreasing <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>)
<span class="r-function">head</span>(counts, <span class="r-number">10</span>)</code></pre>
  </div>
  <div class="compare-panel">
    <div class="compare-panel-header style-tidy">Tidyverse</div>
    <pre><code>tokens <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(word, sort <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">slice_head</span>(n <span class="r-operator">=</span> <span class="r-number">10</span>)</code></pre>
  </div>
</div>

<div class="callout callout-info">
  <strong>The pattern:</strong> Start with your data, then pipe it through a chain of verbs &mdash; <code>filter()</code>, <code>select()</code>, <code>count()</code>, <code>mutate()</code>, <code>group_by()</code>, <code>summarize()</code>. Each verb does one thing. The pipe connects them. That is most of what you need.
</div>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">4</span>
  <h2>Key Verbs Cheat Sheet</h2>
</div>

<p class="narrative">
  These are the tidyverse functions that appear most often in our exercises. All come from the <strong>dplyr</strong> package (loaded automatically with <code>library(tidyverse)</code>).
</p>

<div class="code-block">
  <div class="code-block-header"><span>R — Quick Reference</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
  <pre><code><span class="r-comment"># ── Select columns ────────────────────────────────────────────────</span>
corpus <span class="r-operator">|&gt;</span> <span class="r-function">select</span>(book_id, title, era)

<span class="r-comment"># ── Filter rows ───────────────────────────────────────────────────</span>
corpus <span class="r-operator">|&gt;</span> <span class="r-function">filter</span>(era <span class="r-operator">==</span> <span class="r-string">"Colonial"</span>)

<span class="r-comment"># ── Add or modify a column ────────────────────────────────────────</span>
corpus <span class="r-operator">|&gt;</span> <span class="r-function">mutate</span>(title_short <span class="r-operator">=</span> <span class="r-function">str_trunc</span>(title, <span class="r-number">20</span>))

<span class="r-comment"># ── Count occurrences ─────────────────────────────────────────────</span>
tokens <span class="r-operator">|&gt;</span> <span class="r-function">count</span>(word, sort <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>)

<span class="r-comment"># ── Group and summarize ───────────────────────────────────────────</span>
tokens <span class="r-operator">|&gt;</span>
  <span class="r-function">group_by</span>(era) <span class="r-operator">|&gt;</span>
  <span class="r-function">summarize</span>(total <span class="r-operator">=</span> <span class="r-function">n</span>())

<span class="r-comment"># ── Sort rows ─────────────────────────────────────────────────────</span>
word_counts <span class="r-operator">|&gt;</span> <span class="r-function">arrange</span>(<span class="r-function">desc</span>(n))

<span class="r-comment"># ── Join two tables ───────────────────────────────────────────────</span>
tokens <span class="r-operator">|&gt;</span> <span class="r-function">left_join</span>(corpus, by <span class="r-operator">=</span> <span class="r-string">"book_id"</span>)

<span class="r-comment"># ── Print more rows ───────────────────────────────────────────────</span>
result <span class="r-operator">|&gt;</span> <span class="r-function">print</span>(n <span class="r-operator">=</span> <span class="r-number">20</span>)</code></pre>
</div>

</div><!-- /tutorial-page -->

<script>
(function () {
  "use strict";
  window.copyCode = function (btn) {
    var pre = btn.closest(".code-block").querySelector("pre code") ||
              btn.closest(".compare-panel").querySelector("pre code");
    if (!pre) return;
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
