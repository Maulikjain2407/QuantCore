import matplotlib.pyplot as plt


def plot_equity_curve(backtest_df):

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        backtest_df["date"],
        backtest_df["portfolio_value"],
        linewidth=2
    )

    ax.set_title("Equity Curve")
    ax.set_xlabel("Date")
    ax.set_ylabel("Portfolio Value")

    ax.grid(True)

    fig.tight_layout()

    return fig


def plot_drawdown(backtest_df):

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        backtest_df["date"],
        backtest_df["drawdown"],
        color="red"
    )

    ax.fill_between(
        backtest_df["date"],
        backtest_df["drawdown"],
        0,
        alpha=0.3
    )

    ax.set_title("Drawdown")
    ax.set_xlabel("Date")
    ax.set_ylabel("Drawdown")

    ax.grid(True)

    fig.tight_layout()

    return fig


def plot_cumulative_returns(backtest_df):

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        backtest_df["date"],
        backtest_df["cumulative_return"],
        linewidth=2
    )

    ax.set_title("Cumulative Return")
    ax.set_xlabel("Date")
    ax.set_ylabel("Return")

    ax.grid(True)

    fig.tight_layout()

    return fig


def plot_daily_returns(backtest_df):

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.hist(
        backtest_df["strategy_return"],
        bins=30
    )

    ax.set_title("Daily Returns Distribution")
    ax.set_xlabel("Daily Return")
    ax.set_ylabel("Frequency")

    fig.tight_layout()

    return fig