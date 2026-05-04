# Implementation Priority List

Strategies ranked by composite score. Currently includes Connors first-wave (12 strategies). Expand with each author pass.

Scoring (0–5 each, 20 max):

- **Spec completeness** — fewer NOT_SPECIFIED fields, more deterministic rules
- **Reported performance robustness** — author's claimed Sharpe / win rate / out-of-sample notes
- **Data availability** — whether the data needed is freely accessible (yes for everything in this batch)
- **Computational simplicity** — daily bars, simple indicators, low parameter count

| Rank | Strategy ID | Spec | Perf | Data | Simplicity | Total | Notes |
|------|-------------|------|------|------|------------|-------|-------|
| 1 | connors_rsi2_v1 | 5 | 4 | 5 | 5 | **19** | Iconic, simple, robust template |
| 2 | connors_double7_v1 | 5 | 4 | 5 | 5 | **19** | One-line entry, one-line exit |
| 3 | connors_3day_high_low_v1 | 5 | 4 | 5 | 5 | **19** | Pure price-pattern, no oscillator |
| 4 | connors_mdd_v1 | 5 | 4 | 5 | 5 | **19** | Count-of-down-days, very simple |
| 5 | connors_cumulative_rsi_v1 | 5 | 4 | 5 | 4 | **18** | Slight indicator twist on RSI(2) |
| 6 | connors_r3_v1 | 5 | 4 | 5 | 4 | **18** | Three-bar sequence is more selective |
| 7 | connors_pct_b_v1 | 5 | 3 | 5 | 4 | **17** | Bollinger config (5,1) is non-standard; keep robustness in mind |
| 8 | connors_rsi25_75_v1 | 5 | 4 | 5 | 3 | **17** | Adds optional pyramid; both sides supported |
| 9 | connors_vix_rsi_v1 | 5 | 3 | 4 | 4 | **16** | Needs VIX data series (free); rare signals |
| 10 | connors_crsi_pullback_v1 | 4 | 4 | 4 | 3 | **15** | Composite indicator + ADX adds steps |
| 11 | connors_tps_v1 | 4 | 4 | 5 | 2 | **15** | Pyramiding adds bookkeeping complexity |
| 12 | connors_mdu_v1 | 4 | 3 | 4 | 4 | **15** | Short side; requires borrow assumption |

## Recommended order for first-cut backtests

If the goal is to reproduce Connors-style strategies in code with minimum overhead, build them in this order:

1. `connors_rsi2_v1` — establishes the SMA(200) regime filter, Wilder RSI(2) implementation, end-of-day fill convention. All later strategies reuse these primitives.
2. `connors_double7_v1` — verify rolling-window N-day extremum implementation.
3. `connors_3day_high_low_v1`, `connors_mdd_v1` — pattern-counting primitives.
4. `connors_cumulative_rsi_v1`, `connors_r3_v1` — variations on the RSI(2) template.
5. `connors_pct_b_v1` — Bollinger Bands and %b primitive.
6. `connors_rsi25_75_v1` — adds a different RSI period (4) and optional scale-in.
7. `connors_vix_rsi_v1` — adds external VIX data series.
8. `connors_tps_v1` — full multi-tranche scale-in mechanics.
9. `connors_crsi_pullback_v1` — composite indicator (ConnorsRSI) plus ADX filter.
10. `connors_mdu_v1` — exercises short-side path and borrow modelling.

This sequence minimizes redundant work — each step adds at most one new primitive on top of the prior set.
