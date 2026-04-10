# President Moon Jae-in Twitter Corpus

## Overview

This corpus contains metadata and text fields from the official Twitter account of South Korean President **Moon Jae-in** (문재인), covering the period **2012-01-01 through 2020-06-15**. It includes tweets posted before, during, and after Moon's presidency, offering a timeline for examining changes in communication patterns, issue emphasis, and tone across political contexts.

Each tweet is accompanied by core platform metadata (e.g., creation time, retweet count, favorite count), along with additional subgroup variables designed to facilitate analysis. These additional variables identify the political period in which each tweet was posted, extract the year for temporal analysis, and categorize tweets into analytically meaningful periods surrounding the presidency.

---

## Variables Included

9 columns, 3,148 rows. Each row is one tweet.

### Core Metadata

| Variable | Type | Description |
|----------|------|-------------|
| **username** | string | Twitter handle associated with the account. Always `moonriver365`. |
| **tweet_date** | string | Calendar date of the tweet (`YYYY-MM-DD`). Range: 2012-01-01 to 2020-06-15. |
| **tweet_time** | string | Time of day the tweet was posted (`HH:MM:SS`). |
| **text** | string | Full tweet text. Primarily in Korean; some tweets in Spanish or English (121 tweets contain significant Latin-script text, mostly diplomatic messages). May include URLs, hashtags, emojis, or line breaks. **20 missing values** (likely deleted or media-only tweets). |
| **favorites** | integer | Number of likes at the time of data collection. Range: 0–704,101; median: 183; mean: 2,500. Heavily right-skewed. |
| **retweets** | integer | Number of retweets at the time of data collection. Range: 0–279,581; median: 721; mean: 1,787. Heavily right-skewed. |
| **link** | string | Full URL linking to the original tweet (`https://twitter.com/moonriver365/status/...`). |

---

## Augmented Subgroup Variables

| Variable | Type | Description |
|----------|------|-------------|
| **tweet_year** | integer | Four-digit year extracted from `tweet_date`. 9 values: 2012–2020. |
| **period3** | string | Three-category political period indicator based on tweet date. See below. |

---

## `period3` Values

| Value | Date Range | Tweets | Context |
|-------|-----------|--------|---------|
| `pre_presidency` | Before 2016-12-01 | 1,973 (62.7%) | Opposition politician, party leader, 2012 presidential candidate |
| `transition` | 2016-12-01 to 2017-05-09 | 393 (12.5%) | Park Geun-hye impeachment period, snap election campaign |
| `presidency` | 2017-05-10 onward | 782 (24.8%) | In office as 19th President of South Korea |

---

## Tweets by Year

| Year | Tweets | Note |
|------|--------|------|
| 2012 | 1,427 | 45.3% of all tweets; Moon was an active candidate and opposition figure |
| 2013 | 130 | |
| 2014 | 152 | |
| 2015 | 111 | |
| 2016 | 201 | Includes early impeachment period |
| 2017 | 398 | Presidential transition and first months in office |
| 2018 | 260 | |
| 2019 | 299 | |
| 2020 | 170 | Through June 15 only |

Tweeting declined sharply after taking office, consistent with a shift to official presidential communications channels.

---

## Sample Tweets with Translations

| Date | Period | Korean Text | English Translation |
|------|--------|------------|---------------------|
| 2017-05-09 | transition | 사랑하는 국민여러분, 정말 고맙습니다. 위대한 대한민국, 정의로운 대한민국, 당당한 대한민국. 그 대한민국의 자랑스러운 대통령이 되겠습니다. | "Dear citizens, thank you so much. A great Korea, a just Korea, a dignified Korea. I will become a proud president of that Korea." (Election night) |
| 2017-05-09 | transition | 오늘밤, 광화문, 11시. 함께 해주십시오. | "Tonight, Gwanghwamun, 11 o'clock. Please join me." |
| 2020-06-15 | presidency | 남과 북이 함께 돌파구를 찾아 나설 때가 되었습니다. 더는 여건이 좋아지기만 기다릴 수 없는 시간까지 왔습니다. | "The time has come for the South and North to seek a breakthrough together. We have reached a point where we can no longer just wait for conditions to improve." |
| 2020-06-15 | presidency | "우리 한민족이 반드시 같이 공존공영해서 새로운 21세기에 같이 손잡고 세계 일류 국가로 웅비하자"는 김대중 대통령님의 소회를 기억합니다. | "I remember President Kim Dae-jung's reflection: 'Our Korean people must coexist and co-prosper together, joining hands in the new 21st century to soar as a world-class nation.'" |
| 2016-11-30 | pre_presidency | 대구 서문시장에 희망을 보내주십시오. | "Please send hope to Daegu's Seomun Market." (after a devastating fire) |

---

## Multilingual Content

Approximately 121 tweets contain significant Latin-script text. These are primarily:
- **Spanish-language** diplomatic tweets (e.g., messages to Latin American heads of state)
- **English-language** messages for international audiences

Example (Spanish):
> "Sr. Presidente @JuanOrlandoH, nuestra primera llamada telefónica fue muy significativa. Le agradezco su gran interés al 'Nuevo Trato Digital'."

These multilingual tweets are often paired with a Korean-language version posted at nearly the same timestamp.

---

## Data Quality Notes

- **20 rows** have missing `text` (0.6%), likely corresponding to deleted tweets or media-only posts.
- All other columns are fully populated.

---

## File Formats

- **moon_twitter.csv** — UTF-8 CSV version compatible with Orange Data Mining.

---

## Source

The original dataset was obtained from:

**https://www.kaggle.com/datasets/kihunkim/south-korea-president-moon-moon-jaein-twitter/data**
