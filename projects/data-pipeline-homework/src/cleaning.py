from __future__ import annotations

import pandas as pd
import numpy as np

def fill_missing_median(df: pd.DataFrame, cols: list[str] | None = None) -> pd.DataFrame:
    """Fill NaNs in numeric columns (or in `cols`) with column medians.
    Returns a new DataFrame (does not mutate input).
    """
    out = df.copy()
    if cols is None:
        cols = [c for c in out.columns if pd.api.types.is_numeric_dtype(out[c])]
    for c in cols:
        if c in out.columns and pd.api.types.is_numeric_dtype(out[c]):
            median = out[c].median()
            out[c] = out[c].fillna(median)
    return out

def drop_missing(df: pd.DataFrame, how: str = "any", subset: list[str] | None = None) -> pd.DataFrame:
    """Drop rows containing missing values.
    - how="any" drops a row if *any* value is NA (default).
    - how="all" drops a row if *all* values are NA.
    Optionally restrict to a `subset` of columns.
    Returns a new DataFrame.
    """
    return df.dropna(axis=0, how=how, subset=subset)

def normalize_data(df: pd.DataFrame, cols: list[str] | None = None) -> pd.DataFrame:
    """Standard-score normalize numeric columns: (x - mean) / std.
    Zero-variance columns are left as 0 (after mean-centering).
    Returns a new DataFrame.
    """
    out = df.copy()
    if cols is None:
        cols = [c for c in out.columns if pd.api.types.is_numeric_dtype(out[c])]
    for c in cols:
        if c in out.columns and pd.api.types.is_numeric_dtype(out[c]):
            mu = out[c].mean()
            sigma = out[c].std(ddof=0)
            if sigma and sigma != 0:
                out[c] = (out[c] - mu) / sigma
            else:
                out[c] = out[c] - mu
    return out
