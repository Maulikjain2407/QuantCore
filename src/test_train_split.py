from configs.config import MODEL_DATA_PATH
import pandas as pd

def test_train_split():

    df=pd.read_csv(MODEL_DATA_PATH)

    split_idx=int(len(df)*0.8)

    train_df=df.iloc[:split_idx]
    test_df=df.iloc[split_idx:]

    x_train=train_df.drop(columns=["label","date","future_returns","exit_price","exit_date","exit_reason"])
    y_train=train_df["label"]

    x_test=test_df.drop(columns=["label","date","future_returns","exit_price","exit_date","exit_reason"])
    y_test=test_df["label"]

    return x_train,y_train,x_test,y_test,test_df