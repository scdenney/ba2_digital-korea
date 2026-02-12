---
layout: default
title: Interactive
---

<style>
/* ── Demo app styles ──────────────────────────────────────────────── */
.demo-app {
  max-width: 100%;
}

.demo-header {
  margin-bottom: 1.5rem;
}

.demo-header h1 {
  margin: 0 0 0.5rem;
  font-size: 1.6rem;
  color: var(--leiden-blue);
}

.demo-intro {
  color: #4a4a4a;
  font-size: 0.95rem;
  line-height: 1.6;
  margin: 0 0 1rem;
}

.demo-controls {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  gap: 0.75rem;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.5rem 1rem;
  border: 1px solid #dfe3ee;
  border-radius: 6px;
  background: #fff;
  font-size: 0.9rem;
  cursor: pointer;
  color: var(--leiden-blue);
  font-weight: 600;
  transition: background 0.15s, border-color 0.15s;
}

.btn:hover {
  background: #f5f7fb;
  border-color: var(--leiden-blue);
}

.btn-primary {
  background: var(--leiden-blue);
  color: #fff;
  border-color: var(--leiden-blue);
}

.btn-primary:hover {
  background: #003366;
}

.filter-select {
  padding: 0.5rem 0.75rem;
  border: 1px solid #dfe3ee;
  border-radius: 6px;
  font-size: 0.9rem;
  color: var(--leiden-blue);
  background: #fff;
  cursor: pointer;
}

/* ── Sentence card ──────────────────────────────────────────────── */
.sentence-card {
  background: #f5f7fb;
  border: 1px solid #dfe3ee;
  border-radius: 8px;
  padding: 1.25rem 1.5rem;
  margin-bottom: 1.5rem;
  position: relative;
}

.sentence-card .sentence-text {
  font-size: 1.15rem;
  line-height: 1.7;
  margin: 0 0 0.5rem;
  color: #1d1d1d;
  word-break: keep-all;
}

.sentence-card .sentence-meta {
  font-size: 0.85rem;
  color: #6b7280;
  text-align: right;
}

/* ── Pipeline steps ──────────────────────────────────────────────── */
.pipeline-steps {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 1.5rem;
}

.step-btn {
  padding: 0.45rem 0.9rem;
  border: 2px solid #dfe3ee;
  border-radius: 20px;
  background: #fff;
  font-size: 0.85rem;
  cursor: pointer;
  color: #4a4a4a;
  font-weight: 600;
  transition: all 0.2s;
}

.step-btn:hover {
  border-color: var(--leiden-blue);
  color: var(--leiden-blue);
}

.step-btn.active {
  background: var(--leiden-blue);
  color: #fff;
  border-color: var(--leiden-blue);
}

.step-btn.completed {
  border-color: #10b981;
  color: #10b981;
}

.step-btn.completed.active {
  background: var(--leiden-blue);
  color: #fff;
  border-color: var(--leiden-blue);
}

/* ── Visualization area ──────────────────────────────────────────── */
.viz-area {
  border: 1px solid #dfe3ee;
  border-radius: 8px;
  padding: 1.5rem;
  min-height: 180px;
  margin-bottom: 1rem;
  background: #fff;
  position: relative;
}

.viz-label {
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #6b7280;
  margin-bottom: 0.75rem;
  font-weight: 600;
}

.viz-text {
  font-size: 1.05rem;
  line-height: 1.8;
  word-break: keep-all;
}

/* Cleaned text: show removed chars */
.removed-char {
  text-decoration: line-through;
  color: #ef4444;
  opacity: 0.6;
}

/* ── Token chips ─────────────────────────────────────────────────── */
.token-container {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: flex-start;
}

.token-chip {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  border-radius: 6px;
  padding: 0.4rem 0.6rem 0.3rem;
  font-size: 0.95rem;
  border: 2px solid transparent;
  transition: all 0.3s ease;
  position: relative;
}

.token-chip .token-form {
  font-weight: 600;
  line-height: 1.3;
}

.token-chip .token-tag {
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  opacity: 0;
  transition: opacity 0.3s ease;
  margin-top: 2px;
  white-space: nowrap;
}

