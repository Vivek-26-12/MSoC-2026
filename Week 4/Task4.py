import kagglehub
import pandas as pd
import os

# Download dataset
path = kagglehub.dataset_download("yasserh/titanic-dataset")
print("Path to dataset files:", path)

# Find CSV file
files_in_directory = os.listdir(path)

csv_file = None
for file in files_in_directory:
    if file.endswith(".csv"):
        csv_file = file
        break

# Load dataset
if csv_file:
    full_csv_path = os.path.join(path, csv_file)
    df = pd.read_csv(full_csv_path)
else:
    print("No CSV file found.")
    df = None

# 1. Load the dataset using Pandas
print("\nDataset loaded successfully!")

# 2. Display the first 10 rows
print("\nFirst 10 rows:")
print(df.head(10))

# 3. Find the number of rows and columns
print("\nShape of dataset:")
print(df.shape)

rows, cols = df.shape
print("Number of rows:", rows)
print("Number of columns:", cols)

# 4. Display all column names
print("\nColumn names:")
print(df.columns)

# 5. Check missing values in each column
print("\nMissing values in each column:")
print(df.isnull().sum())

# 6. Generate summary statistics
print("\nSummary statistics:")
print(df.describe(include="all"))