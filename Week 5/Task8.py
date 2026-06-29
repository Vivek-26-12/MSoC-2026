from Task6 import train_model

def predict_sample():
    model, _, X_test, _, y_test = train_model()
    
    sample_X = X_test.iloc[[0]]
    sample_y = y_test.iloc[0]
    sample_pred = model.predict(sample_X)[0]
    
    print(f"Sample Features:\n{sample_X.to_dict('records')[0]}")
    print(f"\nActual Selling Price: {sample_y}")
    print(f"Predicted Selling Price: {sample_pred}")

if __name__ == "__main__":
    predict_sample()
