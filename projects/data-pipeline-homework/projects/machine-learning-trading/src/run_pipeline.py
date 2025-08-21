from __future__ import annotations
import argparse
import numpy as np
import pandas as pd

from data import fetch_ohlc
from features import make_features
from model import split_walk_forward, train_classifier, predict_labels
from evaluate import backtest_directional

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ticker", type=str, default="AAPL")
    ap.add_argument("--period", type=str, default="3y")
    ap.add_argument("--interval", type=str, default="1d")
    args = ap.parse_args()

    raw = fetch_ohlc(args.ticker, period=args.period, interval=args.interval)
    feat = make_features(raw)

    train, test = split_walk_forward(feat, train_frac=0.7)
    clf = train_classifier(train)

    # Predict labels on test; map {0,1} -> {-1,+1} for long/short
    yhat = predict_labels(clf, test)
    signals = pd.Series(np.where(yhat > 0, 1.0, -1.0), index=test.index, name="signal")
    metrics = backtest_directional(signals, test["ret_fwd_1"])

    print(f"Ticker: {args.ticker}  Period: {args.period}  Interval: {args.interval}")
    for k,v in metrics.items():
        print(f"{k}: {v:.4f}")

if __name__ == "__main__":
    main()
