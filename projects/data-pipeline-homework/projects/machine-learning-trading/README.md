# Machine Learning Trading Project — Problem Framing & Scoping

## Problem Statement
This project explores the application of machine learning techniques to financial market data. The goal is to simulate a structured workflow where we use historical market data to predict short-term returns. This matters because understanding how features and models behave on real financial data helps develop skills in quantitative research and data-driven decision-making.

## Stakeholder & User
- **Primary stakeholder**: Myself (student learning quantitative research workflows).
- **End users**: Instructor/TAs for evaluation; future self for reference.
- The workflow mimics a research team analyzing data, building models, and evaluating strategies.

## Useful Answer & Decision
This project is predictive in nature. Useful outputs include:
- Clean datasets ready for modeling
- Feature library
- ML models predicting short-term returns
- Backtest results with metrics like Sharpe ratio, drawdown, and hit-rate

## Assumptions & Constraints
- Data will be collected using `yfinance` (limited intraday granularity)
- Only Python-based offline modeling
- No live trading or real money involved
- Time and computational resources are limited

## Known Unknowns / Risks
- Model performance may vary with different periods or assets
- Features may not generalize across market regimes
- Risk of data leakage or overfitting

## Lifecycle Mapping

| Goal | Stage | Deliverable |
|---|---|---|
| Understand problem & scope | Problem Framing & Scoping | README.md, Stakeholder Memo |
| Collect and clean data | Data Collection | Scripts / datasets in `/data/` |
| Explore and visualize data | Exploratory Analysis | Notebooks in `/notebooks/` |
| Build features & models | Feature Engineering & Modeling | Python scripts in `/src/` |
| Backtest & evaluate | Evaluation | Metrics, charts, summary reports in `/docs/` |

## Repo Plan
- `/data/` – store raw and processed datasets
- `/src/` – code for data processing, features, models, backtesting
- `/notebooks/` – experiments, EDA, scoping notes
- `/docs/` – stakeholder memo, reports
- `/README.md` – this file
- `/requirements.txt` – Python libraries
- `.gitignore` – ignore unnecessary files
- `LICENSE` – MIT License

---

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Example: fetch data and run a basic pipeline
python src/run_pipeline.py --ticker AAPL --period 1y --interval 1d
```

> This repo is for **educational use only** and **NOT investment advice**.
