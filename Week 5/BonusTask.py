import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from Task5 import get_features

def run_bonus_tasks():
    (X_train, X_test, y_train, y_test), feature_cols, price_col, df, df_encoded = get_features()
    
    print("--- Bonus 1: Compare with Decision Tree Regression ---")
    dt_model = DecisionTreeRegressor(random_state=42)
    dt_model.fit(X_train, y_train)
    y_pred_dt = dt_model.predict(X_test)
    print("Decision Tree R² Score:", r2_score(y_test, y_pred_dt))
    
    print("\n--- Bonus 2: Identify the most important features ---")
    feature_importances = pd.Series(dt_model.feature_importances_, index=feature_cols)
    print("Top 5 Features:\n", feature_importances.nlargest(5))
    
    print("\n--- Bonus 3: Perform feature scaling and compare results ---")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    lr_scaled = LinearRegression()
    lr_scaled.fit(X_train_scaled, y_train)
    print("Scaled Linear Regression R² Score:", r2_score(y_test, lr_scaled.predict(X_test_scaled)))
    
    print("\n--- Bonus 4: Try removing outliers and observe performance ---")
    Q1 = df[price_col].quantile(0.25)
    Q3 = df[price_col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df_no_outliers = df_encoded[(df_encoded[price_col] >= lower) & (df_encoded[price_col] <= upper)]
    X_no = df_no_outliers.drop(columns=[price_col])
    y_no = df_no_outliers[price_col]
    X_train_no, X_test_no, y_train_no, y_test_no = train_test_split(X_no, y_no, test_size=0.2, random_state=42)
    
    lr_no = LinearRegression()
    lr_no.fit(X_train_no, y_train_no)
    print("Linear Regression without Outliers R² Score:", r2_score(y_test_no, lr_no.predict(X_test_no)))

if __name__ == "__main__":
    run_bonus_tasks()
