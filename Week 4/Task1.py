import pandas as pd

# 1. Create the DataFrame
data1 = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [21, 19, 22, 20],
    "City": ["Delhi", "Mumbai", "Ahmedabad", "Pune"]
}

df1 = pd.DataFrame(data1)

print("Full DataFrame:")
print(df1)

# 2. Display the first 2 rows
print("\nFirst 2 rows:")
print(df1.head(2))

# 3. Display all column names
print("\nColumn names:")
print(df1.columns)

# 4. Find the shape of the DataFrame
print("\nShape of DataFrame:")
print(df1.shape)   # (rows, columns)

# 5. Display information about the DataFrame
print("\nDataFrame info:")
print(df1.info())