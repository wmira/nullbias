# Gray / Alpha Architect Coverage Report

Author: **Wesley Gray** (with co-authors Tobias Carlisle, Jack Vogel) — Alpha Architect
Pass complete: 2026-05-04
Strategies extracted this pass: **12**

---

## Sources Reviewed

| Source | Type | Year | Strategies extracted |
|--------|------|------|----------------------|
| *Quantitative Value* (with Carlisle) | Book | 2012 | gray_quant_value_v1, gray_magic_formula_v1, gray_ebit_ev_value_v1 |
| *Quantitative Momentum* (with Vogel) | Book | 2016 | gray_quant_momentum_v1 |
| *DIY Financial Advisor* | Book | 2015 | Cross-referenced with TMOM, MA, RAA, Dual Momentum strategies |
| QMOM ETF prospectus + factsheets | Paper | 2015 | gray_qmom_etf_v1 |
| QVAL ETF prospectus + factsheets | Paper | 2014 | gray_qval_etf_v1 |
| "Avoiding the Big Drawdown with Trend-Following Investment Strategies" | Paper | 2015 | gray_tmom_v1, gray_ma12_trend_v1 |
| "RAA Education" white paper + RAA Index page | Paper | 2015 | gray_robust_asset_allocation_v1 |
| "RAA vs Dual Momentum Horserace" | Blog post | 2015 | gray_dual_momentum_aa_v1 |
| "The Global Value Momentum Trend Philosophy" | Paper | 2016 | gray_global_value_momentum_trend_v1 |
| "Frog in the Pan: International Evidence" | Paper | 2017 | gray_intl_quant_momentum_v1 |

## Sources Not Yet Reviewed (or not applicable)

| Topic | Reason |
|-------|--------|
| QGRO ETF (quality + growth) | Sister ETF; could be added as separate strategy if requested |
| Beta-arbitrage research papers | Specialised; not a standalone strategy |
| Numerous blog posts on factor decomposition | Educational rather than standalone strategies |
| The QMOM/QVAL "concentrated portfolio" (50 names) vs "long-form" methodology | Differences captured via etf vs book YAMLs |

---

## Strategies Extracted

| ID | Name | Source | Direction | Score |
|----|------|--------|-----------|-------|
| gray_quant_value_v1 | Quantitative Value (full screen) | QV book 2012 | long_only | 4/5 |
| gray_quant_momentum_v1 | Quantitative Momentum (full screen) | QM book 2016 | long_only | 5/5 |
| gray_qmom_etf_v1 | QMOM ETF live methodology | ETF prospectus | long_only | 4/5 |
| gray_qval_etf_v1 | QVAL ETF live methodology | ETF prospectus | long_only | 4/5 |
| gray_tmom_v1 | Time-Series Momentum (TMOM) | AA white paper | long_only | 5/5 |
| gray_ma12_trend_v1 | 12-month MA trend rule | AA / Faber | long_only | 5/5 |
| gray_robust_asset_allocation_v1 | RAA composite (50% TMOM + 50% MA) | RAA paper | long_only | 5/5 |
| gray_dual_momentum_aa_v1 | Dual Momentum (AA variant of Antonacci) | AA blog | long_only | 5/5 |
| gray_global_value_momentum_trend_v1 | GVMT — combined value + momentum + trend | GVMT paper 2016 | long_only | 4/5 |
| gray_magic_formula_v1 | Magic Formula (Greenblatt baseline) | QV book chapter | long_only | 5/5 |
| gray_ebit_ev_value_v1 | Pure EBIT/EV cheapness decile | QV book chapter | long_only | 5/5 |
| gray_intl_quant_momentum_v1 | IMOM International Quant Momentum | FIP intl paper 2017 | long_only | 4/5 |

**Mean completeness score: 4.58 / 5**

---

## Cross-Reference

Gray's contributions add **factor-investing** primitives that were previously missing or thin in the index:

- **Multi-step value screen** (forensic + quality + cheapness) — first explicit fundamentals-based screen with Beneish M-Score, Altman Z-Score, Piotroski F-Score components.
- **Frog-in-the-Pan momentum quality filter** — distinctive smoothness measure that complements simple ROC ranking. Distinct from Clenow's R²-adjusted slope.
- **TMOM and MA composite** — both rules now sit alongside Carver's continuous-forecast EWMACs as alternative trend specifications.
- **Dual Momentum** — first explicit Antonacci-style rule in the index.
- **Magic Formula and pure EBIT/EV** — illustrate the 'cheapness-only' value baseline against which all other value strategies should be measured (per the QV book's own analysis).
- **GVMT** — combined value+momentum+trend overlay; structurally similar to clenow_te_combined_portfolio_v1 but factor-based rather than strategy-based.

---

## Open Questions Generated

1. **Beneish M-Score, Altman Z-Score, Piotroski F-Score formulas** — encoded in YAML via formula_reference; users implementing must source the underlying fundamentals correctly.
2. **Lagged fundamentals convention** — 3-month delay typical for live trading; documented in look_ahead_bias_warnings of every fundamentals-based YAML.
3. **Live-ETF vs research-version differences** — QMOM and QVAL live ETFs apply additional sector caps and liquidity constraints. Both versions documented as separate YAMLs.
4. **GVMT region weights (50/50 US/Intl)** — illustrative; user should optimise for own preferences.
5. **Magic Formula true performance** — Greenblatt's original 30% claim has not been replicated; Gray's QV book retest produces ~13-14% which is much more believable. Documented.
6. **F-Score threshold (>=7 vs >=6)** — Gray uses both in different contexts; defaulted to >=7 (stricter) in this YAML pass.

---

## Recommendations

1. **Remaining gaps**:
   - Options/volatility (currently 0 strategies). Sinclair (book-only) and tastytrade (free) are the obvious next targets.
   - Pairs trading / cointegration (currently 0). Ernest Chan would fill this.
2. **Alpha Architect's site has many more papers** — 100+ research posts on alphaarchitect.com. The 12 strategies here are the structurally distinct ones; further parameter studies are deferable.
3. The factor category (5/64) is now the smallest in the index — future passes (Bandy, Kaufman) may reasonably stay in mean-reversion / trend territory, while Sinclair/tastytrade would expand the factor and options categories.
