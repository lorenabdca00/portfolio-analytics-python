"""
data_prep.py — Run once to extract data from your assignment Excel file.

Usage:
    python data_prep.py --excel FINC71-303_ExcelSheet_14047473_LorenaBrant.xlsx

Outputs (all to data/ folder):
    monthly_prices.csv           Monthly close prices Jan 2017–Dec 2022
    stock_monthly_returns.csv    Monthly returns per stock
    portfolio_monthly_returns.csv Portfolio weighted monthly returns
    annual_stock_returns.csv     Annual returns per stock 2017–2022
    annual_returns.csv           Annual returns: Portfolio, S&P 500, NASDAQ
    stock_cagr.csv               Stock-level CAGR rankings
    portfolio_config.json        Tickers, weights, sectors
    confirmed_metrics.json       All confirmed performance metrics
"""
import argparse, json, openpyxl, pandas as pd, numpy as np
from pathlib import Path
from datetime import datetime


def to_date(val):
    if isinstance(val, datetime):        return pd.Timestamp(val)
    if isinstance(val, (int, float)):    return pd.Timestamp('1899-12-30') + pd.Timedelta(days=int(val))
    return None


def run(excel_path: str, out_dir: str = 'data'):
    out = Path(out_dir)
    out.mkdir(exist_ok=True)
    wb  = openpyxl.load_workbook(excel_path, read_only=True, data_only=True)
    print(f'Opened:  {excel_path}')
    print(f'Sheets:  {wb.sheetnames}')

    # ── 1. Monthly prices (Sheet1) ────────────────────────────────────────────
    ws   = wb['Sheet1']
    rows = list(ws.iter_rows(values_only=True))
    t_row = rows[9]
    tickers, col_map = [], {}
    for i, v in enumerate(t_row):
        if v and v not in ('Ticker', 'Date', None) and isinstance(v, str) and v.strip():
            t = v.strip(); tickers.append(t); col_map[t] = i

    records = []
    for row in rows[11:]:
        dt = to_date(row[1])
        if dt is None: continue
        rec = {'Date': dt}
        for t, c in col_map.items():
            rec[t] = row[c]
        records.append(rec)

    prices = pd.DataFrame(records).set_index('Date')
    prices.index = pd.to_datetime(prices.index)
    prices = prices.loc['2017':'2022']
    prices.to_csv(out / 'monthly_prices.csv')
    print(f'  monthly_prices.csv          {prices.shape}')

    # ── 2. Stock monthly returns (from prices) ────────────────────────────────
    stock_ret = prices.pct_change().dropna()
    stock_ret.to_csv(out / 'stock_monthly_returns.csv')
    print(f'  stock_monthly_returns.csv   {stock_ret.shape}')

    # ── 3. Portfolio monthly returns (Distribution sheet) ────────────────────
    ws2  = wb['Distribution']
    rows2 = list(ws2.iter_rows(values_only=True))
    port_records = []
    for row in rows2[1:]:
        dt  = to_date(row[0])
        val = row[1]
        if dt is None or not isinstance(val, (int, float)): continue
        port_records.append({'Date': dt, 'Portfolio': float(val)})

    port_ret = pd.DataFrame(port_records).set_index('Date')
    port_ret.index = pd.to_datetime(port_ret.index)
    port_ret['Portfolio'].to_csv(out / 'portfolio_monthly_returns.csv', header=True)
    print(f'  portfolio_monthly_returns.csv  {len(port_ret)} rows')

    # ── 4. Annual stock returns (Benchmark sheet) ─────────────────────────────
    ws3  = wb['Benchmark']
    rows3 = list(ws3.iter_rows(max_row=15, values_only=True))
    years = [int(v) for v in rows3[0] if isinstance(v, (int, float))]
    ann_records = []
    for row in rows3[1:]:
        t = row[0]
        if not t or not isinstance(t, str): continue
        rec = {'Ticker': t.strip(), 'Weight': row[1]}
        for i, y in enumerate(years):
            rec[str(y)] = row[2 + i]
        ann_records.append(rec)

    ann_df = pd.DataFrame(ann_records)
    ann_df.to_csv(out / 'annual_stock_returns.csv', index=False)
    print(f'  annual_stock_returns.csv    {ann_df.shape}')

    # ── 5. Stock CAGR (TopStock sheet) ────────────────────────────────────────
    ws4   = wb['TopStock']
    rows4 = list(ws4.iter_rows(max_row=20, values_only=True))
    top   = []
    for row in rows4:
        if (row[2] and isinstance(row[2], str) and 2 <= len(row[2].strip()) <= 5
                and row[2] not in ('Ticker',)
                and isinstance(row[5], (int, float))
                and isinstance(row[6], (int, float))):
            top.append({'Ticker': row[2], 'Start': row[3], 'End': row[4],
                        'TotalReturn': row[5], 'CAGR': row[6]})

    top_df = pd.DataFrame(top).drop_duplicates('Ticker')
    top_df.to_csv(out / 'stock_cagr.csv', index=False)
    print(f'  stock_cagr.csv              {top_df.shape}')

    # ── 6. Annual benchmark returns (confirmed from slides) ───────────────────
    annual_ret = pd.DataFrame({
        'Portfolio': {2017:0.4452, 2018:-0.0022, 2019:0.4251, 2020:0.5139, 2021:0.4626, 2022:-0.2574},
        'S&P 500':   {2017:0.1942, 2018:-0.0624, 2019:0.2888, 2020:0.1626, 2021:0.2689, 2022:-0.1944},
        'NASDAQ':    {2017:0.3147, 2018:-0.0096, 2019:0.3783, 2020:0.4757, 2021:0.2681, 2022:-0.3307},
    }).T
    annual_ret.index.name = 'Series'
    annual_ret.to_csv(out / 'annual_returns.csv')
    print(f'  annual_returns.csv          {annual_ret.shape}')

    # ── 7. Portfolio config ───────────────────────────────────────────────────
    PORTFOLIO = {
        'NVDA':  {'weight': 0.2192, 'sector': 'Information Technology',  'name': 'NVIDIA Corp'},
        'GOOGL': {'weight': 0.1731, 'sector': 'Communication Services',  'name': 'Alphabet Inc'},
        'AMZN':  {'weight': 0.1296, 'sector': 'Consumer Discretionary',  'name': 'Amazon.com Inc'},
        'HON':   {'weight': 0.1000, 'sector': 'Industrials',             'name': 'Honeywell International'},
        'MA':    {'weight': 0.1000, 'sector': 'Financials',              'name': 'Mastercard Inc'},
        'UNH':   {'weight': 0.1000, 'sector': 'Health Care',             'name': 'UnitedHealth Group'},
        'BALL':  {'weight': 0.0500, 'sector': 'Materials',               'name': 'Ball Corp'},
        'NEE':   {'weight': 0.0500, 'sector': 'Utilities',               'name': 'NextEra Energy'},
        'PG':    {'weight': 0.0381, 'sector': 'Consumer Staples',        'name': 'Procter & Gamble'},
        'EQIX':  {'weight': 0.0200, 'sector': 'Real Estate',             'name': 'Equinix Inc'},
        'SLB':   {'weight': 0.0200, 'sector': 'Energy',                  'name': 'Schlumberger Ltd'},
    }
    with open(out / 'portfolio_config.json', 'w') as f:
        json.dump(PORTFOLIO, f, indent=2)
    print(f'  portfolio_config.json       {len(PORTFOLIO)} stocks')

    # ── 8. Confirmed metrics ──────────────────────────────────────────────────
    confirmed = {
        'CAGR': 0.22498, 'Annualised_Return': 0.22498,
        'Annualised_Vol': 0.06330, 'Sharpe': 3.2241,
        'Treynor': 0.17792, 'Information_Ratio': 1.2591,
        'Beta': 1.1470, 'Alpha_annual': 0.1070,
        'VaR_95': -0.0856, 'CVaR_95': -0.1227,
        'Skewness': -0.4451, 'Kurtosis': -0.0466,
        'RF': 0.0209,
    }
    with open(out / 'confirmed_metrics.json', 'w') as f:
        json.dump(confirmed, f, indent=2)
    print(f'  confirmed_metrics.json      {len(confirmed)} metrics')

    print(f'\nAll data extracted → {out}/  ✓')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract portfolio data from assignment Excel')
    parser.add_argument('--excel', required=True,
                        help='Path to FINC71-303_ExcelSheet_14047473_LorenaBrant.xlsx')
    parser.add_argument('--out', default='data',
                        help='Output directory (default: data/)')
    args = parser.parse_args()
    run(args.excel, args.out)
