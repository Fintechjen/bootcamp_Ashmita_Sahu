from __future__ import annotations
import pandas as pd

def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Return summary stats for numeric columns (and include count for all)."""
    # describe(include='all') mixes types; keep simple & predictable
    numeric_summary = df.describe(include='number').T
    counts = df.count().to_frame(name='non_null_count')
    out = numeric_summary.join(counts, how='outer')
    return out
