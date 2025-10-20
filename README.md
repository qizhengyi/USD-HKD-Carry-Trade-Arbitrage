# USD-HKD Interest-Rate Differential Arbitrage

[![CI](https://github.com/qizhengyi/USD-HKD-Interest-Rate-Differential-Arbitrage/actions/workflows/python-ci.yml/badge.svg)](https://github.com/qizhengyi/USD-HKD-Interest-Rate-Differential-Arbitrage/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

This project implements a **carry trade backtesting framework** that analyzes the **interest rate differential between USD (SOFR)** and **HKD (HIBOR)** under Hong Kong’s linked exchange rate system.  
It automates **data acquisition**, **signal generation**, **threshold-based strategy simulation**, and **performance evaluation**, providing a full end-to-end workflow for carry trade research.

---

## 📊 Project Overview

In Hong Kong’s currency board system, the HKD is pegged to the USD (≈ 7.8 HKD/USD). However, when the **HKD interbank rate (HIBOR)** is significantly **lower** than the **USD overnight rate (SOFR)**, investors can exploit a carry trade opportunity:

1. **Borrow HKD** at a low cost  
2. **Convert to USD** under the fixed peg  
3. **Invest in USD-denominated assets** (e.g., T-bills) to capture the interest rate differential  

This repository provides a complete analytical framework to quantify and backtest this strategy.

---

## ✨ Features

- 📈 **Data Acquisition:**  
  - Fetch SOFR from [FRED](https://fred.stlouisfed.org/) and HIBOR from [HKMA](https://api.hkma.gov.hk)  
  - Support for local CSV input

- 🔍 **Signal Generation:**  
  - Compute daily interest differential and rolling mean  
  - Generate trading signals when the spread exceeds a threshold

- 🧠 **Backtesting Engine:**  
  - Simulate carry trade performance based on interest spreads  
  - Approximate PnL, cumulative equity, and risk metrics

- 📊 **Performance Analysis:**  
  - Annualized return, max drawdown, volatility, Sharpe ratio  
  - Auto-generated visualizations (interest rates, spreads, equity curve)

---

## 🛠️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/qizhengyi/USD-HKD-Interest-Rate-Differential-Arbitrage.git
cd USD-HKD-Interest-Rate-Differential-Arbitrage
pip install -e .[dev]
pre-commit install  # optional
``` 

---

## 🚀 Quick Start

### 1. Run with live data from FRED & HKMA:
```bash
usdhkd-arb --start 2015-01-01 --end 2025-10-01 \
  --rolling 30 --fx_threshold_pp 0.0 \
  --output_csv usd_minus_hkd_on_rolling.csv
```
### 2. Run with local CSV data:

If you already have local CSV files containing the SOFR and HIBOR data (for example, downloaded manually from FRED and HKMA), you can run the backtest using those files instead of fetching data online:

```bash
usdhkd-arb --local_sofr_csv ./data/sofr.csv \
  --local_hibor_csv ./data/hibor.csv --rolling 30
```
### 3. Output Files

After running the script (either with live data or local CSV data), the following output files and visualizations will be automatically generated:

- **`usd_minus_hkd_on_rolling.csv`** – A CSV file containing key time series data:
  - `Date`: Daily observation date  
  - `SOFR_percent`: USD overnight SOFR rate  
  - `HIBOR_ON_percent`: HKD overnight HIBOR fixing  
  - `USD_minus_HKD_ON_diff_pp`: Interest rate differential (in percentage points)  
  - `Rolling_Mean_Diff_pp`: Rolling mean of the differential (default: 30 days)

- **Auto-generated visualizations** (saved as `.png` or displayed inline):
  - 📈 **Interest Rate Plot:** SOFR vs HIBOR over time  
  - 📊 **Differential Plot:** Daily interest rate differential and rolling mean  
  - 💹 **Equity Curve:** Simulated cumulative returns from the carry trade strategy  

These outputs allow you to analyze interest rate spreads, verify signal generation, and evaluate historical performance of the USD-HKD carry trade strategy.
## 📊 Strategy Workflow

The backtesting engine follows a simple but robust **5-step pipeline**, transforming raw interest rate data into actionable trading signals and a simulated carry trade performance:

### 1. Data Loading
- Retrieve USD SOFR and HKD HIBOR time series data from FRED and HKMA APIs.  
- Alternatively, load the same data from local CSV files if already downloaded.

### 2. Signal Calculation
- Compute the **daily interest rate differential** as:  

\[
\text{diff} = \text{SOFR} - \text{HIBOR}
\]

- This differential represents the potential carry trade spread between USD and HKD.

### 3. Signal Smoothing
- Apply a **rolling mean** (default: 30 days) to smooth noise and highlight persistent opportunities.  
- The rolling mean differential is the primary signal used for trade entry decisions.

### 4. Signal-Based Trading Logic
- Enter a USD/HKD carry trade when the smoothed differential exceeds a predefined threshold (`rolling_mean_diff > fx_threshold_pp`).  
- This models borrowing HKD at a lower interest rate, converting to USD, and investing in higher-yielding USD instruments.

### 5. PnL Simulation
- Simulate daily **PnL (profit and loss)** based on the differential and position exposure.  
- Compound the returns over time to produce a **cumulative equity curve**, visualizing historical strategy performance.

---

📈 This pipeline mirrors a real-world macro carry trade strategy and demonstrates how interest rate differentials can be systematically transformed into tradeable signals and evaluated through historical backtesting.
