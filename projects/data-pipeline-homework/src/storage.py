from __future__ import annotations

import os
from pathlib import Path
import pandas as pd

from .config import get_data_dir_raw, get_data_dir_processed

def _ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

def write_df(df: pd.DataFrame, path: str | os.PathLike) -> Path:
    """Write a DataFrame to CSV or Parquet based on the file suffix.
    Ensures parent dirs exist. Returns absolute path to file.
    """
    path = Path(path)
    _ensure_parent(path)
    suffix = path.suffix.lower()

    if suffix == ".csv":
        df.to_csv(path, index=False)
    elif suffix in {".parquet", ".pq"}:
        try:
            df.to_parquet(path, index=False)
        except Exception as e:
            raise RuntimeError(
                "Writing Parquet failed. Ensure 'pyarrow' is installed and supported."
            ) from e
    else:
        raise ValueError(f"Unsupported file extension: {suffix}")

    return path.resolve()

def read_df(path: str | os.PathLike) -> pd.DataFrame:
    """Read a DataFrame from CSV or Parquet based on file suffix."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    suffix = path.suffix.lower()

    if suffix == ".csv":
        return pd.read_csv(path)
    elif suffix in {".parquet", ".pq"}:
        try:
            return pd.read_parquet(path)
        except Exception as e:
            raise RuntimeError(
                "Reading Parquet failed. Ensure 'pyarrow' is installed and supported."
            ) from e
    else:
        raise ValueError(f"Unsupported file extension: {suffix}")

def build_path_raw(filename: str) -> Path:
    return get_data_dir_raw() / filename

def build_path_processed(filename: str) -> Path:
    return get_data_dir_processed() / filename
