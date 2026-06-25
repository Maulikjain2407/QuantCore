from pathlib import Path
from utils.config_loader import load_config

configs=load_config()

BASE_PATH=Path(__file__).resolve().parent.parent
DATA_PATH=BASE_PATH/configs["path"]["data_dir"]
RAW_PATH=DATA_PATH/configs["path"]["raw_data"]
PROCESSED_PATH=DATA_PATH/configs["path"]["processed_data"]
ARTIFACT_DIR=BASE_PATH/configs["path"]["artifacts_dir"]
EXPERIMENT_LOG_PATH=ARTIFACT_DIR/configs["path"]["experiment_logs"]
SAVED_MODEL_PATH=ARTIFACT_DIR/configs["path"]["saved_models"]
MODEL_PATH=SAVED_MODEL_PATH/"random_forest.pkl"


N_JOBS=configs["model"]["random_forests"]["n_jobs"]
RANDOM_STATE=configs["model"]["random_forests"]["random_state"]
N_ESTIMATORS=configs["model"]["random_forests"]["n_estimators"]


TICKER=configs["data"]["tickers"]
START=configs["data"]["start"]
END=configs["data"]["end"]

FILE_PATH= RAW_PATH/f"{TICKER}.csv"
CLEAN_FILE_PATH= PROCESSED_PATH/f"{TICKER}_CLEANED.csv"
FEATURE_ENGINEER_PATH= PROCESSED_PATH/f"{TICKER}_featured.csv"
MODEL_DATA_PATH= PROCESSED_PATH/f"{TICKER}_MODEL_DATA.CSV"

HOLDING_PERIOD=configs["metrics"]["holding_period"]

print(ARTIFACT_DIR)
