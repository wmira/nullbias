#!/usr/bin/env python3
"""
Per-strategy validator. Confirms each strategy YAML has the required schema
fields populated and that no critical entry/exit/sizing field is empty.
Generates reports/validation_report.md.
"""
import sys, glob, os, yaml
from pathlib import Path

ROOT = Path(__file__).parent
STRATEGY_DIR = ROOT / "strategies"
REPORT_FILE = ROOT / "reports" / "validation_report.md"

REQUIRED_TOP = [
    "strategy_id", "name", "author", "source", "category", "asset_class",
    "timeframe", "direction", "universe_definition",
    "entry_signal", "position_sizing", "exit_rules", "backtest_specs",
]

REQUIRED_ENTRY = ["trigger_conditions", "indicators_used", "entry_price", "entry_time"]
REQUIRED_EXIT = ["profit_target", "stop_loss", "exit_price"]
REQUIRED_SIZING = ["method", "max_concurrent_positions"]
REQUIRED_BACKTEST = ["required_data_fields", "data_frequency", "minimum_history_required"]

def is_empty(v):
    if v is None: return True
    if isinstance(v, str) and v.strip() in ("", "TBD", "???", "TODO"): return True
    return False

def validate(path):
    with open(path, "r", encoding="utf-8") as f:
        try:
            doc = yaml.safe_load(f)
        except Exception as e:
            return [f"YAML PARSE ERROR: {e}"]
    if doc is None:
        return ["YAML EMPTY"]
    issues = []
    for k in REQUIRED_TOP:
        if k not in doc or is_empty(doc.get(k)):
            issues.append(f"missing top-level field: {k}")
    e = doc.get("entry_signal") or {}
    for k in REQUIRED_ENTRY:
        if k not in e or is_empty(e.get(k)):
            issues.append(f"entry_signal.{k} empty")
    inds = e.get("indicators_used") or []
    if not isinstance(inds, list) or len(inds) == 0:
        issues.append("entry_signal.indicators_used empty or not a list")
    else:
        for i, ind in enumerate(inds):
            for fld in ("name", "lookback_period", "formula_reference"):
                if fld not in ind or is_empty(ind.get(fld)):
                    issues.append(f"indicator[{i}].{fld} empty")
    x = doc.get("exit_rules") or {}
    for k in REQUIRED_EXIT:
        if k not in x:
            issues.append(f"exit_rules.{k} missing")
    s = doc.get("position_sizing") or {}
    for k in REQUIRED_SIZING:
        if k not in s or is_empty(s.get(k)):
            issues.append(f"position_sizing.{k} empty")
    b = doc.get("backtest_specs") or {}
    for k in REQUIRED_BACKTEST:
        if k not in b or is_empty(b.get(k)):
            issues.append(f"backtest_specs.{k} empty")
    if "ambiguities_and_assumptions" not in doc:
        issues.append("ambiguities_and_assumptions missing")
    return issues

def main():
    files = sorted(glob.glob(str(STRATEGY_DIR / "**" / "*.yaml"), recursive=True))
    files = [f for f in files if "template" not in f and "_template" not in f]
    rows = []
    pass_count = 0
    for f in files:
        rel = os.path.relpath(f, ROOT)
        issues = validate(f)
        status = "PASS" if not issues else "FAIL"
        if not issues:
            pass_count += 1
        rows.append((rel, status, issues))
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_FILE, "w", encoding="utf-8") as out:
        out.write("# Validation Report\n\n")
        out.write(f"Generated: {os.popen('date -u +%Y-%m-%dT%H:%M:%SZ').read().strip()}\n\n")
        out.write(f"Total strategies validated: {len(rows)}\n")
        out.write(f"PASS: {pass_count}\n")
        out.write(f"FAIL: {len(rows) - pass_count}\n\n")
        out.write("| File | Status | Issues |\n|------|--------|--------|\n")
        for rel, status, issues in rows:
            issue_str = "; ".join(issues) if issues else "—"
            out.write(f"| `{rel}` | {status} | {issue_str} |\n")
    print(f"Validated {len(rows)} files. PASS={pass_count} FAIL={len(rows)-pass_count}")
    print(f"Report: {REPORT_FILE}")
    return 0 if pass_count == len(rows) else 1

if __name__ == "__main__":
    sys.exit(main())
