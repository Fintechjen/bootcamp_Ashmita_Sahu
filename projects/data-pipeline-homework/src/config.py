from __future__ import annotations

import os
from pathlib import Path
from dotenv import load_dotenv

_ENV_LOADED = False

def load_env(dotenv_path: str | None = None) -> None:
    """Load environment variables from a .env file (once)."""
    global _ENV_LOADED
    if not _ENV_LOADED:
        load_dotenv(dotenv_path=dotenv_path, override=False)
        _ENV_LOADED = True

def get_key(name: str, default: str | None = None, required: bool = False) -> str | None:
    """Read a single env variable by name, optionally enforcing presence."""
    load_env()
    value = os.getenv(name, default)
    if required and (value is None or value == ""):
        raise RuntimeError(f"Required environment variable '{name}' is missing.")
    return value

def get_data_dir_raw() -> Path:
    load_env()
    return Path(os.getenv("DATA_DIR_RAW", "data/raw")).resolve()

def get_data_dir_processed() -> Path:
    load_env()
    return Path(os.getenv("DATA_DIR_PROCESSED", "data/processed")).resolve()
