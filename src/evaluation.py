from sklearn.metrics import f1_score, accuracy_score,confusion_matrix

def eval_model(model,x_test,y_test):
    y_pred=model.predict(x_test)

    results={
        "Accuracy": accuracy_score(y_test,y_pred),
        "F1_score": f1_score(y_test,y_pred),
        "Confusion_Matrix": confusion_matrix(y_test,y_pred)
    }

    return results,y_pred