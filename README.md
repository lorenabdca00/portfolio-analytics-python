# 📊 Portfolio Analytics — Tech-Enabled America Fund (2017–2022)

> End-to-end quantitative analysis of a $100m multi-sector US equity portfolio:
> performance attribution, risk metrics, factor models, and efficient frontier optimisation.
> Built from real university assignment data — every chart and metric is code-generated, fully reproducible.

---

## 🏦 Background & Assignment Context

This project originates from a two-part assessment in **FINC71-303 — Portfolio Analysis and Investments**
at Bond University, Australia (Assoc. Prof. Rand Low).

**Part 1 — Portfolio Pitch (framed as January 2016)**
Pitch a managed fund to institutional investors. Choose 11 US stocks — one per GICS sector —
define an investment theme, justify portfolio weights, and forecast 6-year performance
(January 2017 – December 2022).

**Part 2 — Performance Presentation**
Report on the fund's actual realised performance using quantitative and statistical analysis:
distributional characteristics, risk-adjusted ratios, CAPM and Fama-French factor regressions,
benchmark comparisons, and a forward-looking investment proposal.

This repository transforms that analysis into a **reproducible Python project**. Every chart,
metric, and regression is generated from code — not calculated manually in Excel.

---

## 🎯 Fund Overview

**Tech-Enabled America Fund Ltd.**

The investment thesis was *tech-enabled transformation across all 11 GICS sectors* — selecting
companies in each sector best positioned to benefit from digital adoption, AI infrastructure,
cloud computing, and platform-driven productivity gains. Rather than a pure technology fund,
this approach captured structural growth while satisfying the assignment's diversification
mandate of one stock per sector.

### Why this theme?

As of January 2016, several structural tailwinds were already visible: cloud migration was
accelerating, mobile payments were displacing cash, healthcare was moving toward data-driven
models, and industrial automation was beginning its digital transformation. A tech-enabled
theme allowed overweighting companies benefiting from these megatrends while maintaining
broad sector exposure — making the fund both growth-oriented and defensible to investors
with diversification requirements.

### Portfolio Holdings & Weight Justification

The task required weights to sum to 100% with no short-selling. All other weight decisions
were discretionary. Weights were determined via **mean-variance optimisation**, blending
historical returns (50%) with CAPM-estimated returns (50%) using:
- Risk-free rate: **2.09%** (US 10-year Treasury, January 2016)
- Market return: **9.54%** (S&P 500 long-run estimate)

Per-stock **minimum and maximum bounds** were self-imposed to prevent over-concentration
and ensure every position remained meaningful. Without these constraints, unconstrained
mean-variance optimisation typically produces extreme corner solutions — allocating nearly
everything to one or two stocks and near-zero to the rest, which is impractical for a
diversified institutional mandate.

| Ticker | Company | GICS Sector | Min | Max | **Weight** |
|--------|---------|-------------|-----|-----|-----------|
| NVDA | NVIDIA Corp | Information Technology | 8% | 25% | **21.92%** |
| GOOGL | Alphabet Inc | Communication Services | 8% | 17% | **17.31%** |
| AMZN | Amazon.com | Consumer Discretionary | 8% | 17% | **12.96%** |
| HON | Honeywell International | Industrials | 5% | 10% | **10.00%** |
| MA | Mastercard Inc | Financials | 5% | 10% | **10.00%** |
| UNH | UnitedHealth Group | Health Care | 4% | 7% | **10.00%** |
| BALL | Ball Corp | Materials | 3% | 5% | **5.00%** |
| NEE | NextEra Energy | Utilities | 3% | 6% | **5.00%** |
| PG | Procter & Gamble | Consumer Staples | 2% | 4% | **3.81%** |
| EQIX | Equinix Inc | Real Estate | 6% | 12% | **2.00%** |
| SLB | Schlumberger Ltd | Energy | 2% | 4% | **2.00%** |

**Why overweight tech (NVDA, GOOGL, AMZN)?** These three represent the infrastructure of
digital transformation — semiconductors, search/cloud, and e-commerce/logistics. As of 2016,
all three had dominant market positions and clear structural growth ahead. The optimiser
confirmed this intuition: NVDA and GOOGL hit their upper bounds (25% and 17% respectively),
meaning even with constraints the model allocated as much as allowed.

