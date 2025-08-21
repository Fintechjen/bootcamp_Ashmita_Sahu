from __future__ import annotations
import numpy as np
import pandas as pd

def sharpe_ratio(daily_rets: pd.Series, periods_per_year: int = 252) -> float:
    mu = daily_rets.mean()
    sigma = daily_rets.std(ddof=0)
    if sigma == 0 or np.isnan(sigma):
        return 0.0
    return (mu / sigma) * np.sqrt(periods_per_year)

def max_drawdown(equity_curve: pd.Series) -> float:
    running_max = equity_curve.cummax()
    dd = equity_curve / running_max - 1.0
    return dd.min()

def hit_rate(signal: pd.Series, fwd_rets: pd.Series) -> float:
    pnl = signal * fwd_rets
    wins = (pnl > 0).sum()
    total = pnl.notna().sum()
    return float(wins) / float(total) if total else 0.0

def backtest_directional(signals: pd.Series, fwd_rets: pd.Series) -> dict:
    # signals in {-1, +1}; fwd_rets aligned to same index
    strat_rets = signals * fwd_rets.fillna(0.0)
    equity = (1 + strat_rets).cumprod()
    return {
        "sharpe": sharpe_ratio(strat_rets),
        "max_drawdown": max_drawdown(equity),
        "hit_rate": hit_rate(signals, fwd_rets),
        "total_return": equity.iloc[-1] - 1.0 if len(equity) else 0.0
    }
