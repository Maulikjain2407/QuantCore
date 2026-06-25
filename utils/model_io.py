import joblib as jb
from configs.config import MODEL_PATH

def save_model(model):
    
    jb.dump(model,MODEL_PATH)

def load_model():
    return jb.load(MODEL_PATH)