# Week 11 Data Dictionary

A short reference key for the two datasets used in the Week 11 application
exercise. Use this if a Korean categorical label slows you down — it is
not meant to teach you what the categories *contain*; that is what you
will discover by reading the documents.

---

## Dataset 1 — `dataset1_kjyg_sample.csv` (Kyongje Yongu, NK)

*Kyongje Yongu* (경제연구, "Economic Research") is the flagship economics journal
of the DPRK Academy of Social Sciences in Pyongyang. Articles are regime-aligned
theoretical and applied economic argumentation — frequently citing the words of
the supreme leader and articulating the ideological framing of the planned
economy. The Week 11 sample is **360 articles, balanced at 120 per leader era**
across the late Kim Il-sung period, the full Kim Jong-il era, and the early Kim
Jong-un era — so any Box Plot grouped by `era` compares equal-sized populations.
Era labels are already in English; here is what each leadership period
corresponds to in case the dates are not familiar.

### `era` values

| Value (as it appears in the CSV) | What it refers to |
|---|---|
| `Kim Il-sung (1987-1994)` | Late Kim Il-sung period — final eight years of his rule, ending with his death in July 1994 |
| `Kim Jong-il (1995-2011)` | Full Kim Jong-il era — from his consolidation of power after Kim Il-sung's death through to his own death in December 2011 |
| `Kim Jong-un (2012-2017)` | Early Kim Jong-un era — from succession through 2017, the period in which "our-style economic management methods" and limited market-tolerant rhetoric appeared |

The three label strings are exactly as written above (with the
parenthetical year range). Box Plot will treat them as three discrete
groups in that order.

---

## Dataset 2 — `dataset2_bluehouse_petitions_sample.csv` (Cheong Wa Dae petitions)

The Cheong Wa Dae (청와대, "Blue House") online petitions platform was launched
by the Moon Jae-in administration in August 2017. Citizens could post a petition
on any topic; petitions reaching 200,000 signatures within 30 days received an
official government response. The corpus is a window into what ordinary South
Koreans wanted to push onto the national agenda — citizen-vernacular political
writing, not journalism or academia. The Week 11 sample is **360 petitions,
balanced at 60 per category** across six thematically distinct categories. The
category labels are in Korean; short English glosses follow.

### `category` values

| Value (Korean, as in the CSV) | English gloss |
|---|---|
| `정치개혁` | Political reform |
| `인권/성평등` | Human rights / gender equality |
| `외교/통일/국방` | Foreign affairs / unification / national defence |
| `육아/교육` | Childcare / education |
| `보건복지` | Health and welfare |
| `일자리` | Jobs / employment |

### `answered_label` values

| Value | Meaning |
|---|---|
| `Answered` | Petition reached the 200,000-signature threshold and received an official government response |
| `Not answered` | Petition did not reach the threshold |

Heads-up: in the 360-row sample, **all 360 petitions are `Not answered`**.
That column has no variance and is not useful as a grouping variable
for this assessment.

### `year` values

`2017` (n = 64) or `2018` (n = 296). The platform launched in August 2017,
so 2018 dominates.
