import pandas as pd

data3 = {
    "Student": ["A", "B", "C", "D"],
    "Maths": [85, 70, 95, 60],
    "Science": [90, 65, 88, 75]
}

df3 = pd.DataFrame(data3)

print("Original DataFrame:")
print(df3)

df3["Total"] = df3["Maths"] + df3["Science"]

df3["Average"] = df3["Total"] / 2

print("\nDataFrame after adding Total and Average:")
print(df3)

highest_total_student = df3.loc[df3["Total"].idxmax()]
print("\nStudent with highest Total:")
print(highest_total_student)

sorted_df3 = df3.sort_values(by="Average", ascending=False)
print("\nSorted by Average (descending):")
print(sorted_df3)

print("\nStudents with Average > 80:")
print(df3[df3["Average"] > 80])