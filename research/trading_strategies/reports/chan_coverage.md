# Chan Coverage Report

Author: **Ernest Chan**
Pass complete: 2026-05-04
Strategies extracted this pass: **12**

---

## Sources Reviewed

| Source | Type | Year | Strategies extracted |
|--------|------|------|----------------------|
| *Quantitative Trading: How to Build Your Own Algorithmic Trading Business* | Book | 2008 | Cross-referenced for context |
| *Algorithmic Trading: Winning Strategies and Their Rationale* | Book | 2013 | 9 strategies (pairs trading family, Bollinger meanrev, Hurst, VR, intraday leveraged ETF, overnight gap, EWA/EWC, seasonal) |
| *Machine Trading: Deploying Computer Algorithms to Conquer the Markets* | Book | 2017 | chan_factor_etf_arb_v1 |
| epchan.blogspot.com — multiple posts | Blog | various | chan_volatility_term_structure_v1; cross-referenced for cointegration breakdown discussion |

## Sources Not Yet Reviewed (or not applicable)

| Topic | Reason |
|-------|--------|
| QTS Capital published research notes | Mostly gated marketing copy |
| PredictNow.ai posts on ML for trading | More about ML method than discrete strategies |
| Specific FX intraday strategies in *Machine Trading* | Need more time / book access |
| Hidden Markov Model regime detection | Mentioned but not deep-extracted |
| Detailed event-driven strategies (corp announcements, earnings) | Mentioned in Machine Trading; deferred |

---

## Strategies Extracted

| ID | Name | Source | Direction | Score |
|----|------|--------|-----------|-------|
| chan_pairs_engle_granger_v1 | Pairs Trading via Engle-Granger | Algorithmic Trading 2013 | long_short | 5/5 |
| chan_pairs_johansen_v1 | Cointegration Baskets via Johansen | Algorithmic Trading 2013 | long_short | 4/5 |
| chan_kalman_filter_pairs_v1 | Pairs with Kalman dynamic β | Algorithmic Trading 2013 | long_short | 4/5 |
| chan_bollinger_meanrev_v1 | Bollinger Mean Reversion | Algorithmic Trading 2013 | long_short | 5/5 |
| chan_hurst_regime_filter_v1 | Hurst Regime Detection | Algorithmic Trading 2013 | long_short | 4/5 |
| chan_variance_ratio_filter_v1 | Variance Ratio Regime Filter | Algorithmic Trading 2013 | long_short | 4/5 |
| chan_intraday_leveraged_etf_momentum_v1 | Trend Day Leveraged ETF | Algorithmic Trading 2013 | long_short | 4/5 |
| chan_overnight_gap_momentum_v1 | Overnight Gap Momentum | Algorithmic Trading 2013 | long_short | 4/5 |
| chan_etf_pairs_ewa_ewc_v1 | EWA/EWC Canonical Pair | Algorithmic Trading 2013 | long_short | 4/5 |
| chan_volatility_term_structure_v1 | VIX/VXX Term Structure | epchan blog 2016 | long_short | 4/5 |
| chan_seasonal_futures_v1 | Seasonal Commodity Patterns | Algorithmic Trading 2013 | long_short | 4/5 |
| chan_factor_etf_arb_v1 | Factor Model ETF Arbitrage | Machine Trading 2017 | long_short | 4/5 |

**Mean completeness score: 4.17 / 5**

---

## Cross-Reference

Chan's pass adds **two entirely new structural primitives** to the index:

- **Pairs trading category** (4 strategies — Engle-Granger, Johansen, Kalman, EWA/EWC). Previously zero pairs strategies in the index. This adds the entire stat-arb / cointegration dimension.
- **Statistical regime filters** (Hurst exponent, Variance Ratio test). First explicit regime-detection overlays based on hypothesis testing rather than moving averages.

It also fills two other gaps:

- **Intraday strategies** (Trend Day, Overnight Gap) — first intraday-timeframe entries in the index.
- **Seasonal trading** — first dedicated seasonal-pattern strategy.

---

## Open Questions Generated

1. **Cointegration test choice** — Engle-Granger vs Johansen. Both encoded as separate YAMLs. Both have known small-sample biases.
2. **Hedge ratio estimation** — OLS rolling vs Kalman filter. Kalman generally preferred for live trading; both encoded.
3. **z-score thresholds** — 2/0.5 is conventional but tunable. Documented in variations.
4. **Factor model selection** — chan_factor_etf_arb_v1 uses SPY + sector ETFs; PCA / FF-3 / FF-5 alternatives noted.
5. **Cointegration breakdown** — Chan's own blog posts emphasise that pairs DO break down. EWA/EWC YAML explicitly notes that this once-canonical pair has degraded post-2013.
6. **Intraday data requirement** — Trend Day leveraged ETF strategy requires 15-min bars, materially harder to source than daily OHLC. Flagged.
7. **OOS robustness of published strategies** — Several Chan strategies (Trend Day, EWA/EWC) appear to have lost edge after publication. Documented in `data_snooping_warnings`.

---

## Recommendations

1. Pairs / stat-arb dimension is now well-covered. The index spans the full structural space: trend, momentum, mean-reversion, factor, pairs, seasonal.
2. **Remaining authors** to consider:
   - **Howard Bandy** — book-only; AmiBroker AFL systems
   - **Linda Raschke** — pattern recognition (Holy Grail, Anti, Turtle Soup); some overlap with Connors
   - **Perry Kaufman** — encyclopedic textbook
   - **López de Prado** — meta-methods (HRP, meta-labeling)
   - **Sinclair / tastytrade** — options/volatility (currently 0 in index)
   - **Longmore** — Robot Wealth crypto + FX bootcamps
3. **Most-impactful next pick**: **López de Prado** would add portfolio-construction methods (Hierarchical Risk Parity, meta-labeling, triple-barrier) that are structurally orthogonal to everything currently in the index.
