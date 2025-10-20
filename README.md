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

```bash
git clone https://github.com/qizhengyi/USD-HKD-Interest-Rate-Differential-Arbitrage.git
cd USD-HKD-Interest-Rate-Differential-Arbitrage
pip install -e .[dev]
pre-commit install  # optional
🚀 Quick Start
1. Run with live data from FRED & HKMA:

1. Run with live data from FRED & HKMA:

### 1. Run with live data from FRED & HKMA:
```bash
usdhkd-arb --start 2015-01-01 --end 2025-10-01 \
  --rolling 30 --fx_threshold_pp 0.0 \
  --output_csv usd_minus_hkd_on_rolling.csv
pip install -e .[dev]
pre-commit install  # optional
2. Run with local CSV data
