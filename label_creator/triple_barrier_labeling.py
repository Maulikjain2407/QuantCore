import numpy as np
import pandas as pd

from configs.config import MODEL_DATA_PATH, FEATURE_ENGINEER_PATH

def create_triple_barrier_label(holding_period,take_profit_multiplier,stop_loss_multiplier):
    
    tf=pd.read_csv(FEATURE_ENGINEER_PATH)
    df=tf.copy()

    labels = []
    future_returns = []
    exit_prices = []
    exit_dates = []
    exit_reasons = []
    holding_days = []
    

    for i in range(len(df)):
        if i + holding_period >= len(df):
            labels.append(np.nan)
            future_returns.append(np.nan)
            exit_prices.append(np.nan)
            exit_dates.append(np.NaT)
            exit_reasons.append(np.nan)
            holding_days.append(np.nan)
            continue
    
        entry_price=df.loc[i,"close"]
        atr_percent=df.loc[i,"atr%"]

        if atr_percent>1:
            atr_percent=atr_percent/100
    
        take_profit_price=entry_price*(1+ take_profit_multiplier*atr_percent)
        stop_loss_price=entry_price*(1- stop_loss_multiplier*atr_percent)

        label= 0
        exit_price=df.loc[i+holding_period, "close"]
        exit_date=df.loc[i+holding_period,"date"]
        exit_reason="TIME"
        days_held=holding_period

        for j in range(1, holding_period+1):

            high= df.loc[i+j,"high"]
            low=df.loc[i+j,"low"]

            tp_hit= high>= take_profit_price
            sl_hit= low<= stop_loss_price

            if tp_hit and sl_hit:
                label=-1
                exit_price=stop_loss_price
                exit_date=df.loc[i+j, "date"]
                exit_reason="STOP LOSS HIT"
                days_held= j
                break
            
            elif tp_hit:
                label = 1
                exit_price=take_profit_price
                exit_date=df.loc[i+j,"date"]
                exit_reason="TAKE PROFIT HIT"
                days_held= j
                break

            elif sl_hit:
                label= -1
                exit_price=stop_loss_price
                exit_date=df.loc[i+j,"date"]
                exit_reason="STOP LOSS HIT"
                days_held =j
                break

        future_return =(exit_price-entry_price)/entry_price

        labels.append(label)
        future_returns.append(future_return)
        exit_prices.append(exit_price)
        exit_dates.append(exit_date)
        exit_reasons.append(exit_reason)
        holding_days.append(days_held)
    
    
    df["label"] = labels
    df["future_return"] = future_returns
    df["exit_price"] = exit_prices
    df["exit_date"] = exit_dates
    df["exit_reason"] = exit_reasons
    df["holding_days"] = holding_days

    df = df.dropna(subset=["label"]).reset_index(drop=True)

    df.to_csv(MODEL_DATA_PATH, index=False)

    return df