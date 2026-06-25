from sklearn.ensemble import RandomForestClassifier

from configs.config import N_JOBS,N_ESTIMATORS,RANDOM_STATE

def train_model(x_train,y_train):
    
    model=RandomForestClassifier(
        n_estimators=N_ESTIMATORS,
        n_jobs=N_JOBS,
        random_state=RANDOM_STATE
    )

    model.fit(x_train,y_train)

    return model