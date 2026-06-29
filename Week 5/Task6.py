from sklearn.linear_model import LinearRegression
from Task5 import get_features

def train_model():
    (X_train, X_test, y_train, y_test), _, _, _, _ = get_features()
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    return lr_model, X_train, X_test, y_train, y_test

if __name__ == "__main__":
    model, _, _, _, _ = train_model()
    print("Linear Regression model successfully built and trained on the training set.")
