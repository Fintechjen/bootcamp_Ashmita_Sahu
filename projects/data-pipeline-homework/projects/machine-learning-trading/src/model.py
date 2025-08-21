from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

FEATURE_COLS = ["ret_1","logret_1","sma_5","sma_20","vol_10","rsi_14","mom_10"]

def split_walk_forward(df: pd.DataFrame, train_frac: float = 0.7):
    n = len(df)
    n_train = int(n * train_frac)
    train = df.iloc[:n_train].copy()
    test = df.iloc[n_train:].copy()
    return train, test

def train_classifier(train: pd.DataFrame):
    X = train[FEATURE_COLS].values
    y = train["y_up"].values
    clf = Pipeline([
        ("scaler", StandardScaler()),
        ("lr", LogisticRegression(max_iter=1000))
    ])
    clf.fit(X, y)
    return clf

def predict_proba(clf, df: pd.DataFrame) -> np.ndarray:
    X = df[FEATURE_COLS].values
    return clf.predict_proba(X)[:,1]

def predict_labels(clf, df: pd.DataFrame) -> np.ndarray:
    X = df[FEATURE_COLS].values
    return clf.predict(X)
