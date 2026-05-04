# Cross-Reference Matrix

Strategies grouped by category and structural template, designed to surface duplicates and parameter variations across authors. Populated with Connors (12), Alvarez (15), Carver (15), Clenow (10), Gray (12), Chan (12), Raschke (8) — total **84**. Expand with each additional author pass.

## By Category

### Mean Reversion (27 of 84) — adds Raschke Turtle Soup long/short and 80-20

#### Sub-template: Oversold pullback above long-term moving average

Pattern: `close > SMA(close, 200)` + oversold momentum oscillator + exit on momentum recovery.

| Strategy ID | Oscillator | Entry threshold | Exit | Key knob |
|-------------|------------|-----------------|------|----------|
| connors_rsi2_v1 | RSI(2) | < 5 | close > SMA(5) | Single-bar oversold |
| connors_r3_v1 | RSI(2) | sequence: >60 → < prior → < prior → <10 | RSI(2) > 70 | Three-bar declining |
| connors_rsi25_75_v1 (long) | RSI(4) | < 25 (add at < 20) | RSI(4) > 55 | Slower oscillator + scale-in |
| connors_cumulative_rsi_v1 | sum RSI(2)[t]+RSI(2)[t-1] | < 35 | RSI(2) > 65 | Two-day cumulative |
| connors_crsi_pullback_v1 | ConnorsRSI(3,2,100) | < 5 | CRSI > 70 | Composite indicator |
| alvarez_rsi2_rule_change_v1 | RSI(2) | < 5 for 2 consecutive days | RSI(2) > 65 | Limit-order at -4% close |
| alvarez_simple_meanrev_v1 | RSI(2) | < 5 | RSI(2) > 65 | 200% invested cap |
| alvarez_abc_meanrev_v1 | RSI(2) + 5% below SMA(10) | < 5 AND ≤ 0.95×SMA(10) | RSI(2) > 65 | Combined two-indicator |
| alvarez_volume_meanrev_v1 | RSI(2) + volume spike | < 5 AND vol > 1.5×SMA(21,vol) | RSI(2) > 65 | Volume-confirmed |
| alvarez_connorsrsi_pullback_v1 | ConnorsRSI(3,2,100) + ADX(10) | < 5 + ADX > 30 | ConnorsRSI > 70 | Limit-order at -10% |
| alvarez_meanrev_entry_timing_v1 | RSI(2) | < 5 | RSI(2) > 65 | Limit-order timing study |

#### Sub-template: Pattern / count-based oversold

| Strategy ID | Pattern | Exit |
|-------------|---------|------|
| connors_double7_v1 | close = rolling 7-day low | close = rolling 7-day high |
| connors_3day_high_low_v1 | 3 lower highs AND 3 lower lows AND close < SMA(5) | close > SMA(5) |
| connors_mdd_v1 | ≥4 down days in last 5, close < SMA(5) | close > SMA(5) |

#### Sub-template: Bollinger / band-extreme

| Strategy ID | Indicator | Entry | Exit |
|-------------|-----------|-------|------|
| connors_pct_b_v1 | %b on Bollinger(5, 1) | < 0.2 for 3 consecutive bars | %b > 0.8 |

#### Sub-template: Pyramid scale-in mean reversion

| Strategy ID | Tranche schedule | Trigger | Exit |
|-------------|------------------|---------|------|
| connors_tps_v1 | 10 / 20 / 30 / 40 % | RSI(2) < 25 (initial), then lower close adds | RSI(2) > 70 closes all |

#### Sub-template: Volatility-spike buy

| Strategy ID | Volatility input | Trigger | Exit |
|-------------|------------------|---------|------|
| connors_vix_rsi_v1 | RSI(2) of VIX > 90, VIX gap up | + SPY RSI(2) < 30, SPY > SMA(200) | SPY RSI(2) > 65 |

#### Sub-template: Counter-trend short

| Strategy ID | Pattern | Direction |
|-------------|---------|-----------|
| connors_mdu_v1 | ≥4 up days in last 5, close > SMA(5), below 200-SMA | short_only |

#### Sub-template: Cross-sectional rotation pulled-back

| Strategy ID | Universe | Rank | Hold |
|-------------|----------|------|------|
| alvarez_weekly_sp500_meanrev_rotation_v1 | S&P500 (above 200-SMA) | Top-5 most-sold (5-day return asc) | 1 week |

