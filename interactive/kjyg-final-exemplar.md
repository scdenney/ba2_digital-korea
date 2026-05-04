---
layout: default
title: "Final Assessment Exemplar — KJYG Sentiment Across Leader Eras"
---

<style>
:root { --leiden-blue: #001158; --pos-green: #22863a; --neg-red: #b33030; --neu-gray: #6b7280; }

.exemplar-page { max-width: 100%; }
.exemplar-header { margin-top: 1rem; margin-bottom: 2rem; padding-bottom: 1.5rem; border-bottom: 2px solid #e2e8f0; }
.exemplar-header h1 { font-size: 1.6rem; color: var(--leiden-blue); margin: 0 0 0.5rem; line-height: 1.3; }
.exemplar-header .meta { font-size: 0.88rem; color: #6b7280; }
.exemplar-meta { font-size: 0.85rem; color: #6b7280; margin-top: 0.4rem; }

.callout { padding: 0.75rem 1rem; border-radius: 6px; margin: 1rem 0; font-size: 0.92rem; line-height: 1.6; border-left: 3px solid; }
.callout-info { background: #eff6ff; border-color: #3b82f6; color: #1e3a8a; }
.callout-tip  { background: #f0fdf4; border-color: #22c55e; color: #166534; }
.callout-warn { background: #fffbeb; border-color: #f59e0b; color: #92400e; }

.section-heading {
  margin: 2rem 0 0.6rem;
  padding-bottom: 0.4rem;
  border-bottom: 1px solid #e2e8f0;
  color: var(--leiden-blue);
  font-size: 1.2rem;
}

.figure-block { margin: 1.25rem 0 1.5rem; }
.figure-block img { width: 100%; max-width: 760px; display: block; margin: 0 auto; border: 1px solid #e2e8f0; border-radius: 6px; }
.figure-caption { font-size: 0.85rem; color: #6b7280; text-align: center; margin-top: 0.4rem; line-height: 1.5; }

.summary-table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.92rem; }
.summary-table th, .summary-table td { padding: 0.5rem 0.75rem; border-bottom: 1px solid #e2e8f0; text-align: left; }
.summary-table th { background: #f8fafc; color: var(--leiden-blue); font-weight: 700; }
.summary-table td.num { text-align: right; font-variant-numeric: tabular-nums; }
</style>

<div class="exemplar-page">

<div class="exemplar-header">
  <h1>Final Assessment Exemplar — KJYG Sentiment Across Leader Eras</h1>
  <div class="meta">A worked example for Task A of the Week 11 Final Assessment. Shows what a complete, well-supported answer looks like.</div>
  <div class="exemplar-meta">Dataset: <code>dataset1_kjyg_sample.csv</code> (360 articles, balanced 120 per era) · Method: KNU sentiment dictionary on Kiwi-tokenized text (NNG/NNP/VV/VA)</div>
</div>

<div class="callout callout-info">
This page is an <strong>exemplar</strong>: it shows what an answer to Task A could look like end-to-end, not a tutorial in how to use Orange. Use it as a reference for the level of analysis and write-up I'm looking for. The same pipeline runs in either Orange or R — what matters is the answer, not the tool.
</div>

<h2 class="section-heading">Research question</h2>

Is the sentiment of *Kyongje Yongu* (경제연구) articles measurably different across the three NK leader eras (Kim Il-sung, Kim Jong-il, Kim Jong-un)? If so, in which direction does the difference run?

<h2 class="section-heading">Methods</h2>

For each of the 360 articles in the sample (120 per era), I tokenized the text with **Kiwi** keeping nouns, verbs, and adjectives (POS tags `NNG`, `NNP`, `VV`, `VA` — the standard sentiment-preprocessing filter). I then matched each token against the **KNU sentiment dictionary** (4,868 positive entries, 9,824 negative entries) and computed a per-document score:

<div style="text-align: center; font-style: italic; margin: 0.75rem 0;">
score = (positive_hits − negative_hits) / number_of_tokens
</div>

Normalizing by token count keeps long and short articles on the same scale. I aggregated by `era` and ran pairwise Welch t-tests across the three eras.

<h2 class="section-heading">Findings</h2>

<div class="figure-block">
  <img src="kjyg_sentiment_boxplot.png" alt="Box plot of KNU sentiment scores by leader era">
  <div class="figure-caption"><strong>Figure 1.</strong> KJYG sentiment distribution by leader era. Boxes show interquartile range; black bar is the median; red diamond is the mean. Dashed line at zero. All three eras span both positive and negative articles, but the means differ.</div>
</div>

<table class="summary-table">
  <thead>
    <tr><th>Era</th><th class="num">N</th><th class="num">Mean</th><th class="num">Median</th><th class="num">SD</th></tr>
  </thead>
  <tbody>
    <tr><td>Kim Il-sung (1987–1994)</td><td class="num">120</td><td class="num">+0.011</td><td class="num">+0.008</td><td class="num">0.027</td></tr>
    <tr><td>Kim Jong-il (1995–2011)</td><td class="num">120</td><td class="num">+0.003</td><td class="num">+0.003</td><td class="num">0.025</td></tr>
    <tr><td>Kim Jong-un (2012–2017)</td><td class="num">120</td><td class="num">+0.007</td><td class="num">+0.010</td><td class="num">0.029</td></tr>
  </tbody>
</table>

The pattern is **U-shaped, not monotonic**. The Kim Il-sung sample has the highest mean sentiment (+0.011); the Kim Jong-il sample has the lowest (+0.003); Kim Jong-un sits between (+0.007). The Kim Il-sung vs.\ Kim Jong-il gap is statistically distinguishable (Welch t = +2.35, p = 0.020). The other two pairs are not (p = 0.26 and 0.29).

<div class="figure-block">
  <img src="kjyg_sentiment_yearly.png" alt="Year-by-year mean KNU sentiment, 1987-2017">
  <div class="figure-caption"><strong>Figure 2.</strong> Mean sentiment by publication year, 1987–2017. Vertical dotted lines mark the leader transitions (1994/95, 2011/12). The deepest negative valence appears in the late 1990s — coinciding with the Arduous March famine (1995–1998) and the early Songun-policy years.</div>
</div>

<h2 class="section-heading">Interpretation</h2>

The headline finding is **not** the simple "Kim Jong-un era is more positive" reading the brief gestured at as a hypothesis. The sentiment dip lands squarely in the **late 1990s**, the years of the *Arduous March* (고난의 행군) famine and Songun-first crisis rhetoric. Articles in those years lean noticeably more negative on the KNU score, pulling the Kim Jong-il era's mean down. The Kim Jong-un era partially recovers — consistent with the more market-tolerant *우리식 경제관리방법* rhetoric that appeared after 2012 — but does not exceed the late Kim Il-sung baseline.

<h2 class="section-heading">Limitations and reflection</h2>

A few things worth flagging in any write-up of this analysis:

- **The KNU dictionary is contemporary South Korean.** Some valence-bearing vocabulary specific to NK economic discourse (e.g., the language of self-criticism, struggle, mass mobilization) is partially captured at best. The score is suggestive, not authoritative.
- **The score is small in absolute terms.** Means cluster between 0.003 and 0.011 — that is, between roughly 3 and 11 net polarity-bearing tokens per 1,000. A reader should not interpret these as "the Kim Il-sung era was overwhelmingly positive"; the right reading is that *relative* to the other periods, it carried a slightly higher density of positive valence.
- **The yearly trend is noisier than the era-level summary.** Some years have only a handful of articles; year-to-year wobble is partly sampling noise.

<div class="callout callout-tip">
<strong>What makes this an "ideal" answer:</strong> a clear research question, a method described before results are shown, a figure that supports the headline claim with a labeled caption referenced in the text, an interpretation that connects the empirical pattern to known historical context, and an honest discussion of what the method does and does not measure.
</div>

</div>
