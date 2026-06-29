import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from Task3 import clean_data

def visualize_data():
    df, _ = clean_data()
    cols_lower = {c.lower(): c for c in df.columns}
    price_col = cols_lower.get('price', df.columns[-1])
    mileage_col = cols_lower.get('mileage', None)
    year_col = cols_lower.get('year', None)
    fuel_col = cols_lower.get('fuel_type', cols_lower.get('fuel', None))
    
    # 1. Histogram
    plt.figure(figsize=(8, 5))
    plt.hist(df[price_col], bins=30, edgecolor='black')
    plt.title('Histogram of Car Prices')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()
    
    # 2. Scatter plot Mileage vs Price
    if mileage_col:
        plt.figure(figsize=(8, 5))
        plt.scatter(df[mileage_col], df[price_col], alpha=0.5)
        plt.title(f'{mileage_col} vs Price')
        plt.xlabel(mileage_col)
        plt.ylabel('Price')
        plt.show()
        
    # 3. Scatter plot Year vs Price
    if year_col:
        plt.figure(figsize=(8, 5))
        plt.scatter(df[year_col], df[price_col], alpha=0.5)
        plt.title(f'{year_col} vs Price')
        plt.xlabel(year_col)
        plt.ylabel('Price')
        plt.show()
        
    # 4. Bar chart of fuel types
    if fuel_col:
        plt.figure(figsize=(8, 5))
        df[fuel_col].value_counts().plot(kind='bar', edgecolor='black')
        plt.title(f'Bar Chart of {fuel_col}')
        plt.xlabel(fuel_col)
        plt.ylabel('Count')
        plt.show()
        
    # 5. Correlation heatmap
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.show()
    
    # 6. Box plot for outliers
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[price_col])
    plt.title('Box plot of Car Prices')
    plt.show()

if __name__ == "__main__":
    visualize_data()
