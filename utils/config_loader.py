from pathlib import Path
import yaml

def load_config():
    with open("configs/configs.yaml", "r") as f:
        return yaml.safe_load(f)