**Why minimal weight to SLB and EQIX?** SLB (energy services) was exposed to oil price
cycles and capex volatility — present for sector diversification but kept at the 2% floor.
EQIX (data centre REIT) was an interesting long-term play but the optimiser assigned it
the floor due to lower expected return relative to its volatility in the input data.

**Ex-ante targets at construction:**
Expected Return: **17.08%** · Std Dev: **13.67%** · Sharpe: **1.10**

---

## 📈 Realised Results (2017–2022)

The fund significantly outperformed both benchmarks. A $100m investment in January 2017
grew to **$338m** by December 2022 — compared to $225m for the NASDAQ-100 and $171m
for the S&P 500.

| Year | Portfolio | S&P 500 | NASDAQ-100 | Key macro event |
|------|-----------|---------|------------|----------------|
| 2017 | **+44.5%** | +19.4% | +31.5% | US tax reform, strong corporate earnings |
| 2018 | -0.2% | -6.2% | -1.0% | US-China trade war, rising rates |
| 2019 | **+42.5%** | +28.9% | +37.8% | Fed pivot to dovish, rate cuts |
| 2020 | **+51.4%** | +16.3% | +47.6% | COVID-19 accelerated digital adoption |
| 2021 | **+46.3%** | +26.9% | +26.8% | Vaccine recovery, tech retention of gains |
| 2022 | -25.7% | -19.4% | **-33.1%** | Inflation spike, aggressive Fed rate hikes |

**Outperformed in 5 of 6 years.** In 2022, the portfolio fell less than NASDAQ (-25.7% vs
-33.1%), reflecting the defensive buffer from UNH, HON, and SLB (which surged +78.5%
as energy recovered).

### Risk-Adjusted Performance

| Metric | Value | Interpretation |
|--------|-------|---------------|
| CAGR | **22.50%** | 2.4× the S&P 500 annual return |
| Monthly Std Dev | 6.33% | Lower than NASDAQ volatility |
| **Sharpe Ratio** | **3.2241** | Exceptional — well above the ~1.0 ex-ante forecast |
| Treynor Ratio | 17.79% | High excess return per unit of systematic risk |
| Information Ratio | 1.2591 | Consistent benchmark outperformance |
| Max Drawdown | -32.29% | Worst peak-to-trough during 2022 rate hike cycle |
| **VaR 95%** | **-8.56%** | 5% chance of losing more than 8.56% in a month |
| CVaR 95% | -12.27% | Average loss in the worst 5% of months |
| Skewness | -0.4451 | Slight left tail — more extreme losses than gains |
| Excess Kurtosis | -0.0466 | Near-normal distribution, few extreme outliers |
| Win Rate | 72.2% | 52 positive months out of 72 |

**Why did realised Sharpe (3.22) far exceed the ex-ante forecast (1.10)?**
The blended expected return model used at construction underestimated NVDA's growth by a
large margin (+32.58% actual CAGR vs ~10.6% forecast). The COVID-19 pandemic also
dramatically accelerated cloud and digital spending — a tail event not in any 2016 model.

### Factor Model Results

| Model | Alpha (p.a.) | p-value | Beta | R² |
|-------|-------------|---------|------|-----|
| CAPM | **~10.7%** | **0.018 ★** | 1.147 | 0.791 |
| FF3 | positive | significant | ~1.15 | higher |
| FF5 | positive | significant | ~1.13 | higher |

The statistically significant positive alpha across all three models confirms the fund
generated returns above what risk factors alone explain. The Fama-French models show:
- **Negative SMB** — large-cap tilt (NVDA, GOOGL, AMZN, MA are mega-caps)
- **Negative HML** — growth tilt (consistent with the tech-enabled theme)

Both exposures were intentional and consistent with the fund's investment thesis.

### Top & Bottom Performers

| | Ticker | CAGR | Driver |
|-|--------|------|--------|
| 🥇 | NVDA | **+32.58%** | AI/GPU demand explosion — largest single contributor |
| 🥈 | UNH | +23.58% | Digital health expansion, Optum analytics platform |
| 🥉 | MA | +22.54% | Structural shift from cash to digital payments |
| 📉 | SLB | -4.38% | Energy services cyclicality, oil capex cuts 2017–2020 |

---

## 📁 Repository Structure

