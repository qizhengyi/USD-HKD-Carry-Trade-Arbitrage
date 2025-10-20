"""
backtest.py - Backtesting logic and visualization.
"""

import pandas as pd
import matplotlib.pyplot as plt

def run_backtest(df: pd.DataFrame) -> pd.DataFrame:
    # Simplified PnL: differential * signal
    df["PnL"] = df["USD_minus_HKD_ON_diff_pp"] * df["Signal"]
    df["Cumulative_Return"] = (1 + df["PnL"] / 100).cumprod() - 1
    return df

def plot_results(df: pd.DataFrame):
    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["Cumulative_Return"], label="Cumulative Return")
    plt.title("USD-HKD Carry Trade Equity Curve")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend()
    plt.grid(True)
    plt.show()
