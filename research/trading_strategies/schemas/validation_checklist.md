# Per-Strategy Validation Checklist

Every strategy YAML must pass every check below before it is marked complete in `master_index.csv`. If any check fails, the spec is incomplete — patch the YAML or move the gap to `open_questions.md`.

## Determinism

- [ ] Every entry condition can be expressed as a single boolean pandas expression on a price/volume DataFrame.
- [ ] Every exit condition can be expressed as a single boolean expression.
- [ ] No subjective language ("strong trend", "obvious breakout") remains.

## Parameters

- [ ] All numeric parameters have specific values (no "approximately", no "around").
- [ ] All lookback periods specified as integers.
- [ ] All thresholds (RSI cutoffs, % moves, ATR multiples) specified numerically.

## Indicator Specification

- [ ] Indicator name listed.
- [ ] Lookback period stated.
- [ ] Smoothing/computation formula stated (Wilder vs simple, EMA vs SMA).
- [ ] Input series stated (close, adjusted_close, high, low, typical price).

## Universe & Data

- [ ] Universe selection rule deterministic (no "best stocks").
- [ ] Liquidity filter quantified.
- [ ] Required data fields listed.
- [ ] Minimum history (warmup) stated.

## Entry / Exit Mechanics

- [ ] Entry price defined (close of signal bar, next open, limit at X, etc.).
- [ ] Entry time defined (intraday vs end-of-day).
- [ ] Exit price defined.
- [ ] Exit priority defined when multiple exit rules can fire.

## Position Sizing

- [ ] Sizing method named.
- [ ] All parameters required by that method are populated.
- [ ] Max concurrent positions stated.

## Look-Ahead & Survivorship

- [ ] No use of future information in any indicator.
- [ ] Survivorship-bias risk noted if universe selection is sensitive.
- [ ] Common look-ahead pitfalls flagged (e.g., "uses today's close to enter today's close — must trade next bar open in live").

## Source Attribution

- [ ] Source type, title, location filled in.
- [ ] Publication year filled in.
- [ ] No verbatim quotes longer than 14 words from copyrighted material.

## Backtestability

- [ ] **Acid test**: A programmer with no domain knowledge could write a working backtest from this YAML alone.
- [ ] If the spec required clarification to backtest, the spec failed and is not complete.
