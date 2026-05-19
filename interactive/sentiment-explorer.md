---
layout: default
title: "Sentiment Analysis: Moon Jae-in's Tweets"
---

<style>
/* ── Page layout ─────────────────────────────────────────────────── */
.tutorial-page { --leiden-blue: #001158; --pos-green: #22863a; --neg-red: #b33030; --neu-gray: #6b7280; }
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

/* ── Narrative text ──────────────────────────────────────────────── */
.narrative {
  font-size: 0.95rem;
  line-height: 1.7;
  color: #374151;
  margin: 1rem 0;
}

.narrative strong { color: var(--leiden-blue); }

/* ── Callouts ────────────────────────────────────────────────────── */
.callout { padding: 0.75rem 1rem; border-radius: 6px; margin: 1rem 0; font-size: 0.88rem; line-height: 1.6; }
.callout-info { background: #eff6ff; border-left: 3px solid #3b82f6; color: #1e40af; }
.callout-tip { background: #f0fdf4; border-left: 3px solid #22c55e; color: #166534; }
.callout-warn { background: #fffbeb; border-left: 3px solid #f59e0b; color: #92400e; }

/* ── R code ribbons ──────────────────────────────────────────────── */
.code-ribbon { border: 1px solid #e2e8f0; border-radius: 8px; margin: 1rem 0; overflow: hidden; }
.code-ribbon summary {
  display: flex; align-items: center; gap: 0.5rem; padding: 0.6rem 1rem;
  background: linear-gradient(to right, #1e293b, #334155);
  cursor: pointer; list-style: none; user-select: none;
}
.code-ribbon summary::-webkit-details-marker { display: none; }
.code-ribbon summary::before { content: "\25B6"; color: #94a3b8; font-size: 0.7rem; transition: transform 0.2s; }
.code-ribbon[open] summary::before { transform: rotate(90deg); }
.ribbon-label { color: #e2e8f0; font-size: 0.85rem; font-weight: 600; flex: 1; }
.ribbon-tag { background: #3b82f6; color: #fff; font-size: 0.7rem; font-weight: 700; padding: 0.15rem 0.5rem; border-radius: 10px; }
.code-ribbon-body { padding: 0.75rem 1rem; background: #f8fafc; }
.code-block { border: 1px solid #e2e8f0; border-radius: 6px; overflow: hidden; margin: 0.5rem 0; }
.code-block-header {
  display: flex; justify-content: space-between; align-items: center;
  padding: 0.35rem 0.75rem; background: #1e293b; color: #94a3b8; font-size: 0.75rem; font-weight: 600;
}
.copy-btn {
  background: transparent; border: 1px solid #475569; color: #94a3b8;
  padding: 0.15rem 0.5rem; border-radius: 4px; font-size: 0.7rem; cursor: pointer; font-family: inherit;
}
.copy-btn:hover { border-color: #94a3b8; color: #e2e8f0; }
.copy-btn.copied { background: #166534; border-color: #22c55e; color: #22c55e; }
.code-block pre {
  margin: 0; padding: 0.75rem; background: #0f172a; overflow-x: auto;
  font-size: 0.82rem; line-height: 1.55;
}
.code-block pre code { color: #e2e8f0; font-family: "SF Mono", "Fira Code", "Consolas", monospace; }
.r-comment { color: #94a3b8; font-style: italic; }
.r-string { color: #86efac; }
.r-function { color: #93c5fd; }
.r-keyword { color: #c4b5fd; }
.r-number { color: #fde68a; }
.r-operator { color: #f9a8d4; }

/* ── Scoring walkthrough ─────────────────────────────────────────── */
.example-selector { display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.75rem 0; }
.example-btn {
  padding: 0.35rem 0.7rem; border-radius: 20px; border: 2px solid #e2e8f0;
  background: #f8fafc; font-size: 0.8rem; font-weight: 600;
  cursor: pointer; transition: all 0.2s; font-family: inherit; color: #374151;
}
.example-btn:hover { border-color: var(--leiden-blue); }
.example-btn.active { background: var(--leiden-blue); color: #fff; border-color: var(--leiden-blue); }
.scoring-card { border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; margin: 0.75rem 0; }
.scoring-tweet { padding: 0.75rem 1rem; background: #f8fafc; border-bottom: 1px solid #e2e8f0; font-size: 0.95rem; line-height: 1.6; }
.scoring-tweet .meta { font-size: 0.75rem; color: #9ca3af; margin-bottom: 0.3rem; }

/* ── Histogram bars ──────────────────────────────────────────────── */
.hist-bar-row { display: flex; align-items: center; gap: 0.4rem; margin-bottom: 0.15rem; }
.hist-label { width: 28px; font-size: 0.75rem; text-align: right; color: #374151; flex-shrink: 0; font-weight: 600; }
.hist-bar-track { flex: 1; height: 18px; background: #f1f5f9; border-radius: 3px; overflow: hidden; }
.hist-bar-fill { height: 100%; border-radius: 3px; transition: width 0.4s; }
.hist-count { font-size: 0.7rem; color: #6b7280; width: 36px; flex-shrink: 0; }

/* ── Period toggle ───────────────────────────────────────────────── */
.period-toggle { display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.75rem 0; }
.period-btn {
  padding: 0.35rem 0.7rem; border-radius: 20px; border: 2px solid #e2e8f0;
  background: #fff; font-size: 0.8rem; font-weight: 600;
  cursor: pointer; transition: all 0.2s; font-family: inherit; color: #374151;
}
.period-btn:hover { border-color: currentColor; }
.period-btn.active { box-shadow: 0 1px 4px rgba(0,0,0,0.1); }
.period-dot { display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 0.3rem; vertical-align: middle; }

/* ── Box plot ────────────────────────────────────────────────────── */
.box-row { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.75rem; }
.box-label { width: 110px; font-size: 0.82rem; text-align: right; color: #374151; flex-shrink: 0; font-weight: 600; }
.box-track { flex: 1; height: 32px; position: relative; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; }
.box-whisker { position: absolute; top: 50%; height: 2px; background: #94a3b8; transform: translateY(-50%); }
.box-rect { position: absolute; top: 4px; bottom: 4px; border-radius: 3px; border: 2px solid; }
.box-median { position: absolute; top: 2px; bottom: 2px; width: 3px; background: #1e293b; border-radius: 1px; transform: translateX(-1px); }
.box-stat { font-size: 0.72rem; color: #6b7280; width: 70px; flex-shrink: 0; }

/* ── Timeline canvas ─────────────────────────────────────────────── */
.chart-container {
  position: relative; border: 1px solid #e2e8f0; border-radius: 8px;
  overflow: hidden; background: #fafbfc; max-width: 760px; margin: 1rem auto;
}
#mainCanvas { display: block; width: 100%; }
.chart-tooltip {
  display: none; position: absolute; background: rgba(15,23,42,0.92);
  color: #f1f5f9; padding: 0.4rem 0.65rem; border-radius: 5px;
  font-size: 0.75rem; line-height: 1.45; pointer-events: none;
  z-index: 10; max-width: 340px;
}

/* ── Top words ───────────────────────────────────────────────────── */
.word-cols { display: flex; gap: 1.5rem; }
.word-col { flex: 1; }
.word-col h4 { font-size: 0.82rem; margin: 0 0 0.5rem; }
.word-bar-row { display: flex; align-items: center; gap: 0.35rem; margin-bottom: 0.2rem; }
.word-bar-label { width: 55px; font-size: 0.8rem; text-align: right; flex-shrink: 0; font-weight: 600; }
.word-bar-track { flex: 1; height: 16px; background: #f1f5f9; border-radius: 3px; overflow: hidden; }
.word-bar-fill { height: 100%; border-radius: 3px; }
.word-bar-count { font-size: 0.68rem; color: #6b7280; width: 30px; flex-shrink: 0; }

/* ── Tweet list ──────────────────────────────────────────────────── */
.sort-controls { display: flex; align-items: center; gap: 0.5rem; margin: 0.75rem 0; font-size: 0.85rem; }
.sort-controls label { color: #6b7280; font-weight: 600; }
.sort-controls select {
  padding: 0.35rem 0.6rem; border: 1px solid #dfe3ee; border-radius: 6px;
  font-size: 0.85rem; font-family: inherit; background: #fff; cursor: pointer;
}
.tweet-list { max-height: 400px; overflow-y: auto; border: 1px solid #e2e8f0; border-radius: 8px; }
.tweet-item { padding: 0.6rem 0.75rem; border-bottom: 1px solid #f1f5f9; font-size: 0.85rem; line-height: 1.5; cursor: default; transition: background 0.15s; }
.tweet-item:hover { background: #f8fafc; }
.tweet-item:last-child { border-bottom: none; }
.tweet-item .tweet-score { display: inline-block; min-width: 30px; text-align: center; font-weight: 700; padding: 0.1rem 0.4rem; border-radius: 10px; font-size: 0.78rem; margin-right: 0.5rem; }
.tweet-item .tweet-score.score-pos { background: #dcfce7; color: var(--pos-green); }
.tweet-item .tweet-score.score-neg { background: #fee2e2; color: var(--neg-red); }
.tweet-item .tweet-score.score-neu { background: #f1f5f9; color: var(--neu-gray); }
.tweet-item .tweet-meta { font-size: 0.72rem; color: #9ca3af; margin-top: 0.2rem; }
.tweet-item .match-word { font-size: 0.72rem; padding: 0.05rem 0.3rem; border-radius: 8px; margin: 0 0.1rem; }
.tweet-item .match-pos { background: #dcfce7; color: var(--pos-green); }
.tweet-item .match-neg { background: #fee2e2; color: var(--neg-red); }

/* ── Loading state ───────────────────────────────────────────────── */
.loading-msg { color: #6b7280; font-size: 0.9rem; font-style: italic; }

@media (max-width: 600px) {
  .tutorial-header h1 { font-size: 1.3rem; }
  .word-cols { flex-direction: column; }
}
</style>

<div class="tutorial-page" id="app">

<div class="tutorial-header">
  <h1>Sentiment Analysis: Moon Jae-in's Tweets</h1>
  <p class="tutorial-subtitle">Explore how dictionary-based sentiment analysis scores 3,148 tweets from President Moon Jae-in's Twitter account (@moonriver365, 2012&ndash;2020). Each tweet is tokenized with Kiwi, then matched against the KNU sentiment dictionary.</p>
  <div class="tutorial-meta">
    <span>Week 9</span>
    <span>Kiwi + KNU sentiment dictionary</span>
    <span>3,148 tweets, 3 periods</span>
  </div>
</div>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">1</span>
  <h2>The Corpus</h2>
</div>

<p class="narrative">
  The <strong>@moonriver365</strong> corpus has 3,148 tweets from 2012 to 2020, sorted into three political periods. Before we score anything, here's what the corpus looks like year by year.
</p>

<div class="callout callout-info">
  <strong>The three periods are Dr. Denney's editorial groupings</strong>, not an official classification. Another researcher could cut the timeline differently.<br><br>
  <span style="display:inline-block;width:12px;height:12px;border-radius:2px;background:#6366f1;vertical-align:middle;margin-right:4px;"></span><strong>Pre-presidency</strong> (2012-01 &rarr; 2016-11, 1,973 tweets) &mdash; Moon as opposition leader: 2012 campaign, Democratic Party chairmanship, legislative politics.<br>
  <span style="display:inline-block;width:12px;height:12px;border-radius:2px;background:#f59e0b;vertical-align:middle;margin-right:4px;"></span><strong>Transition</strong> (2016-12 &rarr; 2017-05, 393 tweets) &mdash; Park Geun-hye impeachment crisis through Moon's early presidential campaign and inauguration (May 10, 2017).<br>
  <span style="display:inline-block;width:12px;height:12px;border-radius:2px;background:#10b981;vertical-align:middle;margin-right:4px;"></span><strong>Presidency</strong> (2017-05 &rarr; 2020-06, 782 tweets) &mdash; Moon in office: inter-Korean summits (2018), Japan trade dispute (2019), COVID-19 (2020).
</div>

<div id="corpusChart"><p class="loading-msg">Loading tweet data&hellip;</p></div>

<div class="callout callout-info">Moon was most active on Twitter during his 2012 presidential campaign. After taking office in May 2017, his tweeting dropped sharply &mdash; the official Cheong Wa Dae account took over most communication.</div>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: load and count the corpus</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-function">library</span>(tidyverse)
<span class="r-function">library</span>(tidytext)

<span class="r-comment"># Load the tweet corpus</span>
tweets <span class="r-operator">&lt;-</span> <span class="r-function">read_csv</span>(<span class="r-string">"moon_twitter.csv"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">filter</span>(<span class="r-operator">!</span><span class="r-function">is.na</span>(text)) <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(
    tweet_id <span class="r-operator">=</span> <span class="r-function">row_number</span>(),
    text <span class="r-operator">=</span> text <span class="r-operator">|&gt;</span>
      <span class="r-function">str_remove_all</span>(<span class="r-string">"https?://\\S+"</span>) <span class="r-operator">|&gt;</span>  <span class="r-comment"># URLs</span>
      <span class="r-function">str_remove_all</span>(<span class="r-string">"@\\w+"</span>) <span class="r-operator">|&gt;</span>             <span class="r-comment"># @mentions</span>
      <span class="r-function">str_trim</span>()
  )

<span class="r-comment"># Tweets per year, split by period</span>
tweets <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(tweet_year, period3) <span class="r-operator">|&gt;</span>
  <span class="r-function">ggplot</span>(<span class="r-function">aes</span>(x <span class="r-operator">=</span> tweet_year, y <span class="r-operator">=</span> n, fill <span class="r-operator">=</span> period3)) <span class="r-operator">+</span>
  <span class="r-function">geom_col</span>() <span class="r-operator">+</span>
  <span class="r-function">scale_fill_manual</span>(values <span class="r-operator">=</span> <span class="r-function">c</span>(
    pre_presidency <span class="r-operator">=</span> <span class="r-string">"#6366f1"</span>,
    transition <span class="r-operator">=</span> <span class="r-string">"#f59e0b"</span>,
    presidency <span class="r-operator">=</span> <span class="r-string">"#10b981"</span>)) <span class="r-operator">+</span>
  <span class="r-function">labs</span>(title <span class="r-operator">=</span> <span class="r-string">"Moon Jae-in tweets per year"</span>,
       x <span class="r-operator">=</span> <span class="r-string">""</span>, y <span class="r-operator">=</span> <span class="r-string">"Tweets"</span>) <span class="r-operator">+</span>
  <span class="r-function">theme_minimal</span>()</code></pre>
    </div>
    <div class="callout callout-tip">This is the R-equivalent of Orange's <strong>Corpus</strong> widget loading the CSV. We add a <code>tweet_id</code> for joining later and clean URLs/mentions, then count tweets per year colored by period.</div>
  </div>
</details>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">2</span>
  <h2>Dictionary Scoring</h2>
</div>

<p class="narrative">
  How one tweet becomes a sentiment score: look up each word in the positive and negative lists. Pick a tweet below to see the words that matched the KNU positive or negative list, then compute the score.
</p>

<div id="scoringSection"><p class="loading-msg">Loading examples&hellip;</p></div>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: tidytext-style sentiment scoring with KNU</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-function">library</span>(tidyverse)
<span class="r-function">library</span>(tidytext)
<span class="r-function">library</span>(elbird)  <span class="r-comment"># Kiwi wrapper for R (Korean morphological analyzer)</span>

<span class="r-comment"># 1. Build the KNU sentiment lexicon as a tibble</span>
knu <span class="r-operator">&lt;-</span> <span class="r-function">bind_rows</span>(
  <span class="r-function">tibble</span>(word <span class="r-operator">=</span> <span class="r-function">read_lines</span>(<span class="r-string">"positive.txt"</span>), sentiment <span class="r-operator">=</span> <span class="r-string">"positive"</span>),
  <span class="r-function">tibble</span>(word <span class="r-operator">=</span> <span class="r-function">read_lines</span>(<span class="r-string">"negative.txt"</span>), sentiment <span class="r-operator">=</span> <span class="r-string">"negative"</span>)
) <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(word <span class="r-operator">=</span> <span class="r-function">str_trim</span>(word)) <span class="r-operator">|&gt;</span>
  <span class="r-function">filter</span>(word <span class="r-operator">!=</span> <span class="r-string">""</span>)

<span class="r-comment"># 2. Kiwi tokenize tweets, keep content words</span>
tokens <span class="r-operator">&lt;-</span> tweets <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(toks <span class="r-operator">=</span> <span class="r-function">map</span>(text, <span class="r-operator">~</span><span class="r-function">tokenize</span>(.x, flatten <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>))) <span class="r-operator">|&gt;</span>
  <span class="r-function">unnest</span>(toks) <span class="r-operator">|&gt;</span>
  <span class="r-function">filter</span>(
    tag <span class="r-operator">%in%</span> <span class="r-function">c</span>(<span class="r-string">"NNG"</span>, <span class="r-string">"NNP"</span>, <span class="r-string">"VA"</span>, <span class="r-string">"VV"</span>),
    <span class="r-function">str_length</span>(form) <span class="r-operator">&gt;=</span> <span class="r-number">2</span>
  ) <span class="r-operator">|&gt;</span>
  <span class="r-function">select</span>(tweet_id, period3, tweet_date, word <span class="r-operator">=</span> form)

<span class="r-comment"># 3. tidytext-style sentiment: inner_join + count + pivot</span>
sentiment_scores <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span>
  <span class="r-function">inner_join</span>(knu, by <span class="r-operator">=</span> <span class="r-string">"word"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(tweet_id, period3, tweet_date, sentiment) <span class="r-operator">|&gt;</span>
  <span class="r-function">pivot_wider</span>(names_from <span class="r-operator">=</span> sentiment, values_from <span class="r-operator">=</span> n,
              values_fill <span class="r-operator">=</span> <span class="r-number">0</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(score <span class="r-operator">=</span> positive <span class="r-operator">-</span> negative)

<span class="r-function">head</span>(sentiment_scores)</code></pre>
    </div>
    <div class="callout callout-tip"><strong>In Orange</strong> (what you'll build): load <code>positive.txt</code> and <code>negative.txt</code> into Sentiment Analysis &rarr; Custom Dictionary. <strong>In R</strong>: the code above uses tidytext's <code>inner_join</code> pattern with a simpler <code>positive - negative</code> count. Exact numbers differ but rankings agree.</div>
  </div>
</details>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">3</span>
  <h2>Score Distribution</h2>
</div>

<p class="narrative">
  Distribution of sentiment scores across all tweets. Many tweets have no dictionary matches and score zero; the rest lean positive. Toggle periods to see how presidential communication differs from pre-presidency.
</p>

<div id="distSection"><p class="loading-msg">Loading distribution&hellip;</p></div>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: plot score distribution</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># Histogram of sentiment scores</span>
<span class="r-function">ggplot</span>(scored, <span class="r-function">aes</span>(x <span class="r-operator">=</span> score)) <span class="r-operator">+</span>
  <span class="r-function">geom_histogram</span>(binwidth <span class="r-operator">=</span> <span class="r-number">1</span>, fill <span class="r-operator">=</span> <span class="r-string">"#6366f1"</span>, alpha <span class="r-operator">=</span> <span class="r-number">0.7</span>,
                 color <span class="r-operator">=</span> <span class="r-string">"white"</span>) <span class="r-operator">+</span>
  <span class="r-function">labs</span>(title <span class="r-operator">=</span> <span class="r-string">"Sentiment Score Distribution"</span>,
       x <span class="r-operator">=</span> <span class="r-string">"Score (positive - negative)"</span>, y <span class="r-operator">=</span> <span class="r-string">"Count"</span>) <span class="r-operator">+</span>
  <span class="r-function">theme_minimal</span>()

<span class="r-comment"># Faceted by period</span>
<span class="r-function">ggplot</span>(scored, <span class="r-function">aes</span>(x <span class="r-operator">=</span> score, fill <span class="r-operator">=</span> period3)) <span class="r-operator">+</span>
  <span class="r-function">geom_histogram</span>(binwidth <span class="r-operator">=</span> <span class="r-number">1</span>, alpha <span class="r-operator">=</span> <span class="r-number">0.7</span>, color <span class="r-operator">=</span> <span class="r-string">"white"</span>) <span class="r-operator">+</span>
  <span class="r-function">facet_wrap</span>(<span class="r-operator">~</span> period3, ncol <span class="r-operator">=</span> <span class="r-number">1</span>) <span class="r-operator">+</span>
  <span class="r-function">scale_fill_manual</span>(values <span class="r-operator">=</span> <span class="r-function">c</span>(
    pre_presidency <span class="r-operator">=</span> <span class="r-string">"#6366f1"</span>,
    transition <span class="r-operator">=</span> <span class="r-string">"#f59e0b"</span>,
    presidency <span class="r-operator">=</span> <span class="r-string">"#10b981"</span>)) <span class="r-operator">+</span>
  <span class="r-function">theme_minimal</span>() <span class="r-operator">+</span>
  <span class="r-function">theme</span>(legend.position <span class="r-operator">=</span> <span class="r-string">"none"</span>)</code></pre>
    </div>
    <div class="callout callout-tip"><strong>In Orange:</strong> connect <strong>Score Documents</strong> to a <strong>Distributions</strong> widget and select the score column.</div>
  </div>
</details>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">4</span>
  <h2>By Period</h2>
</div>

<p class="narrative">
  Comparing sentiment across Moon Jae-in's three political periods. The <strong>box</strong> shows the middle 50% of scores, the <strong>line</strong> inside the box is the median, the <strong>diamond</strong> marks the mean, and <strong>whiskers</strong> show the score range.
</p>

<div id="periodSection"><p class="loading-msg">Loading period data&hellip;</p></div>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: box plot by period</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># Box plot comparing periods</span>
scored <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(period3 <span class="r-operator">=</span> <span class="r-function">factor</span>(period3,
    levels <span class="r-operator">=</span> <span class="r-function">c</span>(<span class="r-string">"pre_presidency"</span>, <span class="r-string">"transition"</span>, <span class="r-string">"presidency"</span>))) <span class="r-operator">|&gt;</span>
  <span class="r-function">ggplot</span>(<span class="r-function">aes</span>(x <span class="r-operator">=</span> period3, y <span class="r-operator">=</span> score, fill <span class="r-operator">=</span> period3)) <span class="r-operator">+</span>
  <span class="r-function">geom_boxplot</span>(alpha <span class="r-operator">=</span> <span class="r-number">0.7</span>, outlier.alpha <span class="r-operator">=</span> <span class="r-number">0.3</span>) <span class="r-operator">+</span>
  <span class="r-function">scale_fill_manual</span>(values <span class="r-operator">=</span> <span class="r-function">c</span>(
    pre_presidency <span class="r-operator">=</span> <span class="r-string">"#6366f1"</span>,
    transition <span class="r-operator">=</span> <span class="r-string">"#f59e0b"</span>,
    presidency <span class="r-operator">=</span> <span class="r-string">"#10b981"</span>)) <span class="r-operator">+</span>
  <span class="r-function">labs</span>(title <span class="r-operator">=</span> <span class="r-string">"Sentiment by Political Period"</span>,
       x <span class="r-operator">=</span> <span class="r-string">""</span>, y <span class="r-operator">=</span> <span class="r-string">"Sentiment Score"</span>) <span class="r-operator">+</span>
  <span class="r-function">theme_minimal</span>() <span class="r-operator">+</span>
  <span class="r-function">theme</span>(legend.position <span class="r-operator">=</span> <span class="r-string">"none"</span>)

<span class="r-comment"># Summary statistics</span>
scored <span class="r-operator">|&gt;</span>
  <span class="r-function">group_by</span>(period3) <span class="r-operator">|&gt;</span>
  <span class="r-function">summarise</span>(n <span class="r-operator">=</span> <span class="r-function">n</span>(), mean <span class="r-operator">=</span> <span class="r-function">mean</span>(score),
            median <span class="r-operator">=</span> <span class="r-function">median</span>(score), sd <span class="r-operator">=</span> <span class="r-function">sd</span>(score))</code></pre>
    </div>
    <div class="callout callout-tip"><strong>In Orange:</strong> connect your scored data to a <strong>Box Plot</strong> widget, set the subgroup to <code>period3</code>.</div>
  </div>
</details>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">5</span>
  <h2>Over Time</h2>
</div>

<p class="narrative">
  Sentiment trends across 8 years. The <strong>dark trend line</strong> is a 120-day rolling average that runs from 2012 to 2020. Hover individual dots to read tweets. Dashed lines mark key events.
</p>

<div class="chart-container" id="chartContainer">
  <canvas id="mainCanvas"></canvas>
  <div id="tooltip" class="chart-tooltip"></div>
</div>

<div class="callout callout-info">The visible rise around inauguration (May 2017) reflects the shift to presidential communication. The dip in mid-2019 aligns with the Japan trade dispute. Note: Moon barely tweeted in 2013&ndash;2015, so the line in that stretch is an average of much thinner data &mdash; the jitter there reflects the thin sample, not a real mood swing.</div>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: sentiment over time with trend line</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># Sentiment over time with LOESS trend</span>
scored <span class="r-operator">|&gt;</span>
  <span class="r-function">mutate</span>(tweet_date <span class="r-operator">=</span> <span class="r-function">as.Date</span>(tweet_date)) <span class="r-operator">|&gt;</span>
  <span class="r-function">ggplot</span>(<span class="r-function">aes</span>(x <span class="r-operator">=</span> tweet_date, y <span class="r-operator">=</span> score,
             color <span class="r-operator">=</span> period3)) <span class="r-operator">+</span>
  <span class="r-function">geom_point</span>(alpha <span class="r-operator">=</span> <span class="r-number">0.15</span>, size <span class="r-operator">=</span> <span class="r-number">1</span>) <span class="r-operator">+</span>
  <span class="r-function">geom_smooth</span>(<span class="r-function">aes</span>(group <span class="r-operator">=</span> <span class="r-number">1</span>), method <span class="r-operator">=</span> <span class="r-string">"loess"</span>,
             span <span class="r-operator">=</span> <span class="r-number">0.15</span>, color <span class="r-operator">=</span> <span class="r-string">"#001158"</span>,
             se <span class="r-operator">=</span> <span class="r-keyword">FALSE</span>, linewidth <span class="r-operator">=</span> <span class="r-number">1</span>) <span class="r-operator">+</span>
  <span class="r-function">scale_color_manual</span>(values <span class="r-operator">=</span> <span class="r-function">c</span>(
    pre_presidency <span class="r-operator">=</span> <span class="r-string">"#6366f1"</span>,
    transition <span class="r-operator">=</span> <span class="r-string">"#f59e0b"</span>,
    presidency <span class="r-operator">=</span> <span class="r-string">"#10b981"</span>)) <span class="r-operator">+</span>
  <span class="r-comment"># Mark key events</span>
  <span class="r-function">geom_vline</span>(xintercept <span class="r-operator">=</span> <span class="r-function">as.Date</span>(<span class="r-string">"2017-05-09"</span>),
             linetype <span class="r-operator">=</span> <span class="r-string">"dashed"</span>, alpha <span class="r-operator">=</span> <span class="r-number">0.5</span>) <span class="r-operator">+</span>
  <span class="r-function">geom_vline</span>(xintercept <span class="r-operator">=</span> <span class="r-function">as.Date</span>(<span class="r-string">"2019-07-04"</span>),
             linetype <span class="r-operator">=</span> <span class="r-string">"dashed"</span>, alpha <span class="r-operator">=</span> <span class="r-number">0.5</span>) <span class="r-operator">+</span>
  <span class="r-function">labs</span>(title <span class="r-operator">=</span> <span class="r-string">"Sentiment Over Time"</span>,
       x <span class="r-operator">=</span> <span class="r-string">""</span>, y <span class="r-operator">=</span> <span class="r-string">"Score"</span>) <span class="r-operator">+</span>
  <span class="r-function">theme_minimal</span>()</code></pre>
    </div>
  </div>
</details>

<!-- ════════════════════════════════════════════════════════════════ -->
<div class="section-heading">
  <span class="section-number">6</span>
  <h2>Explore Tweets</h2>
</div>

<p class="narrative">
  Top matched words, plus the most positive and most negative tweets. Browse by sentiment score or engagement.
</p>

<div id="exploreSection"><p class="loading-msg">Loading tweets&hellip;</p></div>

<details class="code-ribbon">
  <summary><span class="ribbon-label">Show R code: explore top words and extreme tweets</span><span class="ribbon-tag">R</span></summary>
  <div class="code-ribbon-body">
    <div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre><code><span class="r-comment"># Top matched sentiment words, by polarity</span>
tokens <span class="r-operator">|&gt;</span>
  <span class="r-function">inner_join</span>(knu, by <span class="r-operator">=</span> <span class="r-string">"word"</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">count</span>(sentiment, word, sort <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>) <span class="r-operator">|&gt;</span>
  <span class="r-function">group_by</span>(sentiment) <span class="r-operator">|&gt;</span>
  <span class="r-function">slice_max</span>(n, n <span class="r-operator">=</span> <span class="r-number">10</span>)

<span class="r-comment"># Most positive and most negative tweets</span>
extreme_tweets <span class="r-operator">&lt;-</span> sentiment_scores <span class="r-operator">|&gt;</span>
  <span class="r-function">inner_join</span>(tweets <span class="r-operator">|&gt;</span> <span class="r-function">select</span>(tweet_id, text),
             by <span class="r-operator">=</span> <span class="r-string">"tweet_id"</span>)

extreme_tweets <span class="r-operator">|&gt;</span> <span class="r-function">slice_max</span>(score, n <span class="r-operator">=</span> <span class="r-number">5</span>)
extreme_tweets <span class="r-operator">|&gt;</span> <span class="r-function">slice_min</span>(score, n <span class="r-operator">=</span> <span class="r-number">5</span>)

<span class="r-comment"># Box plot: sentiment by period</span>
sentiment_scores <span class="r-operator">|&gt;</span>
  <span class="r-function">ggplot</span>(<span class="r-function">aes</span>(x <span class="r-operator">=</span> period3, y <span class="r-operator">=</span> score, fill <span class="r-operator">=</span> period3)) <span class="r-operator">+</span>
  <span class="r-function">geom_boxplot</span>(alpha <span class="r-operator">=</span> <span class="r-number">0.7</span>) <span class="r-operator">+</span>
  <span class="r-function">theme_minimal</span>()</code></pre>
    </div>
    <div class="callout callout-tip"><strong>In Orange:</strong> connect scored data to <strong>Corpus Viewer</strong> and sort by the score column. Click any tweet to read the full text.</div>
  </div>
</details>

</div><!-- /tutorial-page -->

<script>
window.copyCode = function (btn) {
  var pre = btn.closest(".code-block").querySelector("pre code");
  navigator.clipboard.writeText(pre.textContent).then(function () {
    btn.textContent = "Copied!"; btn.classList.add("copied");
    setTimeout(function () { btn.textContent = "Copy"; btn.classList.remove("copied"); }, 2000);
  });
};
(function () {
  "use strict";

  var PERIOD_COLORS = { p: "#6366f1", t: "#f59e0b", r: "#10b981" };
  var PERIOD_NAMES = { p: "Pre-presidency", t: "Transition", r: "Presidency" };
  var PERIOD_KEYS = ["p", "t", "r"];
  var PERIOD_FULL = { p: "pre_presidency", t: "transition", r: "presidency" };

  var DATA = null;
  var canvasW = 0, canvasH = 0, hoveredIdx = -1;
  var PAD = 40, PADR = 20, PADT = 20, PADB = 30;

  var canvas = document.getElementById("mainCanvas");
  var ctx = canvas.getContext("2d");
  var tooltipEl = document.getElementById("tooltip");

  // ── Canvas helpers ────────────────────────────────────────────────
  function setupCanvas(h) {
    var container = document.getElementById("chartContainer");
    var w = container.clientWidth;
    h = h || Math.round(Math.min(w * 0.5, 380));
    var dpr = window.devicePixelRatio || 1;
    canvas.width = w * dpr; canvas.height = h * dpr;
    canvas.style.width = w + "px"; canvas.style.height = h + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    canvasW = w; canvasH = h;
  }

  function dateToX(dateStr) {
    var d = new Date(dateStr);
    var minD = new Date("2012-01-01"), maxD = new Date("2020-07-01");
    var frac = (d - minD) / (maxD - minD);
    return PAD + frac * (canvasW - PAD - PADR);
  }

  function scoreToY(score, minS, maxS) {
    var frac = (score - minS) / (maxS - minS);
    return canvasH - PADB - frac * (canvasH - PADT - PADB);
  }

  function truncate(s, n) { return s.length > n ? s.slice(0, n) + "\u2026" : s; }

  // ── Tooltip for timeline canvas ───────────────────────────────────
  canvas.addEventListener("mousemove", function (e) {
    if (!DATA) return;
    var rect = canvas.getBoundingClientRect();
    var mx = e.clientX - rect.left, my = e.clientY - rect.top;
    var tl = DATA.timeline, minS = -30, maxS = 35;
    var best = -1, bestDist = 100;
    for (var i = 0; i < tl.length; i++) {
      if (!tl[i].t) continue;
      var x = dateToX(tl[i].d);
      var y = scoreToY(tl[i].s, minS, maxS);
      var d = Math.sqrt((x - mx) * (x - mx) + (y - my) * (y - my));
      if (d < bestDist && d < 18) { bestDist = d; best = i; }
    }
    if (best !== hoveredIdx) {
      hoveredIdx = best;
      drawTimeline();
    }
    if (best >= 0) {
      var t = tl[best];
      var nt = t.nt || 0;
      tooltipEl.innerHTML = "<strong>" + t.d + "</strong> &bull; Score: " + t.s.toFixed(1) +
        " &bull; +" + t.pc + " / -" + t.nc + " in " + nt + " tokens<br>" + truncate(t.t, 100);
      tooltipEl.style.display = "block";
      var dotX = dateToX(t.d);
      var dotY = scoreToY(t.s, minS, maxS);
      var tipW = tooltipEl.offsetWidth;
      var tipH = tooltipEl.offsetHeight;
      var tx = dotX + 12;
      if (tx + tipW > canvasW) tx = dotX - tipW - 12;
      if (tx < 0) tx = 4;
      var ty = dotY - 10;
      if (ty + tipH > canvasH) ty = canvasH - tipH - 4;
      if (ty < 0) ty = 4;
      tooltipEl.style.left = tx + "px";
      tooltipEl.style.top = ty + "px";
    } else {
      tooltipEl.style.display = "none";
    }
  });
  canvas.addEventListener("mouseleave", function () {
    hoveredIdx = -1; tooltipEl.style.display = "none";
    drawTimeline();
  });

  // ── Section 1: Corpus (stacked bar chart) ─────────────────────────
  function renderCorpus() {
    var byYear = {};
    for (var yr = 2012; yr <= 2020; yr++) byYear[yr] = { p: 0, t: 0, r: 0, total: 0 };
    DATA.timeline.forEach(function (e) {
      if (!e.t || !byYear[e.y]) return;
      byYear[e.y][e.p]++;
      byYear[e.y].total++;
    });
    var maxYear = 0;
    for (var yr = 2012; yr <= 2020; yr++) maxYear = Math.max(maxYear, byYear[yr].total);

    var html = '';
    // Legend
    html += '<div style="display:flex;flex-wrap:wrap;gap:0.75rem;margin:0.5rem 0;padding:0.5rem 0.75rem;background:#f9fafb;border-radius:6px;border:1px solid #e5e7eb;">';
    PERIOD_KEYS.forEach(function (k) {
      html += '<span style="display:inline-flex;align-items:center;gap:0.3rem;font-size:0.8rem;color:#374151;"><span style="width:10px;height:10px;border-radius:2px;background:' + PERIOD_COLORS[k] + ';"></span>' + PERIOD_NAMES[k] + ' (' + DATA.period_stats[PERIOD_FULL[k]].n + ')</span>';
    });
    html += '</div>';

    // Stacked bar chart
    html += '<div style="max-width:640px;margin:0.5rem 0 1rem;">';
    for (var yr = 2012; yr <= 2020; yr++) {
      var y = byYear[yr];
      html += '<div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.3rem;">';
      html += '<span style="width:42px;font-size:0.78rem;color:#374151;font-weight:600;text-align:right;">' + yr + '</span>';
      html += '<div style="flex:1;height:20px;background:#f1f5f9;border-radius:3px;overflow:hidden;position:relative;">';
      if (y.total > 0) {
        var pPct = (y.p / maxYear) * 100;
        var tPct = (y.t / maxYear) * 100;
        var rPct = (y.r / maxYear) * 100;
        html += '<div style="position:absolute;left:0;top:0;bottom:0;width:' + pPct + '%;background:' + PERIOD_COLORS.p + ';opacity:0.85;"></div>';
        html += '<div style="position:absolute;left:' + pPct + '%;top:0;bottom:0;width:' + tPct + '%;background:' + PERIOD_COLORS.t + ';opacity:0.85;"></div>';
        html += '<div style="position:absolute;left:' + (pPct + tPct) + '%;top:0;bottom:0;width:' + rPct + '%;background:' + PERIOD_COLORS.r + ';opacity:0.85;"></div>';
      }
      html += '</div>';
      html += '<span style="width:52px;font-size:0.75rem;color:#6b7280;">' + y.total + '</span>';
      html += '</div>';
    }
    html += '</div>';
    document.getElementById("corpusChart").innerHTML = html;
  }

  // ── Section 2: Dictionary Scoring walkthrough ─────────────────────
  var currentExample = 0;

  function renderScoring() {
    var examples = DATA.example_tweets;
    if (!examples || examples.length === 0) {
      document.getElementById("scoringSection").innerHTML = '<p style="color:#6b7280;">No example tweets available.</p>';
      return;
    }
    var html = '<div class="example-selector" id="exampleSelector">';
    examples.forEach(function (ex, i) {
      html += '<button class="example-btn' + (i === currentExample ? ' active' : '') + '" data-idx="' + i + '">' + ex.label + '</button>';
    });
    html += '</div>';
    html += '<div id="scoringDetail"></div>';
    document.getElementById("scoringSection").innerHTML = html;

    document.querySelectorAll("#exampleSelector .example-btn").forEach(function (btn) {
      btn.onclick = function () {
        currentExample = parseInt(this.dataset.idx);
        document.querySelectorAll("#exampleSelector .example-btn").forEach(function (b) { b.classList.remove("active"); });
        this.classList.add("active");
        renderScoringDetail();
      };
    });
    renderScoringDetail();
  }

  function renderScoringDetail() {
    var ex = DATA.example_tweets[currentExample];
    if (!ex) return;
    var scoreColor = ex.score > 0 ? 'var(--pos-green)' : ex.score < 0 ? 'var(--neg-red)' : 'var(--neu-gray)';
    var sign = ex.score > 0 ? '+' : '';
    var perMap = { pre_presidency: 'p', transition: 't', presidency: 'r' };
    var html = '<div class="scoring-card">';
    html += '<div class="scoring-tweet"><div class="meta">' + ex.date + ' &bull; ' + PERIOD_NAMES[perMap[ex.period] || 'p'] + ' &bull; ' + ex.favorites.toLocaleString() + ' likes</div>' + ex.text + '</div>';

    html += '<div style="padding:0.75rem 1rem;">';
    if (ex.pos_matches.length === 0 && ex.neg_matches.length === 0) {
      html += '<p style="color:#9ca3af;font-style:italic;margin:0;">No dictionary matches in this tweet</p>';
    } else {
      if (ex.pos_matches.length > 0) {
        html += '<div style="margin-bottom:0.4rem;"><span style="font-size:0.75rem;color:#6b7280;text-transform:uppercase;letter-spacing:0.04em;font-weight:700;margin-right:0.5rem;">Positive (' + ex.pos_count + ')</span>';
        ex.pos_matches.forEach(function (w) {
          html += '<span style="display:inline-block;padding:0.2rem 0.55rem;margin:0.15rem 0.2rem 0.15rem 0;background:#dcfce7;color:var(--pos-green);border-radius:12px;font-size:0.85rem;font-weight:600;">' + w + '</span>';
        });
        html += '</div>';
      }
      if (ex.neg_matches.length > 0) {
        html += '<div><span style="font-size:0.75rem;color:#6b7280;text-transform:uppercase;letter-spacing:0.04em;font-weight:700;margin-right:0.5rem;">Negative (' + ex.neg_count + ')</span>';
        ex.neg_matches.forEach(function (w) {
          html += '<span style="display:inline-block;padding:0.2rem 0.55rem;margin:0.15rem 0.2rem 0.15rem 0;background:#fee2e2;color:var(--neg-red);border-radius:12px;font-size:0.85rem;font-weight:600;">' + w + '</span>';
        });
        html += '</div>';
      }
    }
    html += '</div>';

    html += '<div style="padding:0.65rem 1rem;background:#f1f5f9;border-top:1px solid #e2e8f0;font-size:0.85rem;line-height:1.5;color:#374151;">';
    html += '100 &times; (' + ex.pos_count + ' &minus; ' + ex.neg_count + ') / ' + ex.n_tokens + ' tokens = <strong style="color:' + scoreColor + ';font-size:1rem;">' + sign + ex.score.toFixed(2) + '</strong>';
    html += '</div></div>';
    document.getElementById("scoringDetail").innerHTML = html;
  }

  // ── Section 3: Score Distribution ─────────────────────────────────
  var distPeriod = "all";

  function renderDistribution() {
    var hist = distPeriod === "all" ? DATA.histogram : DATA.period_histograms[PERIOD_FULL[distPeriod]];
    var allHist = DATA.histogram;
    var allKeys = Object.keys(allHist).map(Number).sort(function (a, b) { return a - b; });
    var firstNonZero = allKeys.find(function (k) { return allHist[String(k)] > 0; });
    var lastNonZero = allKeys.slice().reverse().find(function (k) { return allHist[String(k)] > 0; });
    var displayMin = Math.max(firstNonZero, -15);
    var displayMax = Math.min(lastNonZero, 20);
    var keys = [];
    for (var k = displayMin; k <= displayMax; k++) keys.push(k);
    var maxCount = Math.max.apply(null, keys.map(function (k) { return hist[String(k)] || 0; }));

    var html = '';
    html += '<div class="period-toggle" id="distToggle">';
    html += '<button class="period-btn' + (distPeriod === "all" ? " active" : "") + '" data-p="all" style="' + (distPeriod === "all" ? "background:var(--leiden-blue);color:#fff;border-color:var(--leiden-blue)" : "") + '">All tweets</button>';
    PERIOD_KEYS.forEach(function (k) {
      html += '<button class="period-btn' + (distPeriod === k ? " active" : "") + '" data-p="' + k + '" style="' + (distPeriod === k ? "background:" + PERIOD_COLORS[k] + ";color:#fff;border-color:" + PERIOD_COLORS[k] : "") + '"><span class="period-dot" style="background:' + PERIOD_COLORS[k] + '"></span>' + PERIOD_NAMES[k] + '</button>';
    });
    html += '</div>';

    html += '<div style="max-width:600px;">';
    keys.forEach(function (s) {
      var count = hist[String(s)] || 0;
      var pct = maxCount > 0 ? (count / maxCount * 100) : 0;
      var color = s > 0 ? "var(--pos-green)" : s < 0 ? "var(--neg-red)" : "#94a3b8";
      if (distPeriod !== "all") color = PERIOD_COLORS[distPeriod];
      html += '<div class="hist-bar-row"><span class="hist-label">' + (s > 0 ? "+" : "") + s + '</span>';
      html += '<div class="hist-bar-track"><div class="hist-bar-fill" style="width:' + pct + '%;background:' + color + ';opacity:0.75;"></div></div>';
      html += '<span class="hist-count">' + count + '</span></div>';
    });
    html += '</div>';

    // Stats callout
    var stats;
    if (distPeriod === "all") {
      var allPos = 0, allNeu = 0, allNeg = 0;
      DATA.timeline.forEach(function (e) {
        if (!e.t) return;
        if (e.s > 0) allPos++;
        else if (e.s < 0) allNeg++;
        else allNeu++;
      });
      var total = allPos + allNeu + allNeg;
      stats = {
        pos_pct: Math.round(100 * allPos / total),
        neu_pct: Math.round(100 * allNeu / total),
        neg_pct: Math.round(100 * allNeg / total)
      };
    } else {
      stats = DATA.period_stats[PERIOD_FULL[distPeriod]];
    }
    html += '<div class="callout callout-tip">' + stats.pos_pct + '% positive, ' + stats.neu_pct + '% neutral, ' + stats.neg_pct + '% negative. Political communication skews positive &mdash; leaders frame messages around hope and progress.</div>';

    document.getElementById("distSection").innerHTML = html;

    document.querySelectorAll("#distToggle .period-btn").forEach(function (btn) {
      btn.onclick = function () {
        distPeriod = this.dataset.p;
        renderDistribution();
      };
    });
  }

  // ── Section 4: By Period (box plot) ───────────────────────────────
  function renderPeriod() {
    var periods = [
      { key: "pre_presidency", label: "Pre-presidency", color: PERIOD_COLORS.p },
      { key: "transition", label: "Transition", color: PERIOD_COLORS.t },
      { key: "presidency", label: "Presidency", color: PERIOD_COLORS.r }
    ];

    var globalMin = -20, globalMax = 20;
    var range = globalMax - globalMin;
    var INSET = 5;
    function pct(v) {
      var clipped = Math.max(globalMin, Math.min(globalMax, v));
      var frac = (clipped - globalMin) / range;
      return INSET + frac * (100 - 2 * INSET);
    }

    var html = '';
    var zeroPct = pct(0);

    periods.forEach(function (p) {
      var s = DATA.period_stats[p.key];
      html += '<div class="box-row">';
      html += '<span class="box-label" style="color:' + p.color + '">' + p.label + '</span>';
      html += '<div class="box-track">';
      html += '<div style="position:absolute;top:0;bottom:0;left:' + zeroPct + '%;width:1px;background:#cbd5e1;"></div>';
      var wL = pct(s.min), wR = pct(s.max);
      html += '<div class="box-whisker" style="left:' + wL + '%;width:' + (wR - wL) + '%;"></div>';
      var bL = pct(s.q1), bR = pct(s.q3);
      var bW = Math.max(bR - bL, 1.8);
      html += '<div class="box-rect" style="left:' + bL + '%;width:' + bW + '%;background:' + p.color + '33;border-color:' + p.color + ';"></div>';
      html += '<div class="box-median" style="left:' + pct(s.median) + '%;"></div>';
      var meanPos = pct(s.mean);
      html += '<div style="position:absolute;top:50%;left:' + meanPos + '%;transform:translate(-50%,-50%) rotate(45deg);width:10px;height:10px;background:' + p.color + ';border:1.5px solid #fff;box-shadow:0 0 0 1px ' + p.color + ';"></div>';
      html += '</div>';
      html += '<span class="box-stat">\u03BC ' + s.mean + ', med ' + s.median + ', n=' + s.n + '</span>';
      html += '</div>';
    });

    // Scale
    html += '<div class="box-row"><span class="box-label" style="color:#9ca3af;font-size:0.75rem;">Score</span><div class="box-track" style="border:none;background:none;position:relative;height:20px;">';
    for (var v = globalMin; v <= globalMax; v += 10) {
      html += '<span style="position:absolute;left:' + pct(v) + '%;transform:translateX(-50%);font-size:0.72rem;color:#9ca3af;top:4px;">' + (v > 0 ? "+" : "") + v + '</span>';
    }
    html += '</div><span class="box-stat"></span></div>';

    html += '<div class="callout callout-tip"><strong>Key finding:</strong> Presidency tweets are about <strong>3\u00d7 more positive on average</strong> than pre-presidency tweets (\u03bc=' + DATA.period_stats.presidency.mean + ' vs ' + DATA.period_stats.pre_presidency.mean + '). Most tweets in every period score around zero (no dictionary matches) \u2014 the difference lives in the long tails, which is why the mean shifts but the median stays near zero.</div>';

    document.getElementById("periodSection").innerHTML = html;
  }

  // ── Section 5: Timeline ───────────────────────────────────────────
  function drawTimeline() {
    if (!DATA) return;
    var tl = DATA.timeline, minS = -30, maxS = 35;

    ctx.clearRect(0, 0, canvasW, canvasH);

    // Grid
    ctx.strokeStyle = "#e2e8f0"; ctx.lineWidth = 1;
    for (var s = -25; s <= 30; s += 5) {
      var y = scoreToY(s, minS, maxS);
      ctx.beginPath(); ctx.moveTo(PAD, y); ctx.lineTo(canvasW - PADR, y); ctx.stroke();
      ctx.fillStyle = "#9ca3af"; ctx.font = "11px system-ui"; ctx.textAlign = "right";
      ctx.fillText(s, PAD - 6, y + 4);
    }
    // Zero line
    ctx.strokeStyle = "#cbd5e1"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 3]);
    var y0 = scoreToY(0, minS, maxS);
    ctx.beginPath(); ctx.moveTo(PAD, y0); ctx.lineTo(canvasW - PADR, y0); ctx.stroke();
    ctx.setLineDash([]);

    // Year labels
    ctx.fillStyle = "#9ca3af"; ctx.font = "11px system-ui"; ctx.textAlign = "center";
    for (var yr = 2012; yr <= 2020; yr++) {
      ctx.fillText(yr, dateToX(yr + "-07-01"), canvasH - 8);
    }

    // Dots
    for (var i = 0; i < tl.length; i++) {
      if (!tl[i].t) continue;
      ctx.globalAlpha = i === hoveredIdx ? 0.9 : 0.12;
      ctx.fillStyle = PERIOD_COLORS[tl[i].p];
      ctx.beginPath(); ctx.arc(dateToX(tl[i].d), scoreToY(tl[i].s, minS, maxS), i === hoveredIdx ? 5 : 2.5, 0, Math.PI * 2); ctx.fill();
    }
    ctx.globalAlpha = 1;

    // Rolling mean trend line
    var sorted = tl.filter(function (t) { return t.t; }).slice().sort(function (a, b) { return a.d < b.d ? -1 : 1; });
    var dayMs = 86400000;
    var halfWin = 60 * dayMs;
    var minTweetsInWindow = 10;
    var times = sorted.map(function (t) { return new Date(t.d).getTime(); });
    var minT = times[0], maxT = times[times.length - 1];
    var step = 7 * dayMs;
    var trend = [];
    var lo = 0, hi = 0, sum = 0, n = 0;
    for (var c = minT; c <= maxT; c += step) {
      var from = c - halfWin, to = c + halfWin;
      while (hi < times.length && times[hi] <= to) { sum += sorted[hi].s; n++; hi++; }
      while (lo < hi && times[lo] < from) { sum -= sorted[lo].s; n--; lo++; }
      if (n >= minTweetsInWindow) {
        trend.push({ t: c, avg: sum / n });
      }
    }
    if (trend.length > 1) {
      ctx.strokeStyle = "#001158"; ctx.lineWidth = 2.5; ctx.globalAlpha = 0.85;
      ctx.beginPath();
      var iso0 = new Date(trend[0].t).toISOString().slice(0, 10);
      ctx.moveTo(dateToX(iso0), scoreToY(trend[0].avg, minS, maxS));
      for (var i = 1; i < trend.length; i++) {
        var iso = new Date(trend[i].t).toISOString().slice(0, 10);
        ctx.lineTo(dateToX(iso), scoreToY(trend[i].avg, minS, maxS));
      }
      ctx.stroke();
      ctx.globalAlpha = 1;
    }

    // Event markers
    var events = [
      { d: "2012-12-19", label: "2012 Election", color: "#6366f1", yOff: 0 },
      { d: "2016-12-09", label: "Impeachment", color: "#f59e0b", yOff: 14 },
      { d: "2017-05-09", label: "Inaugurated", color: "#10b981", yOff: 0 },
      { d: "2018-04-27", label: "Summits", color: "#10b981", yOff: 14 },
      { d: "2019-07-04", label: "Japan dispute", color: "#ef4444", yOff: 0 },
      { d: "2020-01-20", label: "COVID-19", color: "#ef4444", yOff: 14 }
    ];
    events.forEach(function (ev) {
      var x = dateToX(ev.d);
      ctx.strokeStyle = ev.color; ctx.lineWidth = 1.5; ctx.globalAlpha = 0.4;
      ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(x, PADT + 20); ctx.lineTo(x, canvasH - PADB); ctx.stroke();
      ctx.setLineDash([]);
      ctx.globalAlpha = 1;
      ctx.fillStyle = ev.color; ctx.font = "bold 10px system-ui"; ctx.textAlign = "center";
      ctx.fillText(ev.label, x, PADT + 10 + ev.yOff);
    });

    ctx.save(); ctx.fillStyle = "#6b7280"; ctx.font = "12px system-ui";
    ctx.translate(12, canvasH / 2); ctx.rotate(-Math.PI / 2);
    ctx.textAlign = "center"; ctx.fillText("Sentiment Score", 0, 0);
    ctx.restore();
  }

  // ── Section 6: Explore tweets ─────────────────────────────────────
  var exploreSort = "most_positive";

  function renderExplore() {
    var html = '';

    // Top words
    html += '<div class="word-cols">';
    html += '<div class="word-col"><h4 style="color:var(--pos-green);">Top Positive Matches</h4>';
    var maxPosCount = DATA.top_positive_words[0].count;
    DATA.top_positive_words.slice(0, 10).forEach(function (w) {
      html += '<div class="word-bar-row"><span class="word-bar-label" style="color:var(--pos-green);">' + w.word + '</span><div class="word-bar-track"><div class="word-bar-fill" style="width:' + (w.count / maxPosCount * 100) + '%;background:var(--pos-green);opacity:0.5;"></div></div><span class="word-bar-count">' + w.count + '</span></div>';
    });
    html += '</div>';
    html += '<div class="word-col"><h4 style="color:var(--neg-red);">Top Negative Matches</h4>';
    var maxNegCount = DATA.top_negative_words[0].count;
    DATA.top_negative_words.slice(0, 10).forEach(function (w) {
      html += '<div class="word-bar-row"><span class="word-bar-label" style="color:var(--neg-red);">' + w.word + '</span><div class="word-bar-track"><div class="word-bar-fill" style="width:' + (w.count / maxNegCount * 100) + '%;background:var(--neg-red);opacity:0.5;"></div></div><span class="word-bar-count">' + w.count + '</span></div>';
    });
    html += '</div></div>';

    html += '<div class="callout callout-info">The top matches are genuine sentiment words \u2014 <strong>\uAC10\uC0AC</strong> (gratitude), <strong>\uD76C\uB9DD</strong> (hope), <strong>\uBC1C\uC804</strong> (development) on the positive side; <strong>\uC704\uAE30</strong> (crisis), <strong>\uAC71\uC815</strong> (worry), <strong>\uACE0\uD1B5</strong> (suffering) on the negative side. A known limitation: <strong>\uC9C0\uC9C0</strong> (support / lose) is ambiguous in Korean.</div>';

    // Tweet browser
    html += '<div class="sort-controls"><label>Browse:</label><select id="sortSelect">';
    html += '<option value="most_positive"' + (exploreSort === "most_positive" ? " selected" : "") + '>Most positive</option>';
    html += '<option value="most_negative"' + (exploreSort === "most_negative" ? " selected" : "") + '>Most negative</option>';
    html += '<option value="most_engaged"' + (exploreSort === "most_engaged" ? " selected" : "") + '>Most liked</option>';
    html += '</select></div>';

    var tweets = DATA[exploreSort] || [];
    html += '<div class="tweet-list">';
    tweets.forEach(function (tw) {
      var score = tw.s !== undefined ? tw.s : tw.score;
      var text = tw.t !== undefined ? tw.t : tw.text;
      var date = tw.d !== undefined ? tw.d : tw.date;
      var period = tw.p !== undefined ? tw.p : (tw.period ? tw.period[0] : "p");
      var favs = tw.f !== undefined ? tw.f : tw.favorites;
      var pm = tw.pm !== undefined ? tw.pm : tw.pos_matches || [];
      var nm = tw.nm !== undefined ? tw.nm : tw.neg_matches || [];
      var nt = tw.nt !== undefined ? tw.nt : tw.n_tokens || 0;
      var scoreClass = score > 0 ? "score-pos" : score < 0 ? "score-neg" : "score-neu";
      var scoreDisplay = (score > 0 ? "+" : "") + (Number.isInteger(score) ? score : score.toFixed(1));
      html += '<div class="tweet-item">';
      html += '<span class="tweet-score ' + scoreClass + '">' + scoreDisplay + '</span>';
      html += '<span>' + text + '</span>';
      html += '<div class="tweet-meta">' + date + ' &bull; ' + (PERIOD_NAMES[period] || period) + ' &bull; ' + (favs || 0).toLocaleString() + ' likes &bull; ' + nt + ' tokens';
      if (pm.length > 0) {
        html += ' &bull; ';
        pm.forEach(function (w) { html += '<span class="match-word match-pos">' + w + '</span>'; });
      }
      if (nm.length > 0) {
        html += ' ';
        nm.forEach(function (w) { html += '<span class="match-word match-neg">' + w + '</span>'; });
      }
      html += '</div></div>';
    });
    html += '</div>';

    document.getElementById("exploreSection").innerHTML = html;

    document.getElementById("sortSelect").onchange = function () {
      exploreSort = this.value;
      renderExplore();
    };
  }

  // ── Init ──────────────────────────────────────────────────────────
  function init() {
    renderCorpus();
    renderScoring();
    renderDistribution();
    renderPeriod();
    setupCanvas();
    drawTimeline();
    renderExplore();

    window.addEventListener("resize", function () {
      setupCanvas();
      drawTimeline();
    });
  }

  fetch("{{ '/interactive/sentiment_data.json' | relative_url }}")
    .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); })
    .then(function (json) {
      DATA = json;
      try { init(); } catch (e) { console.error(e); document.getElementById("corpusChart").innerHTML = '<p style="color:#ef4444;">Error: ' + e.message + '</p>'; }
    })
    .catch(function (err) { document.getElementById("corpusChart").innerHTML = '<p style="color:#ef4444;">Failed to load: ' + err.message + '</p>'; });
})();
</script>
