import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

print("--- Problem 5: Filtering and Analysis ---")

print("\n1. All female passengers:")
female_passengers = df[df['Sex'] == 'female']
print(f"Number of female passengers: {len(female_passengers)}")
print(female_passengers.head())

print("\n2. Passengers older than 30 years:")
older_than_30 = df[df['Age'] > 30]
print(f"Number of passengers older than 30: {len(older_than_30)}")
print(older_than_30.head())

print("\n3. Passengers who survived:")
survivors = df[df['Survived'] == 1]
print(f"Number of survivors: {len(survivors)}")
print(survivors.head())

print("\n4. Female passengers who survived:")
female_survivors = df[(df['Sex'] == 'female') & (df['Survived'] == 1)]
print(f"Number of female survivors: {len(female_survivors)}")
print(female_survivors.head())

print("\n5. Average age of passengers:")
average_age = df['Age'].mean()
print(f"{average_age:.2f} years")

print("\n6. Oldest passenger:")
oldest_idx = df['Age'].idxmax()
oldest_passenger = df.loc[oldest_idx]
print(oldest_passenger)
