from __future__ import annotations
import os
from pathlib import Path
from dotenv import load_dotenv

_ENV_LOADED = False

def load_env(env_file: str = ".env") -> None:
    """Load environment variables once from .env."""
    global _ENV_LOADED
    if not _ENV_LOADED:
        # Do not override existing environment by default
        load_dotenv(env_file, override=False)
        _ENV_LOADED = True

def get_key(name: str, default: str | None = None, required: bool = False) -> str | None:
    """Get an environment variable with optional default/required behavior."""
    load_env()
    val = os.getenv(name, default)
    if required and (val is None or val == ""):
        raise KeyError(f"Missing required env var: {name}")
    return val

def get_data_dir() -> Path:
    """Return the data directory (ensures it exists)."""
    load_env()
    path = Path(get_key("DATA_DIR", "./data"))
    path.mkdir(parents=True, exist_ok=True)
    return path
