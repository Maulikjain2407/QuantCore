from configs.config import MODEL_DATA_PATH
import pandas as pd

def test_train_split():

    df=pd.read_csv(MODEL_DATA_PATH)

    split_idx=int(len(df)*0.8)

    train_df=df.iloc[:split_idx]
    test_df=df.iloc[split_idx:]

    x_train=train_df.drop(columns=["target","date","future_returns"])
    y_train=train_df["target"]

    x_test=test_df.drop(columns=["target","date","future_returns"])
    y_test=test_df["target"]

    return x_train,y_train,x_test,y_test,test_df