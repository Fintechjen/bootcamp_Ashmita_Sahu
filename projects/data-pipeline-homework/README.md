# Data Pipeline Homework (Stages 02–06)

A clean, reproducible Python project that walks through:
- **Tooling setup** (env, .env, Jupyter, git)
- **Python fundamentals** (NumPy, pandas basics)
- **Data acquisition & ingestion** (API + scraping)
- **Data storage** (CSV/Parquet with env-driven paths)
- **Data preprocessing** (missing values & normalization)

> This repo is scaffolded from the provided course homework sheets. See `docs/homework-sheets/`.

## Quickstart

```bash
# 1) Create & activate a virtual env (choose one)
python -m venv .venv && source .venv/bin/activate
# or: conda create -n fe-course python=3.11 -y && conda activate fe-course

# 2) Install deps
pip install -r requirements.txt

# 3) Configure env
cp .env.example .env
# (optional) Edit API_KEY, DATA_DIR_RAW, DATA_DIR_PROCESSED

# 4) Open notebooks
jupyter notebook notebooks/
```

## Project Layout

```
data/
  raw/         # unprocessed files
  processed/   # cleaned/validated files
docs/
  homework-sheets/  # PDFs from course
notebooks/
  00_project_setup.ipynb
  hw03_python_fundamentals.ipynb
  hw04_data_acquisition_ingestion.ipynb
  hw05_data_storage.ipynb
  hw06_data_preprocessing.ipynb
src/
  cleaning.py
  config.py
  storage.py
  utils.py
```

## Notes

- `.env` is **not** committed. Use `.env.example` for keys & data dirs.
- Parquet IO uses **pyarrow** by default.
- `src/cleaning.py` provides modular cleaning utilities you can reuse in notebooks.
- The notebooks fall back to generating a tiny sample dataset if no raw data is present, so you can run top-to-bottom out-of-the-box.
