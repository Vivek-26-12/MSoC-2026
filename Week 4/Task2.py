import pandas as pd

data2 = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [50000, 500, 1500, 12000],
    "Quantity": [5, 20, 15, 7]
}

df2 = pd.DataFrame(data2)

print("Original DataFrame:")
print(df2)

print("\nOnly Product column:")
print(df2["Product"])

print("\nProduct and Price columns:")
print(df2[["Product", "Price"]])

print("\nProducts with Price > 1000:")
print(df2[df2["Price"] > 1000])

print("\nProducts with Quantity < 10:")
print(df2[df2["Quantity"] < 10])

print("\nProducts with Price > 1000 and Quantity < 10:")
print(df2[(df2["Price"] > 1000) & (df2["Quantity"] < 10)])