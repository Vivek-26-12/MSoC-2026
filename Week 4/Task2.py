import pandas as pd

# Create the DataFrame
data2 = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [50000, 500, 1500, 12000],
    "Quantity": [5, 20, 15, 7]
}

df2 = pd.DataFrame(data2)

print("Original DataFrame:")
print(df2)

# 1. Select only the Product column
print("\nOnly Product column:")
print(df2["Product"])

# 2. Select Product and Price columns
print("\nProduct and Price columns:")
print(df2[["Product", "Price"]])

# 3. Find products with Price > 1000
print("\nProducts with Price > 1000:")
print(df2[df2["Price"] > 1000])

# 4. Find products with Quantity < 10
print("\nProducts with Quantity < 10:")
print(df2[df2["Quantity"] < 10])

# 5. Find products satisfying both conditions
# Price > 1000 AND Quantity < 10
print("\nProducts with Price > 1000 and Quantity < 10:")
print(df2[(df2["Price"] > 1000) & (df2["Quantity"] < 10)])