import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter

def load_data():
    try:
        return kagglehub.load_dataset(KaggleDatasetAdapter.PANDAS, "bhavikjikadara/car-price-prediction-dataset", "")
    except Exception:
        return pd.read_csv("car_price_dataset.csv")

if __name__ == "__main__":
    df = load_data()
    print("First 5 rows:\n", df.head())
    print("\nLast 5 rows:\n", df.tail())
    print("\nShape of the dataset:", df.shape)
    print("\nColumn names:", df.columns.tolist())
    print("\nData types:\n", df.dtypes)
