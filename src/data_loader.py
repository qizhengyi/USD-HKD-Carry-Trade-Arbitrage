"""
data_loader.py - Fetch or load SOFR & HIBOR data.
"""

import pandas as pd

def load_data(start: str, end: str):
    # In production, you would fetch from FRED & HKMA APIs.
    # Here we just mock data for demo purposes.
    dates = pd.date_range(start, end, freq='D')
    sofr = pd.DataFrame({"Date": dates, "SOFR_percent": 5.0})
    hibor = pd.DataFrame({"Date": dates, "HIBOR_ON_percent": 3.0})
    return sofr, hibor
