
# Lab 5 - Key Snippets for Regression and Predictive Modeling

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv('housing_data.csv', delim_whitespace=True)
print(df.head())

# Split data into training and test sets
X = df.drop('MEDV', axis=1)  # Features
y = df['MEDV']  # Target variable (Median value of homes)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Simple Linear Regression
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# Predictions and evaluation
y_pred = lin_reg.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")
print(f"R^2 Score: {r2_score(y_test, y_pred)}")

# Plotting the predicted vs actual values
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Predicted vs Actual Values (Linear Regression)')
plt.show()

# K-Nearest Neighbors Regression (K-NN)
knn_reg = KNeighborsRegressor(n_neighbors=5)
knn_reg.fit(X_train, y_train)

# Predictions and evaluation
y_pred_knn = knn_reg.predict(X_test)
print(f"Mean Squared Error (K-NN): {mean_squared_error(y_test, y_pred_knn)}")
print(f"R^2 Score (K-NN): {r2_score(y_test, y_pred_knn)}")

# Plotting the predicted vs actual values for K-NN
plt.scatter(y_test, y_pred_knn)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Predicted vs Actual Values (K-NN Regression)')
plt.show()

# Saving the model results to a CSV
results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
results.to_csv('regression_results.csv', index=False)
