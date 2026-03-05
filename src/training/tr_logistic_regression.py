from src.models.logistic_regression import build_logistic_regression

def train_logistic_regression(X_train, y_train):
    model = build_logistic_regression()
    model.fit(X_train, y_train)
    return model