.show-tags .token-chip .token-tag {
  opacity: 1;
}

/* POS category colors */
.token-chip.cat-noun {
  background: #dbeafe;
  border-color: #93c5fd;
  color: #1e40af;
}
.token-chip.cat-verb {
  background: #ccfbf1;
  border-color: #5eead4;
  color: #0f766e;
}
.token-chip.cat-adjective {
  background: #fef9c3;
  border-color: #fde047;
  color: #854d0e;
}
.token-chip.cat-adverb {
  background: #ede9fe;
  border-color: #c4b5fd;
  color: #5b21b6;
}
.token-chip.cat-particle,
.token-chip.cat-ending {
  background: #f3f4f6;
  border-color: #d1d5db;
  color: #6b7280;
}
.token-chip.cat-affix {
  background: #fce7f3;
  border-color: #f9a8d4;
  color: #9d174d;
}
.token-chip.cat-symbol,
.token-chip.cat-other {
  background: #f3f4f6;
  border-color: #d1d5db;
  color: #9ca3af;
}

/* Filtering states */
.token-chip.dimmed {
  opacity: 0.3;
  transform: scale(0.9);
}

.token-chip.stopword {
  opacity: 0.3;
  text-decoration: line-through;
  transform: scale(0.9);
}

.token-chip.kept {
  border-width: 2px;
  box-shadow: 0 1px 4px rgba(0, 33, 71, 0.15);
}

.token-chip.hidden-token {
  display: none;
}

/* ── Result display ──────────────────────────────────────────────── */
.result-tokens {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.result-token {
  display: inline-block;
  background: var(--leiden-blue);
  color: #fff;
  padding: 0.4rem 0.75rem;
  border-radius: 6px;
  font-size: 0.95rem;
  font-weight: 600;
}

/* ── Navigation ──────────────────────────────────────────────────── */
.nav-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1rem;
}

.step-description {
  font-size: 0.9rem;
  color: #6b7280;
  text-align: center;
  flex: 1;
  padding: 0 1rem;
  line-height: 1.4;
}

/* ── Legend ───────────────────────────────────────────────────────── */
.legend {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1.5rem;
  padding: 0.75rem 1rem;
  background: #f9fafb;
  border-radius: 6px;
  border: 1px solid #e5e7eb;
}

.legend-item {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  font-size: 0.78rem;
  color: #4a4a4a;
}

.legend-swatch {
  width: 14px;
  height: 14px;
  border-radius: 3px;
  border: 1px solid rgba(0,0,0,0.1);
}

/* ── POS tag toggles ─────────────────────────────────────────────── */
.pos-controls {
  margin-bottom: 1rem;
}

.pos-toggles {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  padding: 0.6rem 0.75rem;
  background: #f9fafb;
  border-radius: 6px;
  border: 1px solid #e5e7eb;
  align-items: center;
}

.pos-toggles-label {
  font-size: 0.78rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #6b7280;
  margin-right: 0.3rem;
  white-space: nowrap;
}

.pos-toggle {
  padding: 0.3rem 0.7rem;
  border-radius: 14px;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  border: 2px solid;
  transition: all 0.2s ease;
  user-select: none;
  line-height: 1.3;
}

.pos-toggle .tag-code {
  font-family: "SFMono-Regular", "Consolas", "Liberation Mono", monospace;
  font-size: 0.72rem;
  opacity: 0.7;
  margin-left: 0.2rem;
}

.pos-toggle.off {
  opacity: 0.35;
  filter: grayscale(0.7);
}

