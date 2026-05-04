# Clenow Coverage Report

Author: **Andreas Clenow**
Pass complete: 2026-05-04
Strategies extracted this pass: **10**

---

## Sources Reviewed

| Source | Type | Year | Strategies extracted |
|--------|------|------|---------------------|
| *Following the Trend: Diversified Managed Futures Trading* (1st ed) | Book | 2013 | clenow_core_trend_v1 |
| *Following the Trend* (2nd ed) | Book | 2022 | clenow_ftt_diversified_breakout_v1 (slower-window variant) |
| *Stocks on the Move: Beating the Market with Hedge Fund Momentum Strategies* | Book | 2015 | clenow_stocks_on_the_move_v1, clenow_stocks_on_move_long_short_v1 |
| *Trading Evolved: Anyone Can Build Killer Trading Strategies in Python* | Book | 2019 | 6 strategies (te_simple_trend, te_global_macro_momentum, te_counter_trend, te_curve_trading, te_carry, te_combined_portfolio) |
| followingthetrend.com 'Trading System Rules' page | Web | various | Cross-referenced for FTT and SOM canonical rules |

## Sources Not Yet Reviewed (or not applicable)

| Source | Reason |
|--------|--------|
| Specific instrument-level configurations in book appendices | Aggregated into the strategy YAMLs; per-instrument calibration is left to the user |
| Annual / blog posts on followingthetrend.com | Performance updates rather than new strategies |
| Trading Evolved Python Notebooks | Code companion to book chapters; rules captured in chapter walkthroughs |

---

## Strategies Extracted

| ID | Name | Source | Direction | Score |
|----|------|--------|-----------|-------|
| clenow_core_trend_v1 | Core CTA Trend (FTT) | FTT 2013 | long_short | 5/5 |
| clenow_stocks_on_the_move_v1 | Stocks on the Move (canonical) | SOM 2015 | long_only | 5/5 |
| clenow_te_simple_trend_v1 | TE Simple Long-Only Equity Trend | TE 2019 | long_only | 5/5 |
| clenow_te_global_macro_momentum_v1 | TE Global Macro Momentum | TE 2019 | long_only | 5/5 |
| clenow_te_counter_trend_v1 | TE Counter-Trend (Bollinger) | TE 2019 | long_only | 4/5 |
| clenow_te_curve_trading_v1 | TE Curve Trading (Calendar) | TE 2019 | long_short | 4/5 |
| clenow_te_carry_v1 | TE Futures Carry (cross-sectional) | TE 2019 | long_short | 4/5 |
| clenow_stocks_on_move_long_short_v1 | SOM Long/Short Variant | SOM 2015 | long_short | 4/5 |
| clenow_ftt_diversified_breakout_v1 | FTT Slow Multi-Window Breakout | FTT 2022 | long_short | 4/5 |
| clenow_te_combined_portfolio_v1 | TE Combined Multi-Strategy | TE 2019 | long_short | 4/5 |

**Mean completeness score: 4.4 / 5**

---

## Cross-Reference

Clenow's primary contributions to the index:

- **Core CTA breakout system** — the practitioner's reference 50-day breakout + 3 ATR trailing stop + ATR-targeted position sizing. Closely related to Carver's vol-targeted EWMACs but uses discrete entry/exit rather than continuous forecast.
- **Stocks on the Move (SOM) momentum** — the most-cited equity momentum implementation in retail-quant literature. The exponential regression × R² scoring is genuinely distinctive vs. simple ROC momentum (Alvarez monthly_sp500_rotation_ranking) and academic 12-1 momentum.
- **Cross-strategy combination** — the Trading Evolved combined portfolio is unique in this index for explicitly combining trend + momentum + mean-reversion sub-strategies in fixed allocations.

---

## Open Questions Generated

1. Annualised slope formula — Clenow uses `exp(daily_b × 252) - 1`; some implementations use `daily_b × 252` (un-compounded). Difference matters for very-high-momentum stocks. Documented per strategy.
2. SPY 200-SMA gating in SOM — applies to NEW buys only; existing positions continue per per-stock rules. Documented.
3. SOM weekly rebalance day arbitrary; book uses Wednesday. Documented.
4. SOM long-short variant — short side is real-world hard to monetise after borrow costs. Flagged.
5. TE Combined portfolio fixed weights (40/40/20) — illustrative only; risk-parity is a more principled construction.
6. Curve trading deferred-contract offset — defaults to 6 months; varies by curve.

---

## Recommendations

1. The combined index now has **futures + equities + ETFs + bonds** covered. Remaining major gap: **options/volatility** — Sinclair (book-only) and tastytrade (free).
2. Or fill in **factor/value** with **Wesley Gray / Alpha Architect** — quant value, quant momentum, dual momentum tactical asset allocation, all freely documented.
3. **Ernest Chan** would add pairs-trading / cointegration which is structurally distinct from anything currently in the index.
