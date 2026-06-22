import kagglehub
import pandas as pd
import os

path = kagglehub.dataset_download("yasserh/titanic-dataset")
print("Path to dataset files:", path)

files_in_directory = os.listdir(path)

csv_file = None
for file in files_in_directory:
    if file.endswith(".csv"):
        csv_file = file
        break

if csv_file:
    full_csv_path = os.path.join(path, csv_file)
    df = pd.read_csv(full_csv_path)
else:
    print("No CSV file found.")
    df = None

print("\nDataset loaded successfully!")

print("\nFirst 10 rows:")
print(df.head(10))

print("\nShape of dataset:")
print(df.shape)

rows, cols = df.shape
print("Number of rows:", rows)
print("Number of columns:", cols)

print("\nColumn names:")
print(df.columns)

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nSummary statistics:")
print(df.describe(include="all"))