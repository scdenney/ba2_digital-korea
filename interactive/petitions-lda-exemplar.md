---
layout: default
title: "Final Assessment Exemplar — Petition Topics Across Categories"
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

.topic-table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.92rem; }
.topic-table th, .topic-table td { padding: 0.5rem 0.7rem; border-bottom: 1px solid #e2e8f0; text-align: left; vertical-align: top; }
.topic-table th { background: #f8fafc; color: var(--leiden-blue); font-weight: 700; }
.topic-table td.id { font-weight: 700; color: var(--leiden-blue); width: 4.5rem; }
.topic-table td.label { width: 11rem; font-weight: 600; }
.topic-table td.words { font-family: ui-monospace, "SF Mono", Menlo, monospace; font-size: 0.86rem; color: #374151; }
</style>

<div class="exemplar-page">

<div class="exemplar-header">
  <h1>Final Assessment Exemplar — Petition Topics Across Categories</h1>
  <div class="meta">A worked example for Task B of the Week 11 Final Assessment.</div>
  <div class="exemplar-meta">Dataset: <code>dataset2_bluehouse_petitions_sample.csv</code> (360 petitions, balanced 60 per category) · Method: LDA (k=8) on Kiwi-tokenized text (NNG/NNP/VV/VA)</div>
</div>

<div class="callout callout-info">
This page is an <strong>exemplar</strong>: it shows what an answer to Task B could look like end-to-end. The same pipeline runs in either Orange (LDA widget on a preprocessed corpus) or R (<code>topicmodels</code> on a document-term matrix) — what matters is the answer, not the tool.
</div>

<h2 class="section-heading">Research question</h2>

What latent topics run through the Cheong Wa Dae citizen petitions, and how cleanly do those topics map onto the six official policy categories? Some topics should align tightly with one category; others should cross-cut several.

<h2 class="section-heading">Methods</h2>

I tokenized each petition with Kiwi, kept only nouns, verbs, and adjectives (<code>NNG</code>, <code>NNP</code>, <code>VV</code>, <code>VA</code>) of length ≥ 2, then count-vectorized with <code>min_df = 5</code>, <code>max_df = 0.6</code>. I fit LDA at **k = 8** — deliberately more topics than the six official categories, so that at least one or two topics could plausibly cross-cut. After fitting, I aggregated the document-topic distribution by `category` and took the mean topic share within each category.

<h2 class="section-heading">Findings</h2>

Eight topics; my plain-language labels and the top-10 words per topic are below. Labels are my own — assigned after reading both the top words and a handful of high-share documents from each topic.

<table class="topic-table">
  <thead>
    <tr><th>Topic</th><th>My label</th><th>Top words (Korean)</th></tr>
  </thead>
  <tbody>
    <tr><td class="id">T0</td><td class="label">Civil-service jobs &amp; work hours</td><td class="words">공무원 · 의무 · 기간 · 시간 · 일자리 · 근무 · 교육 · 기업</td></tr>
    <tr><td class="id">T1</td><td class="label">Schools &amp; childcare</td><td class="words">아이 · 교육 · 학교 · 유치원 · 선생 · 키우 · 장애인</td></tr>
    <tr><td class="id">T2</td><td class="label">Hospitals, patients, medicine</td><td class="words">병원 · 환자 · 의료 · 시험 · 인권 · 치료 · 논란</td></tr>
    <tr><td class="id">T3</td><td class="label">Gender, women, punishment</td><td class="words">여성 · 남성 · 사회 · 청소년 · 처벌 · 이유</td></tr>
    <tr><td class="id">T4</td><td class="label">Wrongdoing, victims, foreign actors</td><td class="words">사람 · 회사 · 일본 · 불법 · 피해자 · 학생 · 처벌</td></tr>
    <tr><td class="id">T5</td><td class="label">Inter-Korean &amp; presidential politics</td><td class="words">국민 · 나라 · 북한 · 한국 · 미국 · 대통령 · 정치 · 의원</td></tr>
    <tr><td class="id">T6</td><td class="label">Schoolwork &amp; teachers</td><td class="words">시간 · 학생 · 교사 · 학교 · 채용 · 수업 · 운영</td></tr>
    <tr><td class="id">T7</td><td class="label">Pensions &amp; the state</td><td class="words">국민 · 국가 · 연금 · 청원 · 대통령 · 국민연금 · 대한민국</td></tr>
  </tbody>
</table>

<div class="figure-block">
  <img src="petitions_topic_heatmap.png" alt="Heatmap of mean LDA topic share by official petition category">
  <div class="figure-caption"><strong>Figure 1.</strong> Mean LDA topic share by official petition category (rows: category; columns: topic; cell = mean of doc-topic posterior). Darker cells mark categories where that topic's words concentrate; light cells mean the topic is rare in that category.</div>
</div>

The picture is mixed — exactly what the task asked for.

**Topics that align cleanly with one category.** Topic 0 (civil-service jobs / work hours) is heavily concentrated in **Jobs** (mean share = 0.33, the highest cell in the matrix). Topic 1 (schools and childcare) and Topic 6 (schoolwork and teachers) both peak in **Childcare / education** (0.22 and 0.21). Topic 2 (hospitals, patients, medicine) peaks in **Health and welfare** (0.23). And Topic 3 (gender / women / punishment) is sharply concentrated in **Human rights / gender equality** (0.41 — the single highest cell in the whole heatmap).

**Topics that cross-cut.** Topic 5 — inter-Korean and presidential politics — is the cleanest cross-cutting case: it sits at 0.27 in **Political reform** and 0.25 in **Foreign affairs / unification / defense**, and is essentially absent from every other category. The shared vocabulary (대통령 "president," 정치 "politics," 북한 "North Korea") really does belong to *both* categories — petitions about the executive branch and petitions about North-South relations talk in similar words. Topic 4 (wrongdoing, victims, foreign actors — 사람, 일본, 피해자) is also broadly cross-cutting, with shares of 0.21 across **Foreign**, **Human rights**, and **Political reform**.

<div class="figure-block">
  <img src="petitions_sharpest_topic.png" alt="Bar chart showing concentration of topic T3 (gender / punishment) by category">
  <div class="figure-caption"><strong>Figure 2.</strong> Where topic T3 ("gender, women, punishment") concentrates. Petitions in <em>Human rights / gender equality</em> have a mean T3 share of 0.41 — about three to four times the share in any other category. T3 is the topic with the highest cross-category variance in the matrix, and the cleanest one-to-one alignment with an official category.</div>
</div>

<h2 class="section-heading">Interpretation</h2>

LDA recovers the categorical structure that the Cheong Wa Dae platform's editors put in place — but not perfectly, and the exceptions are where the analysis earns its keep. Five of the eight topics line up tightly with single categories, which is consistent with the categories being meaningful semantic boundaries rather than bureaucratic conveniences. The two cleanly cross-cutting topics (T5 and T4) reveal that political and foreign-policy petitions share a lot of vocabulary, while human-rights and political-reform petitions share *some* vocabulary about wrongdoing and victims. That second overlap is interesting — it suggests citizens framed their grievances about institutional accountability and individual victimhood in overlapping language regardless of which bucket they filed in.

<h2 class="section-heading">Limitations and reflection</h2>

- **Topic count is a choice, not a discovery.** I used k = 8. At k = 6 the topics collapse toward the official categories and the cross-cutting picture disappears. At k = 12 several topics fragment into near-duplicates. Reporting that the cross-cutting result is robust would require running coherence diagnostics across several values of k.
- **Topic labels are interpretive.** The "gender, women, punishment" label for T3 is *my* reading of the top words plus a few high-share documents. A different reader might call it "sexual-violence policy" — both readings are defensible; neither is forced by the math.
- **Mean topic shares smooth over within-category variation.** The petitioners in any single category are not a monolith; a heatmap of means hides outlier petitions whose topic mix looks nothing like the rest of their category.

<div class="callout callout-tip">
<strong>What makes this an "ideal" answer:</strong> labeled topics in plain language, a figure that supports the headline claim with a captioned reference, identification of <em>both</em> a tight category-topic alignment <em>and</em> a clean cross-cutting topic, and an honest note about the choice points (k, topic labels) that shape the result.
</div>

</div>
