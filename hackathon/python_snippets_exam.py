
# Combined Key Python Snippets for Exam Preparation

## 1. Basic Python Operations and Control Flow
# Importing essential libraries
import numpy as np
from scipy import stats
from collections import defaultdict

# Example of control flow using a 'for' loop
for i in range(5):
    print(f"Iteration {i}")

# Example of a basic 'if' statement
x = 10
if x > 5:
    print(f"{x} is greater than 5")

# Working with lists and dictionaries
my_list = [1, 2, 3, 4]
my_list.append(5)
print(my_list[2])
sliced_list = my_list[1:4]
print(sliced_list)

my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key1'])
my_dict['key3'] = 'value3'
del my_dict['key2']

# NumPy operations
arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])
dot_product = np.dot(vector_a, vector_b)
print(dot_product)

# Defining functions
def my_function(x):
    return x ** 2

print(my_function(4))

square = lambda x: x ** 2
print(square(4))

# SciPy statistical functions
data = [1, 2, 2, 3, 4]
mode = stats.mode(data)
print(f"Mode of the data: {mode.mode[0]}")

# defaultdict usage
my_default_dict = defaultdict(int)
my_default_dict['key'] += 1
print(my_default_dict['key'])


## 2. Data Handling and Manipulation with Pandas
import pandas as pd
import matplotlib.pyplot as plt

# Loading and displaying a dataset
data = pd.read_csv('your_data_file.csv')
print(data.head())

# Slicing and transforming data
sliced_data = data[['column1', 'column2']]
data['new_column'] = data['existing_column'].apply(lambda x: x * 2)
print(sliced_data.head())

# Grouping and aggregating data
grouped_data = data.groupby('column_to_group_by').agg({'column_to_aggregate': 'sum'})
print(grouped_data)

# Handling missing data
data.fillna(0, inplace=True)
data.dropna(inplace=True)

# Saving cleaned data
data.to_csv('cleaned_data.csv', index=False)


## 3. Data Engineering and Merging DataFrames with Pandas
# Creating and manipulating DataFrames
df = pd.DataFrame({'column1': [1, 2, 3], 'column2': [4, 5, 6]})
print(df)

# Indexing and conditional selection
print(df.iloc[0, 1])
print(df.loc[0, 'column2'])
filtered_df = df[df['column1'] > 2]
print(filtered_df)

# Combining datasets (merge and concatenate)
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df_combined = pd.concat([df1, df2], ignore_index=True)
print(df_combined)

merged_df = pd.merge(df1, df2, on='A')
print(merged_df)

df.to_csv('cleaned_data.csv', index=False)


## 4. Spatial Data and Autocorrelation with Geopandas and PySAL
import geopandas as gpd
from pysal.explore.esda.moran import Moran
from pysal.lib import weights

# Loading and plotting spatial data
gdf = gpd.read_file('your_shapefile.shp')
gdf.plot(column='imd_score', cmap='OrRd', legend=True)
plt.title('IMD Score Choropleth')
plt.show()

# Computing spatial weights matrix
w = weights.contiguity.Queen.from_dataframe(gdf)
gdf['imd_score_std'] = (gdf['imd_score'] - gdf['imd_score'].mean()) / gdf['imd_score'].std()
gdf['spatial_lag'] = weights.spatial_lag.lag_spatial(w, gdf['imd_score_std'])

# Moran Plot and Moran's I calculation
moran = Moran(gdf['imd_score_std'], w)
plt.scatter(gdf['imd_score_std'], gdf['spatial_lag'])
plt.axvline(0, color='k', linestyle='--')
plt.axhline(0, color='k', linestyle='--')
plt.show()
print(f"Moran's I: {moran.I}, p-value: {moran.p_sim}")


## 5. OSMnx and Network Analysis
import osmnx as ox

# Download and visualize street networks
G = ox.graph_from_place('Liverpool, UK', network_type='drive')
ox.plot_graph(ox.project_graph(G), figsize=(10, 10))

# Simplifying and saving street networks
G_simplified = ox.simplify_graph(G)
ox.save_graph_shapefile(G_simplified, filepath='simplified_network')

# Calculating basic network metrics
stats = ox.basic_stats(G_simplified)
print(stats)


## 6. Regression and Predictive Modeling
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Loading and preparing data
df = pd.read_csv('housing_data.csv', delim_whitespace=True)
X = df.drop('MEDV', axis=1)
y = df['MEDV']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred = lin_reg.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")
print(f"R^2 Score: {r2_score(y_test, y_pred)}")

# K-NN Regression
knn_reg = KNeighborsRegressor(n_neighbors=5)
knn_reg.fit(X_train, y_train)
y_pred_knn = knn_reg.predict(X_test)
print(f"Mean Squared Error (K-NN): {mean_squared_error(y_test, y_pred_knn)}")
print(f"R^2 Score (K-NN): {r2_score(y_test, y_pred_knn)}")
