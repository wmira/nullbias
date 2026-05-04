# Alvarez Coverage Report

Author: **Cesar Alvarez**
Pass complete: 2026-05-04
Strategies extracted this pass: **15** (top-15 selection per spec)

---

## Sources Reviewed

The Alvarez Quant Trading blog (alvarezquanttrading.com) is the entire primary source surface for Cesar Alvarez. Each strategy below was extracted from a specific public blog post; URLs are recorded in each strategy YAML's `source.chapter_or_url` field.

| Source | Type | Year | Strategy extracted |
|--------|------|------|--------------------|
| Weekly Mean Reversion Rotation Strategy on S&P500 Stocks | Blog post | 2018 | `alvarez_weekly_sp500_meanrev_rotation_v1` |
| RSI2 Strategy: Double returns with a simple rule change | Blog post | 2017 | `alvarez_rsi2_rule_change_v1` |
| Country ETF Rotation | Blog post | 2017 | `alvarez_country_etf_rotation_v1` |
| Sector Rotation: Should Trading Rules Make Sense? | Blog post | 2017 | `alvarez_etf_sector_rotation_v1` |
| Three Factor ETF Rotation Strategy | Blog post | 2022 | `alvarez_three_factor_etf_rotation_v1` |
| ETF Bond Rotation | Blog post | 2017 | `alvarez_etf_bond_rotation_v1` |
| SPY, SSO and TLT Strategy | Blog post | 2017 | `alvarez_spy_sso_tlt_v1` |
| SPY TLT Rotation | Blog post | 2017 | `alvarez_spy_tlt_rotation_v1` |
| The 50/50 SPY Strategy | Blog post | 2018 | `alvarez_50_50_spy_v1` |
| The ABCs of creating a mean reversion strategy (Parts 1 & 2) | Blog post | 2018 | `alvarez_abc_meanrev_v1` |
| Simple Ideas for a Mean Reversion Strategy with Good Results | Blog post | 2017 | `alvarez_simple_meanrev_v1` |
| ConnorsRSI Analysis | Blog post | 2018 | `alvarez_connorsrsi_pullback_v1` |
| Volume and Mean Reversion | Blog post | 2017 | `alvarez_volume_meanrev_v1` |
| Mean Reversion Entry: At Open vs. Intraday Pullback vs Confirmation / Mean Reversion Entry Timing | Blog post | 2017 | `alvarez_meanrev_entry_timing_v1` |
| Different ranking methods for a monthly S&P500 Stock Rotation Strategy | Blog post | 2018 | `alvarez_monthly_sp500_rotation_ranking_v1` |

## Sources Not Yet Reviewed

The full alvarezquanttrading.com archive is several hundred posts. The 15 above were chosen for structural distinctness. Many additional posts are parameter sensitivity studies on the templates above. Notable un-extracted posts include:

| Topic / post family | Reason for deferral |
|--------------------|---------------------|
| Mean Reversion Check Up posts (annual) | Performance updates, not new strategies |
| Numerous RSI(2) parameter sweeps | Variations on `alvarez_rsi2_rule_change_v1` and `connors_rsi2_v1` |
| ConnorsRSI parameter sweeps | Variations on `alvarez_connorsrsi_pullback_v1` |
| Stop-loss studies | Methodology / not strategies |
| External Strategy Rule Evaluation | Methodology |
| SPY-buying-on-the-open studies | Sub-variants of timing strategies |
| Stocks-on-the-Move replication | Cross-author content (Clenow); will appear under Clenow |
| Holding-period and time-stop studies | Methodology |

These can be picked up in a "deep" Alvarez pass later if desired. The current 15 cover the structurally unique strategies on the blog.

---

## Strategies Extracted

