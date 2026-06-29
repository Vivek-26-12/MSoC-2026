import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from Task6 import train_model

def evaluate():
    model, _, X_test, _, y_test = train_model()
    y_pred = model.predict(X_test)
    
    print("--- Model Evaluation Metrics ---")
    print("MAE (Mean Absolute Error):", mean_absolute_error(y_test, y_pred))
    print("MSE (Mean Squared Error):", mean_squared_error(y_test, y_pred))
    print("RMSE (Root Mean Squared Error):", np.sqrt(mean_squared_error(y_test, y_pred)))
    print("R² Score:", r2_score(y_test, y_pred))

if __name__ == "__main__":
    evaluate()
