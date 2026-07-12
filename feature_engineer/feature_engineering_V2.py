import pandas as pd
import numpy as np
from configs.config import FEATURE_ENGINEER_PATH, CLEAN_FILE_PATH


def create_feature():

    df=pd.read_csv(CLEAN_FILE_PATH)

    #Returns 5 Day,10 Day, log

    df["ret_5"]=df["close"].pct_change(5)
    df["ret_10"]=df["close"].pct_change(10) 
    df["ret_log"]=np.log(df["close"]/df["close"].shift(1))


    #SMA 5 Day, 10 Day

    df["sma_5"]=df["close"].rolling(5).mean()
    df["sma_10"]=df["close"].rolling(10).mean()
   

   #EMA 5 Day, 9 Day, 10 Day, 12 Day, 26 Day

    df["ema_5"]=df["close"].ewm(span=5, adjust= False).mean()
    df["ema_9"]=df["close"].ewm(span=9, adjust= False).mean()
    df["ema_10"]=df["close"].ewm(span=10, adjust= False).mean()
    df["ema_12"]=df["close"].ewm(span=12, adjust= False).mean()
    df["ema_26"]=df["close"].ewm(span=26, adjust= False).mean()


    # Distance from SMA, EMA

    df["dist_from_SMA_5"]=(df["close"]-df["sma_5"])/df["sma_5"]
    df["dist_from_SMA_10"]=(df["close"]-df["sma_10"])/df["sma_10"]
    df["dist_from_EMA_5"]=(df["close"]-df["ema_5"])/df["ema_5"]
    df["dist_from_EMA_10"]=(df["close"]-df["ema_10"])/df["ema_10"]


    #MACD & MACD Signal
    df["MACD"]= df["ema_12"]-df["ema_26"]
    df["MACD_Signal"]= df["MACD"].ewn(span=9,adjust=False).mean()

    
    #Rolling STD

    df["rolling_STD"]=df["close"].rolling(1).std()


    #Volatility

    #Historical

    df["historical_volatility"]= df["ret_log"].rolling(20).std * np.sqrt(252)
    
    #Realised

    df["realised_volatility"] = np.sqrt((df["ret_log"] ** 2).rolling(window=20).sum())

    #Volume change

    df["vol_change"]=df["volumne"].pct_change()


    #RSI

    delta=df["close"].diff()

    gain=delta.clip(lower=0)
    loss=-delta.clip(upper=0)

    avg_gain=gain.ewp(alpha=1/14, adjust=False).mean()
    avg_loss=loss.ewp(alpha=1/14, adjust=False).mean()

    rs=avg_gain/avg_loss

    df["rsi"]=100-(100/(1+rs))

    #ATR% 

    TR1=df["high"]-df["low"]
    TR2=(df["high"]-df["close"].shift(1)).abs()
    TR3=(df["low"]-df["close"].shift(1)).abs()

    TR = pd.concat([TR1, TR2, TR3], axis=1).max(axis=1)
    
    ATR=TR.ewm(alpha=1/14,adjust=False).mean()

    df["atr%"]=ATR/df["close"]

    #Body size

    df["body_size"]=(df["close"]-df["open"]).abs()

    # Upper wick and Lower wick
    
    df["upper_wick"] = df["high"] - df[["open", "close"]].max(axis=1)
    df["lower_wick"] = df[["open", "close"]].min(axis=1) - df["low"]

    df=df.dropna()

    df.to_csv(FEATURE_ENGINEER_PATH, index=False)

    return df