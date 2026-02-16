# Change-Point-Analysis-and-Statistical-Modeling-of-Time-Series-Data-w11
# Brent Oil Price Forecasting & Volatility Risk Monitoring System


A production-grade time series forecasting system built to support risk-aware decision-making in energy-linked financial portfolios.
This project implements a modular ARIMA-based forecasting pipeline with automated testing, CI validation, and volatility monitoring.

---

## Business Problem

Oil price volatility directly impacts:

* Energy trading firms
* Commodity-linked investment portfolios
* Airlines and logistics companies
* Risk management desks

Inaccurate forecasts or poor uncertainty estimation can result in:

* Mispriced hedges
* Increased portfolio exposure
* Significant financial losses

This system provides forward-looking price forecasts **with quantified uncertainty** to support disciplined, risk-informed decisions.

---

## Solution Overview

This project transforms historical Brent oil price data into a reliable forecasting pipeline through:

* ARIMA time-series modeling
* Out-of-sample backtesting
* Rolling volatility calculation (risk proxy)
* Forecast confidence intervals
* Modular, production-style architecture
* Automated unit testing with CI validation

The system is structured to prioritize:

* Reproducibility
* Transparency
* Reliability
* Auditability

---

## Project Structure

```
brent-risk-forecast/
│
├── data/
│   └── raw/
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── model.py
│   ├── forecasting.py
│   ├── evaluation.py
│   └── main.py
│
├── tests/
│
├── .github/workflows/
│   └── ci.yml
│
├── requirements.txt
└── README.md
```

---

### Code Quality

* Modular architecture
* Type hints on all functions
* Configuration managed via `dataclass`
* No hard-coded magic numbers

### Testing

* 6+ unit tests covering:

  * Data loading
  * Preprocessing
  * Volatility calculation
  * ARIMA fitting
  * Forecast generation
  * RMSE validation

### CI/CD

* GitHub Actions pipeline
* Automatic test execution on push
* CI badge for build transparency

---

## Technical Details

### Data

* Historical Brent oil prices
* Chronologically ordered
* Date-indexed time series

### Model

* ARIMA (p, d, q)
* Trained on 80% of historical data
* Evaluated on 20% out-of-sample data

### Evaluation Metrics

* RMSE
* MAPE
* Confidence interval width
* Rolling standard deviation (volatility proxy)

---

## Risk & Volatility Monitoring

In addition to price forecasts, this system computes:

* 30-day rolling volatility
* Forecast confidence bands
* Uncertainty width as a risk signal

This enables interpretation such as:

* Increasing volatility regime
* Narrow vs. wide forecast uncertainty
* Stability vs. instability periods

---

## Why This Matters for Finance

Unlike academic notebooks, this system:

* Separates training and testing data
* Quantifies uncertainty
* Validates correctness automatically
* Can be extended into decision-support dashboards
* Prioritizes risk awareness over pure prediction

It demonstrates how statistical modeling can be transformed into a reliable financial analytics tool.

## Future Improvements

With additional time, the system could be extended to include:

* Walk-forward cross-validation
* Regime detection
* GARCH volatility modeling
* Value-at-Risk estimation
* Interactive Streamlit dashboard

-
