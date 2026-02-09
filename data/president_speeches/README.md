# Course Data Files

This directory contains truncated corpora and datasets used in class demonstrations and assignments. Full corpora are maintained in the [NLP Corpora for Korean Studies](https://github.com/scdenney/nlp_corpora) repository.

---

## Presidential Speeches (Democratic Era)

**File:** `president_speeches_democratic_era.csv`

### Description

A proportionally sampled subset of Korean presidential speeches from the democratic era (6th Republic onward), drawn from the full presidential speeches corpus. This truncated version is used for in-class demonstrations and assignments in Weeks 2-5.

### Source

Full corpus: [nlp_corpora/data/president_speeches](https://github.com/scdenney/nlp_corpora/tree/main/data/president_speeches)

### Truncation Method

1. **Filtered** to democratic-era presidents only: Roh Tae-woo (노태우) through Moon Jae-in (문재인), excluding authoritarian-era presidents (이승만, 윤보선, 박정희, 최규하, 전두환).
2. **Proportionally sampled** from each president's speeches to produce a corpus of ~750 speeches (with a minimum of 50 per president), preserving the relative representation across administrations.
3. **Random seed:** 42 (for reproducibility).
4. **Sorted** by date.

### Sample Composition

| President | Speeches in Full Corpus | Sampled |
|-----------|------------------------|---------|
| 노태우 (Roh Tae-woo) | 601 | 77 |
| 김영삼 (Kim Young-sam) | 728 | 93 |
| 김대중 (Kim Dae-jung) | 822 | 106 |
| 노무현 (Roh Moo-hyun) | 780 | 100 |
| 이명박 (Lee Myung-bak) | 1,027 | 132 |
| 박근혜 (Park Geun-hye) | 493 | 63 |
| 문재인 (Moon Jae-in) | 1,389 | 178 |
| **Total** | **5,840** | **749** |

### Variables

| Variable | Description |
|----------|-------------|
| `division_number` | Source document reference number |
| `president` | President name (Korean) |
| `title` | Speech title from original source |
| `date` | Speech date (format varies: `YYYY` or `YYYY.MM.DD`) |
| `location` | 국내 (domestic) or 국외 (foreign) |
| `kind` | Speech type (e.g., 취임사, 기념사, 신년사) |
| `speech_text` | Full speech text in Korean |

### File Size

~4.4 MB (749 speeches)