| ID | Name | Source | Direction | Score |
|----|------|--------|-----------|-------|
| alvarez_weekly_sp500_meanrev_rotation_v1 | Weekly Mean Rev Rotation S&P500 | 2018 blog | long_only | 4/5 |
| alvarez_rsi2_rule_change_v1 | RSI(2) Rule Change | 2017 blog | long_only | 4/5 |
| alvarez_country_etf_rotation_v1 | Country ETF Rotation | 2017 blog | long_only | 5/5 |
| alvarez_etf_sector_rotation_v1 | Sector Rotation (Middle-Rank) | 2017 blog | long_only | 5/5 |
| alvarez_three_factor_etf_rotation_v1 | Three-Factor ETF Rotation | 2022 blog | long_only | 4/5 |
| alvarez_etf_bond_rotation_v1 | ETF Bond Rotation | 2017 blog | long_only | 4/5 |
| alvarez_spy_sso_tlt_v1 | SPY/SSO/TLT | 2017 blog | long_only | 4/5 |
| alvarez_spy_tlt_rotation_v1 | SPY/TLT Rotation | 2017 blog | long_only | 5/5 |
| alvarez_50_50_spy_v1 | 50/50 SPY | 2018 blog | long_only | 4/5 |
| alvarez_abc_meanrev_v1 | ABCs Mean Reversion | 2018 blog | long_only | 4/5 |
| alvarez_simple_meanrev_v1 | Simple Mean Reversion | 2017 blog | long_only | 5/5 |
| alvarez_connorsrsi_pullback_v1 | ConnorsRSI Pullback (Alvarez variant) | 2018 blog | long_only | 4/5 |
| alvarez_volume_meanrev_v1 | Volume + Mean Reversion | 2017 blog | long_only | 5/5 |
| alvarez_meanrev_entry_timing_v1 | Mean Reversion Entry Timing | 2017 blog | long_only | 5/5 |
| alvarez_monthly_sp500_rotation_ranking_v1 | Monthly S&P500 Rotation | 2018 blog | long_only | 4/5 |

**Mean completeness score: 4.4 / 5**

Strategies scored 4/5 (rather than 5/5) commonly leave a tunable open — exact volatility threshold, exact rebalance band, optional regime gate, etc. — because Alvarez's posts often present parameter studies rather than a single canonical instance. Defaults documented in `ambiguities_and_assumptions`.

---

## Cross-Reference

Two main families:

- **Mean reversion** (9 strategies): variations on the RSI(2)/SMA-200 template with different filters (volume, ConnorsRSI, limit-order entry, ranking method)
- **Momentum / rotation** (6 strategies): monthly ETF rotations using ROC, vol, and combined factor scores

The mean-reversion strategies share substantial structure with Connors templates; the momentum/rotation work is distinctively Alvarez and adds *new* sub-categories to the cross-reference matrix:

- `dual_momentum_rotation_with_safe_asset` (Country ETF)
- `sector_rotation_anti_top_rank` (counter-intuitive middle-rank)
- `multi_factor_etf_rotation` (Three Factor)
- `regime_switch_with_leverage` (SPY/SSO/TLT)
- `monthly_stock_rotation_with_alternative_rankers`

---

## Open Questions Generated

The following items have been added to `open_questions.md`:

1. **Numerous Alvarez parameter sweeps** — for each canonical template, Cesar tested many variations (RSI thresholds, ranker choices, time-stop bars). The current YAMLs encode the author's "default / most representative" config. A complete `v1`/`v2`/`v3` pass per strategy could capture the parameter family.
2. **Mean Reversion Check Up posts** — annual sanity checks of strategy performance. Useful for documenting *out-of-sample* performance but not new strategies; defer.
3. **Holding-period / time-stop studies** — methodology posts that affect every strategy's `time_stop` field. Treat as cross-cutting later.

---

## Recommendations

1. **Connors → Alvarez cross-references already in place**: every Alvarez mean-reversion strategy YAML lists `connors_rsi2_v1` or `connors_crsi_pullback_v1` in `related_strategy_ids`.
2. **Next author pick** — momentum side of the project is now well-covered by Alvarez's rotation work. Going to **Carver** next is the highest-leverage move (futures-trend / EWMAC family is currently underrepresented in the index, and his free GitHub repo `pysystemtrade` has every strategy in code form already).
3. Alternatively, **Clenow** would close out the equity-momentum + CTA-trend gap with a focused 10–15 strategies.
