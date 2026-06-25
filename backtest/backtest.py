import pandas as pd

def run_backtest(test_df,y_pred):
    
    outcome=pd.DataFrame()

    outcome["date"]=test_df["date"].values
    outcome["future_returns"]=test_df["future_returns"].values
    outcome["predictions"]=y_pred

    outcome["strategy_return"]=(outcome["predictions"]*outcome["future_returns"])

    return outcome