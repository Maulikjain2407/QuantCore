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

    