### Momentum / Rotation (16 of 76) — adds Chan intraday leveraged ETF + overnight gap

#### Sub-template: Single-asset relative strength

| Strategy ID | Universe | Ranker | Allocation |
|-------------|----------|--------|------------|
| alvarez_spy_tlt_rotation_v1 | SPY, TLT | 3-month return | 100% to top-1 |

#### Sub-template: Multi-asset class rotation with safety asset

| Strategy ID | Universe | Ranker | Safety asset |
|-------------|----------|--------|--------------|
| alvarez_country_etf_rotation_v1 | Country ETFs | 6m return + dual SMA filter | IEF |
| alvarez_etf_bond_rotation_v1 | Bond ETFs | 3m return + 6m SMA filter | SHY/cash |
| alvarez_three_factor_etf_rotation_v1 | Sector ETFs | rank-sum of (20-day ROC desc, 6m ROC desc, 100-day vol asc) | cash |

#### Sub-template: Counter-momentum sector rotation

| Strategy ID | Anomaly | Direction |
|-------------|---------|-----------|
| alvarez_etf_sector_rotation_v1 | Buy mid-rank sectors (4–6 of 9), not top-3 | long_only |

#### Sub-template: Cross-sectional momentum on stocks

| Strategy ID | Universe | Ranker | Top-N |
|-------------|----------|--------|-------|
| alvarez_monthly_sp500_rotation_ranking_v1 | S&P500 (above 100-SMA) | 12-1 momentum | Top-10 |

#### Sub-template: Regime-dependent leverage

| Strategy ID | Bull alloc | Bear alloc |
|-------------|------------|------------|
| alvarez_50_50_spy_v1 | 50% SPY + 50% SSO (~1.5x net) | 100% TLT |
| alvarez_spy_sso_tlt_v1 | SSO if low-vol; else SPY | 100% TLT |

---

## Trend Following / CTA (24 of 84) — Carver + Clenow + Gray + Raschke (Holy Grail, Anti, 3-10, NR4/NR7)

#### Sub-template: Continuous-forecast EWMA crossover

| Strategy ID | L_fast | L_slow | Forecast scalar | Turnover/year |
|-------------|--------|--------|-----------------|---------------|
| carver_ewmac_2_8_v1 | 2 | 8 | 12.1 | ~25× |
| carver_ewmac_4_16_v1 | 4 | 16 | 8.53 | ~12× |
| carver_ewmac_8_32_v1 | 8 | 32 | 5.95 | ~6× |
| carver_ewmac_16_64_v1 | 16 | 64 | 4.10 | ~3× |
| carver_ewmac_32_128_v1 | 32 | 128 | 2.79 | ~1.5× |
| carver_ewmac_64_256_v1 | 64 | 256 | 1.91 | <1× |

#### Sub-template: Channel breakout (continuous forecast)

| Strategy ID | Window | Smoothing |
|-------------|--------|-----------|
| carver_breakout_20_v1 | 20 | EWMA span=5 |
| carver_breakout_80_v1 | 80 | EWMA span=20 |

#### Sub-template: Cross-sectional / asset-class trend

| Strategy ID | Construction |
|-------------|--------------|
| carver_assettrend_v1 | EWMAC(16,64) demeaned by asset class |
| carver_acceleration_v1 | First-difference of EWMAC(16,64) raw forecast |

#### Sub-template: Donchian breakout + ATR stop (discrete entry/exit)

| Strategy ID | Window | Stop | Sizing |
|-------------|--------|------|--------|
| clenow_core_trend_v1 | 50-day Donchian + EMA(50) > EMA(100) confirm | 3 × ATR(100) trailing | ATR-targeted (20 bps per ATR) |
| clenow_ftt_diversified_breakout_v1 | 100-day Donchian + EMA(100) > EMA(200) confirm | 3 × ATR(100) trailing | Same |

#### Sub-template: Simple long-only MA trend filter

| Strategy ID | Filters | Universe |
|-------------|---------|----------|
| clenow_te_simple_trend_v1 | close > SMA(200) AND close > close[t-90] | S&P 500 |

#### Sub-template: Multi-strategy portfolio meta

| Strategy ID | Sub-strategies | Allocation |
|-------------|----------------|------------|
| clenow_te_combined_portfolio_v1 | SOM + TE_global_macro + TE_counter_trend | 40/40/20 |

## Pairs / Stat-Arb (4 of 76) — entirely Chan

