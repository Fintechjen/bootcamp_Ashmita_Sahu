# Stakeholder Memo

## Audience
- Primary stakeholder: student author
- Reviewers: Instructor / TAs
- Future self referencing reusable workflow

## Objective
Predict short-term returns for a given ticker, evaluate if the signal has any edge under a simple backtest (no costs, long-only/long-short variations).

## Scope (MVP)
- Fetch OHLCV data via `yfinance`
- Engineer a small set of time-series features (returns, rolling stats, RSI)
- Train a simple classifier to predict the **direction** of next-day return
- Backtest signals on a holdout set and report: Sharpe, max drawdown, hit-rate

## Out of Scope
- Live trading
- Execution costs and slippage modelling
- Portfolio construction across many assets
- Complex risk management

## Risks & Mitigations
- **Leakage**: Align targets as *future* returns; use walk-forward split.
- **Overfitting**: Keep feature set small; use cross-validation on train.
- **Regime shifts**: Evaluate over multiple time windows; document instability.
- **Data quality**: Validate NAs, dupes, timezone alignment.

## Deliverables
- `notebooks/00_scope_and_plan.ipynb`
- `src/data.py`, `src/features.py`, `src/model.py`, `src/evaluate.py`, `src/run_pipeline.py`
- `docs/metrics_example.md` after first run
