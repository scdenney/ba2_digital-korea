---
layout: default
title: "Final Assessment Exemplar — Clustering KJYG into Four Distinctive Voices"
---

<style>
:root { --leiden-blue: #001158; }

.exemplar-page { max-width: 100%; }
.exemplar-header { margin-top: 1rem; margin-bottom: 2rem; padding-bottom: 1.5rem; border-bottom: 2px solid #e2e8f0; }
.exemplar-header h1 { font-size: 1.6rem; color: var(--leiden-blue); margin: 0 0 0.5rem; line-height: 1.3; }
.exemplar-header .meta { font-size: 0.88rem; color: #6b7280; }
.exemplar-meta { font-size: 0.85rem; color: #6b7280; margin-top: 0.4rem; }

.callout { padding: 0.75rem 1rem; border-radius: 6px; margin: 1rem 0; font-size: 0.92rem; line-height: 1.6; border-left: 3px solid; }
.callout-info { background: #eff6ff; border-color: #3b82f6; color: #1e3a8a; }
.callout-tip  { background: #f0fdf4; border-color: #22c55e; color: #166534; }

.section-heading {
  margin: 2rem 0 0.6rem;
  padding-bottom: 0.4rem;
  border-bottom: 1px solid #e2e8f0;
  color: var(--leiden-blue);
  font-size: 1.2rem;
}

.figure-block { margin: 1.25rem 0 1.5rem; }
.figure-block img { width: 100%; max-width: 820px; display: block; margin: 0 auto; border: 1px solid #e2e8f0; border-radius: 6px; }
.figure-caption { font-size: 0.85rem; color: #6b7280; text-align: center; margin-top: 0.4rem; line-height: 1.5; }

.cluster-table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.92rem; }
.cluster-table th, .cluster-table td { padding: 0.55rem 0.7rem; border-bottom: 1px solid #e2e8f0; text-align: left; vertical-align: top; }
.cluster-table th { background: #f8fafc; color: var(--leiden-blue); font-weight: 700; }
.cluster-table td.id { font-weight: 700; color: var(--leiden-blue); width: 4rem; }
.cluster-table td.label { width: 12rem; font-weight: 600; }
.cluster-table td.words { font-family: ui-monospace, "SF Mono", Menlo, monospace; font-size: 0.84rem; color: #374151; }
.cluster-table td.num { text-align: right; font-variant-numeric: tabular-nums; width: 4rem; }
</style>

<div class="exemplar-page">

<div class="exemplar-header">
  <h1>Final Assessment Exemplar — Clustering KJYG into Four Distinctive Voices</h1>
  <div class="meta">A worked example for Task C of the Week 11 Final Assessment.</div>
  <div class="exemplar-meta">Dataset: <code>dataset1_kjyg_sample.csv</code> (360 articles, 120 per leader era) · Method: TF-IDF + Ward agglomerative clustering, cut at k = 4</div>
</div>

<div class="callout callout-info">
This page is an <strong>exemplar</strong>: it shows what an answer to Task C could look like end-to-end. The same pipeline runs in either Orange (Hierarchical Clustering widget on a TF-IDF Bag-of-Words output) or R (<code>hclust</code> on a TF-IDF document-term matrix) — what matters is the answer, not the tool.
</div>

<h2 class="section-heading">Research question</h2>

If we cluster the 360 *Kyongje Yongu* articles into a small number of groups by the words they use, what makes each cluster distinctive — both in vocabulary and in tone? Do the resulting clusters track the leader eras, or do they cut across them?

<h2 class="section-heading">Methods</h2>

I tokenized each article with Kiwi, kept only nouns, verbs, and adjectives (<code>NNG</code>, <code>NNP</code>, <code>VV</code>, <code>VA</code>) of length ≥ 2, then computed a TF-IDF document-term matrix (<code>min_df = 4</code>, <code>max_df = 0.5</code>, sublinear-TF). I ran agglomerative clustering with Ward linkage and cut the dendrogram at **k = 4**. To characterize each cluster, I computed the mean TF-IDF of every term *within* the cluster minus its mean TF-IDF *outside* the cluster, then took the top-10 distinctively over-represented terms. I also pulled in the per-document KNU sentiment score from the [Task A exemplar]({{ '/interactive/kjyg-final-exemplar' | relative_url }}) so that each cluster has a tone reading as well as a vocabulary reading.

<h2 class="section-heading">Findings</h2>

<div class="figure-block">
  <img src="kjyg_dendrogram.png" alt="Dendrogram from Ward-linkage hierarchical clustering of KJYG articles">
  <div class="figure-caption"><strong>Figure 1.</strong> Ward-linkage dendrogram on TF-IDF vectors (truncated to last 30 leaves; numbers in parentheses are leaf cluster sizes). Cutting at k = 4 yields the four colored branches.</div>
</div>

The four clusters and what makes each distinctive:

<table class="cluster-table">
  <thead>
    <tr><th>Cluster</th><th>My label</th><th>Top distinctive terms (TF-IDF over-representation)</th><th class="num">N</th><th class="num">Sent.</th></tr>
  </thead>
  <tbody>
    <tr>
      <td class="id">C1</td>
      <td class="label">Anti-imperialist polemic</td>
      <td class="words">자본주의 · 미국 · 자본 · 독점 · 제국주의 · 위기 · 시장 · 자본가 · 지배 · 미제</td>
      <td class="num">63</td>
      <td class="num">−0.005</td>
    </tr>
    <tr>
      <td class="id">C2</td>
      <td class="label">Technical / managerial economics</td>
      <td class="words">제품 · 계산 · 정보 · 효과 · 지출 · 수입 · 지표 · 자료 · 기업소 · 경영</td>
      <td class="num">193</td>
      <td class="num">+0.008</td>
    </tr>
    <tr>
      <td class="id">C3</td>
      <td class="label">Songun &amp; heavy-industry self-reliance</td>
      <td class="words">국방 · 혁명 · 선군 · 조국 · 공업 · 중공업 · 자립 · 민족 · 군사 · 대국</td>
      <td class="num">38</td>
      <td class="num">+0.013</td>
    </tr>
    <tr>
      <td class="id">C4</td>
      <td class="label">Mass-line collectivist ideology</td>
      <td class="words">주인 · 대중 · 지도 · 사상 · 집단 · 집단주의 · 의식 · 공산주의 · 경리 · 농촌</td>
      <td class="num">66</td>
      <td class="num">+0.013</td>
    </tr>
  </tbody>
</table>

The "Sent." column is the per-cluster mean of the KNU sentiment score from the Task A exemplar. **Cluster 1 is the only cluster with negative mean sentiment** — and the vocabulary makes the reason obvious: 위기 (crisis), 제국주의 (imperialism), 미제 (US imperialism), 독점 (monopoly), 지배 (domination). The negativity is not aimed at North Korea; it is aimed *at* capitalism and the United States. The other three clusters carry positive sentiment in roughly the same range.

<div class="figure-block">
  <img src="kjyg_cluster_era.png" alt="Heatmap showing within-cluster era distribution for the four clusters">
  <div class="figure-caption"><strong>Figure 2.</strong> Within-cluster era distribution. Each row sums to 100%. Two of the four clusters are strongly era-skewed (C4 is two-thirds Kim Il-sung; C3 is 58% Kim Jong-il); the other two are spread more evenly across eras.</div>
</div>

The clusters are partly era-aligned, and partly not — which is the more interesting finding:

- **C4 (mass-line collectivism)** is **67% Kim Il-sung** and only 14% Kim Jong-il, 20% Kim Jong-un. Mass-line / collectivist ideological vocabulary is concentrated in the late-Kim Il-sung period and largely fades after.
- **C3 (Songun &amp; heavy industry)** is **58% Kim Jong-il**, which is exactly when the Songun "military-first" doctrine was the operative state policy. This is a cluster that genuinely tracks an era because the vocabulary tracks an era.
- **C2 (technical / managerial economics — the largest cluster, n = 193)** is mostly evenly split, but **plurality Kim Jong-un (44%)**. The shift toward technical management language is consistent with the *우리식 경제관리방법* / "our-style economic management" rhetoric that became prominent after 2012.
- **C1 (anti-imperialist polemic)** sits roughly in the middle on era — it appears across all three periods, which fits its function: anti-US polemic is a steady-state register in *Kyongje Yongu*, not a feature of any one leader's economic program.

<h2 class="section-heading">Interpretation</h2>

What the clustering reveals is that *Kyongje Yongu* runs **at least four distinct registers** simultaneously, and that those registers are not fully reducible to "the era it was published in." Two of the four clusters — collectivist ideology and Songun rhetoric — really do peak in particular periods, and the peaks make historical sense. But the polemical register and the technical-managerial register are present in every era. A reader looking only at era-level summaries (as in Task A's sentiment exemplar) misses the fact that, in any given year, the journal is doing several different things at once. The Task A finding that Kim Jong-il-era articles are slightly more negative on average is itself partially explained here: the negative sentiment lives almost entirely in cluster C1, which is no more (or less) prevalent in the Kim Jong-il era than in the others; what changes is the *mix* of the other registers.

<h2 class="section-heading">Limitations and reflection</h2>

- **Cluster sizes are uneven.** C2 contains 54% of all articles. That suggests either a genuinely dominant register (technical economics is what the journal mostly does) or that the chosen distance + linkage simply pull a single mass into one cluster. Trying complete linkage or k-means at the same k would help check.
- **The sentiment column reads cluster-level tone, not document-level tone.** Within C1, some articles are far more negative than the −0.005 mean would suggest; the cluster summary glosses over that range.
- **The cluster labels are interpretive.** Calling C4 "mass-line collectivist ideology" rests on words like 대중 ("masses") and 집단주의 ("collectivism") together with reading a few high-TF-IDF documents from that cluster. A reader fluent in DPRK economic discourse might propose more precise labels.

<div class="callout callout-tip">
<strong>What makes this an "ideal" answer:</strong> short labels in the student's own words for each of the 3–5 clusters, distinctive vocabulary cited from the data (not just the top frequency words but TF-IDF over-representation), a tone reading attached to each cluster, and an interpretation that engages with whether and where the clusters track the obvious metadata variable (era).
</div>

</div>
