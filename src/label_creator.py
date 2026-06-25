from configs.config import MODEL_DATA_PATH , FEATURE_ENGINEER_PATH
import pandas as pd

def create_label():
    
    df= pd.read_csv(FEATURE_ENGINEER_PATH)

    df["future_returns"]=((df["close"].shift(-5))/df["close"])-1

    df = df.dropna(subset=["future_returns"])

    df["target"]= (df["future_returns"]> 0.01).astype(int)
    df.to_csv(MODEL_DATA_PATH,index=False)

create_label()