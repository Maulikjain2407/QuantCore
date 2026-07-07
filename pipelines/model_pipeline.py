from src.data_loader import get_data
from src.data_cleaner import clean_data
from src.feature_engineering import create_feature
from src.label_creator import create_label
from src.test_train_split import test_train_split

from models.model import train_model
from utils.model_io import save_model

def run_train_pipeline():

    get_data()
    clean_data()
    create_feature()
    create_label()
    x_train,y_train,x_test,y_test,test_df=test_train_split()
    
    model=train_model(x_train=x_train,y_train=y_train)

    save_model(model=model)


if __name__=="__main__":
    run_train_pipeline()