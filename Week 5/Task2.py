from Task1 import load_data

def explore_data():
    df = load_data()
    df_clean = df.drop_duplicates()
    return df, df_clean

if __name__ == "__main__":
    df, df_clean = explore_data()
    print("--- Explore the Dataset ---")
    df.info()
    print("\nDescribe:\n", df.describe())
    print("\nMissing values:\n", df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())
    print(f"\nRemoved duplicates. New shape: {df_clean.shape}")
