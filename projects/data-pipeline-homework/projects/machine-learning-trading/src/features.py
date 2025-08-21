from __future__ import annotations
import numpy as np
import pandas as pd

def rsi(series: pd.Series, window: int = 14) -> pd.Series:
    delta = series.diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    roll_up = up.ewm(alpha=1/window, adjust=False).mean()
    roll_down = down.ewm(alpha=1/window, adjust=False).mean()
    rs = roll_up / roll_down.replace(0, np.nan)
    return 100 - (100 / (1 + rs))

def make_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    price = out["Close"].astype(float)
    out["ret_1"] = price.pct_change()
    out["logret_1"] = np.log(price).diff()
    out["sma_5"] = price.rolling(5).mean()
    out["sma_20"] = price.rolling(20).mean()
    out["vol_10"] = price.pct_change().rolling(10).std()
    out["rsi_14"] = rsi(price, 14)
    out["mom_10"] = price.pct_change(10)
    # Target: next-day direction (classification)
    out["ret_fwd_1"] = price.pct_change().shift(-1)
    out["y_up"] = (out["ret_fwd_1"] > 0).astype(int)
    out = out.dropna().reset_index(drop=True)
    return out
