from src.test_train_split import test_train_split

from utils.model_io import load_model

from backtest.backtest import run_backtest
from backtest.metrics import calculate_metrics

def run_backtest_pipeline():

    _, _, x_test, _, test_df = test_train_split()

    model = load_model()

    y_pred = model.predict(x_test)

    backtest_df = run_backtest(
        test_df,
        y_pred
    )

    metrics = calculate_metrics(
        backtest_df
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

if __name__ == "__main__":
    run_backtest_pipeline()