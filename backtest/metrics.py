import numpy as np
from configs.config import HOLDING_PERIOD
def cumulative_returns(strategy_returns):
    cumulative=(1+strategy_returns).cumprod()

    return cumulative.iloc[-1]-1

def sharpe_ratio(strategy_returns,holding_period=HOLDING_PERIOD):
    mean_return=strategy_returns.mean()
    std_return=strategy_returns.std()

    if std_return==0:
        return 0
    else:
        
        annualisation_factor=np.sqrt(252/holding_period)
        sharpe= annualisation_factor*(mean_return/std_return)

        return sharpe
    
def max_drawdown(strategy_returns):
    cumulative=(1+strategy_returns).cumprod()
    running_max=cumulative.cummax()

    drawdown=(cumulative-running_max)/running_max

    return drawdown.min()

def calculate_metrics(
    backtest_df,
    holding_period=HOLDING_PERIOD
):

    strategy_returns = backtest_df[
        "strategy_return"
    ]

    return {
        "cumulative_return":
            cumulative_returns(
                strategy_returns
            ),

        "sharpe_ratio":
            sharpe_ratio(
                strategy_returns,
                holding_period
            ),

        "max_drawdown":
            max_drawdown(
                strategy_returns
            )
    }