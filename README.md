# Finance A/B Test with Linear Regression

This project evaluates whether a redesigned financial education module causes an increase in users’ savings behavior compared to the current module. We will run an A/B test (control vs treatment) and estimate the treatment effect with linear regression while controlling for baseline activity and demographics. The primary stakeholder is the product team improving engagement and retention; end users are app customers who benefit from clearer guidance and nudges. The main outputs are a causal effect estimate (with CIs), simple predictive checks, and an implementation decision recommendation.
## 📦 Data Storage

### Folder Layout
- `data/raw/`  
  Holds raw ingested files (CSV, timestamped). Created automatically by the notebooks/utilities.  
  Example: `data/raw/sample_20250828-123456.csv`

- `data/processed/`  
  Holds cleaned/curated data in efficient formats for downstream tasks.  
  - **CSV**: plain text for portability.  
  - **Parquet**: columnar storage (requires `pyarrow` or `fastparquet`).  
  - **SQLite** (optional): structured SQL database for queries.  
  Example:  
  - `data/processed/sample_20250828-123456.parquet`  
  - `data/processed/sample.sqlite`

### Environment Variables
- `.env` file at project root, **never committed** to version control.  
  Example entries:
  ```ini
  ALPHAVANTAGE_API_KEY=your_key_here
  TICKER=AAPL
  DATA_DIR=./data

