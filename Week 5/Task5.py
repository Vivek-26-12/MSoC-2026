from sklearn.model_selection import train_test_split
from Task3 import clean_data

def get_features():
    df, df_encoded = clean_data()
    cols_lower = {c.lower(): c for c in df.columns}
    price_col = cols_lower.get('price', df.columns[-1])
    
    X = df_encoded.drop(columns=[price_col])
    y = df_encoded[price_col]
    
    return train_test_split(X, y, test_size=0.2, random_state=42), X.columns, price_col, df, df_encoded

if __name__ == "__main__":
    (X_train, X_test, y_train, y_test), _, _, _, _ = get_features()
    print("Features selected and split into train/test sets.")
    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape: {X_test.shape}")
    print(f"y_train shape: {y_train.shape}")
    print(f"y_test shape: {y_test.shape}")
