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

def sortino_ratio(strategy_returns,holding_period=HOLDING_PERIOD):
    
    mean_return=strategy_returns.mean()

    downside_returns= strategy_returns[strategy_returns<0]

    downside_std=downside_returns.std()

    if downside_std==0:
        return 0

    annualisation_factor=np.sqrt(252/holding_period)

    sortino=annualisation_factor*(mean_return/downside_std)

    return sortino
    
def calmar_ratio(strategy_returns,holding_period=HOLDING_PERIOD):

    cumulative=(1+strategy_returns).prod()

    years = (len(strategy_returns)*holding_period) / 252
    annual_return=(cumulative**(1/years))-1

    maximum_drawdown=abs(max_drawdown(strategy_returns))

    if maximum_drawdown==0:
        return 0
    
    calmar=annual_return/maximum_drawdown

    return calmar

def recovery_factor(strategy_returns):
    total_returns=cumulative_returns(strategy_returns)

    maximum_drawdown=abs(max_drawdown(strategy_returns))

    if maximum_drawdown==0:
        return 0
    
    recover= total_returns/maximum_drawdown

    return recover

def CAGR(strategy_returns,holding_period=HOLDING_PERIOD):

    cumulative=(1+strategy_returns).prod()

    years=(len(strategy_returns)*holding_period)/252

    if years==0:
        return 0
    
    cagr=(cumulative**(1/years))-1

    return cagr

def calculate_metrics(backtest_df,holding_period=HOLDING_PERIOD):

    strategy_returns = backtest_df["strategy_return"]

    return {    

        "cumulative_return":
            cumulative_returns(strategy_returns),

        "sharpe_ratio":
            sharpe_ratio(strategy_returns,holding_period),

        "sortino_ratio":
            sortino_ratio(strategy_returns,holding_period),

        "max_drawdown":
            max_drawdown(strategy_returns),

        "calmar_ratio":
            calmar_ratio(strategy_returns,holding_period),

        "recovery_factor":
            recovery_factor(strategy_returns),

        "cagr":
            CAGR(strategy_returns,holding_period)
    }