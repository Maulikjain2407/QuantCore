# QuantCore

QuantCore is a modular quantitative trading research project built in Python. It collects market data, generates alpha factors, trains machine learning models, and evaluates trading strategies through backtesting.

The project is designed as a learning-focused yet extensible foundation for quantitative finance, systematic trading research, and machine learning-driven alpha generation.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-013243?logo=numpy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-F7931E?logo=scikitlearn&logoColor=white)
![Joblib](https://img.shields.io/badge/Joblib-Model_Serialization-green)
![PyYAML](https://img.shields.io/badge/PyYAML-Configuration-red)
![yFinance](https://img.shields.io/badge/yFinance-Market_Data-00A86B)

![Random Forest](https://img.shields.io/badge/Model-Random_Forest-success)
![Backtesting](https://img.shields.io/badge/Backtesting-Implemented-brightgreen)
![Status](https://img.shields.io/badge/Status-Under_Developement-brightgreen)
![License](https://img.shields.io/badge/License-MIT-success)

---

## Features

* Historical market data collection using Yahoo Finance
* Data cleaning and preprocessing pipeline
* Alpha factor generation through feature engineering
* Label creation using future returns
* Machine learning-based signal generation
* Random Forest classifier for prediction
* Model persistence with Joblib
* Strategy backtesting engine
* Performance evaluation using:

  * Cumulative Return
  * Sharpe Ratio
  * Maximum Drawdown
* Modular architecture for future expansion

---

## Project Structure

```text
QuantCore/
│
├── configs/
│   ├── config.py
│   └── config.yaml
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── model.py
│
├── pipelines/
│   ├── model_pipeline.py
│   └── backtesting_pipeline.py
│
├── src/
│   ├── data_loader.py
│   ├── data_cleaner.py
│   ├── feature_engineering.py
│   ├── label_creator.py
│   └── test_train_split.py
│
├── utils/
│   ├── config_loader.py
│   └── model_io.py
│
├── backtest/
│   ├── backtest.py
│   └── metrics.py
│
├── artifacts/
│   ├── saved_models/
│   └── experiment_logs/
│
└── README.md
```

---

## Workflow

```text
Yahoo Finance
      ↓
Data Loader
      ↓
Data Cleaner
      ↓
Feature Engineering
      ↓
Label Creation
      ↓
Train/Test Split
      ↓
Random Forest Model
      ↓
Model Persistence
      ↓
Predictions
      ↓
Backtesting
      ↓
Performance Metrics
```

---

## Feature Engineering

The following alpha factors are currently generated:

### Returns

* `ret_1d`
* `ret_5d`
* `ret_10d`
* `ret_20d`

### Volatility

* `volatility_5d`
* `volatility_20d`

### Trend Factors

* `close_sma10_ratio`
* `close_sma20_ratio`

### Volume Factor

* `volume_ratio`

### Range Factor

* `range_ratio`

---

## Label Generation

The target variable is generated using future 5-day returns.

```python
future_returns = (close.shift(-5) / close) - 1
target = (future_returns > 0.01).astype(int)
```

A positive label indicates that the stock gained more than 1% over the next five trading days.

---

## Model

Current model:

* Random Forest Classifier

Default configuration:

```yaml
model:
  random_forests:
    n_estimators: 100
    random_state: 42
    n_jobs: -1
```

---

## Performance Metrics

### Cumulative Return

Measures total strategy return over the testing period.

### Sharpe Ratio

Measures risk-adjusted return.

### Maximum Drawdown

Measures the largest decline from a previous portfolio peak.

---

## Configuration

All project settings are controlled through:

```text
configs/config.yaml
```

Example:

```yaml
path:
  data_dir: data
  raw_data: raw
  processed_data: processed
  artifacts_dir: artifacts
  experiment_logs: experiment_logs
  saved_models: saved_models

model:
  random_forests:
    n_jobs: -1
    random_state: 42
    n_estimators: 100

data:
  tickers: "AAPL"
  start: "2020-01-01"
  end: "2025-01-01"

metrics:
  holding_period: 5
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Maulikjain2407/QuantCore.git
cd QuantCore
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows:

```bash
venv\Scripts\activate
```

#### Linux / macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Training Pipeline

Run the training pipeline:

```bash
python -m pipelines.model_pipeline
```

This pipeline performs:

1. Data Download
2. Data Cleaning
3. Feature Engineering
4. Label Creation
5. Train/Test Split
6. Model Training
7. Model Saving

Saved model:

```text
artifacts/saved_models/random_forest.pkl
```

---

## Backtesting Pipeline

Run the backtesting pipeline:

```bash
python -m pipelines.backtesting_pipeline
```

Example output:

```text
Backtest Results
----------------
Cumulative Return: 22.31%
Sharpe Ratio: 0.49
Max Drawdown: -23.47%
```

---

## Current Limitations

* Single asset support
* No transaction costs
* No slippage modeling
* Fixed holding period
* Single machine learning model
* No walk-forward validation

---

## Future Improvements

### Machine Learning

* XGBoost
* LightGBM
* Neural Networks
* Transformer Models

### Quantitative Research

* Feature Importance Analysis
* Hyperparameter Optimization
* Walk-Forward Validation
* Cross Validation
* Multi-Factor Models

### Backtesting

* Transaction Costs
* Slippage
* Position Sizing
* Portfolio-Level Backtesting
* Multi-Asset Support

### Production Features

* Logging
* Experiment Tracking
* Model Versioning
* Automated Retraining
* Cloud Deployment

---

## Technology Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* Joblib
* PyYAML
* yFinance

---

## Project Goal

QuantCore aims to provide a clean, modular, and extensible framework for learning quantitative finance, researching alpha factors, and developing machine learning-driven trading strategies. The project is designed to evolve from a research-oriented educational project into a more production-grade quantitative research platform.
