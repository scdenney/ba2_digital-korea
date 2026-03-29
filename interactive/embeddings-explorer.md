---
layout: default
title: "Word Embeddings: Presidential Speeches"
---

<style>
:root { --leiden-blue: #001158; }
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
  z-index: 10; max-width: 300px; white-space: nowrap;
}

.nav-row { display: flex; justify-content: space-between; align-items: center; margin: 0.5rem 0; }
.step-description { font-size: 0.88rem; color: #6b7280; text-align: center; flex: 1; padding: 0 1rem; line-height: 1.4; }

.detail-panel { margin: 1rem 0; min-height: 60px; }
.step-info { animation: fadeIn 0.3s ease; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
.step-info p { font-size: 0.92rem; line-height: 1.65; color: #374151; margin: 0.5rem 0; }
.step-info strong { color: var(--leiden-blue); }

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

.cluster-detail { border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; margin: 0.75rem 0; animation: fadeIn 0.3s ease; }
.cluster-detail-header { padding: 0.6rem 1rem; font-weight: 700; font-size: 0.85rem; color: #fff; }
.cluster-detail-body { padding: 0.75rem 1rem; }
.cluster-card-section { margin-bottom: 0.6rem; }
.cluster-card-section-title { font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; color: #9ca3af; margin-bottom: 0.25rem; }

.wc-word { display: inline-block; cursor: default; font-weight: 600; transition: opacity 0.15s; }
.wc-word:hover { opacity: 0.7; }

.mini-bar-row { display: flex; align-items: center; gap: 0.4rem; margin-bottom: 0.2rem; }
.mini-bar-label { width: 50px; font-size: 0.75rem; text-align: right; color: #374151; flex-shrink: 0; }
.mini-bar-track { flex: 1; height: 14px; background: #f1f5f9; border-radius: 3px; overflow: hidden; }
.mini-bar-fill { height: 100%; border-radius: 3px; }
.mini-bar-count { font-size: 0.68rem; color: #6b7280; width: 28px; text-align: right; flex-shrink: 0; }

.color-legend { display: flex; flex-wrap: wrap; gap: 0.75rem; margin: 0.75rem 0; padding: 0.6rem 0.75rem; background: #f9fafb; border-radius: 6px; border: 1px solid #e5e7eb; }
.color-legend-item { display: inline-flex; align-items: center; gap: 0.3rem; font-size: 0.78rem; color: #4a4a4a; }
.color-legend-dot { width: 10px; height: 10px; border-radius: 50%; }

.word-search-input {
  width: 100%; max-width: 320px; padding: 0.6rem 1rem; border: 2px solid #e2e8f0;
  border-radius: 8px; font-size: 1rem; font-family: inherit; outline: none; transition: border-color 0.2s;
}
.word-search-input:focus { border-color: var(--leiden-blue); }
.word-search-input::placeholder { color: #9ca3af; }
.sim-results { margin-top: 0.75rem; }
.sim-row { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.35rem; }
.sim-word { font-weight: 700; font-size: 0.95rem; width: 80px; text-align: right; color: #1e293b; }
.sim-bar-track { flex: 1; height: 20px; background: #f1f5f9; border-radius: 4px; overflow: hidden; }
.sim-bar-fill { height: 100%; background: var(--leiden-blue); border-radius: 4px; transition: width 0.3s; }
.sim-score { font-size: 0.78rem; color: #6b7280; width: 45px; }

.callout { padding: 0.75rem 1rem; border-radius: 6px; margin: 0.75rem 0; font-size: 0.85rem; line-height: 1.6; }
.callout-info { background: #eff6ff; border-left: 3px solid #3b82f6; color: #1e40af; }
.callout-tip { background: #f0fdf4; border-left: 3px solid #22c55e; color: #166534; }

.analogy-card { border: 1px solid #e2e8f0; border-radius: 8px; padding: 0.75rem 1rem; margin-bottom: 0.75rem; background: #fafbfc; }
.analogy-label { font-size: 1rem; font-weight: 700; color: #1e293b; margin-bottom: 0.4rem; }
.analogy-results { font-size: 0.88rem; color: #374151; }
.analogy-top { font-weight: 700; color: var(--leiden-blue); }

/* Pipeline demo */
.pipeline-demo { border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; margin: 0.75rem 0; }
.pipeline-step-box { padding: 0.6rem 1rem; border-bottom: 1px solid #e2e8f0; }
.pipeline-step-box:last-child { border-bottom: none; }
.pipeline-step-label { font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; color: #9ca3af; margin-bottom: 0.25rem; }
.pipeline-step-content { font-size: 0.88rem; color: #374151; line-height: 1.5; }
.pipeline-step-content code { background: #f1f5f9; padding: 0.15rem 0.4rem; border-radius: 3px; font-size: 0.82rem; }
.pipeline-arrow { text-align: center; color: #9ca3af; font-size: 1.2rem; padding: 0.15rem 0; }
.pipeline-highlight { background: #eff6ff; }

/* Stacked bars */
.comp-row { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.4rem; }
.comp-label { width: 50px; font-size: 0.8rem; text-align: right; color: #374151; flex-shrink: 0; font-weight: 600; }
.comp-bar-track { flex: 1; height: 22px; background: #f1f5f9; border-radius: 4px; overflow: hidden; display: flex; }
.comp-segment { height: 100%; transition: width 0.4s; }

/* Selection panel */
.selection-panel { border: 1px solid #e2e8f0; border-radius: 8px; margin: 0.75rem 0; max-height: 300px; overflow-y: auto; }
.selection-item { padding: 0.5rem 0.75rem; border-bottom: 1px solid #f1f5f9; font-size: 0.82rem; line-height: 1.5; }
.selection-item:last-child { border-bottom: none; }
.selection-item strong { color: var(--leiden-blue); }
.selection-item .snippet { color: #6b7280; font-size: 0.78rem; margin-top: 0.2rem; }
.selection-count { font-size: 0.82rem; color: #6b7280; margin: 0.5rem 0; }
.sel-rect { stroke: var(--leiden-blue); stroke-width: 1.5; fill: rgba(0,17,88,0.08); stroke-dasharray: 4 3; pointer-events: none; }

@media (max-width: 600px) {
  .demo-header h1 { font-size: 1.3rem; }
  .step-btn { font-size: 0.75rem; padding: 0.35rem 0.6rem; }
}
</style>

<div class="demo-app" id="app">
  <div class="demo-header">
    <h1>Word Embeddings: Presidential Speeches</h1>
    <p class="demo-intro">Explore how BERT embeddings represent 749 presidential speeches as vectors, revealing thematic structure invisible to bag-of-words methods. <strong>Drag on the chart to select speeches and read their text.</strong></p>
    <div class="tutorial-meta">
      <span>Week 8</span>
      <span>KLUE BERT embeddings</span>
      <span>749 speeches, 7 presidents</span>
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

  <div id="detailPanel" class="detail-panel"><p style="color:#6b7280;font-size:0.9rem;">Loading speech data&hellip;</p></div>
  <div id="selectionPanel"></div>
</div>

<script>
(function () {
  "use strict";

  var STEPS = [
    { id: "corpus",    label: "1. The Corpus",        desc: "749 speeches from 7 presidents. Each dot is one speech. Hover to explore, drag to select." },
    { id: "pipeline",  label: "2. Inside BERT",        desc: "How one speech becomes a vector of 768 numbers." },
    { id: "cluster",   label: "3. Topic Clusters",     desc: "K-means (k=5) found 5 thematic groups. Click a cluster to explore." },
    { id: "president", label: "4. By President",       desc: "Presidents spread across all clusters. Topic \u2014 not speaker \u2014 drives the structure." },
    { id: "compose",   label: "5. Who Talks About What", desc: "Each president's speech mix across topics." },
    { id: "words",     label: "6. Word Explorer",      desc: "Search for a Korean word to see its nearest neighbors." },
    { id: "analogies", label: "7. Analogies",          desc: "Vector arithmetic: A \u2212 B + C \u2248 ?" }
  ];

  var CLUSTER_PALETTE = ["#B85C38","#4A7C8A","#6B8E5A","#8A6D8A","#D4956A"];
  var PRES_PALETTE = ["#a855f7","#f97316","#14b8a6","#f43f5e","#6366f1","#eab308","#22c55e"];

  var DATA = null, PRES_COLORS = {};
  var currentStep = 0, canvasW = 0, canvasH = 0;
  var colorMode = "gray", highlightCluster = null, hoveredIdx = -1;
  var DOT_R = 3.5, PAD = 28;

  // Selection state
  var isDragging = false, selStart = null, selEnd = null, selectedIndices = [];

  var canvas = document.getElementById("scatterCanvas");
  var ctx = canvas.getContext("2d");
  var tooltipEl = document.getElementById("tooltip");
  var stepsEl = document.getElementById("pipelineSteps");
  var prevBtn = document.getElementById("prevBtn");
  var nextBtn = document.getElementById("nextBtn");
  var stepDesc = document.getElementById("stepDesc");
  var detailPanel = document.getElementById("detailPanel");
  var selectionPanel = document.getElementById("selectionPanel");

  function setupCanvas() {
    var container = document.getElementById("scatterContainer");
    var w = container.clientWidth;
    var h = Math.round(Math.min(w * 0.6, 460));
    var dpr = window.devicePixelRatio || 1;
    canvas.width = w * dpr; canvas.height = h * dpr;
    canvas.style.width = w + "px"; canvas.style.height = h + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    canvasW = w; canvasH = h;
  }

  function tx(v) { return PAD + v * (canvasW - 2 * PAD); }
  function ty(v) { return PAD + (1 - v) * (canvasH - 2 * PAD); }

  function draw() {
    ctx.clearRect(0, 0, canvasW, canvasH);
    if (!DATA) return;
    var sp = DATA.speeches;
    var hasSelection = selectedIndices.length > 0;

    for (var i = 0; i < sp.length; i++) {
      var s = sp[i], x = tx(s.x), y = ty(s.y);
      var r = (i === hoveredIdx) ? DOT_R + 2 : DOT_R;
      var color, alpha;

      if (colorMode === "gray") { color = "#94a3b8"; alpha = 0.45; }
      else if (colorMode === "cluster") {
        color = CLUSTER_PALETTE[s.cluster % 5];
        alpha = (highlightCluster === null || highlightCluster === s.cluster) ? 0.7 : 0.06;
      } else if (colorMode === "president") {
        color = PRES_COLORS[s.president] || "#94a3b8"; alpha = 0.7;
      }

      if (hasSelection) alpha = selectedIndices.indexOf(i) >= 0 ? 1 : 0.08;
      if (i === hoveredIdx) alpha = 1;

      ctx.globalAlpha = alpha; ctx.fillStyle = color;
      ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2); ctx.fill();
    }

    // Draw selection rect
    if (isDragging && selStart && selEnd) {
      ctx.globalAlpha = 1; ctx.strokeStyle = "var(--leiden-blue, #001158)";
      ctx.lineWidth = 1.5; ctx.setLineDash([4, 3]);
      ctx.fillStyle = "rgba(0,17,88,0.06)";
      var rx = Math.min(selStart.x, selEnd.x), ry = Math.min(selStart.y, selEnd.y);
      var rw = Math.abs(selEnd.x - selStart.x), rh = Math.abs(selEnd.y - selStart.y);
      ctx.fillRect(rx, ry, rw, rh);
      ctx.strokeRect(rx, ry, rw, rh);
      ctx.setLineDash([]);
    }

    // Highlight example speech in pipeline step
    if (currentStep === 1 && DATA.example_speech) {
      var ex = DATA.example_speech;
      ctx.globalAlpha = 1; ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.arc(tx(ex.x), ty(ex.y), DOT_R + 5, 0, Math.PI * 2); ctx.stroke();
    }

    ctx.globalAlpha = 1;
  }

  // ── Tooltip ────────────────────────────────────────────────────────
  canvas.addEventListener("mousemove", function (e) {
    if (isDragging) return;
    if (!DATA) return;
    var rect = canvas.getBoundingClientRect();
    var mx = e.clientX - rect.left, my = e.clientY - rect.top;
    var best = -1, bestDist = 100;
    for (var i = 0; i < DATA.speeches.length; i++) {
      var dx = tx(DATA.speeches[i].x) - mx, dy = ty(DATA.speeches[i].y) - my;
      var d = Math.sqrt(dx * dx + dy * dy);
      if (d < bestDist && d < 15) { bestDist = d; best = i; }
    }
    hoveredIdx = best; draw();
    if (best >= 0) {
      var s = DATA.speeches[best];
      tooltipEl.style.display = "block";
      tooltipEl.style.left = Math.min(tx(s.x) + 12, canvasW - 200) + "px";
      tooltipEl.style.top = (ty(s.y) - 10) + "px";
      tooltipEl.innerHTML = "<strong>" + s.president + "</strong><br>" + s.full_title + "<br><em>" + s.kind + " \u2022 " + (s.topic || "") + "</em>";
    } else { tooltipEl.style.display = "none"; }
  });
  canvas.addEventListener("mouseleave", function () { hoveredIdx = -1; tooltipEl.style.display = "none"; draw(); });

  // ── Box selection ──────────────────────────────────────────────────
  canvas.addEventListener("mousedown", function (e) {
    var rect = canvas.getBoundingClientRect();
    selStart = { x: e.clientX - rect.left, y: e.clientY - rect.top };
    selEnd = null; isDragging = true; selectedIndices = [];
    tooltipEl.style.display = "none";
  });
  canvas.addEventListener("mousemove", function (e) {
    if (!isDragging) return;
    var rect = canvas.getBoundingClientRect();
    selEnd = { x: e.clientX - rect.left, y: e.clientY - rect.top };
    draw();
  });
  canvas.addEventListener("mouseup", function () {
    if (!isDragging || !selStart || !selEnd) { isDragging = false; return; }
    isDragging = false;
    var x1 = Math.min(selStart.x, selEnd.x), x2 = Math.max(selStart.x, selEnd.x);
    var y1 = Math.min(selStart.y, selEnd.y), y2 = Math.max(selStart.y, selEnd.y);
    if (x2 - x1 < 5 && y2 - y1 < 5) { selectedIndices = []; selStart = selEnd = null; showSelectionResults(); draw(); return; }

    selectedIndices = [];
    for (var i = 0; i < DATA.speeches.length; i++) {
      var sx = tx(DATA.speeches[i].x), sy = ty(DATA.speeches[i].y);
      if (sx >= x1 && sx <= x2 && sy >= y1 && sy <= y2) selectedIndices.push(i);
    }
    draw(); showSelectionResults();
  });

  function showSelectionResults() {
    if (selectedIndices.length === 0) { selectionPanel.innerHTML = ""; return; }
    var html = '<div class="selection-count"><strong>' + selectedIndices.length + ' speeches selected</strong> \u2014 click elsewhere to deselect</div>';
    html += '<div class="selection-panel">';
    selectedIndices.slice(0, 30).forEach(function (i) {
      var s = DATA.speeches[i];
      html += '<div class="selection-item"><strong>' + s.president + '</strong> \u2022 ' + s.full_title + ' <em>(' + s.kind + ')</em>';
      html += '<div class="snippet">' + s.snippet + '</div></div>';
    });
    if (selectedIndices.length > 30) html += '<div class="selection-item" style="color:#9ca3af;">... and ' + (selectedIndices.length - 30) + ' more</div>';
    html += '</div>';
    selectionPanel.innerHTML = html;
  }

  // ── Step buttons ───────────────────────────────────────────────────
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

  function goToStep(idx) {
    currentStep = idx; buildStepButtons();
    prevBtn.disabled = idx === 0; nextBtn.disabled = idx === STEPS.length - 1;
    stepDesc.textContent = STEPS[idx].desc;
    highlightCluster = null; selectedIndices = []; selStart = selEnd = null;
    selectionPanel.innerHTML = "";

    var handlers = [showCorpus, showPipeline, showClusters, showPresident, showComposition, showWordSearch, showAnalogies];
    var modes = ["gray", "gray", "cluster", "president", "cluster", "cluster", "cluster"];
    colorMode = modes[idx];

    // Hide chart on steps that don't need it
    var showChart = idx <= 4;
    document.querySelector(".scatter-wrap").style.display = showChart ? "" : "none";

    handlers[idx](); if (showChart) draw();
  }

  prevBtn.onclick = function () { if (currentStep > 0) goToStep(currentStep - 1); };
  nextBtn.onclick = function () { if (currentStep < STEPS.length - 1) goToStep(currentStep + 1); };

  // ── Step 1: Corpus ─────────────────────────────────────────────────
  function showCorpus() {
    var counts = {};
    DATA.president_order.forEach(function (p) { counts[p] = 0; });
    DATA.speeches.forEach(function (s) { counts[s.president]++; });
    var html = '<div class="step-info"><p><strong>749 presidential speeches</strong> from the democratic era (1988\u20132022), positioned by their BERT embedding.</p>';
    html += '<div class="color-legend">';
    DATA.president_order.forEach(function (p, i) {
      html += '<span class="color-legend-item"><span class="color-legend-dot" style="background:' + PRES_PALETTE[i] + '"></span>' + p + ' (' + counts[p] + ')</span>';
    });
    html += '</div><div class="callout callout-info">Drag a rectangle on the chart to select speeches and read their text.</div></div>';
    detailPanel.innerHTML = html;
  }

  // ── Step 2: Pipeline ───────────────────────────────────────────────
  function showPipeline() {
    var ex = DATA.example_speech;
    var vec = ex.vector_sample.map(function (v) { return v.toFixed(3); }).join(", ");
    var html = '<div class="step-info">';
    html += '<p>Let\u2019s follow <strong>one speech</strong> through the pipeline. The red circle on the chart shows where it lands.</p>';
    html += '<div class="pipeline-demo">';
    html += '<div class="pipeline-step-box"><div class="pipeline-step-label">Input: raw speech</div>';
    html += '<div class="pipeline-step-content"><strong>' + ex.president + '</strong> \u2014 ' + ex.title + '<br><span style="color:#6b7280;font-size:0.82rem;">\u201C' + ex.snippet + '\u201D</span></div></div>';
    html += '<div class="pipeline-arrow">\u2193</div>';
    html += '<div class="pipeline-step-box pipeline-highlight"><div class="pipeline-step-label">KLUE BERT reads the full text</div>';
    html += '<div class="pipeline-step-content">The model processes every word <strong>in context</strong>, building an understanding of the whole speech.</div></div>';
    html += '<div class="pipeline-arrow">\u2193</div>';
    html += '<div class="pipeline-step-box"><div class="pipeline-step-label">Output: 768-dimensional vector</div>';
    html += '<div class="pipeline-step-content"><code>[' + vec + ', \u2026]</code><br>A single list of 768 numbers that captures the speech\u2019s meaning.</div></div>';
    html += '<div class="pipeline-arrow">\u2193</div>';
    html += '<div class="pipeline-step-box"><div class="pipeline-step-label">t-SNE projection \u2192 dot on the chart</div>';
    html += '<div class="pipeline-step-content">768 dimensions compressed to 2D. Speeches about similar topics land <strong>near each other</strong>.</div></div>';
    html += '</div>';
    html += '<div class="callout callout-info">This speech landed in the <strong>' + ex.topic + '</strong> region of the map.</div>';
    html += '</div>';
    detailPanel.innerHTML = html;
  }

  // ── Step 3: Clusters ───────────────────────────────────────────────
  function showClusters() {
    var html = '<div class="step-info"><p>K-means (k=5) found <strong>five thematic groups</strong>. Click a cluster to explore.</p>';
    html += '<div class="cluster-legend-row">';
    for (var c = 0; c < 5; c++) {
      var n = DATA.speeches.filter(function (s) { return s.cluster === c; }).length;
      html += '<button class="cluster-legend-btn" data-cluster="' + c + '"><span class="cluster-legend-dot" style="background:' + CLUSTER_PALETTE[c] + '"></span>' + DATA.topic_labels[c] + ' (' + n + ')</button>';
    }
    html += '</div><div id="clusterCard"></div></div>';
    detailPanel.innerHTML = html;
    detailPanel.querySelectorAll(".cluster-legend-btn").forEach(function (btn) {
      btn.onclick = function () {
        var c = parseInt(this.dataset.cluster);
        highlightCluster = (highlightCluster === c) ? null : c;
        detailPanel.querySelectorAll(".cluster-legend-btn").forEach(function (b) { b.classList.remove("active"); });
        if (highlightCluster !== null) { this.classList.add("active"); showClusterCard(c); }
        else { document.getElementById("clusterCard").innerHTML = ""; }
        draw();
      };
    });
  }

  function showClusterCard(c) {
    var words = DATA.cluster_words[String(c)] || [];
    var dist = DATA.cluster_president_dist[String(c)] || {};
    var maxCount = Math.max.apply(null, DATA.president_order.map(function (p) { return dist[p] || 0; }));
    var html = '<div class="cluster-detail"><div class="cluster-detail-header" style="background:' + CLUSTER_PALETTE[c] + '">' + DATA.topic_labels[c] + '</div>';
    html += '<div class="cluster-detail-body">';
    html += '<div class="cluster-card-section"><div class="cluster-card-section-title">Distinctive words</div>';
    var maxS = words.length > 0 ? words[0].score : 1;
    words.slice(0, 15).forEach(function (w) {
      var sz = 0.7 + (w.score / maxS) * 0.9;
      html += '<span class="wc-word" style="font-size:' + sz + 'rem;color:' + CLUSTER_PALETTE[c] + ';margin:0.1rem 0.25rem;">' + w.word + '</span>';
    });
    html += '</div><div class="cluster-card-section"><div class="cluster-card-section-title">President composition</div>';
    DATA.president_order.forEach(function (p, i) {
      var cnt = dist[p] || 0; var pct = maxCount > 0 ? (cnt / maxCount * 100) : 0;
      html += '<div class="mini-bar-row"><span class="mini-bar-label">' + p + '</span><div class="mini-bar-track"><div class="mini-bar-fill" style="width:' + pct + '%;background:' + PRES_PALETTE[i] + '"></div></div><span class="mini-bar-count">' + cnt + '</span></div>';
    });
    html += '</div></div></div>';
    document.getElementById("clusterCard").innerHTML = html;
  }

  // ── Step 4: President ──────────────────────────────────────────────
  function showPresident() {
    var html = '<div class="step-info"><p>Colored by <strong>president</strong>. Each president\u2019s speeches are <strong>spread across the map</strong>.</p>';
    html += '<div class="callout callout-tip">The embedding space is organized by <strong>topic</strong>, not by speaker. All presidents give diplomacy speeches, memorial speeches, policy speeches \u2014 and those land in similar regions.</div>';
    html += '<div class="color-legend">';
    DATA.president_order.forEach(function (p, i) {
      html += '<span class="color-legend-item"><span class="color-legend-dot" style="background:' + PRES_PALETTE[i] + '"></span>' + p + '</span>';
    });
    html += '</div></div>';
    detailPanel.innerHTML = html;
  }

  // ── Step 5: Composition ────────────────────────────────────────────
  function showComposition() {
    var comp = DATA.composition;
    var html = '<div class="step-info"><p>Each president\u2019s speeches broken down by topic:</p>';
    DATA.president_order.forEach(function (p) {
      var rows = comp.filter(function (r) { return r.president === p; });
      html += '<div class="comp-row"><span class="comp-label">' + p + '</span><div class="comp-bar-track">';
      rows.forEach(function (r, i) {
        if (r.pct > 0) html += '<div class="comp-segment" style="width:' + r.pct + '%;background:' + CLUSTER_PALETTE[i] + ';" title="' + r.topic + ': ' + r.pct + '%"></div>';
      });
      html += '</div></div>';
    });
    html += '<div class="color-legend" style="margin-top:0.5rem;">';
    DATA.topic_labels.forEach(function (t, i) {
      html += '<span class="color-legend-item"><span class="color-legend-dot" style="background:' + CLUSTER_PALETTE[i] + '"></span>' + t + '</span>';
    });
    html += '</div>';
    html += '<div class="callout callout-tip">\uBB38\uC7AC\uC778 (Moon) has 43% in COVID & Governance. \uB178\uD0DC\uC6B0 (Roh TW) has 52% in Memorial & National. \uAE40\uB300\uC911 (Kim DJ) leads in Diplomacy.</div>';
    html += '</div>';
    detailPanel.innerHTML = html;
  }

  // ── Step 6: Word search ────────────────────────────────────────────
  function showWordSearch() {
    var html = '<div class="step-info">';
    html += '<p>Type a Korean word to see its <strong>10 nearest neighbors</strong> in embedding space:</p>';
    html += '<div style="margin:0.75rem 0;"><input class="word-search-input" id="wordInput" type="text" placeholder="Type a Korean word (e.g. \uACBD\uC81C, \uBBFC\uC8FC, \uB300\uD1B5\uB839)"></div>';
    html += '<div id="simResults"></div>';
    html += '<div class="callout callout-info">Try: <strong>\uACBD\uC81C</strong>, <strong>\uD1B5\uC77C</strong>, <strong>\uBC31\uC2E0</strong>, <strong>\uC678\uAD50</strong>, <strong>\uAD50\uC721</strong>, <strong>\uC778\uAD8C</strong>, <strong>\uC11C\uC6B8</strong>, <strong>\uC5EC\uC790</strong></div>';
    html += '</div>';
    detailPanel.innerHTML = html;
    var input = document.getElementById("wordInput");
    input.addEventListener("input", function () {
      var word = this.value.trim(), el = document.getElementById("simResults");
      if (!word) { el.innerHTML = ""; return; }
      var results = DATA.word_similarities[word];
      if (!results) { el.innerHTML = '<p style="color:#6b7280;font-size:0.88rem;">No data for \u201C' + word + '\u201D. Try one of the suggested words.</p>'; return; }
      var h = '';
      results.forEach(function (r) {
        h += '<div class="sim-row"><span class="sim-word">' + r.word + '</span><div class="sim-bar-track"><div class="sim-bar-fill" style="width:' + (r.score * 100) + '%"></div></div><span class="sim-score">' + r.score.toFixed(3) + '</span></div>';
      });
      el.innerHTML = h;
    });
    setTimeout(function () { input.focus(); }, 100);
  }

  // ── Step 7: Analogies ──────────────────────────────────────────────
  function showAnalogies() {
    var html = '<div class="step-info"><p>Vector arithmetic reveals semantic relationships:</p>';
    DATA.word_analogies.forEach(function (a) {
      html += '<div class="analogy-card"><div class="analogy-label">' + a.label + ' = ?</div><div class="analogy-results">';
      a.results.forEach(function (r, i) {
        html += (i === 0 ? '<span class="analogy-top">' : '<span>') + r.word + ' (' + r.score.toFixed(3) + ')</span>';
        if (i < a.results.length - 1) html += ' \u00b7 ';
      });
      html += '</div></div>';
    });
    html += '<div class="callout callout-tip">The model was never taught geography or family relationships. It <strong>discovered</strong> these patterns from Korean text.</div></div>';
    detailPanel.innerHTML = html;
  }

  // ── Init ───────────────────────────────────────────────────────────
  function init() {
    DATA.president_order.forEach(function (p, i) { PRES_COLORS[p] = PRES_PALETTE[i]; });
    buildStepButtons(); setupCanvas(); goToStep(0);
    window.addEventListener("resize", function () { setupCanvas(); draw(); });
  }

  fetch("{{ '/interactive/embeddings_data.json' | relative_url }}")
    .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); })
    .then(function (json) {
      DATA = json;
      try { init(); } catch (e) { detailPanel.innerHTML = '<p style="color:#ef4444;">Error: ' + e.message + '</p>'; console.error(e); }
    })
    .catch(function (err) { detailPanel.innerHTML = '<p style="color:#ef4444;">Failed to load: ' + err.message + '</p>'; });
})();
</script>
