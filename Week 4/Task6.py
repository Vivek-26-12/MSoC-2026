import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

print("--- Problem 6: GroupBy and Insights ---")

print("\n1. Survival rate by gender:")
survival_rate_by_gender = df.groupby('Sex')['Survived'].mean()
print(survival_rate_by_gender)

print("\n2. Average age by passenger class:")
avg_age_by_class = df.groupby('Pclass')['Age'].mean()
print(avg_age_by_class)

print("\n3. Number of passengers in each class:")
passengers_by_class = df.groupby('Pclass')['PassengerId'].count()
print(passengers_by_class)

print("\n4. Class with the highest survival rate:")
survival_rate_by_class = df.groupby('Pclass')['Survived'].mean()
highest_survival_class = survival_rate_by_class.idxmax()
highest_survival_rate = survival_rate_by_class.max()
print(f"Class {highest_survival_class} with a survival rate of {highest_survival_rate:.2%}")

print("\n5. Average fare paid by each class:")
avg_fare_by_class = df.groupby('Pclass')['Fare'].mean()
print(avg_fare_by_class)

print("\n6. Short Report:")
report = """
Summary of Findings from the Titanic Dataset Analysis:

- Survival and Gender: The survival rate was significantly higher for females compared to males.
- Age and Class: Passengers in 1st class tended to be older on average than those in 2nd and 3rd classes.
- Class Distribution: The majority of passengers travelled in 3rd class.
- Survival and Class: 1st class passengers had the highest survival rate, suggesting a priority in rescue efforts.
- Fare and Class: As expected, the average fare paid was highest for 1st class and lowest for 3rd class.
"""
print(report)
