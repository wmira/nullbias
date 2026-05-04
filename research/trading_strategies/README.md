# Trading Strategy Extraction Project

Comprehensive deep-dive: extract, document, and standardize every published trading strategy from a defined list of practitioner-authors. Output is detailed enough that a downstream LLM can implement each strategy as executable backtest code (Python / vectorbt / backtrader / zipline) without ambiguity.

Spec source: `trading_strategy_extraction_spec.md` (uploaded by user).

## Directory Layout

```
trading_strategies/
├── README.md                       # This file
├── master_index.csv                # All strategies, one row each
├── master_index.json               # Same data, JSON form
├── open_questions.md               # Unresolved ambiguities / gaps
├── schemas/
│   ├── strategy_template.yaml      # Canonical schema per spec
│   └── validation_checklist.md     # Per-strategy QA criteria
├── strategies/
│   ├── connors/                    # Larry Connors strategies
│   ├── bandy/                      # Howard Bandy
│   ├── alvarez/                    # Cesar Alvarez
│   ├── raschke/                    # Linda Raschke
│   ├── clenow/                     # Andreas Clenow
│   ├── carver/                     # Robert Carver
│   ├── kaufman/                    # Perry Kaufman
│   ├── chan/                       # Ernest Chan
│   ├── lopez_de_prado/             # Marcos López de Prado
│   ├── gray/                       # Wesley Gray / Alpha Architect
│   ├── sinclair/                   # Euan Sinclair
│   ├── tastytrade/                 # tastytrade research
│   └── longmore/                   # Kris Longmore / Robot Wealth
└── reports/
    ├── source_inventory.md         # Phase 1: bibliographies
    ├── <author>_coverage.md        # Per-author coverage report
    ├── cross_reference_matrix.md   # Strategies grouped by category
    └── implementation_priority.md  # Ranking by completeness/perf/data
```

## Naming Convention

`strategy_id`: `<author_lastname>_<short_name>_<version>` — e.g., `connors_rsi2_v1`, `carver_ewmac_16_64`, `clenow_stocks_on_the_move_v1`.

Filename: `<strategy_id>.yaml`.

## Quality Bar

A downstream LLM should be able to write a working Python backtest from any single strategy file *without asking clarifying questions*. If clarification is needed, the spec is incomplete — log it in `open_questions.md` and patch the YAML.

## Status

| Phase | Description | Status |
|-------|-------------|--------|
| 0 | Scaffolding & schema | In progress |
| 1 | Source inventory (all authors) | Pending |
| 2 | Strategy extraction — per author | Pending (Connors first) |
| 3 | Standardization to schema | Concurrent with 2 |
| 4 | Validation pass | Pending |
| 5 | Cross-reference & priority list | Pending |

## Copyright Note

This project documents *strategies and methodologies* in original wording, citing original sources. No verbatim text from copyrighted books is reproduced. Where book-only details are unclear, items are flagged in `open_questions.md` rather than guessed.
