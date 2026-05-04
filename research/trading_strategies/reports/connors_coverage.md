# Connors Coverage Report

Author: **Larry Connors**
Pass complete: 2026-05-04
Strategies extracted this pass: **12**

---

## Sources Reviewed

| Source | Type | Year | Coverage |
|--------|------|------|----------|
| Short Term Trading Strategies That Work (with C. Alvarez) | Book | 2008 | 4 strategies extracted (RSI(2), Cumulative RSI, Double 7's, VIX RSI) |
| High Probability ETF Trading (with C. Alvarez) | Book | 2009 | 7 strategies extracted (R3, 3-Day High/Low, MDD, MDU, RSI 25/75, %b, TPS) |
| ConnorsRSI Guidebook / Pullbacks Guidebook | Paper | 2012 | 1 strategy extracted (CRSI Pullback) |

## Sources Not Yet Reviewed (this pass)

| Source | Type | Year | Reason |
|--------|------|------|--------|
| *Street Smarts* (with L. Raschke) | Book | 1995 | Strategies overlap heavily with Raschke's later content; will be extracted under Raschke author folder, cross-linked to Connors |
| *How Markets Really Work* | Book | 2004 | Mostly statistical observations rather than discrete strategies; will pass for "study findings → strategy templates" later |
| *Investment Secrets of a Hedge Fund Manager* | Book | 1995 | Older systematic strategies; some overlap with later books |
| *Connors on Advanced Trading Strategies* | Book | 1998 | TBD — may contain unique strategies |
| *ETF Gap Trading Strategies That Work* | Book | 2010 | Gap-based strategies; not yet covered. Open Question. |
| *Buy the Fear, Sell the Greed* | Book | 2018 | 7 behavioral quant strategies; not yet covered. Open Question. |
| Connors Research Trading Strategy Series (other volumes) | Paper | 2012–2018 | Multiple volumes; CRSI Pullbacks captured. Others may include "Trading the ConnorsRSI on Stocks Above $5 + ADX", "ConnorsRSI Pullbacks with Volume", etc. — Open Question. |
| TradingMarkets.com archives | Web | various | Many posts archived; sweep with Wayback Machine. Open Question. |
| Connors Windows Strategy | Paper | various | Distinct strategy; not yet captured. Open Question. |

---

## Strategies Extracted

| ID | Name | Source | Direction | Score |
|----|------|--------|-----------|-------|
| connors_rsi2_v1 | RSI(2) | Short Term Trading Strategies That Work (2008) | long_only | 5/5 |
| connors_r3_v1 | R3 | High Probability ETF Trading (2009) | long_only | 5/5 |
| connors_double7_v1 | Double 7's | Short Term Trading Strategies That Work (2008) | long_only | 5/5 |
| connors_3day_high_low_v1 | 3-Day High/Low Method | High Probability ETF Trading (2009) | long_only | 5/5 |
| connors_mdd_v1 | Multiple Days Down | High Probability ETF Trading (2009) | long_only | 5/5 |
| connors_mdu_v1 | Multiple Days Up | High Probability ETF Trading (2009) | short_only | 4/5 |
| connors_rsi25_75_v1 | RSI 25 / RSI 75 | High Probability ETF Trading (2009) | long_short | 5/5 |
| connors_pct_b_v1 | %b (Bollinger Bands) | High Probability ETF Trading (2009) | long_only | 5/5 |
| connors_tps_v1 | TPS (Time/Price/Scale-In) | High Probability ETF Trading (2009) | long_short | 4/5 |
| connors_cumulative_rsi_v1 | Cumulative RSI | Short Term Trading Strategies That Work (2008) | long_only | 5/5 |
| connors_crsi_pullback_v1 | ConnorsRSI Pullback | Connors Research guidebook (2012) | long_only | 4/5 |
| connors_vix_rsi_v1 | VIX RSI | Short Term Trading Strategies That Work (2008) | long_only | 5/5 |

**Mean completeness score: 4.75 / 5**

Strategies scored less than 5/5 have one or more `NOT_SPECIFIED` fields where the published rules genuinely leave a parameter open (typically max-position-pct, time stops, or short-side details). Each such field carries a justification in the strategy's `ambiguities_and_assumptions` block.

---

## Cross-Reference

The 12 strategies are all in the **mean-reversion** family. Sub-categories represented:

- Oversold-pullback (RSI-based): rsi2, r3, rsi25_75, cumulative_rsi
- Pattern-based: double7, 3day_high_low, mdd, mdu
- Bollinger-based: pct_b
- Composite indicator: crsi_pullback
- Volatility spike: vix_rsi
- Pyramid scale-in: tps

All long-only strategies share the `close > SMA(close, 200)` regime filter; all short variants use the inverse. Most exit on `close > SMA(close, 5)` or an RSI-overbought threshold.

---

## Open Questions Generated

The following items have been added to `open_questions.md`:

1. *Buy the Fear, Sell the Greed* (2018) — 7 strategies — book required for full extraction.
2. *ETF Gap Trading Strategies That Work* (2010) — book required.
3. *Connors on Advanced Trading Strategies* (1998) — book required.
4. Connors Windows Strategy — Connors Research papers; some publicly available, sweep needed.
5. *How Markets Really Work* — convert statistical findings (e.g., "stocks above 200-SMA outperform after pullback") to documented templates.
6. Other Connors Research Trading Strategy Series volumes — sweep public PDFs.

---

## Recommendations

1. Move Connors-Raschke *Street Smarts* strategies to the Raschke folder for clean attribution; cross-link.
2. If user has access to *Buy the Fear, Sell the Greed*, that single book likely adds 7 high-value strategies.
3. The mean-reversion-on-pullback family is densely populated; future Cesar Alvarez extraction will surface many parameter variations of these same templates that should be documented as separate variants per the spec ("do not merge strategies that appear similar but have different parameters").