/* Individual POS tag colors */
.pos-toggle.tgl-NNG { background: #dbeafe; border-color: #93c5fd; color: #1e40af; }
.pos-toggle.tgl-NNP { background: #bfdbfe; border-color: #60a5fa; color: #1e3a8a; }
.pos-toggle.tgl-VV  { background: #ccfbf1; border-color: #5eead4; color: #0f766e; }
.pos-toggle.tgl-VA  { background: #fef9c3; border-color: #fde047; color: #854d0e; }
.pos-toggle.tgl-MAG { background: #ede9fe; border-color: #c4b5fd; color: #5b21b6; }
.pos-toggle.tgl-NNB { background: #e0f2fe; border-color: #7dd3fc; color: #075985; }
.pos-toggle.tgl-NR  { background: #f0fdf4; border-color: #86efac; color: #166534; }
.pos-toggle.tgl-NP  { background: #eef2ff; border-color: #a5b4fc; color: #3730a3; }
.pos-toggle.tgl-XR  { background: #fce7f3; border-color: #f9a8d4; color: #9d174d; }
.pos-toggle.tgl-stopwords { background: #fef2f2; border-color: #fca5a5; color: #991b1b; }

/* ── Responsive ──────────────────────────────────────────────────── */
@media (max-width: 600px) {
  .demo-header h1 { font-size: 1.3rem; }
  .pipeline-steps { gap: 0.3rem; }
  .step-btn { font-size: 0.75rem; padding: 0.35rem 0.6rem; }
  .token-chip { font-size: 0.85rem; padding: 0.3rem 0.45rem; }
  .viz-area { padding: 1rem; }
}
</style>

<div class="demo-app" id="app">
  <div class="demo-header">
    <h1>Text Preprocessing Pipeline</h1>
    <p class="demo-intro">Step through the text preprocessing pipeline on real sentences from Korean presidential speeches. Each step shows what happens to the text — from raw input to cleaned, analysis-ready output. Use the POS tag and stopword controls in steps 5–6 to experiment with different filtering settings.</p>
    <div class="demo-controls">
      <button class="btn btn-primary" id="randomBtn">Random Sentence</button>
      <select class="filter-select" id="presidentFilter">
        <option value="all">All Presidents</option>
      </select>
    </div>
  </div>

  <div class="sentence-card" id="sentenceCard">
    <p class="sentence-text" id="sentenceText"></p>
    <p class="sentence-meta" id="sentenceMeta"></p>
  </div>

  <div class="pipeline-steps" id="pipelineSteps"></div>

  <div class="viz-area" id="vizArea">
    <div class="viz-label" id="vizLabel"></div>
    <div class="viz-content" id="vizContent"></div>
  </div>

  <div class="nav-row">
    <button class="btn" id="prevBtn">Previous</button>
    <span class="step-description" id="stepDesc"></span>
    <button class="btn" id="nextBtn">Next</button>
  </div>

  <div class="legend" id="legend"></div>
</div>

<script>
(function () {
  "use strict";

  // ── Step definitions ────────────────────────────────────────────
  var STEPS = [
    { id: "raw",      label: "1. Raw Text",  desc: "The original sentence exactly as it appears in the speech." },
    { id: "clean",    label: "2. Clean",      desc: "Punctuation, URLs, and special characters are removed." },
    { id: "tokenize", label: "3. Tokenize",   desc: "The sentence is split into individual morphemes (smallest meaningful units)." },
    { id: "pos",      label: "4. POS Tag",    desc: "Each morpheme is labelled with its part-of-speech category." },
    { id: "filter",   label: "5. Filter",     desc: "Only content words (nouns, verbs, adjectives, adverbs) are kept; stopwords and short tokens are removed." },
    { id: "result",   label: "6. Result",     desc: "The final preprocessed output \u2014 ready for computational analysis." }
  ];

  var LEGEND_DATA = [
    { label: "Noun",      bg: "#dbeafe", border: "#93c5fd" },
    { label: "Verb",      bg: "#ccfbf1", border: "#5eead4" },
    { label: "Adjective", bg: "#fef9c3", border: "#fde047" },
    { label: "Adverb",    bg: "#ede9fe", border: "#c4b5fd" },
    { label: "Particle / Ending", bg: "#f3f4f6", border: "#d1d5db" },
    { label: "Affix",     bg: "#fce7f3", border: "#f9a8d4" }
  ];

  // ── POS tag toggle definitions (individual Kiwi tags) ───────────
  // These match the POS_TAGS setting in the Orange preprocessing scripts.
  // Default: NNG + NNP only (standard for Korean topic modeling).
  var POS_TAG_TOGGLES = [
    { tag: "NNG", label: "Common Noun",  defaultOn: true },
    { tag: "NNP", label: "Proper Noun",  defaultOn: true },
    { tag: "VV",  label: "Verb",         defaultOn: false },
    { tag: "VA",  label: "Adjective",    defaultOn: false },
    { tag: "MAG", label: "Adverb",       defaultOn: false },
    { tag: "NNB", label: "Bound Noun",   defaultOn: false },
    { tag: "NR",  label: "Numeral",      defaultOn: false },
    { tag: "NP",  label: "Pronoun",      defaultOn: false },
    { tag: "XR",  label: "Root",         defaultOn: false }
  ];

  // Active state for each tag toggle + stopwords toggle
  var activeTags = {};
  POS_TAG_TOGGLES.forEach(function (t) { activeTags[t.tag] = t.defaultOn; });
  var removeStopwords = true;

  // ── State ───────────────────────────────────────────────────────
  var data = [];
  var currentEntry = null;
  var currentStep = 0;
  var activeFilter = "all";

  // ── DOM refs ────────────────────────────────────────────────────
  var randomBtn      = document.getElementById("randomBtn");
  var presidentFilter = document.getElementById("presidentFilter");
  var sentenceText   = document.getElementById("sentenceText");
  var sentenceMeta   = document.getElementById("sentenceMeta");
  var pipelineSteps  = document.getElementById("pipelineSteps");
  var vizArea        = document.getElementById("vizArea");
  var vizLabel       = document.getElementById("vizLabel");
  var vizContent     = document.getElementById("vizContent");
  var prevBtn        = document.getElementById("prevBtn");
  var nextBtn        = document.getElementById("nextBtn");
  var stepDesc       = document.getElementById("stepDesc");
  var legendEl       = document.getElementById("legend");

  // ── Build static UI ─────────────────────────────────────────────
  function buildStepButtons() {
    pipelineSteps.innerHTML = "";
    STEPS.forEach(function (s, i) {
      var btn = document.createElement("button");
      btn.className = "step-btn";
      btn.textContent = s.label;
      btn.setAttribute("data-step", i);
      btn.addEventListener("click", function () { goToStep(i); });
      pipelineSteps.appendChild(btn);
    });
  }

  function buildLegend() {
    legendEl.innerHTML = "";
    LEGEND_DATA.forEach(function (item) {
      var el = document.createElement("span");
      el.className = "legend-item";
      el.innerHTML = '<span class="legend-swatch" style="background:' + item.bg + ';border-color:' + item.border + '"></span>' + item.label;
      legendEl.appendChild(el);
    });
  }

  function populatePresidents() {
    var presidents = [];
    var seen = {};
    data.forEach(function (e) {
      if (!seen[e.president]) {
        presidents.push(e.president);
        seen[e.president] = true;
      }
    });
    presidents.sort();
    presidents.forEach(function (p) {
      var opt = document.createElement("option");
      opt.value = p;
      opt.textContent = p;
      presidentFilter.appendChild(opt);
    });
  }

  // ── Filtering & selection ───────────────────────────────────────
  function getFiltered() {
    if (activeFilter === "all") return data;
    return data.filter(function (e) { return e.president === activeFilter; });
  }

  function pickRandom() {
    var pool = getFiltered();
    if (pool.length === 0) return;
    var entry = pool[Math.floor(Math.random() * pool.length)];
    currentEntry = entry;
    currentStep = 0;
    renderSentenceCard();
    goToStep(0);
  }

  // ── Render sentence card ────────────────────────────────────────
  function renderSentenceCard() {
    if (!currentEntry) return;
    sentenceText.textContent = "\u201C" + currentEntry.raw + "\u201D";
    sentenceMeta.textContent = "\u2014 " + currentEntry.president + ", " + currentEntry.source_title;
  }

  // ── Step navigation ─────────────────────────────────────────────
  function goToStep(n) {
    if (n < 0 || n >= STEPS.length) return;
    currentStep = n;
    updateStepButtons();
    renderStep();
    updateNav();
  }

  function updateStepButtons() {
    var btns = pipelineSteps.querySelectorAll(".step-btn");
    btns.forEach(function (btn, i) {
      btn.classList.remove("active", "completed");
      if (i === currentStep) btn.classList.add("active");
      else if (i < currentStep) btn.classList.add("completed");
    });
  }

  function updateNav() {
    prevBtn.disabled = (currentStep === 0);
    nextBtn.disabled = (currentStep === STEPS.length - 1);
    stepDesc.textContent = STEPS[currentStep].desc;
  }

  // ── Step renderers ──────────────────────────────────────────────
  function renderStep() {
    if (!currentEntry) return;
    var step = STEPS[currentStep].id;

    switch (step) {
      case "raw":      renderRaw(); break;
      case "clean":    renderClean(); break;
      case "tokenize": renderTokenize(); break;
      case "pos":      renderPos(); break;
      case "filter":   renderFilter(); break;
      case "result":   renderResult(); break;
    }
  }

  function renderRaw() {
    vizLabel.textContent = "Raw Text";
    vizContent.innerHTML = '<div class="viz-text">' + escHtml(currentEntry.raw) + '</div>';
    vizArea.classList.remove("show-tags");
  }

  function renderClean() {
    vizLabel.textContent = "Cleaned Text";
    // Diff raw vs cleaned to highlight removals
    var raw = currentEntry.raw;
    var cleaned = currentEntry.cleaned;
    var html = diffHighlight(raw, cleaned);
    vizContent.innerHTML = '<div class="viz-text">' + html + '</div>';
    vizArea.classList.remove("show-tags");
  }

  function renderTokenize() {
    vizLabel.textContent = "Morpheme Tokens";
    vizContent.innerHTML = buildTokenChips(false, false);
    vizArea.classList.remove("show-tags");
  }

  function renderPos() {
    vizLabel.textContent = "Part-of-Speech Tags";
    vizContent.innerHTML = buildTokenChips(true, false);
    vizArea.classList.add("show-tags");
  }

  function renderFilter() {
    vizLabel.textContent = "Content-Word Filtering";
    var html = buildPosToggles() + buildTokenChips(true, true);
    vizContent.innerHTML = html;
    vizArea.classList.add("show-tags");
    bindToggleEvents();
  }

  function renderResult() {
    vizLabel.textContent = "Preprocessed Result";
    var html = buildPosToggles();
    var tokens = currentEntry.tokens;
    var kept = [];
    tokens.forEach(function (t) {
      if (isTokenKept(t)) kept.push(t.form);
    });
    html += '<div class="result-tokens">';
    if (kept.length === 0) {
      html += '<span style="color:#6b7280;font-style:italic;">No tokens match the current filter.</span>';
    } else {
      kept.forEach(function (w) {
        html += '<span class="result-token">' + escHtml(w) + '</span>';
      });
    }
    html += '</div>';
    vizContent.innerHTML = html;
    vizArea.classList.remove("show-tags");
    bindToggleEvents();
  }

  // ── Token chip builder ──────────────────────────────────────────
  function isTokenKept(t) {
    var tagOn = activeTags[t.tag] || false;
    if (!tagOn) return false;
    if (removeStopwords && t.is_stopword) return false;
    if (t.form.length < 2) return false;
    if (isDigitOnly(t.form)) return false;
    return true;
  }

  function buildTokenChips(showTags, showFilter) {
    var tokens = currentEntry.tokens;
    var html = '<div class="token-container">';
    tokens.forEach(function (t) {
      var classes = "token-chip cat-" + t.category;

      if (showFilter) {
        if (removeStopwords && t.is_stopword) {
          classes += " stopword";
        } else if (!isTokenKept(t)) {
          classes += " dimmed";
        } else {
          classes += " kept";
        }
      }

      html += '<span class="' + classes + '">';
      html += '<span class="token-form">' + escHtml(t.form) + '</span>';
      if (showTags) {
        html += '<span class="token-tag">' + escHtml(t.tag) + '</span>';
      }
      html += '</span>';
    });
    html += '</div>';
    return html;
  }

  // ── POS toggle builder ────────────────────────────────────────
  function buildPosToggles() {
    var html = '<div class="pos-controls">';
    // POS tag row
    html += '<div class="pos-toggles" style="margin-bottom:0.4rem;">';
    html += '<span class="pos-toggles-label">POS Tags:</span>';
    POS_TAG_TOGGLES.forEach(function (t) {
      var on = activeTags[t.tag];
      html += '<button class="pos-toggle tgl-' + t.tag + (on ? '' : ' off') + '" data-tag="' + t.tag + '">';
      html += escHtml(t.label) + ' <span class="tag-code">' + t.tag + '</span>';
      html += '</button>';
    });
    html += '</div>';
    // Stopwords row
    html += '<div class="pos-toggles">';
    html += '<span class="pos-toggles-label">Stopwords:</span>';
    html += '<button class="pos-toggle tgl-stopwords' + (removeStopwords ? '' : ' off') + '" data-action="stopwords">';
    html += 'Remove stopwords';
    html += '</button>';
    html += '</div>';
    html += '</div>';
    return html;
  }

  function bindToggleEvents() {
    // POS tag toggles
    var tagBtns = vizContent.querySelectorAll(".pos-toggle[data-tag]");
    tagBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var tag = btn.getAttribute("data-tag");
        activeTags[tag] = !activeTags[tag];
        renderStep();
      });
    });
    // Stopwords toggle
    var swBtn = vizContent.querySelector(".pos-toggle[data-action='stopwords']");
    if (swBtn) {
      swBtn.addEventListener("click", function () {
        removeStopwords = !removeStopwords;
        renderStep();
      });
    }
  }

  // ── Helpers ─────────────────────────────────────────────────────
  function escHtml(s) {
    var div = document.createElement("div");
    div.appendChild(document.createTextNode(s));
    return div.innerHTML;
  }

  function isDigitOnly(s) {
    return /^\d+$/.test(s);
  }

  // Simple character-level diff to show what was removed in cleaning
  function diffHighlight(raw, cleaned) {
    // Build a set of chars in cleaned (order-preserving match)
    var ci = 0;
    var result = "";
    for (var ri = 0; ri < raw.length; ri++) {
      if (ci < cleaned.length && raw[ri] === cleaned[ci]) {
        result += escHtml(raw[ri]);
        ci++;
      } else {
        // This char was removed
        if (raw[ri].trim() === "") {
          result += raw[ri]; // whitespace stays
        } else {
          result += '<span class="removed-char">' + escHtml(raw[ri]) + '</span>';
        }
      }
    }
    return result;
  }

  // ── Event listeners ─────────────────────────────────────────────
  randomBtn.addEventListener("click", pickRandom);

  presidentFilter.addEventListener("change", function () {
    activeFilter = this.value;
    pickRandom();
  });

  prevBtn.addEventListener("click", function () { goToStep(currentStep - 1); });
  nextBtn.addEventListener("click", function () { goToStep(currentStep + 1); });

  // Keyboard navigation
  document.addEventListener("keydown", function (e) {
    if (e.target.tagName === "INPUT" || e.target.tagName === "SELECT" || e.target.tagName === "TEXTAREA") return;
    if (e.key === "ArrowRight" || e.key === "l") goToStep(currentStep + 1);
    if (e.key === "ArrowLeft" || e.key === "h") goToStep(currentStep - 1);
    if (e.key === "r") pickRandom();
  });

  // ── Load data & init ────────────────────────────────────────────
  function init() {
    buildStepButtons();
    buildLegend();

    fetch("{{ '/interactive/preprocessing_data.json' | relative_url }}")
      .then(function (r) { return r.json(); })
      .then(function (json) {
        data = json;
        populatePresidents();
        pickRandom();
      })
      .catch(function (err) {
        vizContent.innerHTML = '<p style="color:#ef4444;">Failed to load demo data. Please try refreshing the page.</p>';
        console.error("Failed to load preprocessing data:", err);
      });
  }

  init();
})();
</script>
