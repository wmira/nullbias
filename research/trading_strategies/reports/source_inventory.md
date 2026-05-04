# Source Inventory — All Target Authors

Phase 1 deliverable. For each author, this lists the publications and online assets that contain rules-based trading strategies. Free / publicly accessible items are marked **[free]**; commercial books are marked **[book]** (require best-effort recall from public references). SSRN papers are typically free.

---

## 1. Larry Connors

### Books
- **[book]** *Street Smarts: High Probability Short-Term Trading Strategies* (1995, with Linda Bradford Raschke). M. Gordon Publishing.
- **[book]** *Investment Secrets of a Hedge Fund Manager* (1995).
- **[book]** *Connors on Advanced Trading Strategies* (1998).
- **[book]** *How Markets Really Work: A Quantitative Guide to Stock Market Behavior* (2004, with Conor Sen). M. Gordon.
- **[book]** *Short Term Trading Strategies That Work* (2008, with Cesar Alvarez). TradingMarkets Publishing Group. ISBN 978-0-9755513-9-9.
- **[book]** *High Probability ETF Trading: 7 Professional Strategies* (2009, with Cesar Alvarez). ISBN 978-0-615-29741-5.
- **[book]** *ETF Gap Trading Strategies That Work* (2010).
- **[book]** *The Connors Research Trading Strategy Series* (multi-volume; 2012–2018). Includes "ConnorsRSI" pullback guidebooks.
- **[book]** *Buy the Fear, Sell the Greed: 7 Behavioral Quant Strategies for Traders* (2018). ISBN 978-0-578-20650-9.

### Papers / Public Research
- **[free]** *ConnorsRSI: An Introduction to ConnorsRSI* — Connors Research guidebook. (PDF circulated; e.g., qmatix.com mirror.)
- **[free]** Various Connors Research short papers historically posted to TradingMarkets.com (some now archived on the Wayback Machine).

### Strategies known to be in scope
RSI(2), Cumulative RSI, R3, Double 7's, 3-Day High/Low, MDU/MDD, RSI 25/75, %b (Bollinger Bands), TPS (Time/Price/Scale-In), ConnorsRSI Pullback, VIX RSI, Crash + Rally Down, multi-day pullback variants, Buy-the-Fear/Sell-the-Greed strategies (~7), Connors Windows.

---

## 2. Howard Bandy

### Books
- **[book]** *Quantitative Trading Systems* (2007, 2nd ed 2011). Blue Owl Press.
- **[book]** *Mean Reversion Trading Systems* (2013). Blue Owl Press.
- **[book]** *Modeling Trading System Performance* (2011).
- **[book]** *Quantitative Technical Analysis* (2015).

### Public assets
- **[free]** Author website (blueowlpress.com) — historical articles and AmiBroker code samples.

### Note
Many of Bandy's strategy templates are in AmiBroker AFL code in his books. Strategies are frequently parameter studies (e.g., RSI-based, Bollinger-based) rather than discrete named systems.

---

## 3. Cesar Alvarez

### Public assets
- **[free]** alvarezquanttrading.com — comprehensive blog archive (2012–present). Each post typically contains rules + backtest results.
- **[book]** Co-author with Connors on *Short Term Trading Strategies That Work* (2008) and *High Probability ETF Trading* (2009).

### Strategies
Many discrete strategies, e.g.: simple-RSI variations, ConnorsRSI long/short, country-ETF rotation, sector rotation, mean reversion in S&P 500, monthly rotation, high-RSI continuation, volatility regime switch.

---

## 4. Linda Raschke

### Books
- **[book]** *Street Smarts* (with Connors, 1995).
- **[book]** *Trading Sardines* (2018, memoir; selective methodology).

### Public assets
- **[free]** LBR Group educational pages and YouTube interviews.

### Strategies known to be in scope
"Holy Grail" (ADX + EMA pullback), "Anti" pattern, "Turtle Soup" (failed Donchian), "80-20s", "3-10 Oscillator" trades. Many overlap with *Street Smarts*.

---

## 5. Andreas Clenow

### Books
- **[book]** *Following the Trend: Diversified Managed Futures Trading* (2012). Wiley.
- **[book]** *Stocks on the Move: Beating the Market with Hedge Fund Momentum Strategies* (2015).
- **[book]** *Trading Evolved: Anyone Can Build Killer Trading Systems in Python* (2019).

### Public assets
- **[free]** followingthetrend.com — articles and excerpts.
- **[free]** GitHub: pytrendfollow (community implementations).

### Strategies known to be in scope
Diversified CTA core breakout (50–100 day), Stocks on the Move momentum (top-N by exponential-regression slope, weekly rebalance, ATR-targeted sizing, regime-filtered), various variations in *Trading Evolved* (e.g., asset class rotation, equity momentum with regime filter).

---

## 6. Robert Carver

### Books
- **[book]** *Systematic Trading* (2015). Harriman House.
- **[book]** *Smart Portfolios* (2017).
- **[book]** *Leveraged Trading* (2019).
- **[book]** *Advanced Futures Trading Strategies* (2023). Harriman House — explicitly catalogues 30 trading rules.

### Public assets
- **[free]** qoppac.blogspot.com — extensive blog with rule definitions.
- **[free]** GitHub: `pysystemtrade` — open-source Python implementation of his systems.

