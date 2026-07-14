from src.test_train_split import test_train_split

from utils.model_io import load_model
from utils.logger import save, log
from utils.visualiser import (
    plot_equity_curve,
    plot_drawdown,
    plot_cumulative_returns,
    plot_daily_returns
)

from backtest.backtest import run_backtest
from backtest.metrics import calculate_metrics


def run_backtest_pipeline():

    log("Loading Test Data")

    _, _, x_test, _, test_df = test_train_split()

    log("Loading Model")

    model = load_model()

    log("Generating Predictions")

    y_pred = model.predict(x_test)

    log("Running Backtest")

    backtest_df = run_backtest(
        test_df,
        y_pred
    )

    log("Calculating Metrics")

    metrics = calculate_metrics(
        backtest_df
    )

    save(backtest_df, "backtest")
    
    save(metrics, "metrics")

    save(
        plot_equity_curve(backtest_df),
        "equity_curve"
    )

    save(
        plot_drawdown(backtest_df),
        "drawdown"
    )

    save(
        plot_cumulative_returns(backtest_df),
        "cumulative_return"
    )

    save(
        plot_daily_returns(backtest_df),
        "daily_returns"
    )

    print("\nBacktest Results")
    print("----------------")

    print(
        f"Cumulative Return: "
        f"{metrics['cumulative_return']:.2%}"
    )

    print(
        f"Sharpe Ratio: "
        f"{metrics['sharpe_ratio']:.2f}"
    )

    print(
        f"Max Drawdown: "
        f"{metrics['max_drawdown']:.2%}"
    )

    print(
        f"Sortino Ratio: "
        f"{metrics['sortino_ratio']:.2f}"
    )

    print(
        f"Calmar Ratio: "
        f"{metrics['calmar_ratio']:.2f}"
    )

    print(
        f"Recovery Factor: "
        f"{metrics['recovery_factor']:.2f}"
    )

    print(
        f"CAGR: "
        f"{metrics['cagr']:.2%}"
    )


if __name__ == "__main__":
    run_backtest_pipeline()