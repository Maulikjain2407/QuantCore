# QuantCore

> **QuantCore** is a modular quantitative research framework built in Python for developing, evaluating, and improving machine learning-driven trading strategies. The project integrates market data collection, feature engineering, Triple Barrier Labeling, machine learning, and backtesting into a reproducible research pipeline inspired by professional quantitative research workflows, QuantCore emphasizes **research, experimentation, and systematic strategy evaluation**, 
<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-013243?logo=numpy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-F7931E?logo=scikitlearn&logoColor=white)
![Joblib](https://img.shields.io/badge/Joblib-Model_Serialization-green)
![PyYAML](https://img.shields.io/badge/PyYAML-Configuration-red)
![yFinance](https://img.shields.io/badge/yFinance-Market_Data-00A86B)

![Random Forest](https://img.shields.io/badge/Model-Random_Forest-success)
![Backtesting](https://img.shields.io/badge/Backtesting-Advanced-brightgreen)
![Triple Barrier Labeling](https://img.shields.io/badge/Labeling-Triple_Barrier-blueviolet)

![Version](https://img.shields.io/badge/Version-V2-success)
![Status](https://img.shields.io/badge/Status-Under_Developement-brightgreen)
![License](https://img.shields.io/badge/License-MIT-success)

</p>

---

## Table of Contents

* [About QuantCore](#about-quantcore)
* [Key Features](#key-features)
* [Project Architecture](#project-architecture)
* [Project Structure](#project-structure)
* [Workflow](#workflow)
* [Feature Engineering](#feature-engineering)
* [Triple Barrier Labeling](#triple-barrier-labeling)
* [Machine Learning Pipeline](#machine-learning-pipeline)
* [Backtesting Engine](#backtesting-engine)
* [Performance Metrics](#performance-metrics)
* [Configuration](#configuration)
* [Installation](#installation)
* [Training Pipeline](#training-pipeline)
* [Backtesting Pipeline](#backtesting-pipeline)
* [Roadmap](#roadmap)
* [Technology Stack](#technology-stack)
* [License](#license)

---

# About QuantCore

QuantCore began as a machine learning trading project and has gradually evolved into a **quantitative research framework** focused on building, evaluating, and improving systematic trading strategies.

The primary objective of the project is not to create a profitable trading bot, but to understand and implement the research workflow followed by quantitative researchers. 

Rather than relying on simplistic prediction targets, QuantCore incorporates **Triple Barrier Labelling**, richer market-derived features, and a more comprehensive backtesting framework to evaluate strategies under more realistic conditions.

The project is built around a modular architecture, allowing individual components to be improved or replaced independently. As new research ideas emerge, they can be integrated without redesigning the entire system.

Current areas of research include:

* Feature engineering for alpha generation
* Triple Barrier Labelling
* Machine learning for financial prediction
* Strategy backtesting
* Risk-adjusted performance evaluation
* Experiment logging and visualization
* Systematic model improvement
---

# Key Features

## Data Pipeline

* Historical market data collection using Yahoo Finance
* Automated data cleaning and preprocessing
* Configurable data pipeline
* YAML-based configuration management
* Modular architecture for easy extension

---

## Feature Engineering

Generate market-derived alpha factors across multiple categories, including:

### Returns

* 1-Day Return
* 5-Day Return
* 10-Day Return
* 20-Day Return

### Trend Indicators

* SMA 10 Ratio
* SMA 20 Ratio

### Volatility Indicators

* Rolling Volatility (5)
* Rolling Volatility (20)
* Average True Range (ATR)
* ATR Percentage

### Volume Indicators

* Volume Ratio

### Price Action Features

* Candle Body Size
* Upper Wick
* Lower Wick
* Candle Range

---

## Triple Barrier Labelling

QuantCore V2 replaces traditional fixed-return labels with **Triple Barrier Labelling (TBL)**.

Each observation is evaluated using three predefined exit conditions:

* Maximum Holding Period
* ATR-Based Take Profit Barrier
* ATR-Based Stop Loss Barrier

The first barrier reached determines the final label.

Compared to fixed future-return labels, this approach produces targets that better reflect actual trading outcomes and provide a stronger foundation for supervised learning in financial markets.

---

## Machine Learning Pipeline

Current implementation:

* Random Forest Classifier

Pipeline includes:

* Feature Selection
* Train/Test Split
* Model Training
* Prediction Generation
* Model Serialization
* Experiment Tracking

The modular design allows additional models such as XGBoost, LightGBM, CatBoost, and Neural Networks to be integrated with minimal changes to the overall pipeline.

---

## Backtesting Engine

The backtesting module evaluates model predictions using a portfolio simulation framework.

Current functionality includes:

* Portfolio Return Calculation
* Strategy Return Calculation
* Cash Tracking
* Prediction-Based Trade Simulation

Performance is evaluated using:

* Cumulative Return
* Sharpe Ratio
* Sortino Ratio
* Maximum Drawdown
* Calmar Ratio
* Recovery Factor
* CAGR

These metrics provide a broader understanding of both profitability and risk, enabling more rigorous evaluation of trading strategies.

---

## Experiment Logging

Every experiment can be recorded for future comparison, making it easier to reproduce results and evaluate improvements across different iterations of the project.

Logging includes:

* Model Information
* Hyperparameters
* Performance Metrics
* Timestamped Results

---

## Performance Visualization

QuantCore includes visualization utilities for analysing trading performance through graphical outputs.

Available visualizations include:

* Equity Curve
* Cumulative Returns
* Drawdown Curve
* Strategy Performance Charts

These plots provide additional insight beyond numerical metrics and help identify behavioural characteristics of trading strategies.

---

# Project Architecture

QuantCore follows a modular, pipeline-driven architecture where each stage performs a single responsibility. This design allows individual modules to be modified, replaced, or extended without affecting the rest of the system, making experimentation significantly easier.

```text
                           QuantCore Architecture

                    ┌──────────────────────────────┐
                    │      Yahoo Finance API       │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │        Data Loader           │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │       Data Cleaner           │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │    Feature Engineering       │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │ Triple Barrier Labeling (TBL)│
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │      Train/Test Split        │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │   Random Forest Classifier   │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │       Predictions            │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │     Backtesting Engine       │
                    └──────────────┬───────────────┘
                                   │
             ┌─────────────────────┴─────────────────────┐
             ▼                                           ▼
    ┌──────────────────┐                      ┌──────────────────┐
    │ Performance      │                      │ Experiment Logs  │
    │ Metrics          │                      │ & Visualisations │
    └──────────────────┘                      └──────────────────┘
```

### Design Principles

The architecture is built around a few key principles:

* **Modularity** – Each component has a single responsibility.
* **Reproducibility** – Experiments can be recreated using configuration files.
* **Research-Oriented** – Designed for testing hypotheses rather than deploying trading systems.
* **Extensibility** – New models, features, and backtesting techniques can be added with minimal code changes.

---

# Project Structure

```text
QuantCore/
│
├── artifacts/
│   ├── experiment_logs/
│   └── saved_models/
│    
├── backtest/
│   ├── backtest.py
│   └── metrics.py
│
├── configs/
│   ├── config.py
│   └── config.yaml
│
├── data/
│   ├── processed/
│   └── raw/
│
├── feature_engineer/
│   ├── feature_engineering_V2.py
│   └── feature_engineering.py
│
├── label_creator/
│   ├── label_creator.py
│   └── triple_barrier_labeling.py
│
├── models/
│   └── model.py
│
├── pipelines/
│   ├── backtesting_pipeline.py
│   └── model_pipeline.py
│
├── src/
│   ├── data_cleaner.py
│   ├── data_loader.py
│   ├── evaluation.py
│   ├── pipeline.py
│   └── test_train_split.py
│
├── utils/
│   ├── config_loader.py
│   ├── logger.py
│   ├── model_io.py
│   └── visualiser.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

### Directory Overview

| Directory             | Purpose                                                                          |
| ----------------------| -------------------------------------------------------------------------------- |
| **configs/**          | Stores project configuration files.                                              |
| **data/**             | Contains raw and processed market data.                                          |
| **src/**              | Core data processing modules.                                                    |
| **label_creator/**    | Label creator modules.                                                           |
| **feature_engineer/** | Feature engineering modules.                                                     |
| **models/**           | Machine learning model implementations.                                          |
| **pipelines/**        | End-to-end training and backtesting workflows.                                   |
| **backtest/**         | Strategy simulation and performance evaluation.                                  |
| **utils/**            | Helper modules for configuration, logging, visualization, and model persistence. |
| **artifacts/**        | Stores trained models, experiment logs, and generated plots.                     |

---

# Workflow

The QuantCore workflow follows a sequential research pipeline from data collection to strategy evaluation.

```text
Yahoo Finance
      │
      ▼
Data Collection
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Triple Barrier Labeling
      │
      ▼
Train/Test Split
      │
      ▼
Random Forest Training
      │
      ▼
Model Prediction
      │
      ▼
Backtesting
      │
      ▼
Performance Metrics
      │
      ▼
Experiment Logging
      │
      ▼
Performance Visualisation
```

### Workflow Breakdown

### 1. Data Collection

Historical OHLCV data is downloaded using **Yahoo Finance** and stored locally for processing.

### 2. Data Cleaning

The dataset is cleaned by handling missing values, formatting columns, and preparing the data for feature generation.

### 3. Feature Engineering

Raw market data is transformed into informative quantitative factors that describe market behaviour.

### 4. Triple Barrier Labeling

Each observation is labelled using realistic trading exit conditions rather than fixed future returns.

### 5. Model Training

A Random Forest classifier learns relationships between engineered features and future market behaviour.

### 6. Prediction

The trained model generates trading signals on unseen data.

### 7. Backtesting

Signals are converted into simulated trades to evaluate the overall trading strategy.

### 8. Performance Evaluation

Risk-adjusted performance metrics, experiment logs, and visualisations are generated for further analysis.

---

# Feature Engineering

Feature engineering is the core of QuantCore. Rather than relying on raw market prices, the framework derives quantitative factors that describe trend, momentum, volatility, liquidity, and candlestick behaviour.

The current implementation groups engineered features into five categories.

---

## Return Features

Return-based factors capture short- and medium-term price momentum.

| Feature     | Description                  |
| ----------- | ---------------------------- |
| **ret_1d**  | One-day percentage return    |
| **ret_5d**  | Five-day percentage return   |
| **ret_10d** | Ten-day percentage return    |
| **ret_20d** | Twenty-day percentage return |

These features help identify persistent price movements and momentum effects.

---

## Trend Features

Trend indicators measure how current prices compare to their recent averages.

| Feature               | Description                      |
| --------------------- | -------------------------------- |
| **close_sma10_ratio** | Price relative to the 10-day SMA |
| **close_sma20_ratio** | Price relative to the 20-day SMA |

These ratios help identify bullish and bearish market regimes.

---

## Volatility Features

Volatility measures describe the magnitude of market fluctuations.

| Feature            | Description                                    |
| ------------------ | ---------------------------------------------- |
| **volatility_5d**  | Five-day rolling volatility                    |
| **volatility_20d** | Twenty-day rolling volatility                  |
| **ATR**            | Average True Range                             |
| **ATR %**          | ATR expressed as a percentage of closing price |

ATR-based features are also used by the Triple Barrier Labeling algorithm.

---

## Volume Features

Trading volume provides information about market participation.

| Feature          | Description                                      |
| ---------------- | ------------------------------------------------ |
| **volume_ratio** | Current volume relative to recent average volume |

High volume often confirms the strength of market movements.

---

## Price Action Features

Candlestick characteristics provide additional information beyond closing prices.

| Feature          | Description                           |
| ---------------- | ------------------------------------- |
| **Body Size**    | Difference between open and close     |
| **Upper Wick**   | Distance between high and candle body |
| **Lower Wick**   | Distance between low and candle body  |
| **Candle Range** | Difference between high and low       |

These features help the model capture buying pressure, selling pressure, indecision, and volatility within individual trading sessions.

---

## Why Feature Engineering Matters

Machine learning models cannot directly infer market structure from raw OHLCV data alone. Feature engineering transforms historical prices into meaningful quantitative signals that better represent market behaviour.

As QuantCore evolves, additional research-driven features such as momentum oscillators, mean-reversion signals, factor models, and statistical indicators will continue to be incorporated and evaluated through systematic experimentation.

# Triple Barrier Labeling

One of the most significant improvements introduced in **QuantCore V2** is the transition from traditional fixed-return labels to **Triple Barrier Labeling (TBL)**.

Conventional labeling techniques often assign labels based on whether the future return exceeds a predefined threshold after a fixed number of trading days. While simple to implement, this approach ignores how a trade would realistically exit in live markets.

Triple Barrier Labeling addresses this limitation by simulating three possible exit conditions for every observation.

---

## Why Triple Barrier Labeling?

Traditional labels answer the question:

> **"Was the price higher after *N* days?"**

Triple Barrier Labeling instead asks:

> **"Which exit condition would have occurred first if this trade had actually been executed?"**

This produces labels that are considerably more representative of real trading behaviour.

---

## Labeling Process

For every trading signal, three barriers are defined:

* **Upper Barrier (Take Profit)**
* **Lower Barrier (Stop Loss)**
* **Vertical Barrier (Maximum Holding Period)**

The first barrier reached determines the final label.

```text
                         Vertical Barrier
                               │
                               ▼

Entry ●────────────────────────│──────────── Time

        ╱╲
       ╱  ╲
      ╱    ╲
─────╯      ╰────────────── Price

Upper Barrier  →  Take Profit

Lower Barrier  →  Stop Loss
```

---

## Barrier Definitions

### Upper Barrier

The upper barrier represents the **Take Profit** level.

It is calculated using the Average True Range (ATR):

```text
Take Profit = Entry Price + (ATR × Take Profit Multiplier)
```

If the price reaches this level before any other barrier, the trade is labelled as a profitable outcome.

---

### Lower Barrier

The lower barrier represents the **Stop Loss** level.

```text
Stop Loss = Entry Price − (ATR × Stop Loss Multiplier)
```

If the price reaches this level first, the trade is considered unsuccessful.

---

### Vertical Barrier

The vertical barrier limits the maximum duration of a trade.

If neither the take-profit nor stop-loss barrier is reached before the predefined holding period expires, the trade exits at the closing price of the final day.

This prevents trades from remaining open indefinitely and reflects realistic position management.

---

## Current Configuration

QuantCore V2 currently uses:

| Parameter              |          Value |
| ---------------------- | -------------: |
| Holding Period         | 5 Trading Days |
| Take Profit Multiplier |        2 × ATR |
| Stop Loss Multiplier   |        1 × ATR |

These parameters can be modified directly through the project configuration file.

---

## Advantages of Triple Barrier Labeling

Compared with fixed-return labeling, Triple Barrier Labeling offers several advantages:

* More realistic trade outcomes
* Explicit risk management through stop losses
* Volatility-adjusted exit levels using ATR
* Better alignment with systematic trading strategies
* Improved quality of supervised learning labels

---

# Machine Learning Pipeline

After feature engineering and label generation, QuantCore trains a supervised machine learning model to predict future trading outcomes.

The current implementation uses a **Random Forest Classifier**, chosen for its robustness, interpretability, and ability to model non-linear relationships commonly found in financial data.

---

## Pipeline Overview

```text
Engineered Features
        │
        ▼
Triple Barrier Labels
        │
        ▼
Train/Test Split
        │
        ▼
Random Forest Training
        │
        ▼
Model Prediction
        │
        ▼
Model Persistence
```

---

## Current Model

The default model used in QuantCore is:

* **Random Forest Classifier**

Current configuration:

```yaml
model:
  random_forests:
    n_estimators: 100
    random_state: 42
    n_jobs: -1
```

---

## Why Random Forest?

Random Forest was selected as the initial baseline model because it offers:

* Strong performance on tabular financial data
* Ability to capture non-linear relationships
* Reduced overfitting through ensemble learning
* Minimal feature scaling requirements
* Feature importance estimation
* Stable baseline for future model comparisons

---

## Training Pipeline

The complete training workflow consists of:

1. Download historical market data
2. Clean and preprocess data
3. Generate quantitative features
4. Create Triple Barrier Labels
5. Perform train-test split
6. Train the Random Forest classifier
7. Generate predictions
8. Save the trained model

---

## Model Persistence

After training, the model is automatically serialized using **Joblib**.

Saved models are stored in:

```text
artifacts/saved_models/
```

## Future Machine Learning Research

The modular architecture allows new algorithms to be integrated with minimal code changes.

Planned additions include:

* XGBoost
* LightGBM
* CatBoost
* Logistic Regression
* Support Vector Machines
* Neural Networks
* Ensemble Learning
* Model Stacking

---

# Backtesting Engine

Training an accurate machine learning model is only one component of quantitative trading research.

The true value of a strategy is determined by how its predictions perform under simulated market conditions.

The QuantCore backtesting engine converts model predictions into trading decisions and evaluates their financial performance using realistic portfolio metrics.

---

## Backtesting Workflow

```text
Model Predictions
        │
        ▼
Trading Signals
        │
        ▼
Strategy Returns
        │
        ▼
Portfolio Simulation
        │
        ▼
Performance Metrics
```

---

## Current Functionality

The backtesting engine currently supports:

* Prediction-based trade simulation
* Strategy return calculation
* Portfolio value tracking
* Cash management
* Equity curve generation
* Risk-adjusted performance evaluation

---

## Performance Evaluation

Each strategy is evaluated using multiple complementary metrics rather than relying solely on cumulative returns.

Current evaluation includes:

| Metric                | Description                                                                  |
| --------------------- | ---------------------------------------------------------------------------- |
| **Cumulative Return** | Measures the total return generated by the strategy over the testing period. |
| **Sharpe Ratio**      | Measures return per unit of total risk (volatility).                         |
| **Sortino Ratio**     | Measures return relative to downside risk only.                              |
| **Maximum Drawdown**  | Largest decline from a previous portfolio peak.                              |
| **Calmar Ratio**      | Annualized return relative to maximum drawdown.                              |
| **Recovery Factor**   | Measures how effectively the strategy recovers from drawdowns.               |
| **CAGR**              | Compound Annual Growth Rate of the portfolio.                                |

---

## Why Multiple Metrics?

No single metric can fully evaluate a trading strategy.

For example:

* A strategy may achieve high returns but experience severe drawdowns.
* Another may produce lower returns while maintaining excellent risk-adjusted performance.

QuantCore therefore evaluates every experiment using multiple complementary metrics to provide a balanced assessment of both profitability and risk.

---

# Sample Results

The following example demonstrates the output produced after running the QuantCore backtesting pipeline.

```text id="v9lh5o"
Backtest Results
----------------
Cumulative Return: -32.36%
Sharpe Ratio: -0.42
Max Drawdown: -66.49%
Sortino Ratio: -0.64
Calmar Ratio: -0.12
Recovery Factor: -0.49
CAGR: -7.67%
```

# Installation

## Clone the Repository

```bash id="g7m2xf"
git clone https://github.com/Maulikjain2407/QuantCore.git

cd QuantCore
```

---

## Create a Virtual Environment

### Windows

```bash id="4gcpw5"
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash id="n1m4dy"
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash id="hyb3gu"
pip install -r requirements.txt
```

---

## Verify Installation

```bash id="88txvj"
python --version
```

Ensure that Python **3.10 or higher** is installed before running the project.

---

# Usage

QuantCore is divided into two primary pipelines:

1. **Model Training Pipeline**
2. **Backtesting Pipeline**

---

## Training Pipeline

Run the following command:

```bash id="lxwxp9"
python -m pipelines.model_pipeline
```

This pipeline performs:

1. Download Market Data
2. Data Cleaning
3. Feature Engineering
4. Triple Barrier Labeling
5. Train/Test Split
6. Random Forest Training
7. Model Saving

The trained model is automatically stored inside:

```text id="cqlnlj"
artifacts/saved_models/
```

---

## Backtesting Pipeline

Execute:

```bash id="10ocnk"
python -m pipelines.backtesting_pipeline
```

The backtesting pipeline performs:

* Loads the trained model
* Generates predictions
* Simulates trading decisions
* Calculates portfolio returns
* Computes performance metrics
* Saves experiment logs
* Generates performance visualizations

---

## Output Artifacts

Running both pipelines produces several outputs.

| Output            | Location                     |
| ----------------- | ---------------------------- |
| Processed Data    | `data/processed/`            |
| Trained Models    | `artifacts/saved_models/`    |
| Experiment Logs   | `artifacts/experiment_logs/` |
| Performance Plots | `artifacts/visualisations/`  |

---

## Typical Workflow

```text id="jlwm3i"
Clone Repository
        │
        ▼
Install Dependencies
        │
        ▼
Configure Parameters
        │
        ▼
Run Model Pipeline
        │
        ▼
Train Random Forest
        │
        ▼
Run Backtesting Pipeline
        │
        ▼
Review Metrics
        │
        ▼
Analyse Results
        │
        ▼
Improve Strategy
```

The workflow is intentionally iterative. Each experiment contributes new insights that guide future improvements to feature engineering, labeling methods, model selection, and backtesting methodology.

# Configuration

QuantCore is designed to be highly configurable. Rather than modifying source code, most project settings can be adjusted through the central configuration file.

All configurable parameters are stored in:

```text
configs/config.yaml
```

---

## Example Configuration

```yaml
path:
  data_dir: data
  raw_data: raw
  processed_data: processed

  artifacts_dir: artifacts
  experiment_logs: experiment_logs
  saved_models: saved_models
  plots: visualisations

data:
  ticker: AAPL
  start: "2020-01-01"
  end: "2025-01-01"

model:
  random_forest:
    n_estimators: 100
    random_state: 42
    n_jobs: -1

labeling:
  holding_period: 5
  take_profit_multiplier: 2
  stop_loss_multiplier: 1

backtest:
  initial_capital: 100000
```

---

## Configuration Categories

### Data

Defines the market data source and historical date range used for training and evaluation.

| Parameter | Description                    |
| --------- | ------------------------------ |
| `ticker`  | Asset ticker symbol            |
| `start`   | Start date for data collection |
| `end`     | End date for data collection   |

---

### Model

Controls the machine learning model used during training.

Current configurable parameters include:

* Number of trees
* Random seed
* Number of CPU cores

---

### Triple Barrier Labeling

These parameters directly influence the label generation process.

| Parameter                | Description                          |
| ------------------------ | ------------------------------------ |
| `holding_period`         | Maximum trade duration               |
| `take_profit_multiplier` | ATR multiplier for the upper barrier |
| `stop_loss_multiplier`   | ATR multiplier for the lower barrier |

Changing these values allows different trading hypotheses to be evaluated without modifying the implementation.

---

### Backtesting

Portfolio simulation parameters can also be configured.

Current settings include:

* Initial Capital

---

# Roadmap

QuantCore is being developed incrementally, with each version introducing more realistic quantitative research capabilities.

---

## ✅ Version 1

The initial release established the core machine learning pipeline.

### Implemented

* Historical Market Data Collection
* Data Cleaning
* Feature Engineering
* Future Return Labeling
* Random Forest Classifier
* Basic Backtesting
* Sharpe Ratio
* Maximum Drawdown
* Cumulative Return

---

## ✅ Version 2 (Current)

Version 2 shifts QuantCore from a machine learning project toward a research-oriented quantitative framework.

### New Features

#### Feature Engineering

* ATR
* ATR Percentage
* Body Size
* Upper Wick
* Lower Wick
* Candle Range

#### Labeling

* Triple Barrier Labeling
* Configurable Holding Period
* ATR-Based Take Profit
* ATR-Based Stop Loss

#### Backtesting

* Portfolio Simulation
* Cash Tracking
* Enhanced Performance Metrics

#### Performance Metrics

* Sortino Ratio
* Calmar Ratio
* Recovery Factor
* CAGR

#### Research Utilities

* Experiment Logging
* Performance Visualisation

---

## 🚧 Version 3 (Planned)

The next major milestone focuses on transforming QuantCore into a more comprehensive quantitative research platform.

### Research Enhancements

* Feature Importance Analysis
* Confusion Matrix
* Label Distribution Analysis
* Prediction Distribution
* Trade Statistics
* Win Rate
* Profit Factor
* Average Holding Period

### Machine Learning

* XGBoost
* LightGBM
* CatBoost
* Logistic Regression
* Model Comparison Framework
* Hyperparameter Optimisation

### Validation

* Walk-Forward Validation
* Time-Series Cross Validation
* Purged Cross Validation

### Backtesting

* Transaction Costs
* Slippage
* Position Sizing
* Portfolio-Level Backtesting

---
# Technology Stack

QuantCore is built entirely using open-source technologies commonly employed in data science, machine learning, and quantitative finance workflows.

---

## Programming Language

| Technology       | Purpose                                               |
| ---------------- | ----------------------------------------------------- |
| **Python 3.10+** | Core programming language used throughout the project |

---

## Data Processing

| Library    | Purpose                                       |
| ---------- | --------------------------------------------- |
| **Pandas** | Data manipulation and preprocessing           |
| **NumPy**  | Numerical computing and vectorized operations |

---

## Machine Learning

| Library          | Purpose                                                      |
| ---------------- | ------------------------------------------------------------ |
| **Scikit-Learn** | Random Forest implementation, model training, and evaluation |
| **Joblib**       | Model serialization and persistence                          |

---

## Market Data

| Library                      | Purpose                                 |
| ---------------------------- | --------------------------------------- |
| **Yahoo Finance (yfinance)** | Historical OHLCV market data collection |

---

## Configuration Management

| Library    | Purpose                                  |
| ---------- | ---------------------------------------- |
| **PyYAML** | Project configuration through YAML files |

---

## Visualization

| Library        | Purpose                                      |
| -------------- | -------------------------------------------- |
| **Matplotlib** | Performance visualization and research plots |

---

## Development Tools

| Tool        | Purpose                               |
| ----------- | ------------------------------------- |
| **Git**     | Version control                       |
| **GitHub**  | Source code hosting and collaboration |
| **VS Code** | Primary development environment       |

---

## Project Dependencies

* Python 3.10+
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* yFinance
* PyYAML
* Joblib
* 
---

# License

This project is licensed under the **MIT License**.

The MIT License is a permissive open-source license that allows anyone to use, modify, distribute, and build upon this project with minimal restrictions, provided that the original copyright notice and license are included.

---