### Strategies known to be in scope
EWMAC trend filters at multiple speeds (2/8, 4/16, 8/32, 16/64, 32/128, 64/256), carry, normalised momentum, breakout, mean reversion, skew, value, asset-class allocation, volatility-targeted position sizing.

---

## 7. Perry Kaufman

### Books
- **[book]** *Trading Systems and Methods* (Wiley; many editions, latest 6th ed 2020). Encyclopedic; many strategies.
- **[book]** *Smarter Trading* (1995).

### Public assets
- **[free]** perrykaufman.com — articles.

### Note
Strategies are often parameter studies of well-known patterns (KAMA — Kaufman's Adaptive Moving Average — being the signature original).

---

## 8. Ernest Chan

### Books
- **[book]** *Quantitative Trading: How to Build Your Own Algorithmic Trading Business* (2008).
- **[book]** *Algorithmic Trading: Winning Strategies and Their Rationale* (2013).
- **[book]** *Machine Trading* (2017).

### Public assets
- **[free]** epchan.blogspot.com — blog with strategy-level posts.
- **[free]** SSRN papers under "Ernest P. Chan" / QTS Capital research notes.

### Strategies known to be in scope
Pairs trading via cointegration (Engle-Granger, Johansen), Bollinger-based mean reversion, momentum factor with portfolio overlay, variance ratio test for regime detection, intraday momentum on stocks, futures calendar spreads, ETF pair trades.

---

## 9. Marcos López de Prado

### Books
- **[book]** *Advances in Financial Machine Learning* (2018).
- **[book]** *Machine Learning for Asset Managers* (2020).

### Public assets
- **[free]** SSRN papers (extensive — fractional differentiation, triple-barrier method, meta-labeling, CSCV, HRP).

### Note
Most contributions are *meta-methods* (labeling, sample weighting, risk parity construction, backtest evaluation) rather than entry-exit strategies. Document those that are testable as portfolio rules (e.g., HRP weighting, meta-labeling on a base strategy).

---

## 10. Wesley Gray / Alpha Architect

### Books
- **[book]** *Quantitative Value* (2012, with Tobias Carlisle).
- **[book]** *Quantitative Momentum* (2016, with Jack Vogel).
- **[book]** *DIY Financial Advisor* (2015).

### Public assets
- **[free]** alphaarchitect.com — research blog with full rule disclosures, ETF white papers.

### Strategies known to be in scope
Quantitative Value (multi-factor screen + quality + Magic-Formula-style ranking), Quantitative Momentum (12-2 momentum + frog-in-the-pan smoothness), absolute + relative momentum tactical asset allocation, sector momentum.

---

## 11. Euan Sinclair

### Books
- **[book]** *Volatility Trading* (2008, 2nd ed 2013).
- **[book]** *Option Trading: Pricing and Volatility Strategies and Techniques* (2010).
- **[book]** *Positional Option Trading: An Advanced Guide* (2020).

### Public assets
- **[free]** Sporadic interviews and conference talks (Quantopian/Trading Tech Summit recordings).

### Strategies known to be in scope
Volatility risk-premium harvesting (variance swap proxies via short straddles/strangles), delta-hedged short volatility, calendar spreads, tail-hedged short premium, IV–RV gap trade.

---

## 12. tastytrade research

### Public assets
- **[free]** research.tastytrade.com — large archive of segments and white papers; rules and stats are explicit.

### Strategies known to be in scope
Short strangle 45-DTE, short straddle 45-DTE, short put 45-DTE, iron condor, IV-rank gating (IVR>30), 21-DTE management rule, 50% profit-take rule, defined-risk variants, Beta-weighted-delta neutral approach.

---

## 13. Kris Longmore (Robot Wealth)

### Public assets
- **[free]** robotwealth.com — extensive bootcamp posts, "Algorithmic Trading Bootcamp" rules archive.
- **[free]** Robot Wealth GitHub.

### Strategies known to be in scope
Crypto market-making, momentum portfolio, mean-reversion bootcamp builds, crypto-stat-arb pairs, FX carry.

---

## 14. Ernie Chan / PredictNow / QTS

(Same author as #8; some overlap.) Additional research notes from PredictNow.ai and QTS Capital's published reports — typically gated marketing copy, but a few public papers exist.

---

## Coverage Summary

| Author | Free coverage potential | Book-only coverage | Strategy estimate |
|--------|------------------------|-------------------|-------------------|
| Connors | Medium-High (many strategies extensively reproduced in third-party blogs) | Some | 20–35 |
| Bandy | Low | Most | 10–20 (book-only) |
| Alvarez | Very High | N/A | 30–50 |
| Raschke | Medium | Some | 5–10 |
| Clenow | High (well-documented online) | Yes | 10–20 |
| Carver | Very High (qoppac + pysystemtrade) | Yes | 25–40 |
| Kaufman | Low | Most | 15–25 (book-only) |
| Chan | High | Yes | 15–25 |
| López de Prado | Very High (SSRN) | N/A | 5–15 (testable rules) |
| Gray | Very High (alphaarchitect) | Yes | 10–20 |
| Sinclair | Low | Most | 5–15 (book-only) |
| tastytrade | Very High | N/A | 10–20 |
| Longmore | Very High | N/A | 10–20 |
| **Total** | | | **~170–300** |

Aligned with the spec's estimate of 150–300 strategies. The free-source surface area covers an estimated 60–70% of total volume; book-only items will be flagged in `open_questions.md` for follow-up with the user when book access is available.

---

*Last updated: 2026-05-04*
