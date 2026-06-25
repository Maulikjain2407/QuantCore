import pandas as pd

from configs.config import FEATURE_ENGINEER_PATH, CLEAN_FILE_PATH


def create_feature():

    df=pd.read_csv(CLEAN_FILE_PATH)

    # Returns 1 day, 5 days, 10 days , 20 days
    df["ret_1d"]=df["close"].pct_change(1)
    df["ret_5d"]=df["close"].pct_change(5)
    df["ret_10d"]=df["close"].pct_change(10)
    df["ret_20d"]=df["close"].pct_change(20)

    # volatility

    df["volatility_5d"]= df["ret_1d"].rolling(5).std()
    df["volatility_20d"]= df["ret_1d"].rolling(20).std()

    #close/sma ratio

    sma_10=df["close"].rolling(10).mean()
    sma_20=df["close"].rolling(20).mean()

    df["close_sma10_ratio"]=df["close"]/sma_10
    df["close_sma20_ratio"]=df["close"]/sma_20

    #volume ratio

    avg_vol_20= df["volume"].rolling(20).mean()
    df["volume_ratio"]=df["volume"]/avg_vol_20

    #daily range ratio

    df["range_ratio"]=(df["high"]-df["low"])/df["close"]

    # dropping NAN values as initially the vlaues such as return of day 20 will not be there due to the reason that the dataset has just started hencewe drop the NAN 
    df=df.dropna()

    df.to_csv(FEATURE_ENGINEER_PATH, index=False)

    return df