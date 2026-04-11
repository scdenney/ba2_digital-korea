---
layout: default
title: "Sentiment Analysis: Moon Jae-in's Tweets"
---

<style>
:root { --leiden-blue: #001158; --pos-green: #22863a; --neg-red: #b33030; --neu-gray: #6b7280; }
.demo-app { max-width: 100%; }
.demo-header { margin-bottom: 1.5rem; margin-top: 1rem; }
.demo-header h1 { margin: 0 0 0.5rem; font-size: 1.6rem; color: var(--leiden-blue); }
.demo-intro { color: #4a4a4a; font-size: 0.95rem; line-height: 1.6; margin: 0 0 0.75rem; }
.tutorial-meta { display: flex; flex-wrap: wrap; gap: 1rem; font-size: 0.82rem; color: #9ca3af; }
.tutorial-meta span { display: inline-flex; align-items: center; gap: 0.3rem; }

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

.btn {
  display: inline-block; padding: 0.5rem 1rem; border: 1px solid #dfe3ee;
  border-radius: 6px; background: #fff; font-size: 0.9rem; cursor: pointer;
  color: var(--leiden-blue); font-weight: 600; font-family: inherit;
  transition: background 0.15s, border-color 0.15s;
}
.btn:hover { background: #f5f7fb; border-color: var(--leiden-blue); }
.btn:disabled { opacity: 0.4; cursor: default; }

.chart-wrap { margin: 0.5rem 0 1rem; }
.chart-container {
  position: relative; border: 1px solid #e2e8f0; border-radius: 8px;
  overflow: hidden; background: #fafbfc; max-width: 760px; margin: 0 auto;
}
#mainCanvas { display: block; width: 100%; }
.chart-tooltip {
  display: none; position: absolute; background: rgba(15,23,42,0.92);
  color: #f1f5f9; padding: 0.4rem 0.65rem; border-radius: 5px;
  font-size: 0.75rem; line-height: 1.45; pointer-events: none;
  z-index: 10; max-width: 340px;
}

.nav-row { display: flex; justify-content: space-between; align-items: center; margin: 0.5rem 0; }
.step-description { font-size: 0.88rem; color: #6b7280; text-align: center; flex: 1; padding: 0 1rem; line-height: 1.4; }

.detail-panel { margin: 1rem 0; min-height: 60px; }
.step-info { animation: fadeIn 0.3s ease; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
.step-info p { font-size: 0.92rem; line-height: 1.65; color: #374151; margin: 0.5rem 0; }
.step-info strong { color: var(--leiden-blue); }

.callout { padding: 0.75rem 1rem; border-radius: 6px; margin: 0.75rem 0; font-size: 0.85rem; line-height: 1.6; }
.callout-info { background: #eff6ff; border-left: 3px solid #3b82f6; color: #1e40af; }
.callout-tip { background: #f0fdf4; border-left: 3px solid #22c55e; color: #166534; }
.callout-warn { background: #fffbeb; border-left: 3px solid #f59e0b; color: #92400e; }

/* Scoring walkthrough */
.scoring-card { border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; margin: 0.75rem 0; }
.scoring-tweet { padding: 0.75rem 1rem; background: #f8fafc; border-bottom: 1px solid #e2e8f0; font-size: 0.95rem; line-height: 1.6; }
.scoring-tweet .meta { font-size: 0.75rem; color: #9ca3af; margin-bottom: 0.3rem; }
.scoring-table { width: 100%; border-collapse: collapse; }
.scoring-table th { background: #f1f5f9; padding: 0.4rem 0.75rem; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.04em; color: #6b7280; text-align: left; }
.scoring-table td { padding: 0.4rem 0.75rem; border-top: 1px solid #f1f5f9; font-size: 0.88rem; }
.scoring-table .pos { color: var(--pos-green); font-weight: 700; }
.scoring-table .neg { color: var(--neg-red); font-weight: 700; }
.scoring-table .total-row td { border-top: 2px solid #e2e8f0; font-weight: 700; }
.example-selector { display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.75rem 0; }
.example-btn {
  padding: 0.35rem 0.7rem; border-radius: 20px; border: 2px solid #e2e8f0;
  background: #f8fafc; font-size: 0.8rem; font-weight: 600;
  cursor: pointer; transition: all 0.2s; font-family: inherit; color: #374151;
}
.example-btn:hover { border-color: var(--leiden-blue); }
.example-btn.active { background: var(--leiden-blue); color: #fff; border-color: var(--leiden-blue); }

/* Histogram */
.hist-bar-row { display: flex; align-items: center; gap: 0.4rem; margin-bottom: 0.15rem; }
.hist-label { width: 28px; font-size: 0.75rem; text-align: right; color: #374151; flex-shrink: 0; font-weight: 600; }
.hist-bar-track { flex: 1; height: 18px; background: #f1f5f9; border-radius: 3px; overflow: hidden; }
.hist-bar-fill { height: 100%; border-radius: 3px; transition: width 0.4s; }
.hist-count { font-size: 0.7rem; color: #6b7280; width: 36px; flex-shrink: 0; }

/* Box plot */
.box-row { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.75rem; }
.box-label { width: 110px; font-size: 0.82rem; text-align: right; color: #374151; flex-shrink: 0; font-weight: 600; }
.box-track { flex: 1; height: 32px; position: relative; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; }
.box-whisker { position: absolute; top: 50%; height: 2px; background: #94a3b8; transform: translateY(-50%); }
.box-rect { position: absolute; top: 4px; bottom: 4px; border-radius: 3px; border: 2px solid; }
.box-median { position: absolute; top: 2px; bottom: 2px; width: 3px; background: #1e293b; border-radius: 1px; transform: translateX(-1px); }
.box-stat { font-size: 0.72rem; color: #6b7280; width: 70px; flex-shrink: 0; }

/* Period toggle */
.period-toggle { display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.75rem 0; }
.period-btn {
  padding: 0.35rem 0.7rem; border-radius: 20px; border: 2px solid #e2e8f0;
  background: #fff; font-size: 0.8rem; font-weight: 600;
  cursor: pointer; transition: all 0.2s; font-family: inherit; color: #374151;
}
.period-btn:hover { border-color: currentColor; }
.period-btn.active { box-shadow: 0 1px 4px rgba(0,0,0,0.1); }
.period-dot { display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 0.3rem; vertical-align: middle; }

/* Tweet list */
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

/* Top words */
.word-cols { display: flex; gap: 1.5rem; }
.word-col { flex: 1; }
.word-col h4 { font-size: 0.82rem; margin: 0 0 0.5rem; }
.word-bar-row { display: flex; align-items: center; gap: 0.35rem; margin-bottom: 0.2rem; }
.word-bar-label { width: 55px; font-size: 0.8rem; text-align: right; flex-shrink: 0; font-weight: 600; }
.word-bar-track { flex: 1; height: 16px; background: #f1f5f9; border-radius: 3px; overflow: hidden; }
.word-bar-fill { height: 100%; border-radius: 3px; }
.word-bar-count { font-size: 0.68rem; color: #6b7280; width: 30px; flex-shrink: 0; }

/* Sort controls */
.sort-controls { display: flex; align-items: center; gap: 0.5rem; margin: 0.75rem 0; font-size: 0.85rem; }
.sort-controls label { color: #6b7280; font-weight: 600; }
.sort-controls select {
  padding: 0.35rem 0.6rem; border: 1px solid #dfe3ee; border-radius: 6px;
  font-size: 0.85rem; font-family: inherit; background: #fff; cursor: pointer;
}

/* ── R code ribbons ────────────────────────────────────────────── */
.code-ribbon { border: 1px solid #e2e8f0; border-radius: 8px; margin: 0.75rem 0; overflow: hidden; }
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

@media (max-width: 600px) {
  .demo-header h1 { font-size: 1.3rem; }
  .step-btn { font-size: 0.75rem; padding: 0.35rem 0.6rem; }
  .word-cols { flex-direction: column; }
}
</style>

<div class="demo-app" id="app">
  <div class="demo-header">
    <h1>Sentiment Analysis: Moon Jae-in's Tweets</h1>
    <p class="demo-intro">Explore how dictionary-based sentiment analysis scores 3,148 tweets from President Moon Jae-in's Twitter account (@moonriver365, 2012&ndash;2020). Each tweet is tokenized with Kiwi (a Korean morphological analyzer), then matched against the KNU sentiment dictionary. <strong>You'll see the same numbers when you run this in Orange with the Custom Dictionary option.</strong></p>
    <div class="tutorial-meta">
      <span>Week 9</span>
      <span>Kiwi + KNU sentiment dictionary</span>
      <span>3,148 tweets, 3 periods</span>
    </div>
  </div>

  <div class="pipeline-steps" id="pipelineSteps"></div>

  <div class="chart-wrap">
    <div class="chart-container" id="chartContainer">
      <canvas id="mainCanvas"></canvas>
      <div id="tooltip" class="chart-tooltip"></div>
    </div>
  </div>

  <div class="nav-row">
    <button class="btn" id="prevBtn" disabled>Previous</button>
    <span class="step-description" id="stepDesc"></span>
    <button class="btn" id="nextBtn">Next</button>
  </div>

  <div id="detailPanel" class="detail-panel"><p style="color:#6b7280;font-size:0.9rem;">Loading tweet data&hellip;</p></div>
</div>

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

  var STEPS = [
    { id: "corpus",   label: "1. The Corpus",       desc: "3,148 tweets from @moonriver365 (2012–2020), grouped into three political periods." },
    { id: "scoring",  label: "2. Dictionary Scoring", desc: "How one tweet becomes a sentiment score: look up each word in the positive and negative lists." },
    { id: "dist",     label: "3. Score Distribution", desc: "Most tweets score zero (no dictionary matches). The rest lean positive." },
    { id: "period",   label: "4. By Period",         desc: "Compare the three political periods side by side." },
    { id: "timeline", label: "5. Over Time",         desc: "Sentiment trends across 8 years. Events leave visible marks." },
    { id: "explore",  label: "6. Explore Tweets",    desc: "Top matched words, plus the most positive and most negative tweets." }
  ];

  var PERIOD_COLORS = { p: "#6366f1", t: "#f59e0b", r: "#10b981" };
  var PERIOD_NAMES = { p: "Pre-presidency", t: "Transition", r: "Presidency" };
  var PERIOD_KEYS = ["p", "t", "r"];

  var DATA = null;
  var currentStep = 0, canvasW = 0, canvasH = 0, hoveredIdx = -1;
  var PAD = 40, PADR = 20, PADT = 20, PADB = 30;

  var canvas = document.getElementById("mainCanvas");
  var ctx = canvas.getContext("2d");
  var tooltipEl = document.getElementById("tooltip");
  var stepsEl = document.getElementById("pipelineSteps");
  var prevBtn = document.getElementById("prevBtn");
  var nextBtn = document.getElementById("nextBtn");
  var stepDesc = document.getElementById("stepDesc");
  var detailPanel = document.getElementById("detailPanel");

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

  // ── Step buttons & navigation ────────────────────────────────────
  function buildStepButtons() {
    stepsEl.innerHTML = "";
    STEPS.forEach(function (s, i) {
      var btn = document.createElement("button");
      btn.className = "step-btn" + (i === currentStep ? " active" : "") + (i < currentStep ? " completed" : "");
      btn.textContent = s.label;
      btn.onclick = function () { goToStep(i); };
      stepsEl.appendChild(btn);
    });
  }

  function goToStep(i) {
    currentStep = i;
    buildStepButtons();
    prevBtn.disabled = i === 0;
    nextBtn.disabled = i === STEPS.length - 1;
    stepDesc.textContent = STEPS[i].desc;
    hoveredIdx = -1;
    tooltipEl.style.display = "none";

    // Only show the canvas on steps that use it (timeline is the only one now)
    var chartContainer = document.getElementById("chartContainer");
    var usesCanvas = (i === 4);
    chartContainer.style.display = usesCanvas ? "block" : "none";

    var renderers = [showCorpus, showScoring, showDistribution, showPeriod, showTimeline, showExplore];
    renderers[i]();
  }

  prevBtn.onclick = function () { if (currentStep > 0) goToStep(currentStep - 1); };
  nextBtn.onclick = function () { if (currentStep < STEPS.length - 1) goToStep(currentStep + 1); };

  // ── Helpers ──────────────────────────────────────────────────────
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

  function scoreColor(s) {
    return s > 0 ? "rgba(34,134,58,0.6)" : s < 0 ? "rgba(179,48,48,0.6)" : "rgba(148,163,184,0.5)";
  }

  function truncate(s, n) { return s.length > n ? s.slice(0, n) + "\u2026" : s; }

  // ── Step 1: Corpus overview (tweets per year by period) ─────────
  function showCorpus() {
    // Build counts per year, split by period
    var byYear = {};
    for (var yr = 2012; yr <= 2020; yr++) byYear[yr] = { p: 0, t: 0, r: 0, total: 0 };
    DATA.timeline.forEach(function (e) {
      if (!e.t || !byYear[e.y]) return;
      byYear[e.y][e.p]++;
      byYear[e.y].total++;
    });
    var maxYear = 0;
    for (var yr = 2012; yr <= 2020; yr++) maxYear = Math.max(maxYear, byYear[yr].total);

    var html = '<div class="step-info">';
    html += '<p>The <strong>@moonriver365</strong> corpus has ' + DATA.total_tweets + ' tweets from 2012 to 2020, sorted into three political periods. Before we score anything, here\'s what the corpus looks like year by year.</p>';

    // Legend
    html += '<div style="display:flex;flex-wrap:wrap;gap:0.75rem;margin:0.5rem 0;padding:0.5rem 0.75rem;background:#f9fafb;border-radius:6px;border:1px solid #e5e7eb;">';
    PERIOD_KEYS.forEach(function (k) {
      html += '<span style="display:inline-flex;align-items:center;gap:0.3rem;font-size:0.8rem;color:#374151;"><span style="width:10px;height:10px;border-radius:2px;background:' + PERIOD_COLORS[k] + ';"></span>' + PERIOD_NAMES[k] + ' (' + DATA.period_stats[{p:"pre_presidency",t:"transition",r:"presidency"}[k]].n + ')</span>';
    });
    html += '</div>';

    // Stacked bar chart, one row per year
    html += '<div style="max-width:640px;margin:0.5rem 0 1rem;">';
    for (var yr = 2012; yr <= 2020; yr++) {
      var y = byYear[yr];
      var totalPct = (y.total / maxYear) * 100;
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

    html += '<div class="callout callout-info">Moon was most active on Twitter during his 2012 presidential campaign. After taking office in May 2017, his tweeting dropped sharply — the official Cheong Wa Dae account took over most communication. Next: how do we turn these tweets into sentiment scores?</div>';

    html += '<details class="code-ribbon"><summary><span class="ribbon-label">Show R code: load and count the corpus</span><span class="ribbon-tag">R</span></summary><div class="code-ribbon-body">';
    html += '<div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>';
    html += '<pre><code><span class="r-function">library</span>(tidyverse)\n<span class="r-function">library</span>(tidytext)\n\n<span class="r-comment"># Load the tweet corpus</span>\ntweets <span class="r-operator">&lt;-</span> <span class="r-function">read_csv</span>(<span class="r-string">"moon_twitter.csv"</span>) <span class="r-operator">|&gt;</span>\n  <span class="r-function">filter</span>(<span class="r-operator">!</span><span class="r-function">is.na</span>(text)) <span class="r-operator">|&gt;</span>\n  <span class="r-function">mutate</span>(\n    tweet_id <span class="r-operator">=</span> <span class="r-function">row_number</span>(),\n    text <span class="r-operator">=</span> text <span class="r-operator">|&gt;</span>\n      <span class="r-function">str_remove_all</span>(<span class="r-string">"https?://\\\\S+"</span>) <span class="r-operator">|&gt;</span>  <span class="r-comment"># URLs</span>\n      <span class="r-function">str_remove_all</span>(<span class="r-string">"@\\\\w+"</span>) <span class="r-operator">|&gt;</span>             <span class="r-comment"># @mentions</span>\n      <span class="r-function">str_trim</span>()\n  )\n\n<span class="r-comment"># Tweets per year, split by period</span>\ntweets <span class="r-operator">|&gt;</span>\n  <span class="r-function">count</span>(tweet_year, period3) <span class="r-operator">|&gt;</span>\n  <span class="r-function">ggplot</span>(<span class="r-function">aes</span>(x <span class="r-operator">=</span> tweet_year, y <span class="r-operator">=</span> n, fill <span class="r-operator">=</span> period3)) <span class="r-operator">+</span>\n  <span class="r-function">geom_col</span>() <span class="r-operator">+</span>\n  <span class="r-function">scale_fill_manual</span>(values <span class="r-operator">=</span> <span class="r-function">c</span>(\n    pre_presidency <span class="r-operator">=</span> <span class="r-string">"#6366f1"</span>,\n    transition <span class="r-operator">=</span> <span class="r-string">"#f59e0b"</span>,\n    presidency <span class="r-operator">=</span> <span class="r-string">"#10b981"</span>)) <span class="r-operator">+</span>\n  <span class="r-function">labs</span>(title <span class="r-operator">=</span> <span class="r-string">"Moon Jae-in tweets per year"</span>,\n       x <span class="r-operator">=</span> <span class="r-string">""</span>, y <span class="r-operator">=</span> <span class="r-string">"Tweets"</span>) <span class="r-operator">+</span>\n  <span class="r-function">theme_minimal</span>()</code></pre></div>';
    html += '<div class="callout callout-tip">This is the R-equivalent of Orange\'s <strong>Corpus</strong> widget loading the CSV. We add a <code>tweet_id</code> for joining later and clean URLs/mentions, then count tweets per year colored by period.</div>';
    html += '</div></details>';
    html += '</div>';
    detailPanel.innerHTML = html;
  }

  // Tooltip for timeline scatter (Step 5 only)
  canvas.addEventListener("mousemove", function (e) {
    if (!DATA || currentStep !== 4) return;
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
      if (currentStep === 4) drawTimeline();
    }
    if (best >= 0) {
      var t = tl[best];
      var nt = t.nt || 0;
      tooltipEl.innerHTML = "<strong>" + t.d + "</strong> &bull; Score: " + t.s.toFixed(1) +
        " &bull; +" + t.pc + " / -" + t.nc + " in " + nt + " tokens<br>" + truncate(t.t, 100);
      tooltipEl.style.display = "block";
      // Bounds-checked positioning
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
    if (currentStep === 4) drawTimeline();
  });

  // ── Step 2: Dictionary Scoring walkthrough ───────────────────────
  var currentExample = 0;
  function showScoring() {
    var examples = DATA.example_tweets;
    if (!examples || examples.length === 0) {
      detailPanel.innerHTML = '<p style="color:#6b7280;">No example tweets available.</p>';
      return;
    }

    var html = '<div class="step-info">';
    html += '<p>Pick a tweet. For each one, we show the words that matched the KNU positive or negative list, then compute the score.</p>';
    html += '<div class="example-selector" id="exampleSelector">';
    examples.forEach(function (ex, i) {
      html += '<button class="example-btn' + (i === currentExample ? ' active' : '') + '" data-idx="' + i + '">' + ex.label + '</button>';
    });
    html += '</div>';
    html += '<div id="scoringDetail"></div>';
    html += '<details class="code-ribbon"><summary><span class="ribbon-label">Show R code: tidytext-style sentiment scoring with KNU</span><span class="ribbon-tag">R</span></summary><div class="code-ribbon-body">';
    html += '<div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>';
    html += '<pre><code><span class="r-function">library</span>(tidyverse)\n<span class="r-function">library</span>(tidytext)\n<span class="r-function">library</span>(elbird)  <span class="r-comment"># Kiwi wrapper for R (Korean morphological analyzer)</span>\n\n<span class="r-comment"># 1. Build the KNU sentiment lexicon as a tibble</span>\nknu <span class="r-operator">&lt;-</span> <span class="r-function">bind_rows</span>(\n  <span class="r-function">tibble</span>(word <span class="r-operator">=</span> <span class="r-function">read_lines</span>(<span class="r-string">"positive.txt"</span>), sentiment <span class="r-operator">=</span> <span class="r-string">"positive"</span>),\n  <span class="r-function">tibble</span>(word <span class="r-operator">=</span> <span class="r-function">read_lines</span>(<span class="r-string">"negative.txt"</span>), sentiment <span class="r-operator">=</span> <span class="r-string">"negative"</span>)\n) <span class="r-operator">|&gt;</span>\n  <span class="r-function">mutate</span>(word <span class="r-operator">=</span> <span class="r-function">str_trim</span>(word)) <span class="r-operator">|&gt;</span>\n  <span class="r-function">filter</span>(word <span class="r-operator">!=</span> <span class="r-string">""</span>)\n\n<span class="r-comment"># 2. Kiwi tokenize tweets, keep content words</span>\ntokens <span class="r-operator">&lt;-</span> tweets <span class="r-operator">|&gt;</span>\n  <span class="r-function">mutate</span>(toks <span class="r-operator">=</span> <span class="r-function">map</span>(text, <span class="r-operator">~</span><span class="r-function">tokenize</span>(.x, flatten <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>))) <span class="r-operator">|&gt;</span>\n  <span class="r-function">unnest</span>(toks) <span class="r-operator">|&gt;</span>\n  <span class="r-function">filter</span>(\n    tag <span class="r-operator">%in%</span> <span class="r-function">c</span>(<span class="r-string">"NNG"</span>, <span class="r-string">"NNP"</span>, <span class="r-string">"VA"</span>, <span class="r-string">"VV"</span>),\n    <span class="r-function">str_length</span>(form) <span class="r-operator">&gt;=</span> <span class="r-number">2</span>\n  ) <span class="r-operator">|&gt;</span>\n  <span class="r-function">select</span>(tweet_id, period3, tweet_date, word <span class="r-operator">=</span> form)\n\n<span class="r-comment"># 3. tidytext-style sentiment: inner_join + count + pivot</span>\nsentiment_scores <span class="r-operator">&lt;-</span> tokens <span class="r-operator">|&gt;</span>\n  <span class="r-function">inner_join</span>(knu, by <span class="r-operator">=</span> <span class="r-string">"word"</span>) <span class="r-operator">|&gt;</span>\n  <span class="r-function">count</span>(tweet_id, period3, tweet_date, sentiment) <span class="r-operator">|&gt;</span>\n  <span class="r-function">pivot_wider</span>(names_from <span class="r-operator">=</span> sentiment, values_from <span class="r-operator">=</span> n,\n              values_fill <span class="r-operator">=</span> <span class="r-number">0</span>) <span class="r-operator">|&gt;</span>\n  <span class="r-function">mutate</span>(score <span class="r-operator">=</span> positive <span class="r-operator">-</span> negative)\n\n<span class="r-function">head</span>(sentiment_scores)</code></pre></div>';
    html += '<div class="callout callout-tip"><strong>In Orange</strong> (what you\'ll build): load <code>positive.txt</code> and <code>negative.txt</code> into Sentiment Analysis → Custom Dictionary. <strong>In R</strong>: the code above uses tidytext\'s <code>inner_join</code> pattern with a simpler <code>positive − negative</code> count. Exact numbers differ but rankings agree.</div>';
    html += '</div></details>';
    html += '</div>';
    detailPanel.innerHTML = html;

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
    var html = '<div class="scoring-card">';
    html += '<div class="scoring-tweet"><div class="meta">' + ex.date + ' &bull; ' + PERIOD_NAMES[ex.period[0]] + ' &bull; ' + ex.favorites.toLocaleString() + ' likes</div>' + ex.text + '</div>';

    // Matched words shown as colored chips
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

    // Formula line
    html += '<div style="padding:0.65rem 1rem;background:#f1f5f9;border-top:1px solid #e2e8f0;font-size:0.85rem;line-height:1.5;color:#374151;">';
    html += '100 &times; (' + ex.pos_count + ' &minus; ' + ex.neg_count + ') / ' + ex.n_tokens + ' tokens = <strong style="color:' + scoreColor + ';font-size:1rem;">' + sign + ex.score.toFixed(2) + '</strong>';
    html += '</div></div>';
    document.getElementById("scoringDetail").innerHTML = html;
  }

  // ── Step 3: Score Distribution ───────────────────────────────────
  var distPeriod = "all";
  function showDistribution() {
    var hist = distPeriod === "all" ? DATA.histogram : DATA.period_histograms[{p:"pre_presidency",t:"transition",r:"presidency"}[distPeriod]];
    // Use the ALL-tweets histogram to determine the display range so the
    // x-axis is consistent when toggling periods. Drop leading/trailing
    // empty bins and clip sparse tails beyond |15|.
    var allHist = DATA.histogram;
    var allKeys = Object.keys(allHist).map(Number).sort(function (a, b) { return a - b; });
    // Find first and last non-zero bins in the full range
    var firstNonZero = allKeys.find(function (k) { return allHist[String(k)] > 0; });
    var lastNonZero = allKeys.slice().reverse().find(function (k) { return allHist[String(k)] > 0; });
    // Clip the displayed range to keep the histogram readable
    var displayMin = Math.max(firstNonZero, -15);
    var displayMax = Math.min(lastNonZero, 20);
    var keys = [];
    for (var k = displayMin; k <= displayMax; k++) keys.push(k);
    var maxCount = Math.max.apply(null, keys.map(function (k) { return hist[String(k)] || 0; }));

    var html = '<div class="step-info">';
    html += '<p>Distribution of sentiment scores across all tweets. Many tweets have no dictionary matches and score zero; the rest lean positive. Toggle periods to see how presidential communication differs from pre-presidency.</p>';
    html += '<div class="period-toggle" id="distToggle">';
    html += '<button class="period-btn' + (distPeriod === "all" ? " active" : "") + '" data-p="all" style="' + (distPeriod === "all" ? "background:var(--leiden-blue);color:#fff;border-color:var(--leiden-blue)" : "") + '">All tweets</button>';
    PERIOD_KEYS.forEach(function (k) {
      var fullKey = {p:"pre_presidency",t:"transition",r:"presidency"}[k];
      html += '<button class="period-btn' + (distPeriod === k ? " active" : "") + '" data-p="' + k + '" style="' + (distPeriod === k ? "background:" + PERIOD_COLORS[k] + ";color:#fff;border-color:" + PERIOD_COLORS[k] : "") + '"><span class="period-dot" style="background:' + PERIOD_COLORS[k] + '"></span>' + PERIOD_NAMES[k] + '</button>';
    });
    html += '</div>';

    // Histogram bars
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

    // Compute overall pct on the fly (so it always matches the data)
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
      stats = DATA.period_stats[{p:"pre_presidency",t:"transition",r:"presidency"}[distPeriod]];
    }
    html += '<div class="callout callout-tip">' + stats.pos_pct + '% positive, ' + stats.neu_pct + '% neutral, ' + stats.neg_pct + '% negative. Political communication skews positive &mdash; leaders frame messages around hope and progress.</div>';
    html += '<details class="code-ribbon"><summary><span class="ribbon-label">Show R code: plot score distribution</span><span class="ribbon-tag">R</span></summary><div class="code-ribbon-body">';
    html += '<div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>';
    html += '<pre><code><span class="r-comment"># Histogram of sentiment scores</span>\n<span class="r-function">ggplot</span>(scored, <span class="r-function">aes</span>(x <span class="r-operator">=</span> score)) <span class="r-operator">+</span>\n  <span class="r-function">geom_histogram</span>(binwidth <span class="r-operator">=</span> <span class="r-number">1</span>, fill <span class="r-operator">=</span> <span class="r-string">"#6366f1"</span>, alpha <span class="r-operator">=</span> <span class="r-number">0.7</span>,\n                 color <span class="r-operator">=</span> <span class="r-string">"white"</span>) <span class="r-operator">+</span>\n  <span class="r-function">labs</span>(title <span class="r-operator">=</span> <span class="r-string">"Sentiment Score Distribution"</span>,\n       x <span class="r-operator">=</span> <span class="r-string">"Score (positive - negative)"</span>, y <span class="r-operator">=</span> <span class="r-string">"Count"</span>) <span class="r-operator">+</span>\n  <span class="r-function">theme_minimal</span>()\n\n<span class="r-comment"># Faceted by period</span>\n<span class="r-function">ggplot</span>(scored, <span class="r-function">aes</span>(x <span class="r-operator">=</span> score, fill <span class="r-operator">=</span> period3)) <span class="r-operator">+</span>\n  <span class="r-function">geom_histogram</span>(binwidth <span class="r-operator">=</span> <span class="r-number">1</span>, alpha <span class="r-operator">=</span> <span class="r-number">0.7</span>, color <span class="r-operator">=</span> <span class="r-string">"white"</span>) <span class="r-operator">+</span>\n  <span class="r-function">facet_wrap</span>(<span class="r-operator">~</span> period3, ncol <span class="r-operator">=</span> <span class="r-number">1</span>) <span class="r-operator">+</span>\n  <span class="r-function">scale_fill_manual</span>(values <span class="r-operator">=</span> <span class="r-function">c</span>(\n    pre_presidency <span class="r-operator">=</span> <span class="r-string">"#6366f1"</span>,\n    transition <span class="r-operator">=</span> <span class="r-string">"#f59e0b"</span>,\n    presidency <span class="r-operator">=</span> <span class="r-string">"#10b981"</span>)) <span class="r-operator">+</span>\n  <span class="r-function">theme_minimal</span>() <span class="r-operator">+</span>\n  <span class="r-function">theme</span>(legend.position <span class="r-operator">=</span> <span class="r-string">"none"</span>)</code></pre></div>';
    html += '<div class="callout callout-tip"><strong>In Orange:</strong> connect <strong>Score Documents</strong> to a <strong>Distributions</strong> widget and select the score column.</div>';
    html += '</div></details>';
    html += '</div>';
    detailPanel.innerHTML = html;

    document.querySelectorAll("#distToggle .period-btn").forEach(function (btn) {
      btn.onclick = function () {
        distPeriod = this.dataset.p;
        showDistribution();
      };
    });
  }

  // ── Step 4: By Period (box plot) ─────────────────────────────────
  function showPeriod() {
    var periods = [
      { key: "pre_presidency", label: "Pre-presidency", color: PERIOD_COLORS.p },
      { key: "transition", label: "Transition", color: PERIOD_COLORS.t },
      { key: "presidency", label: "Presidency", color: PERIOD_COLORS.r }
    ];

    // Fixed display range matching the histogram (step 3).
    // Most tweets fall within ±20; outliers beyond are clipped.
    var globalMin = -20, globalMax = 20;
    var range = globalMax - globalMin;

    // Percentage positioning — independent of canvas width
    function pct(v) {
      var clipped = Math.max(globalMin, Math.min(globalMax, v));
      return ((clipped - globalMin) / range) * 100;
    }

    var html = '<div class="step-info">';
    html += '<p>Comparing sentiment across Moon Jae-in\'s three political periods. The <strong>box</strong> shows the middle 50% of scores, the <strong>line</strong> inside the box is the median, the <strong>diamond</strong> marks the mean, and <strong>whiskers</strong> show the score range.</p>';

    var zeroPct = pct(0);

    periods.forEach(function (p) {
      var s = DATA.period_stats[p.key];
      html += '<div class="box-row">';
      html += '<span class="box-label" style="color:' + p.color + '">' + p.label + '</span>';
      html += '<div class="box-track">';
      // Zero reference line
      html += '<div style="position:absolute;top:0;bottom:0;left:' + zeroPct + '%;width:1px;background:#cbd5e1;"></div>';
      // Whisker (clipped to display range)
      var wL = pct(s.min), wR = pct(s.max);
      html += '<div class="box-whisker" style="left:' + wL + '%;width:' + (wR - wL) + '%;"></div>';
      // Box (Q1-Q3). When Q1 = Q3 (collapsed), show a small visible bar.
      var bL = pct(s.q1), bR = pct(s.q3);
      var bW = Math.max(bR - bL, 1.8);
      html += '<div class="box-rect" style="left:' + bL + '%;width:' + bW + '%;background:' + p.color + '33;border-color:' + p.color + ';"></div>';
      // Median line
      html += '<div class="box-median" style="left:' + pct(s.median) + '%;"></div>';
      // Mean marker (diamond) — shows the actual difference when medians are all 0
      var meanPos = pct(s.mean);
      html += '<div style="position:absolute;top:50%;left:' + meanPos + '%;transform:translate(-50%,-50%) rotate(45deg);width:10px;height:10px;background:' + p.color + ';border:1.5px solid #fff;box-shadow:0 0 0 1px ' + p.color + ';"></div>';
      html += '</div>';
      html += '<span class="box-stat">\u03BC ' + s.mean + ', med ' + s.median + ', n=' + s.n + '</span>';
      html += '</div>';
    });

    // Scale (every 10 points so labels don't overlap)
    html += '<div class="box-row"><span class="box-label" style="color:#9ca3af;font-size:0.75rem;">Score</span><div class="box-track" style="border:none;background:none;position:relative;height:20px;">';
    for (var v = globalMin; v <= globalMax; v += 10) {
      html += '<span style="position:absolute;left:' + pct(v) + '%;transform:translateX(-50%);font-size:0.72rem;color:#9ca3af;top:4px;">' + (v > 0 ? "+" : "") + v + '</span>';
    }
    html += '</div><span class="box-stat"></span></div>';

    html += '<div class="callout callout-tip"><strong>Key finding:</strong> Presidency tweets are about <strong>3\u00d7 more positive on average</strong> than pre-presidency tweets (\u03bc=' + DATA.period_stats.presidency.mean + ' vs ' + DATA.period_stats.pre_presidency.mean + '). Most tweets in every period score around zero (no dictionary matches) \u2014 the difference lives in the long tails, which is why the mean shifts but the median stays near zero.</div>';
    html += '<details class="code-ribbon"><summary><span class="ribbon-label">Show R code: box plot by period</span><span class="ribbon-tag">R</span></summary><div class="code-ribbon-body">';
    html += '<div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>';
    html += '<pre><code><span class="r-comment"># Box plot comparing periods</span>\nscored <span class="r-operator">|&gt;</span>\n  <span class="r-function">mutate</span>(period3 <span class="r-operator">=</span> <span class="r-function">factor</span>(period3,\n    levels <span class="r-operator">=</span> <span class="r-function">c</span>(<span class="r-string">"pre_presidency"</span>, <span class="r-string">"transition"</span>, <span class="r-string">"presidency"</span>))) <span class="r-operator">|&gt;</span>\n  <span class="r-function">ggplot</span>(<span class="r-function">aes</span>(x <span class="r-operator">=</span> period3, y <span class="r-operator">=</span> score, fill <span class="r-operator">=</span> period3)) <span class="r-operator">+</span>\n  <span class="r-function">geom_boxplot</span>(alpha <span class="r-operator">=</span> <span class="r-number">0.7</span>, outlier.alpha <span class="r-operator">=</span> <span class="r-number">0.3</span>) <span class="r-operator">+</span>\n  <span class="r-function">scale_fill_manual</span>(values <span class="r-operator">=</span> <span class="r-function">c</span>(\n    pre_presidency <span class="r-operator">=</span> <span class="r-string">"#6366f1"</span>,\n    transition <span class="r-operator">=</span> <span class="r-string">"#f59e0b"</span>,\n    presidency <span class="r-operator">=</span> <span class="r-string">"#10b981"</span>)) <span class="r-operator">+</span>\n  <span class="r-function">labs</span>(title <span class="r-operator">=</span> <span class="r-string">"Sentiment by Political Period"</span>,\n       x <span class="r-operator">=</span> <span class="r-string">""</span>, y <span class="r-operator">=</span> <span class="r-string">"Sentiment Score"</span>) <span class="r-operator">+</span>\n  <span class="r-function">theme_minimal</span>() <span class="r-operator">+</span>\n  <span class="r-function">theme</span>(legend.position <span class="r-operator">=</span> <span class="r-string">"none"</span>)\n\n<span class="r-comment"># Summary statistics</span>\nscored <span class="r-operator">|&gt;</span>\n  <span class="r-function">group_by</span>(period3) <span class="r-operator">|&gt;</span>\n  <span class="r-function">summarise</span>(n <span class="r-operator">=</span> <span class="r-function">n</span>(), mean <span class="r-operator">=</span> <span class="r-function">mean</span>(score),\n            median <span class="r-operator">=</span> <span class="r-function">median</span>(score), sd <span class="r-operator">=</span> <span class="r-function">sd</span>(score))</code></pre></div>';
    html += '<div class="callout callout-tip"><strong>In Orange:</strong> connect your scored data to a <strong>Box Plot</strong> widget, set the subgroup to <code>period3</code>.</div>';
    html += '</div></details>';
    html += '</div>';
    detailPanel.innerHTML = html;
  }

  // ── Step 5: Timeline with trend ──────────────────────────────────
  function drawTimeline() {
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

    // Dots (faded)
    for (var i = 0; i < tl.length; i++) {
      if (!tl[i].t) continue;
      ctx.globalAlpha = i === hoveredIdx ? 0.9 : 0.12;
      ctx.fillStyle = PERIOD_COLORS[tl[i].p];
      ctx.beginPath(); ctx.arc(dateToX(tl[i].d), scoreToY(tl[i].s, minS, maxS), i === hoveredIdx ? 5 : 2.5, 0, Math.PI * 2); ctx.fill();
    }
    ctx.globalAlpha = 1;

    // Time-based rolling mean: 90-day centered window, weekly steps.
    // Only draw segments where the window has at least 15 tweets, so
    // sparse periods (e.g. 2014-15, when Moon barely tweeted) don't get
    // a misleading smoothed line.
    var sorted = tl.filter(function (t) { return t.t; }).slice().sort(function (a, b) { return a.d < b.d ? -1 : 1; });
    var dayMs = 86400000;
    var halfWin = 45 * dayMs;
    var minTweetsInWindow = 15;
    var times = sorted.map(function (t) { return new Date(t.d).getTime(); });
    var minT = times[0], maxT = times[times.length - 1];
    var step = 7 * dayMs;
    var trend = [];
    var lo = 0, hi = 0, sum = 0, n = 0;
    for (var c = minT; c <= maxT; c += step) {
      var from = c - halfWin, to = c + halfWin;
      while (hi < times.length && times[hi] <= to) { sum += sorted[hi].s; n++; hi++; }
      while (lo < hi && times[lo] < from) { sum -= sorted[lo].s; n--; lo++; }
      trend.push({
        t: c,
        avg: n >= minTweetsInWindow ? sum / n : null,
        n: n
      });
    }
    if (trend.length > 1) {
      ctx.strokeStyle = "#001158"; ctx.lineWidth = 2.5; ctx.globalAlpha = 0.85;
      var penDown = false;
      for (var i = 0; i < trend.length; i++) {
        var pt = trend[i];
        if (pt.avg === null) { penDown = false; continue; }
        var iso = new Date(pt.t).toISOString().slice(0, 10);
        var x = dateToX(iso);
        var y = scoreToY(pt.avg, minS, maxS);
        if (!penDown) { ctx.beginPath(); ctx.moveTo(x, y); penDown = true; }
        else { ctx.lineTo(x, y); }
      }
      if (penDown) ctx.stroke();
      ctx.globalAlpha = 1;
    }

    // Event markers
    // Event markers with staggered label positions to avoid overlap
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

  function showTimeline() {
    setupCanvas();
    drawTimeline();

    var html = '<div class="step-info">';
    html += '<p>The <strong>dark trend line</strong> is a 90-day rolling average, drawn only where the window contains at least 15 tweets. Sparse stretches (Moon barely tweeted in 2013–2015) show as gaps so the line never smooths over missing data. Hover individual dots to read tweets. Dashed lines mark key events.</p>';
    html += '<div class="callout callout-info">The visible rise around inauguration (May 2017) reflects the shift to presidential communication. The dip in mid-2019 aligns with the Japan trade dispute. Notice how the line disappears during low-volume stretches — there isn\'t enough data to trust a smoothed estimate there.</div>';
    html += '<details class="code-ribbon"><summary><span class="ribbon-label">Show R code: sentiment over time with trend line</span><span class="ribbon-tag">R</span></summary><div class="code-ribbon-body">';
    html += '<div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>';
    html += '<pre><code><span class="r-comment"># Sentiment over time with LOESS trend</span>\nscored <span class="r-operator">|&gt;</span>\n  <span class="r-function">mutate</span>(tweet_date <span class="r-operator">=</span> <span class="r-function">as.Date</span>(tweet_date)) <span class="r-operator">|&gt;</span>\n  <span class="r-function">ggplot</span>(<span class="r-function">aes</span>(x <span class="r-operator">=</span> tweet_date, y <span class="r-operator">=</span> score,\n             color <span class="r-operator">=</span> period3)) <span class="r-operator">+</span>\n  <span class="r-function">geom_point</span>(alpha <span class="r-operator">=</span> <span class="r-number">0.15</span>, size <span class="r-operator">=</span> <span class="r-number">1</span>) <span class="r-operator">+</span>\n  <span class="r-function">geom_smooth</span>(<span class="r-function">aes</span>(group <span class="r-operator">=</span> <span class="r-number">1</span>), method <span class="r-operator">=</span> <span class="r-string">"loess"</span>,\n             span <span class="r-operator">=</span> <span class="r-number">0.15</span>, color <span class="r-operator">=</span> <span class="r-string">"#001158"</span>,\n             se <span class="r-operator">=</span> <span class="r-keyword">FALSE</span>, linewidth <span class="r-operator">=</span> <span class="r-number">1</span>) <span class="r-operator">+</span>\n  <span class="r-function">scale_color_manual</span>(values <span class="r-operator">=</span> <span class="r-function">c</span>(\n    pre_presidency <span class="r-operator">=</span> <span class="r-string">"#6366f1"</span>,\n    transition <span class="r-operator">=</span> <span class="r-string">"#f59e0b"</span>,\n    presidency <span class="r-operator">=</span> <span class="r-string">"#10b981"</span>)) <span class="r-operator">+</span>\n  <span class="r-comment"># Mark key events</span>\n  <span class="r-function">geom_vline</span>(xintercept <span class="r-operator">=</span> <span class="r-function">as.Date</span>(<span class="r-string">"2017-05-09"</span>),\n             linetype <span class="r-operator">=</span> <span class="r-string">"dashed"</span>, alpha <span class="r-operator">=</span> <span class="r-number">0.5</span>) <span class="r-operator">+</span>\n  <span class="r-function">geom_vline</span>(xintercept <span class="r-operator">=</span> <span class="r-function">as.Date</span>(<span class="r-string">"2019-07-04"</span>),\n             linetype <span class="r-operator">=</span> <span class="r-string">"dashed"</span>, alpha <span class="r-operator">=</span> <span class="r-number">0.5</span>) <span class="r-operator">+</span>\n  <span class="r-function">labs</span>(title <span class="r-operator">=</span> <span class="r-string">"Sentiment Over Time"</span>,\n       x <span class="r-operator">=</span> <span class="r-string">""</span>, y <span class="r-operator">=</span> <span class="r-string">"Score"</span>) <span class="r-operator">+</span>\n  <span class="r-function">theme_minimal</span>()</code></pre></div>';
    html += '</div></details>';
    html += '</div>';
    detailPanel.innerHTML = html;
  }

  // ── Step 6: Explore tweets ───────────────────────────────────────
  var exploreSort = "most_positive";
  function showExplore() {
    // Top words display
    var html = '<div class="step-info">';
    html += '<p>Browse tweets by sentiment score. The most common dictionary matches across the corpus:</p>';
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
    html += '<details class="code-ribbon"><summary><span class="ribbon-label">Show R code: explore top words and extreme tweets</span><span class="ribbon-tag">R</span></summary><div class="code-ribbon-body">';
    html += '<div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>';
    html += '<pre><code><span class="r-comment"># Top matched sentiment words, by polarity</span>\ntokens <span class="r-operator">|&gt;</span>\n  <span class="r-function">inner_join</span>(knu, by <span class="r-operator">=</span> <span class="r-string">"word"</span>) <span class="r-operator">|&gt;</span>\n  <span class="r-function">count</span>(sentiment, word, sort <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>) <span class="r-operator">|&gt;</span>\n  <span class="r-function">group_by</span>(sentiment) <span class="r-operator">|&gt;</span>\n  <span class="r-function">slice_max</span>(n, n <span class="r-operator">=</span> <span class="r-number">10</span>)\n\n<span class="r-comment"># Most positive and most negative tweets</span>\nextreme_tweets <span class="r-operator">&lt;-</span> sentiment_scores <span class="r-operator">|&gt;</span>\n  <span class="r-function">inner_join</span>(tweets <span class="r-operator">|&gt;</span> <span class="r-function">select</span>(tweet_id, text),\n             by <span class="r-operator">=</span> <span class="r-string">"tweet_id"</span>)\n\nextreme_tweets <span class="r-operator">|&gt;</span> <span class="r-function">slice_max</span>(score, n <span class="r-operator">=</span> <span class="r-number">5</span>)\nextreme_tweets <span class="r-operator">|&gt;</span> <span class="r-function">slice_min</span>(score, n <span class="r-operator">=</span> <span class="r-number">5</span>)\n\n<span class="r-comment"># Box plot: sentiment by period</span>\nsentiment_scores <span class="r-operator">|&gt;</span>\n  <span class="r-function">ggplot</span>(<span class="r-function">aes</span>(x <span class="r-operator">=</span> period3, y <span class="r-operator">=</span> score, fill <span class="r-operator">=</span> period3)) <span class="r-operator">+</span>\n  <span class="r-function">geom_boxplot</span>(alpha <span class="r-operator">=</span> <span class="r-number">0.7</span>) <span class="r-operator">+</span>\n  <span class="r-function">theme_minimal</span>()</code></pre></div>';
    html += '<div class="callout callout-tip"><strong>In Orange:</strong> connect scored data to <strong>Corpus Viewer</strong> and sort by the score column. Click any tweet to read the full text.</div>';
    html += '</div></details>';

    // Tweet browser
    html += '<div class="sort-controls"><label>Browse:</label><select id="sortSelect">';
    html += '<option value="most_positive"' + (exploreSort === "most_positive" ? " selected" : "") + '>Most positive</option>';
    html += '<option value="most_negative"' + (exploreSort === "most_negative" ? " selected" : "") + '>Most negative</option>';
    html += '<option value="most_engaged"' + (exploreSort === "most_engaged" ? " selected" : "") + '>Most liked</option>';
    html += '</select></div>';

    var tweets = DATA[exploreSort] || [];
    html += '<div class="tweet-list">';
    tweets.forEach(function (tw) {
      // Support both compact keys (d,s,p,f,t,pm,nm) and full keys (date,score,period,...)
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
    html += '</div></div>';
    detailPanel.innerHTML = html;

    document.getElementById("sortSelect").onchange = function () {
      exploreSort = this.value;
      showExplore();
    };
  }

  // ── Init ─────────────────────────────────────────────────────────
  function init() {
    buildStepButtons(); setupCanvas(); goToStep(0);
    window.addEventListener("resize", function () { goToStep(currentStep); });
  }

  fetch("{{ '/interactive/sentiment_data.json' | relative_url }}")
    .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); })
    .then(function (json) {
      DATA = json;
      try { init(); } catch (e) { detailPanel.innerHTML = '<p style="color:#ef4444;">Error: ' + e.message + '</p>'; console.error(e); }
    })
    .catch(function (err) { detailPanel.innerHTML = '<p style="color:#ef4444;">Failed to load: ' + err.message + '</p>'; });
})();
</script>