| Strategy ID | Method | Structure |
|-------------|--------|-----------|
| chan_pairs_engle_granger_v1 | Engle-Granger CADF cointegration | 2-leg pair; OLS hedge ratio + ADF on residual |
| chan_pairs_johansen_v1 | Johansen test | N-leg basket with eigenvector weights |
| chan_kalman_filter_pairs_v1 | Kalman dynamic hedge ratio | 2-leg pair; β evolves over time |
| chan_etf_pairs_ewa_ewc_v1 | Canonical example | EWA/EWC on Engle-Granger or Kalman |

## Seasonal (1 of 76)

| Strategy ID | Pattern |
|-------------|---------|
| chan_seasonal_futures_v1 | Calendar-based commodity seasonality (NG, HO, RB, agriculturals) |

## Factor (14 of 76) — Carver + Clenow + Gray + Chan

| Strategy ID | Construction |
|-------------|--------------|
| carver_carry_v1 | Vol-normalised futures term-structure carry, EWMA-smoothed |
| carver_skew_v1 | 365-day realised skewness, sign-flipped, cross-sectionally demeaned |
| clenow_te_curve_trading_v1 | Calendar spread z-score mean reversion |
| clenow_te_carry_v1 | Cross-sectional carry (long top quartile, short bottom quartile) |
| gray_quant_value_v1 | Forensic + quality + cheapness multi-step screen |
| gray_qval_etf_v1 | QVAL ETF: live methodology version of QV |
| gray_magic_formula_v1 | Greenblatt 2-factor (cheapness × ROC) baseline |
| gray_ebit_ev_value_v1 | Pure EBIT/EV decile (cheapness only) |
| gray_global_value_momentum_trend_v1 | 50/50 value+momentum + per-region trend overlay |
| chan_hurst_regime_filter_v1 | Hurst exponent overlay (mean rev vs trend regime) |
| chan_variance_ratio_filter_v1 | VR test overlay (statistical regime detection) |
| chan_volatility_term_structure_v1 | VIX/VXV ratio for VXX positioning |
| chan_factor_etf_arb_v1 | Factor model residual mean reversion on sector ETFs |

## Portfolio-Level Overlay (1 of 42)

| Strategy ID | Function |
|-------------|----------|
| carver_vol_target_overlay_v1 | Volatility-targeted continuous-forecast position sizing; prerequisite for all other Carver rules |

## By Asset Class

| Asset | Strategy count | Strategies |
|-------|---------------|------------|
| Futures | 22 | 15 Carver + 4 Clenow + 3 Chan (overnight gap, seasonal, Hurst/VR overlays) |
| ETFs | 32 | All Connors + 5 Alvarez + 2 Clenow + 6 Gray + 7 Chan (most pairs/regime/factor strategies) |
| Equities | 30 | Alvarez mean-rev + 4 Connors + 4 Clenow + 8 Gray + 5 Chan (pairs, Bollinger, regime overlays) |
| Bonds | 2 | alvarez_etf_bond_rotation, alvarez_spy_tlt_rotation |
| FX | 1 | (carver overlay supports FX) |
| Options | 0 | (none yet) |

---

## By Direction

| Direction | Count | Notes |
|-----------|-------|-------|
| long_only | 41 | + raschke_turtle_soup_long_v1 |
| short_only | 2 | + raschke_turtle_soup_short_v1 |
| long_short | 41 | + 6 Raschke (holy_grail, anti, 80-20, 3-10, ID/NR4, NR7) |

---

## Common Building Blocks

These appear across multiple strategies and are candidates for shared utility code in any backtest framework:

- **200-period simple moving average regime filter** (10 of 12 strategies)
- **5-period simple moving average exit / pullback definition** (8 of 12)
- **2-period Wilder RSI** (8 of 12)
- **Rolling N-day high/low close** (2 of 12)
- **End-of-day signal, end-of-day fill** (12 of 12)

---

## Open: Cross-Author Duplication Watch

When subsequent authors are extracted, watch for:

- **RSI-based oversold pullbacks** (Alvarez has many variations of these on his blog; document each as separate strategy ID rather than merging)
- **Bollinger %b** (likely also in Bandy's *Mean Reversion Trading Systems*)
- **Volatility-regime-gated buys** (Chan has analogous structures)
- **Trend-followed-by-pullback** (Carver's blog covers similar templates with different parameters)

The spec instructs: *"Do not merge strategies that appear similar but have different parameters — document each variant."*
