"""
strategy.py - Compute interest rate differentials and trading signals.
"""

import pandas as pd

def compute_signals(df: pd.DataFrame, rolling: int = 30, fx_threshold_pp: float = 0.0):
    df["USD_minus_HKD_ON_diff_pp"] = df["SOFR_percent"] - df["HIBOR_ON_percent"]
    df["Rolling_Mean_Diff_pp"] = df["USD_minus_HKD_ON_diff_pp"].rolling(rolling).mean()

    # Generate trading signals (1 = enter carry trade, 0 = no trade)
    df["Signal"] = (df["Rolling_Mean_Diff_pp"] > fx_threshold_pp).astype(int)
    return df
