from __future__ import annotations
from typing import Literal, Optional
import pandas as pd
import yfinance as yf

def fetch_ohlc(
    ticker: str,
    period: str = "5y",
    interval: str = "1d",
    auto_reset_index: bool = True,
) -> pd.DataFrame:
    """Fetch OHLCV via yfinance and standardize column names."""
    df = yf.download(ticker, period=period, interval=interval, progress=False)
    if auto_reset_index:
        df = df.reset_index()
    # Ensure expected columns
    cols = ["Date","Open","High","Low","Close","Adj Close","Volume"]
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")
    return df