```
portfolio-analytics-python/
│
├── notebooks/
│   ├── 01_data_and_returns.ipynb       # Holdings pie chart, annual returns bar chart,
│   │                                   # $100m cumulative wealth chart, stock CAGR
│   │                                   # rankings, annual returns heatmap by stock
│   ├── 02_performance_metrics.ipynb    # Full metrics table, return distribution with
│   │                                   # VaR & CVaR, drawdown chart, seasonality heatmap
│   ├── 03_factor_models.ipynb          # CAPM scatter + regression, Fama-French 3-factor
│   │                                   # and 5-factor models, factor loading charts
│   └── 04_optimisation.ipynb           # Efficient frontier (15,000 Monte Carlo),
│                                       # Max Sharpe, Min Variance, weight comparison
│
├── data/                               # Pre-extracted from assignment Excel files
│   ├── portfolio_monthly_returns.csv   # 72 monthly returns (Jan 2017 – Dec 2022)
│   ├── stock_monthly_returns.csv       # Monthly returns per stock
│   ├── annual_returns.csv              # Annual: Portfolio, S&P 500, NASDAQ
│   ├── annual_stock_returns.csv        # Annual return per stock 2017–2022
│   ├── stock_cagr.csv                  # CAGR rankings (NVDA 32.58% → SLB -4.38%)
│   ├── monthly_prices.csv              # Monthly close prices
│   ├── portfolio_config.json           # Tickers, weights, sectors, names
│   └── confirmed_metrics.json          # All confirmed performance metrics
│
├── data_prep.py                        # Extracts data from Excel (run once)
├── requirements.txt                    # Python dependencies
└── README.md
```

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. (Optional) Re-extract from original Excel assignment file
python data_prep.py --excel FINC71-303_ExcelSheet_14047473_LorenaBrant.xlsx

# 3. Launch Jupyter and run notebooks in order 01 → 02 → 03 → 04
jupyter notebook
```

> The `data/` folder is pre-populated — skip step 2 to run immediately.

---

## 📊 Charts Generated

| File | Notebook | What it shows |
|------|----------|--------------|
| `sector_allocation.png` | NB01 | Portfolio allocation by GICS sector (pie chart) |
| `annual_returns.png` | NB01 | Annual returns: Portfolio vs S&P 500 vs NASDAQ |
| `cumulative_returns.png` | NB01 | $100m wealth chart with macro event annotations |
| `stock_cagr_chart.png` | NB01 | Stock CAGR rankings — top & bottom performers |
| `annual_stock_heatmap.png` | NB01 | Annual return heatmap per stock (2017–2022) |
| `return_distribution.png` | NB02 | Monthly return histogram with VaR & CVaR |
| `drawdown.png` | NB02 | Cumulative return + rolling drawdown (two-panel) |
| `seasonality_heatmap.png` | NB02 | Monthly returns heatmap with annual totals |
| `capm_regression.png` | NB03 | Portfolio vs market excess return scatter |
| `factor_loadings.png` | NB03 | FF3 and FF5 factor coefficients (★ = significant) |
| `efficient_frontier.png` | NB04 | Frontier + actual fund + Max Sharpe + Min Variance |
| `weight_comparison.png` | NB04 | Actual weights vs optimised alternatives |

---

## 🛠 Tech Stack

**Python:** `Python 3.11` · `pandas` · `numpy` · `matplotlib` · `seaborn` · `scipy` · `statsmodels` · `openpyxl` · `pandas-datareader`

**Excel:** Mean-variance optimisation (Solver add-in) · Covariance matrix · CAPM expected returns · Portfolio weight constraints · ANOVA regression output · Capital IQ Pro data integration

---

## 📚 Data Sources

| Source | Used for |
|--------|---------|
| `FINC71-303_ExcelSheet_14047473_LorenaBrant.xlsx` | Monthly prices, portfolio returns, confirmed metrics, regression outputs |
| `FINC71-303_ASS1_14047473_LorenaBrant.xlsx` | Covariance matrix, CAPM betas, optimisation weights and constraints |
| Ken French Data Library (via `pandas-datareader`) | Fama-French 3-factor and 5-factor monthly data |

---

## 👤 Author

**Lorena Brant**
Master of Business Data Analytics · Bond University, Australia
 · Open to relocate

[lorenabrant.edu@gmail.com](mailto:lorenabrant.edu@gmail.com) · [LinkedIn](https://linkedin.com/in/lorena-brant)
