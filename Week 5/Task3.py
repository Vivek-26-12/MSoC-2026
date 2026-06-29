import pandas as pd
from Task2 import explore_data

def clean_data():
    _, df_clean = explore_data()
    df_clean = df_clean.dropna()
    categorical_cols = df_clean.select_dtypes(include=['object']).columns
    df_encoded = pd.get_dummies(df_clean, columns=categorical_cols, drop_first=True)
    return df_clean, df_encoded

if __name__ == "__main__":
    df_clean, df_encoded = clean_data()
    print("Data cleaned (missing values dropped, categorical data one-hot encoded).")
    print(f"Original shape (no duplicates): {df_clean.shape}")
    print(f"Encoded shape: {df_encoded.shape}")
    print("\nFirst 5 rows of encoded data:\n", df_encoded.head())
