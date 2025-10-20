"""
main.py - Entry point for the USD-HKD Carry Trade Arbitrage project.

This script orchestrates the entire pipeline:
1. Load data from FRED & HKMA APIs or local CSV files
2. Compute interest rate differentials
3. Generate trading signals based on rolling mean and thresholds
4. Run backtest simulation and calculate cumulative returns
5. Save results and visualize performance
"""

import argparse
import pandas as pd
from src.data_loader import load_data
from src.strategy import compute_signals
from src.backtest import run_backtest, plot_results


def main(args):
    # 1️⃣ Load data
    if args.local_sofr_csv and args.local_hibor_csv:
        print("📊 Loading local CSV data...")
        df = pd.read_csv(args.local_sofr_csv, parse_dates=["Date"])
        hibor = pd.read_csv(args.local_hibor_csv, parse_dates=["Date"])
    else:
        print("🌐 Fetching data from APIs (FRED & HKMA)...")
        df, hibor = load_data(start=args.start, end=args.end)

    # Merge data
    data = pd.merge(df, hibor, on="Date", how="inner")

    # 2️⃣ Compute interest rate differential and rolling mean
    print("⚙️ Calculating differential and rolling mean...")
    data = compute_signals(
        data,
        rolling=args.rolling,
        fx_threshold_pp=args.fx_threshold_pp
    )

    # 3️⃣ Run backtest
    print("📈 Running backtest simulation...")
    results = run_backtest(data)

    # 4️⃣ Save output CSV
    if args.output_csv:
        results.to_csv(args.output_csv, index=False)
        print(f"✅ Results saved to: {args.output_csv}")

    # 5️⃣ Plot results
    print("📊 Generating charts...")
    plot_results(results)
    print("🚀 Strategy execution completed!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="USD-HKD Carry Trade Arbitrage Strategy")

    # CLI arguments
    parser.add_argument("--start", type=str, default="2015-01-01", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, default="2025-10-01", help="End date (YYYY-MM-DD)")
    parser.add_argument("--rolling", type=int, default=30, help="Rolling window size in days")
    parser.add_argument("--fx_threshold_pp", type=float, default=0.0, help="FX differential threshold (pp)")
    parser.add_argument("--output_csv", type=str, default="usd_minus_hkd_on_rolling.csv", help="Output CSV file path")
    parser.add_argument("--local_sofr_csv", type=str, help="Path to local SOFR CSV file")
    parser.add_argument("--local_hibor_csv", type=str, help="Path to local HIBOR CSV file")

    args = parser.parse_args()
    main(args)
