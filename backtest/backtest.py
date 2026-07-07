import pandas as pd

INITIAL_CAPITAL = 100000


def run_backtest(test_df, y_pred):

    outcome = pd.DataFrame()

    outcome["date"] = test_df["date"].values

    outcome["future_returns"] = test_df["future_returns"].values

    outcome["predictions"] = y_pred

    outcome["strategy_return"] = (
        outcome["predictions"] * outcome["future_returns"]
    )

    outcome["cumulative_return"] = (
        1 + outcome["strategy_return"]
    ).cumprod() - 1

    outcome["portfolio_value"] = (
        INITIAL_CAPITAL * (1 + outcome["cumulative_return"])
    )

    outcome["running_max"] = (
        outcome["portfolio_value"].cummax()
    )

    outcome["drawdown"] = (
        outcome["portfolio_value"] - outcome["running_max"]
    ) / outcome["running_max"]

    outcome.drop(columns=["running_max"], inplace=True)

    return outcome