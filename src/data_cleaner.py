import pandas as pd

from configs.config import FILE_PATH,CLEAN_FILE_PATH

def clean_data():
    
    if CLEAN_FILE_PATH.exists():
        return pd.read_csv(CLEAN_FILE_PATH)
    else:
        
        df=pd.read_csv(FILE_PATH)

        for col in df:
            df.columns = df.columns.str.lower()

        df=df.drop_duplicates()
        df["date"]=pd.to_datetime(df["date"])
        df= df.sort_values("date")
        df=df.dropna()
        df.to_csv(CLEAN_FILE_PATH,index=False)

        return df