import pandas as pd

data1 = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [21, 19, 22, 20],
    "City": ["Delhi", "Mumbai", "Ahmedabad", "Pune"]
}

df1 = pd.DataFrame(data1)

print("Full DataFrame:")
print(df1)

print("\nFirst 2 rows:")
print(df1.head(2))

print("\nColumn names:")
print(df1.columns)

print("\nShape of DataFrame:")
print(df1.shape)

print("\nDataFrame info:")
print(df1.info())