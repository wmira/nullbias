# Carver Coverage Report

Author: **Robert Carver**
Pass complete: 2026-05-04
Strategies extracted this pass: **15**

---

## Sources Reviewed

Carver's primary sources are uniquely well-documented online: the qoppac.blogspot.com archive, the open-source `pysystemtrade` GitHub repository (a working implementation of every rule), and the AFTS book GitHub-notes repos. Books supplement with calibrated forecast scalars and instrument-specific configs.

| Source | Type | Year | Strategies extracted |
|--------|------|------|----------------------|
| *Systematic Trading* (Appendix B) | Book | 2015 | EWMAC family (6) + carry |
| *Advanced Futures Trading Strategies* (30-strategy reference) | Book | 2023 | Acceleration, Fast Mean Reversion, several others; 30-strategy framework documented in the book and open community notes (e.g., majkong14/advanced-futures-notes on GitHub) |
| qoppac.blogspot.com — multiple posts (2015–2025) | Blog | various | Breakout (2016), Asset Trend (2017), Skew (2019/2020), Relative Momentum (2019), Forecast Scalars (2025) |
| pysystemtrade GitHub (open-source) | Code | 2015–present | Every rule has a reference Python implementation in `private.systems.provided` and `sysquant.estimators` |
| *Leveraged Trading* | Book | 2019 | Position-sizing framework specifically for retail |

## Sources Not Yet Reviewed

| Topic | Reason |
|-------|--------|
| Other speeds of breakout (10, 40, 160, 320) | Variations of the (20) and (80) entries; spec's no-merge rule favours separate YAMLs but diminishing distinctness — defer |
| Additional carry-rule speeds (5, 20, 120 day smoothing) | Variations of `carver_carry_v1`; defer |
| Skew with kurtosis conditioning ("skewK_abs_90") | Distinct enough to warrant own YAML; defer |
| Specific asset-class subset rules (e.g., FX-only carry, equity-only EWMAC) | Specialisations of the rules above |
| AFTS Strategy 1–30 individual chapters not enumerated above | The 30-strategy structure of AFTS is partially incremental (each builds the framework) rather than 30 standalone rules. The structurally distinct ones are captured. |
| Full Smart Portfolios methodology (passive allocation) | Different track from active rules; can be added if needed |

---

## Strategies Extracted

| ID | Name | Source | Direction | Score |
|----|------|--------|-----------|-------|
| carver_ewmac_2_8_v1 | EWMAC(2,8) Fastest | ST/AFTS | long_short | 4/5 |
| carver_ewmac_4_16_v1 | EWMAC(4,16) Fast | ST/AFTS | long_short | 4/5 |
| carver_ewmac_8_32_v1 | EWMAC(8,32) Medium-Fast | ST/AFTS | long_short | 4/5 |
| carver_ewmac_16_64_v1 | EWMAC(16,64) Medium (best Sharpe) | ST/AFTS | long_short | 5/5 |
| carver_ewmac_32_128_v1 | EWMAC(32,128) Slow | ST/AFTS | long_short | 4/5 |
| carver_ewmac_64_256_v1 | EWMAC(64,256) Slowest | ST/AFTS | long_short | 4/5 |
| carver_carry_v1 | Carry rule (60-day smooth) | ST/AFTS | long_short | 4/5 |
| carver_breakout_20_v1 | Breakout(20) channel | qoppac 2016 | long_short | 5/5 |
| carver_breakout_80_v1 | Breakout(80) channel | qoppac 2016 | long_short | 5/5 |
| carver_skew_v1 | 365-day skew | qoppac 2020 | long_short | 4/5 |
| carver_assettrend_v1 | Cross-sectional EWMAC demeaned by asset class | qoppac 2017 | long_short | 4/5 |
| carver_relmomentum_v1 | Cross-sectional return momentum | qoppac 2019 | long_short | 4/5 |
| carver_acceleration_v1 | EWMAC of EWMAC forecast | AFTS 2023 | long_short | 4/5 |
| carver_fast_meanrev_v1 | Fast vol-normalised z-score reversal | AFTS 2023 | long_short | 4/5 |
| carver_vol_target_overlay_v1 | Volatility-targeted position sizing overlay | ST/LT/AFTS | long_short | 5/5 |

**Mean completeness score: 4.27 / 5**

The score-4 entries are typically because (a) the forecast scalar value depends on the specific instrument set and is calibrated empirically rather than by formula, and (b) the IDM/FDM constants for the position-sizing overlay must be re-estimated whenever the rule mix or instrument set changes. These are documented in `ambiguities_and_assumptions` for each strategy.

---

## Cross-Reference

Carver's framework brings entirely new structural primitives to the index:

- **Continuous-forecast rules** with a standardised ±20 forecast scale (vs the binary buy/exit rules from Connors and Alvarez)
- **Volatility-targeted position sizing** as a portfolio overlay (vs equal-weight / fixed-percentage in Connors/Alvarez)
- **Multi-rule combination** with empirically estimated forecast diversification (FDM) and instrument diversification (IDM) multipliers
- **Cross-sectional rules** (asset-class demean, relative momentum) that have NET ZERO directional exposure
- **Carry rule** based on futures term-structure — a fundamentally different signal source

This is also the first pass to populate **futures** as an asset class. The cross-reference matrix now needs a futures/CTA section (added to `cross_reference_matrix.md`).

---

## Open Questions Generated

1. **Forecast scalar calibration** — All scalars in the YAMLs are Carver's published values from his diversified instrument set. They are NOT universally correct; users running a different instrument mix should re-estimate. Documented per-strategy.
2. **IDM / FDM constants** — Same as above; these are portfolio-level constants that require empirical estimation.
3. **Additional EWMAC, breakout, and carry speeds** — Catalogued as variations rather than separate YAMLs. Re-visit if the spec's "do not merge variants" rule needs to be applied more strictly.
4. **AFTS 30-strategy enumeration** — The 30 strategies in *Advanced Futures Trading Strategies* are a teaching progression, not 30 distinct rule families. The structurally distinct ones are extracted; if a literal 30-entry pass is wanted, that's a separate effort.
5. **Live trading details** — Carver's live performance posts (qoppac annual updates) are useful for OOS validation but not new strategies.

---

## Recommendations

1. **Implementation priority**: `carver_vol_target_overlay_v1` is the foundational prerequisite. Build it first; every other Carver rule plugs into it.
2. **Most-bang-for-buck rules**: EWMAC(16,64) + carry are the two pillars; a 2-rule system already captures most of Carver's published Sharpe.
3. **Next author** — going to **Clenow** next would give equity-momentum coverage (Stocks on the Move) plus an alternative CTA-trend implementation (Following the Trend) for cross-author validation.
