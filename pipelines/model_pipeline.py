from src.data_loader import get_data
from src.data_cleaner import clean_data
from feature_engineer.feature_engineering_V2 import create_feature
from label_creator.triple_barrier_labeling import create_triple_barrier_label
from src.test_train_split import test_train_split
from configs.config import STOP_LOSS_MULTIPLIER,TAKE_PROFIT_MULTIPLER,HOLDING_PERIOD

from models.model import train_model
from utils.model_io import save_model

def run_train_pipeline():

    get_data()
    clean_data()
    create_feature()
    create_triple_barrier_label(holding_period=HOLDING_PERIOD,take_profit_multiplier=TAKE_PROFIT_MULTIPLER,stop_loss_multiplier=STOP_LOSS_MULTIPLIER)
    x_train,y_train,x_test,y_test,test_df=test_train_split()
    
    model=train_model(x_train=x_train,y_train=y_train)

    save_model(model=model)


if __name__=="__main__":
    run_train_pipeline()