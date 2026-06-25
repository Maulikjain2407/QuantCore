import yfinance as yf
import pandas as pd

from configs.config import RAW_PATH,TICKER,START,END,FILE_PATH

def get_data():
    if FILE_PATH.exists():
        return pd.read_csv(FILE_PATH)
    else:
        data=yf.download(tickers=TICKER,start=START, end=END)

        if isinstance(data.columns, pd.MultiIndex):
            data.columns= data.columns.get_level_values(0)

        data.reset_index(inplace=True)
        data.to_csv(FILE_PATH, index=False)
        return data