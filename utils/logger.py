from pathlib import Path
from datetime import datetime
import json

import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from configs.config import EXPERIMENT_LOG_PATH


RUN_PATH = EXPERIMENT_LOG_PATH/datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
RUN_PATH.mkdir(parents=True, exist_ok=True)


def log(message):
    print(f"[INFO] {message}")


def save(obj, name):
    path = RUN_PATH / name

    if isinstance(obj, pd.DataFrame):
        obj.to_csv(path.with_suffix(".csv"), index=False)

    elif isinstance(obj, dict):
        with open(path.with_suffix(".json"), "w") as f:
            json.dump(obj, f, indent=4)

    elif isinstance(obj, np.ndarray):
        np.save(path.with_suffix(".npy"), obj)

    elif isinstance(obj, Figure):
        obj.savefig(path.with_suffix(".png"), dpi=300, bbox_inches="tight")
        plt.close(obj)

    else:
        joblib.dump(obj, path.with_suffix(".pkl"))


def get_run_path():
    return RUN_PATH