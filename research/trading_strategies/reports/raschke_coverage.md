# Raschke Coverage Report

Author: **Linda Bradford Raschke**
Pass complete: 2026-05-04
Strategies extracted this pass: **8**

---

## Sources Reviewed

| Source | Type | Year | Strategies extracted |
|--------|------|------|---------------------|
| *Street Smarts: High Probability Short-Term Trading Strategies* (with Larry Connors) | Book | 1995 | 6 strategies (Holy Grail, Anti, Turtle Soup long/short, 80-20, ID/NR4, NR7) |
| LBR Group educational pages and 'Terminology & Setups' FAQ on lindaraschke.net | Web | various | Cross-referenced for canonical parameters |
| 3-10 Oscillator (LBR's signature; used since 1981) | Web | 1981 | raschke_3_10_oscillator_v1 |
| Trading Sardines memoir | Book | 2018 | Cross-referenced; not strategy-source (autobiographical) |

## Sources Not Yet Reviewed

| Topic | Reason |
|-------|--------|
| Specific intraday LBR Group setups for ES futures | Mentioned in LBR Group videos; insufficient public detail to encode mechanically |
| Pattern variants like "1-2-3 Pivot" / "Whipsnake" | Sometimes attributed to Cooper rather than Raschke; defer |
| LBR's pattern recognition courses (subscription-only) | Beyond free-source scope |
| Market-internals analysis (TICK, TRIN-based setups) | Mentioned in interviews but rules not fully published |

---

## Strategies Extracted

| ID | Name | Source | Direction | Score |
|----|------|--------|-----------|-------|
| raschke_holy_grail_v1 | Holy Grail ADX/EMA20 | Street Smarts 1995 | long_short | 4/5 |
| raschke_anti_v1 | Anti Stochastic Pullback | Street Smarts 1995 | long_short | 4/5 |
| raschke_turtle_soup_long_v1 | Turtle Soup (Long) | Street Smarts 1995 | long_only | 5/5 |
| raschke_turtle_soup_short_v1 | Turtle Soup (Short) | Street Smarts 1995 | short_only | 5/5 |
| raschke_80_20_v1 | 80-20 Range Reversal | Street Smarts 1995 | long_short | 4/5 |
| raschke_3_10_oscillator_v1 | 3-10 First Cross | LBR Group | long_short | 4/5 |
| raschke_id_nr4_v1 | ID/NR4 Breakout | Street Smarts 1995 | long_short | 5/5 |
| raschke_nr7_v1 | NR7 Narrow-Range Breakout | Street Smarts 1995 | long_short | 5/5 |

**Mean completeness score: 4.5 / 5**

The lower-scored entries (4/5) reflect Raschke's hybrid systematic-discretionary style — some setups (Holy Grail's "first pullback", Anti's "impulse" definition) include qualitative components that require an explicit mechanical proxy. Each YAML's `ambiguities_and_assumptions` block documents the chosen proxy.

---

## Cross-Reference

Raschke's pass adds **pattern-recognition primitives** that were thin in the index:

- **Volatility-contraction breakouts** (NR4/NR7/ID-NR4) — first family of inside-day / narrow-range setups in the index. Conceptually similar to Carver's breakout rule but using bar-pattern triggers rather than channel breakouts.
- **Failed-breakout fade** (Turtle Soup) — distinct mean-reversion sub-template that targets stop clusters above/below recent extremes. Different mechanic from the count-based or RSI-based mean reversions already in the index.
- **Day-after extreme reversal** (80-20) — first explicit price-action reversal pattern.
- **3-10 Oscillator** — first SMA-based momentum indicator in the index (vs MACD's EMA construction).

---

## Open Questions Generated

1. **'First pullback' definition** — Holy Grail and Anti both rely on identifying the FIRST pullback after trend confirmation. Mechanical proxy documented per YAML.
2. **'Impulse' definition** for Anti pattern — encoded as "single-bar move > 1.5 × ATR(20)" or "3 consecutive bars same direction".
3. **Turtle Soup edge erosion** — Trend-following systems that the Turtle Soup fades have evolved; original edge has likely diminished post-2010.
4. **Bracket-order execution** — ID/NR4 and NR7 require buy-stop + sell-stop bracket orders; backtest must simulate intraday tick-precision fills.
5. **Tick buffers in Turtle Soup** — '5-10 ticks' translates to 0.05-0.1% on most instruments; document conversion.
6. **Stochastic variant 7,10,4** — Raschke's specific settings; standard 14,3 stochastic does NOT trigger the same patterns.

---

## Recommendations

1. **Pattern-trading family is now well-covered**. Combined with Connors' RSI patterns, Alvarez's variants, and Chan's regime filters, the daily-bar pattern space is fairly complete.
2. **Remaining authors**:
   - **Howard Bandy** — book-only AmiBroker AFL systems
   - **Perry Kaufman** — encyclopedic textbook; KAMA family
   - **López de Prado** — meta-methods (HRP, meta-labeling)
   - **Sinclair** — book-only options/volatility (gap remains)
   - **Longmore (Robot Wealth)** — crypto + FX + bootcamp content
3. Most-impactful remaining pick is probably **López de Prado** — adds portfolio-construction methods (HRP, meta-labeling) that are structurally orthogonal to everything currently in the index.
