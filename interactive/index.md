---
layout: default
title: Interactive
---

<style>
.interactive-page { max-width: 100%; }

.interactive-header {
  margin-top: 1rem;
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 2px solid #e2e8f0;
}

.interactive-header h1 {
  font-size: 1.6rem;
  color: var(--leiden-blue);
  margin: 0 0 0.5rem;
}

.interactive-intro {
  font-size: 0.95rem;
  color: #4b5563;
  line-height: 1.7;
  margin: 0;
}

/* ── Exercise cards ──────────────────────────────────────────────── */
.exercise-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.25rem;
  margin-top: 1.5rem;
}

.exercise-card {
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  overflow: hidden;
  transition: box-shadow 0.2s, transform 0.15s;
  background: #fff;
  display: flex;
  flex-direction: column;
}

.exercise-card:hover {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  transform: translateY(-2px);
}

.exercise-card a {
  text-decoration: none;
  color: inherit;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.exercise-card-accent {
  height: 4px;
}

.exercise-card-body {
  padding: 1.25rem 1.5rem;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.exercise-card-week {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #9ca3af;
  margin-bottom: 0.4rem;
}

.exercise-card-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--leiden-blue);
  margin-bottom: 0.4rem;
  line-height: 1.3;
}

.exercise-card-desc {
  font-size: 0.88rem;
  color: #4b5563;
  line-height: 1.6;
  flex: 1;
}

.exercise-card-footer {
  padding: 0.6rem 1.5rem;
  border-top: 1px solid #f1f5f9;
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.exercise-tag {
  display: inline-block;
  padding: 0.15rem 0.5rem;
  border-radius: 10px;
  font-size: 0.7rem;
  font-weight: 600;
  background: #f1f5f9;
  color: #64748b;
}

/* ── Color accents for different types ───────────────────────────── */
.accent-blue { background: var(--leiden-blue); }
.accent-teal { background: #0891b2; }
.accent-amber { background: #b45309; }
.accent-violet { background: #7c3aed; }
.accent-slate { background: #475569; }

@media (max-width: 600px) {
  .exercise-grid { grid-template-columns: 1fr; }
}
</style>

<div class="interactive-page">

<div class="interactive-header">
  <h1>Interactive Exercises</h1>
  <p class="interactive-intro">Hands-on exercises that accompany the weekly lectures. Step through text analysis pipelines, explore real Korean-language corpora, and see how computational methods work on actual data.</p>
</div>

<div class="exercise-grid">

  <div class="exercise-card">
    <a href="{{ '/interactive/tidyverse-primer' | relative_url }}">
      <div class="exercise-card-accent accent-slate"></div>
      <div class="exercise-card-body">
        <div class="exercise-card-week">Pre-requisite</div>
        <div class="exercise-card-title">Quick Start: Tidyverse &amp; the Pipe Operator</div>
        <p class="exercise-card-desc">New to tidyverse? This short primer covers installation, the pipe operator (<code>|&gt;</code>), and how tidyverse code compares to the base R you learned in Swirl. Read this before the exercises below.</p>
      </div>
      <div class="exercise-card-footer">
        <span class="exercise-tag">R</span>
        <span class="exercise-tag">tidyverse</span>
        <span class="exercise-tag">Pipe operator</span>
      </div>
    </a>
  </div>

  <div class="exercise-card">
    <a href="{{ '/interactive/preprocessing-pipeline' | relative_url }}">
      <div class="exercise-card-accent accent-blue"></div>
      <div class="exercise-card-body">
        <div class="exercise-card-week">Weeks 3 &ndash; 4</div>
        <div class="exercise-card-title">Text Preprocessing Pipeline</div>
        <p class="exercise-card-desc">Step through the six-stage Korean text preprocessing pipeline on real presidential speech sentences. Toggle POS tags and stopwords to see how filtering choices shape the final output.</p>
      </div>
      <div class="exercise-card-footer">
        <span class="exercise-tag">Presidential Speeches</span>
        <span class="exercise-tag">Kiwi / POS tags</span>
      </div>
    </a>
  </div>

  <div class="exercise-card">
    <a href="{{ '/interactive/nikh-textbooks' | relative_url }}">
      <div class="exercise-card-accent accent-teal"></div>
      <div class="exercise-card-body">
        <div class="exercise-card-week">Week 5</div>
        <div class="exercise-card-title">Exploring Korean History Textbooks in R</div>
        <p class="exercise-card-desc">Word clouds, frequency analysis, and concordance using the NIKH history textbook corpus. Compare how language differs across colonial, authoritarian, and democratic eras &mdash; with optional R code you can expand and run yourself.</p>
      </div>
      <div class="exercise-card-footer">
        <span class="exercise-tag">R</span>
        <span class="exercise-tag">NIKH Textbooks</span>
        <span class="exercise-tag">Word clouds</span>
        <span class="exercise-tag">Concordance</span>
      </div>
    </a>
  </div>

  <div class="exercise-card">
    <a href="{{ '/interactive/clustering-analysis' | relative_url }}">
      <div class="exercise-card-accent accent-violet"></div>
      <div class="exercise-card-body">
        <div class="exercise-card-week">Week 7</div>
        <div class="exercise-card-title">Clustering Korean History Textbooks</div>
        <p class="exercise-card-desc">Hierarchical clustering on TF-IDF vectors from 11 NIKH textbooks. See a dendrogram, compare cluster assignments to era labels, and explore which words make each cluster distinctive.</p>
      </div>
      <div class="exercise-card-footer">
        <span class="exercise-tag">R</span>
        <span class="exercise-tag">NIKH Textbooks</span>
        <span class="exercise-tag">Clustering</span>
        <span class="exercise-tag">TF-IDF</span>
      </div>
    </a>
  </div>

  <div class="exercise-card">
    <a href="{{ '/interactive/kmeans-speeches' | relative_url }}">
      <div class="exercise-card-accent accent-violet"></div>
      <div class="exercise-card-body">
        <div class="exercise-card-week">Week 7</div>
        <div class="exercise-card-title">K-Means Clustering: Presidential Speeches</div>
        <p class="exercise-card-desc">K-means on 749 democratic-era speeches. Use silhouette scores to choose <em>k</em>, then discover whether clusters group by president or by topic &mdash; with a surprising result.</p>
      </div>
      <div class="exercise-card-footer">
        <span class="exercise-tag">R</span>
        <span class="exercise-tag">Presidential Speeches</span>
        <span class="exercise-tag">K-Means</span>
        <span class="exercise-tag">Silhouette</span>
      </div>
    </a>
  </div>

</div>

</div>
