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
    <p class="demo-intro">Explore how dictionary-based sentiment analysis scores 3,148 tweets from President Moon Jae-in's Twitter account (@moonriver365, 2012&ndash;2020). See how positive and negative word counts produce document-level sentiment scores &mdash; and where the method breaks down.</p>
    <div class="tutorial-meta">
      <span>Week 9</span>
      <span>Dictionary-based sentiment</span>
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
    { id: "corpus",   label: "1. The Corpus",       desc: "3,148 tweets from @moonriver365. Each dot is one tweet plotted by date and sentiment score." },
    { id: "scoring",  label: "2. Dictionary Scoring", desc: "How one tweet becomes a sentiment score: look up each word in the positive/negative dictionaries." },
    { id: "dist",     label: "3. Score Distribution", desc: "Most tweets are mildly positive or neutral. Toggle periods to compare." },
    { id: "period",   label: "4. By Period",         desc: "Presidency tweets are notably more positive than pre-presidency tweets." },
    { id: "timeline", label: "5. Over Time",         desc: "Sentiment trends across 8 years. Events leave visible marks." },
    { id: "explore",  label: "6. Explore Tweets",    desc: "Browse the most positive, most negative, and most-liked tweets." }
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

    // Only show the canvas on steps that use it (corpus scatter + timeline)
    var chartContainer = document.getElementById("chartContainer");
    var usesCanvas = (i === 0 || i === 4);
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

  // ── Step 1: Corpus scatter ───────────────────────────────────────
  function drawCorpus() {
    var tl = DATA.timeline, minS = -6, maxS = 10;

    ctx.clearRect(0, 0, canvasW, canvasH);

    // Axes
    ctx.strokeStyle = "#e2e8f0"; ctx.lineWidth = 1;
    for (var s = -4; s <= 8; s += 2) {
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
      var x = dateToX(yr + "-07-01");
      ctx.fillText(yr, x, canvasH - 8);
    }

    // Dots
    for (var i = 0; i < tl.length; i++) {
      var t = tl[i];
      if (!t.t) continue;
      var x = dateToX(t.d);
      var y = scoreToY(t.s, minS, maxS);
      ctx.globalAlpha = i === hoveredIdx ? 1 : 0.45;
      ctx.fillStyle = PERIOD_COLORS[t.p];
      ctx.beginPath(); ctx.arc(x, y, i === hoveredIdx ? 5 : 3, 0, Math.PI * 2); ctx.fill();
    }
    ctx.globalAlpha = 1;

    // Y-axis label
    ctx.save(); ctx.fillStyle = "#6b7280"; ctx.font = "12px system-ui";
    ctx.translate(12, canvasH / 2); ctx.rotate(-Math.PI / 2);
    ctx.textAlign = "center"; ctx.fillText("Sentiment Score", 0, 0);
    ctx.restore();
  }

  function showCorpus() {
    setupCanvas();
    drawCorpus();

    // Legend
    var html = '<div class="step-info">';
    html += '<p>Each dot is one tweet. <strong>Color</strong> shows the political period. <strong>Vertical position</strong> shows the dictionary sentiment score (positive words minus negative words). Hover over dots to read tweets.</p>';
    html += '<div style="display:flex;flex-wrap:wrap;gap:0.75rem;margin:0.5rem 0;padding:0.5rem 0.75rem;background:#f9fafb;border-radius:6px;border:1px solid #e5e7eb;">';
    PERIOD_KEYS.forEach(function (k) {
      html += '<span style="display:inline-flex;align-items:center;gap:0.3rem;font-size:0.8rem;color:#374151;"><span style="width:10px;height:10px;border-radius:50%;background:' + PERIOD_COLORS[k] + ';"></span>' + PERIOD_NAMES[k] + ' (' + DATA.period_stats[{p:"pre_presidency",t:"transition",r:"presidency"}[k]].n + ')</span>';
    });
    html += '</div>';
    html += '<div class="callout callout-info">Notice how the presidency dots (green) tend to sit higher. Moon\'s official presidential tweets use more positive language than his earlier opposition-era tweets.</div>';
    html += '<details class="code-ribbon"><summary><span class="ribbon-label">Show R code: load, clean, and explore the corpus</span><span class="ribbon-tag">R</span></summary><div class="code-ribbon-body">';
    html += '<div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>';
    html += '<pre><code><span class="r-function">library</span>(tidyverse)\n\n<span class="r-comment"># Load the tweet corpus</span>\ntweets <span class="r-operator">&lt;-</span> <span class="r-function">read_csv</span>(<span class="r-string">"moon_twitter.csv"</span>)\n<span class="r-function">glimpse</span>(tweets)\n\n<span class="r-comment"># Minimal cleaning: remove URLs, @mentions, RT markers</span>\n<span class="r-comment"># (do NOT remove stopwords or stem --- sentiment needs the raw text)</span>\ntweets <span class="r-operator">&lt;-</span> tweets <span class="r-operator">|&gt;</span>\n  <span class="r-function">filter</span>(<span class="r-operator">!</span><span class="r-function">is.na</span>(text)) <span class="r-operator">|&gt;</span>\n  <span class="r-function">mutate</span>(text <span class="r-operator">=</span> text <span class="r-operator">|&gt;</span>\n    <span class="r-function">str_remove_all</span>(<span class="r-string">"https?://\\\\S+"</span>) <span class="r-operator">|&gt;</span>\n    <span class="r-function">str_remove_all</span>(<span class="r-string">"@\\\\w+"</span>) <span class="r-operator">|&gt;</span>\n    <span class="r-function">str_remove_all</span>(<span class="r-string">"^RT\\\\s*:?"</span>) <span class="r-operator">|&gt;</span>\n    <span class="r-function">str_trim</span>())\n\n<span class="r-comment"># Counts by period and year</span>\ntweets <span class="r-operator">|&gt;</span> <span class="r-function">count</span>(period3)\ntweets <span class="r-operator">|&gt;</span> <span class="r-function">count</span>(tweet_year) <span class="r-operator">|&gt;</span> <span class="r-function">print</span>(n <span class="r-operator">=</span> <span class="r-number">9</span>)</code></pre></div>';
    html += '<div class="callout callout-tip"><strong>In Orange:</strong> load with Corpus widget, inspect with Data Table. No preprocessing widget yet --- that comes in step 2.</div>';
    html += '</div></details>';
    html += '</div>';
    detailPanel.innerHTML = html;
  }

  // Tooltip for scatter
  canvas.addEventListener("mousemove", function (e) {
    if (!DATA || (currentStep !== 0 && currentStep !== 4)) return;
    var rect = canvas.getBoundingClientRect();
    var mx = e.clientX - rect.left, my = e.clientY - rect.top;
    var tl = DATA.timeline, minS = -6, maxS = 10;
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
      if (currentStep === 0) drawCorpus();
      else if (currentStep === 4) drawTimeline();
    }
    if (best >= 0) {
      var t = tl[best];
      tooltipEl.innerHTML = "<strong>" + t.d + "</strong> &bull; Score: " + t.s + " (+" + t.pc + " / -" + t.nc + ")<br>" + truncate(t.t, 100);
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
    if (currentStep === 0) drawCorpus();
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
    html += '<p>Dictionary-based sentiment works by looking up each word in positive and negative word lists, then summing the scores. Select a tweet to see the process:</p>';
    html += '<div class="example-selector" id="exampleSelector">';
    examples.forEach(function (ex, i) {
      html += '<button class="example-btn' + (i === currentExample ? ' active' : '') + '" data-idx="' + i + '">' + ex.label + '</button>';
    });
    html += '</div>';
    html += '<div id="scoringDetail"></div>';
    html += '<div class="callout callout-info"><strong>How this interactive scores tweets:</strong> Kiwi tokenization $\\rightarrow$ keep NNG/NNP/VA/VV stems (length $\\geq$ 2) $\\rightarrow$ look up in stem-indexed KNU. <strong>Same preprocessing you\'ll run in Orange.</strong></div>';
    html += '<details class="code-ribbon"><summary><span class="ribbon-label">Show R code: Kiwi stems + KNU weighted scoring</span><span class="ribbon-tag">R</span></summary><div class="code-ribbon-body">';
    html += '<div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>';
    html += '<pre><code><span class="r-function">library</span>(tidyverse)\n<span class="r-function">library</span>(elbird)  <span class="r-comment"># Kiwi wrapper for R</span>\n\n<span class="r-comment"># Load stem-indexed KNU (stem + score, -2 to +2)</span>\nknu <span class="r-operator">&lt;-</span> <span class="r-function">read_tsv</span>(<span class="r-string">"SentiWord_Dict_stems.txt"</span>,\n  col_names <span class="r-operator">=</span> <span class="r-function">c</span>(<span class="r-string">"stem"</span>, <span class="r-string">"score"</span>))\n\n<span class="r-comment"># Kiwi tokenize, keep content stems (length >= 2)</span>\nstems <span class="r-operator">&lt;-</span> tweets <span class="r-operator">|&gt;</span>\n  <span class="r-function">mutate</span>(tok <span class="r-operator">=</span> <span class="r-function">map</span>(text, <span class="r-operator">~</span><span class="r-function">tokenize</span>(.x, flatten <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>))) <span class="r-operator">|&gt;</span>\n  <span class="r-function">unnest</span>(tok) <span class="r-operator">|&gt;</span>\n  <span class="r-function">filter</span>(tag <span class="r-operator">%in%</span> <span class="r-function">c</span>(<span class="r-string">"NNG"</span>, <span class="r-string">"NNP"</span>, <span class="r-string">"VA"</span>, <span class="r-string">"VV"</span>),\n         <span class="r-function">str_length</span>(form) <span class="r-operator">&gt;=</span> <span class="r-number">2</span>)\n\n<span class="r-comment"># Join with KNU and sum scores per tweet</span>\nscored <span class="r-operator">&lt;-</span> stems <span class="r-operator">|&gt;</span>\n  <span class="r-function">left_join</span>(knu, by <span class="r-operator">=</span> <span class="r-function">c</span>(<span class="r-string">"form"</span> <span class="r-operator">=</span> <span class="r-string">"stem"</span>)) <span class="r-operator">|&gt;</span>\n  <span class="r-function">group_by</span>(tweet_date, period3) <span class="r-operator">|&gt;</span>\n  <span class="r-function">summarise</span>(\n    knu_score <span class="r-operator">=</span> <span class="r-function">sum</span>(score, na.rm <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>),\n    n_pos <span class="r-operator">=</span> <span class="r-function">sum</span>(score <span class="r-operator">&gt;</span> <span class="r-number">0</span>, na.rm <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>),\n    n_neg <span class="r-operator">=</span> <span class="r-function">sum</span>(score <span class="r-operator">&lt;</span> <span class="r-number">0</span>, na.rm <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>),\n    .groups <span class="r-operator">=</span> <span class="r-string">"drop"</span>)</code></pre></div>';
    html += '<div class="callout callout-tip"><strong>In Orange:</strong> Python Script runs Kiwi, outputs stems as <code>processed_text</code>. Sentiment Analysis widget loads positive_stems.txt and negative_stems.txt as custom dictionary, scores each tweet.</div>';
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
    var html = '<div class="scoring-card">';
    html += '<div class="scoring-tweet"><div class="meta">' + ex.date + ' &bull; ' + PERIOD_NAMES[ex.period[0]] + ' &bull; ' + ex.favorites.toLocaleString() + ' likes</div>' + ex.text + '</div>';
    html += '<table class="scoring-table"><thead><tr><th>Word</th><th>Dictionary</th><th>Score</th></tr></thead><tbody>';

    ex.pos_matches.forEach(function (w) {
      html += '<tr><td>' + w + '</td><td class="pos">positive</td><td class="pos">+1</td></tr>';
    });
    ex.neg_matches.forEach(function (w) {
      html += '<tr><td>' + w + '</td><td class="neg">negative</td><td class="neg">&minus;1</td></tr>';
    });
    html += '<tr class="total-row"><td><strong>Total</strong></td><td>+' + ex.pos_count + ' / &minus;' + ex.neg_count + '</td><td><strong style="color:' + (ex.score > 0 ? 'var(--pos-green)' : ex.score < 0 ? 'var(--neg-red)' : 'var(--neu-gray)') + '">' + (ex.score > 0 ? '+' : '') + ex.score + '</strong></td></tr>';
    html += '</tbody></table></div>';
    document.getElementById("scoringDetail").innerHTML = html;
  }

  // ── Step 3: Score Distribution ───────────────────────────────────
  var distPeriod = "all";
  function showDistribution() {
    var hist = distPeriod === "all" ? DATA.histogram : DATA.period_histograms[{p:"pre_presidency",t:"transition",r:"presidency"}[distPeriod]];
    var keys = Object.keys(hist).map(Number).sort(function (a, b) { return a - b; });
    var maxCount = Math.max.apply(null, keys.map(function (k) { return hist[String(k)]; }));

    var html = '<div class="step-info">';
    html += '<p>Distribution of sentiment scores across all tweets. Most cluster around <strong>0 to +2</strong>. Toggle to see how the distribution shifts by period.</p>';
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
      var count = hist[String(s)];
      var pct = maxCount > 0 ? (count / maxCount * 100) : 0;
      var color = s > 0 ? "var(--pos-green)" : s < 0 ? "var(--neg-red)" : "#94a3b8";
      if (distPeriod !== "all") color = PERIOD_COLORS[distPeriod];
      html += '<div class="hist-bar-row"><span class="hist-label">' + (s > 0 ? "+" : "") + s + '</span>';
      html += '<div class="hist-bar-track"><div class="hist-bar-fill" style="width:' + pct + '%;background:' + color + ';opacity:0.75;"></div></div>';
      html += '<span class="hist-count">' + count + '</span></div>';
    });
    html += '</div>';

    var stats = distPeriod === "all" ? {
      pos_pct: Math.round(100 * 1356 / DATA.total_tweets),
      neu_pct: Math.round(100 * 1195 / DATA.total_tweets),
      neg_pct: Math.round(100 * 597 / DATA.total_tweets)
    } : DATA.period_stats[{p:"pre_presidency",t:"transition",r:"presidency"}[distPeriod]];
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

    // Compute range from actual data
    var globalMin = Infinity, globalMax = -Infinity;
    periods.forEach(function (p) {
      var s = DATA.period_stats[p.key];
      if (s.min < globalMin) globalMin = s.min;
      if (s.max > globalMax) globalMax = s.max;
    });
    // Round outward to nearest even number for cleaner scale
    globalMin = Math.floor(globalMin / 2) * 2;
    globalMax = Math.ceil(globalMax / 2) * 2;
    var range = globalMax - globalMin;

    // Percentage positioning — independent of canvas width
    function pct(v) { return ((v - globalMin) / range) * 100; }

    var html = '<div class="step-info">';
    html += '<p>Comparing sentiment across Moon Jae-in\'s three political periods. The <strong>box</strong> shows the middle 50% of scores (Q1 to Q3), the <strong>line</strong> marks the median, and <strong>whiskers</strong> extend to min/max.</p>';

    // Zero line reference
    var zeroPct = pct(0);

    periods.forEach(function (p) {
      var s = DATA.period_stats[p.key];
      html += '<div class="box-row">';
      html += '<span class="box-label" style="color:' + p.color + '">' + p.label + '</span>';
      html += '<div class="box-track">';
      // Zero reference line
      html += '<div style="position:absolute;top:0;bottom:0;left:' + zeroPct + '%;width:1px;background:#cbd5e1;"></div>';
      // Whisker
      var wL = pct(s.min), wR = pct(s.max);
      html += '<div class="box-whisker" style="left:' + wL + '%;width:' + (wR - wL) + '%;"></div>';
      // Box (Q1-Q3)
      var bL = pct(s.q1), bR = pct(s.q3);
      var bW = Math.max(bR - bL, 1.2); // minimum visible width
      html += '<div class="box-rect" style="left:' + bL + '%;width:' + bW + '%;background:' + p.color + '22;border-color:' + p.color + ';"></div>';
      // Median
      html += '<div class="box-median" style="left:' + pct(s.median) + '%;"></div>';
      html += '</div>';
      html += '<span class="box-stat">med ' + s.median + ', \u03BC ' + s.mean + ', n=' + s.n + '</span>';
      html += '</div>';
    });

    // Scale
    html += '<div class="box-row"><span class="box-label" style="color:#9ca3af;font-size:0.75rem;">Score</span><div class="box-track" style="border:none;background:none;position:relative;">';
    for (var v = globalMin; v <= globalMax; v += 2) {
      html += '<span style="position:absolute;left:' + pct(v) + '%;transform:translateX(-50%);font-size:0.7rem;color:#9ca3af;top:4px;">' + (v > 0 ? "+" : "") + v + '</span>';
    }
    html += '</div><span class="box-stat"></span></div>';

    html += '<div class="callout callout-tip"><strong>Key finding:</strong> Presidency tweets have a higher median sentiment (' + DATA.period_stats.presidency.median + ') than pre-presidency (' + DATA.period_stats.pre_presidency.median + '). The means tell the same story (\u03BC=' + DATA.period_stats.presidency.mean + ' vs \u03BC=' + DATA.period_stats.pre_presidency.mean + '). This reflects the shift from opposition criticism to presidential communication.</div>';
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
    var tl = DATA.timeline, minS = -6, maxS = 10;

    ctx.clearRect(0, 0, canvasW, canvasH);

    // Grid
    ctx.strokeStyle = "#e2e8f0"; ctx.lineWidth = 1;
    for (var s = -4; s <= 8; s += 2) {
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

    // Moving average trend line (90-day window)
    var sorted = tl.filter(function (t) { return t.t; }).slice().sort(function (a, b) { return a.d < b.d ? -1 : 1; });
    var windowSize = 60;
    var trend = [];
    for (var i = windowSize; i < sorted.length; i++) {
      var windowSlice = sorted.slice(i - windowSize, i);
      var avg = windowSlice.reduce(function (sum, t) { return sum + t.s; }, 0) / windowSize;
      trend.push({ d: sorted[i].d, avg: avg });
    }
    if (trend.length > 1) {
      ctx.strokeStyle = "#001158"; ctx.lineWidth = 2.5; ctx.globalAlpha = 0.8;
      ctx.beginPath();
      ctx.moveTo(dateToX(trend[0].d), scoreToY(trend[0].avg, minS, maxS));
      for (var i = 1; i < trend.length; i++) {
        ctx.lineTo(dateToX(trend[i].d), scoreToY(trend[i].avg, minS, maxS));
      }
      ctx.stroke();
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
    html += '<p>The <strong>dark trend line</strong> shows a 60-tweet moving average. Hover individual dots to read tweets. Dashed lines mark key events.</p>';
    html += '<div class="callout callout-info">The visible rise around inauguration (May 2017) reflects the shift to presidential communication. The dip in mid-2019 aligns with the Japan trade dispute. Try hovering tweets near the event markers.</div>';
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

    html += '<div class="callout callout-info">Top matches reflect Kiwi-tokenized lemmas: verbs/adjectives in citation form (<strong>\uC88B\uB2E4</strong> good, <strong>\uD06C\uB2E4</strong> big, <strong>\uC544\uD504\uB2E4</strong> painful) and nouns (<strong>\uD76C\uB9DD</strong> hope, <strong>\uAC10\uC0AC</strong> thanks, <strong>\uC704\uAE30</strong> crisis). Homograph ambiguity remains: <strong>\uC9C0\uC9C0</strong> (lose/support) still scores as the dictionary entry.</div>';
    html += '<details class="code-ribbon"><summary><span class="ribbon-label">Show R code: explore top words and extreme tweets</span><span class="ribbon-tag">R</span></summary><div class="code-ribbon-body">';
    html += '<div class="code-block"><div class="code-block-header"><span>R</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>';
    html += '<pre><code><span class="r-comment"># Top matched stems (after Kiwi + KNU join)</span>\nstems <span class="r-operator">|&gt;</span>\n  <span class="r-function">left_join</span>(knu, by <span class="r-operator">=</span> <span class="r-function">c</span>(<span class="r-string">"form"</span> <span class="r-operator">=</span> <span class="r-string">"stem"</span>)) <span class="r-operator">|&gt;</span>\n  <span class="r-function">filter</span>(<span class="r-operator">!</span><span class="r-function">is.na</span>(score), score <span class="r-operator">!=</span> <span class="r-number">0</span>) <span class="r-operator">|&gt;</span>\n  <span class="r-function">count</span>(form, score, sort <span class="r-operator">=</span> <span class="r-keyword">TRUE</span>) <span class="r-operator">|&gt;</span>\n  <span class="r-function">head</span>(<span class="r-number">20</span>)\n\n<span class="r-comment"># Most positive tweets (by KNU weighted score)</span>\ntweets <span class="r-operator">|&gt;</span>\n  <span class="r-function">left_join</span>(scored, by <span class="r-operator">=</span> <span class="r-function">c</span>(<span class="r-string">"tweet_date"</span>, <span class="r-string">"period3"</span>)) <span class="r-operator">|&gt;</span>\n  <span class="r-function">arrange</span>(<span class="r-function">desc</span>(knu_score)) <span class="r-operator">|&gt;</span>\n  <span class="r-function">select</span>(tweet_date, period3, knu_score, text) <span class="r-operator">|&gt;</span>\n  <span class="r-function">head</span>(<span class="r-number">5</span>)\n\n<span class="r-comment"># Most negative tweets</span>\ntweets <span class="r-operator">|&gt;</span>\n  <span class="r-function">left_join</span>(scored, by <span class="r-operator">=</span> <span class="r-function">c</span>(<span class="r-string">"tweet_date"</span>, <span class="r-string">"period3"</span>)) <span class="r-operator">|&gt;</span>\n  <span class="r-function">arrange</span>(knu_score) <span class="r-operator">|&gt;</span>\n  <span class="r-function">select</span>(tweet_date, period3, knu_score, text) <span class="r-operator">|&gt;</span>\n  <span class="r-function">head</span>(<span class="r-number">5</span>)</code></pre></div>';
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

      var scoreClass = score > 0 ? "score-pos" : score < 0 ? "score-neg" : "score-neu";
      html += '<div class="tweet-item">';
      html += '<span class="tweet-score ' + scoreClass + '">' + (score > 0 ? "+" : "") + score + '</span>';
      html += '<span>' + text + '</span>';
      html += '<div class="tweet-meta">' + date + ' &bull; ' + (PERIOD_NAMES[period] || period) + ' &bull; ' + (favs || 0).toLocaleString() + ' likes';
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
