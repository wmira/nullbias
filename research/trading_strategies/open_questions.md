# Open Questions Log

Issues encountered during extraction where critical detail is missing, ambiguous, or only available behind a paywall. Format: one entry per item, dated.

| Date | Author | Strategy | Question / Gap | Source needed | Status |
|------|--------|----------|----------------|---------------|--------|
| 2026-05-04 | Connors | Buy the Fear, Sell the Greed strategies (~7) | Full rules of all 7 behavioral quant strategies | Book: *Buy the Fear, Sell the Greed* (2018) | Open — awaiting book access |
| 2026-05-04 | Connors | ETF Gap strategies | Specific gap thresholds and entry/exit rules | Book: *ETF Gap Trading Strategies That Work* (2010) | Open — awaiting book access |
| 2026-05-04 | Connors | Connors on Advanced Trading Strategies (1998) | Catalog of strategies; book era is 1990s — may include earlier systems | Book | Open — awaiting book access |
| 2026-05-04 | Connors | How Markets Really Work statistical templates | Convert published statistics (e.g., "stocks above 200-SMA outperform after pullback") into discrete strategy specs | Book: *How Markets Really Work* (2004) | Open |
| 2026-05-04 | Connors | Connors Windows Strategy | Full rules; published as a Connors Research paper | Connors Research paper / public PDF sweep | Open |
| 2026-05-04 | Connors | Other Connors Research Trading Strategy Series volumes | "ConnorsRSI Pullbacks With Volume", "ConnorsRSI on Stocks Above $5 + ADX", etc. | Public PDF sweep needed | Open |
| 2026-05-04 | Connors | TradingMarkets.com archive | Historical articles and original publications of strategy variants | Wayback Machine sweep | Open |
| 2026-05-04 | Connors | RSI(2) Wilder smoothing assumption | Author does not explicitly say Wilder vs simple smoothing in all texts | Default assumed Wilder per RSI standard convention | Resolved (assumption documented per strategy) |
| 2026-05-04 | Connors | %b Bollinger Bands stdev convention (ddof=0 vs ddof=1) | Sample vs population stdev choice not stated | Default ddof=0 (TA-Lib convention); diff is small at period 5 | Resolved (assumption documented) |
| 2026-05-04 | Connors | Streak series in ConnorsRSI | "Increment from zero" vs "reset to ±1 on reversal" varies by platform | Defaulted to increment-from-zero per Stockcharts canonical doc | Resolved (assumption documented) |
| 2026-05-04 | Alvarez | Parameter sweeps as separate variants | Many Alvarez posts test multiple RSI thresholds, ranker choices, time-stop bars. Current YAMLs encode the "most representative" config | A v2/v3 pass per template could capture the parameter family | Open — defer to deep-pass |
| 2026-05-04 | Alvarez | Mean Reversion Check Up annual posts | Out-of-sample performance updates rather than new strategies | Useful as performance reference but not strategy specs | Defer (not blocking) |
| 2026-05-04 | Alvarez | Holding-period / time-stop methodology studies | Cross-cutting parameter affecting every strategy's `time_stop` field | Apply uniformly later as methodology refinement | Open — defer |
| 2026-05-04 | Alvarez | Three-Factor rotation: factor weighting | Author uses simple rank-sum; weighted-rank not tested | Rank-sum is documented default; alternatives in `variations` | Resolved (default chosen) |
| 2026-05-04 | Alvarez | 50/50 SPY: rebalance trigger | Daily evaluation but allocation only changes on regime flip — drift management not specified | Default: rebalance only on regime flip | Resolved (assumption documented) |
| 2026-05-04 | Alvarez | SPY/SSO/TLT low-vol threshold | Threshold parameterised in author's spreadsheet rather than fixed in post | Default 12% annualised realised vol of SPY | Resolved (assumption documented; sweep recommended) |
| 2026-05-04 | Carver | Forecast scalars instrument-dependent | Carver's published scalars (12.1, 8.53, 5.95, 4.10, 2.79, 1.91 for EWMAC; 30 for breakout; ~30 for carry; 60 for skew; ~13 for relmomentum; 100 for acceleration; 50 for fast meanrev) are calibrated for his diversified instrument set | Document published values; user must re-estimate for own instrument set | Resolved (assumption documented per strategy) |
| 2026-05-04 | Carver | IDM and FDM constants | Instrument and forecast diversification multipliers ~2.5 and ~1.4 respectively in Carver's framework. Empirically estimated; require re-estimation when instrument or rule mix changes | Documented in vol_target_overlay; flagged in each rule | Resolved |
| 2026-05-04 | Carver | Additional speeds for breakout, carry, EWMAC | Carver tests breakout 10/40/160/320, carry smoothing 5/20/120, etc. Per spec's "do not merge variants" rule, each speed could warrant its own YAML | Currently captured via `variations` field; expand later if a literal-spec pass is wanted | Open — defer |
| 2026-05-04 | Carver | AFTS 30-strategy chapter enumeration | The 30 strategies in *Advanced Futures Trading Strategies* are a teaching progression, not 30 distinct rule families | Structurally distinct ones extracted; literal 30-entry pass requires book access | Open — defer / requires book |
| 2026-05-04 | Carver | Skew with kurtosis conditioning ("skewK_abs_90") | Distinct enough to warrant own YAML | Defer to deep-pass | Open — defer |
| 2026-05-04 | Carver | Vol estimator: 25-day vs blended long+short | Carver's pysystemtrade uses an adjusted estimator combining 25-day and 10-year averages. Most YAMLs encode the simpler 25-day variant | Document in `ambiguities_and_assumptions`; switch to blended if running long backtests | Resolved (default chosen) |
| 2026-05-04 | Carver | Annualisation factor 16 vs sqrt(252) | Carver uses 16 (≈ sqrt(256)) as a round number in his framework. Some implementations use sqrt(252) ≈ 15.87 | Default to Carver's 16 for consistency; difference < 1% | Resolved |
| 2026-05-04 | Carver | Skewness convention (Pearson moment vs Fisher-Pearson bias-adjusted) | Pandas default is bias-adjusted; scipy.stats has options | Document the chosen library/parameter in implementation | Open (resolution per implementation) |
| 2026-05-04 | Clenow | SOM annualised slope: compounded vs un-compounded | exp(b × 252) - 1 vs b × 252 | Default to compounded (exp form); difference small for typical slopes | Resolved (assumption documented per strategy) |
| 2026-05-04 | Clenow | SOM SPY 200-SMA gating | Applies to NEW positions only — existing positions held per per-stock rules | Documented in entry_signal | Resolved |
| 2026-05-04 | Clenow | SOM rebalance day arbitrary | Author uses Wednesday but explicitly says any day is fine | Documented | Resolved |
| 2026-05-04 | Clenow | SOM long-short borrow / short-fee modeling | Real-world short side eats meaningful return; idealised backtests overstate | Flagged in `look_ahead_bias_warnings` and `notes` | Open — needs realistic short-fee model in implementation |
| 2026-05-04 | Clenow | TE Combined portfolio fixed weights (40/40/20) | Illustrative only; not derived from optimisation | Documented; risk-parity offered as variation | Resolved (assumption documented) |
| 2026-05-04 | Clenow | Curve trading deferred-contract offset | 6-month default; some curves are quarterly | Documented per strategy; per-curve adjustment required | Resolved |
| 2026-05-04 | Clenow | FTT breakout window inclusive vs exclusive of bar t | Convention matters for same-day signals | Defaulted to EXCLUSIVE of bar t; documented | Resolved |
| 2026-05-04 | Gray | Beneish M-Score / Altman Z-Score / Piotroski F-Score formulas | Multi-component composite scores from financial statements | Encoded via formula_reference; user must source fundamentals correctly | Resolved (formulas documented per strategy) |
| 2026-05-04 | Gray | Lagged fundamentals convention (3-month delay) | Critical for live-tradable backtests; naive use of as-restated data creates major look-ahead | Documented in look_ahead_bias_warnings | Resolved |
| 2026-05-04 | Gray | F-Score threshold (>=7 vs >=6) | Both documented in QV book | Defaulted to >=7 (stricter) | Resolved (documented in YAML; alt in variations) |
| 2026-05-04 | Gray | Magic Formula true performance | Greenblatt's 30% claim vs Gray's 13-14% retest | Documented in author_reported_results notes | Resolved (note added) |
| 2026-05-04 | Gray | QMOM/QVAL live ETF vs research version | Live ETFs apply additional sector caps and liquidity constraints | Both versions documented as separate YAMLs (ETF vs book) | Resolved |
| 2026-05-04 | Gray | TMOM excess vs absolute return convention | Some implementations use simple `return > 0` (absolute) instead of excess vs T-Bill | Documented; both produce similar results | Resolved (default = excess) |
| 2026-05-04 | Gray | RAA composite formula (50/50 weighting) | Some implementations require BOTH = 1 (logical AND) instead of weighted average | Documented; canonical AA version is the 50/50 weighted | Resolved |
| 2026-05-04 | Gray | GVMT region weights (50/50 US/Intl) | Illustrative only | Documented; user can change | Resolved |
| 2026-05-04 | Chan | Engle-Granger vs Johansen cointegration test choice | Both have known small-sample biases; Chan recommends Johansen when cointegration is weak | Both encoded as separate YAMLs | Resolved |
| 2026-05-04 | Chan | Hedge ratio: rolling OLS vs Kalman filter | Kalman handles drift better but adds parameter (Q matrix) | Both encoded as separate YAMLs | Resolved |
| 2026-05-04 | Chan | EWA/EWC pair has degraded post-2013 | Once-canonical pair has weakened cointegration | Documented in author_reported_results notes; flagged as illustrative | Resolved |
| 2026-05-04 | Chan | Trend Day leveraged ETF strategy OOS performance | Profits dissipated after publication | Documented in data_snooping_warnings | Resolved |
| 2026-05-04 | Chan | Overnight gap on SPY | Behaviour has shifted to mean-reverting in recent years per modern research | Documented; STOXX 50 was the better example in book era | Resolved |
| 2026-05-04 | Chan | Intraday data requirement | Trend Day strategy needs 15-min bars | Flagged in backtest_specs; many users won't have data feed | Open — data sourcing |
| 2026-05-04 | Chan | Hurst R/S vs Detrended Fluctuation Analysis | R/S has small-sample bias; DFA more robust | Defaulted to R/S per Chan's book; DFA in variations | Resolved |
| 2026-05-04 | Chan | XIV delisting Feb 2018 | Volmageddon ended XIV; SVXY changed to -0.5x | Documented in survivorship_bias_warnings of vol term structure YAML | Resolved |
| 2026-05-04 | Chan | Factor model selection (chan_factor_etf_arb_v1) | SPY+sector vs PCA vs FF-3 vs FF-5 | Defaulted to SPY+sector ETFs per Chan; alternatives in variations | Resolved |
