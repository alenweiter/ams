
# Lab 2 - Visualization Snippets

import pandas as pd
import matplotlib.pyplot as plt

# Creating a histogram
data['column'].hist(bins=20)
plt.title('Histogram of Column')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Kernel density plot
data['column'].plot(kind='kde')
plt.title('Kernel Density Plot')
plt.xlabel('Value')
plt.show()

# Creating line and bar plots
data.plot(x='x_column', y='y_column', kind='line')  # Line plot
plt.title('Line Plot')
plt.show()

data.plot(x='x_column', y='y_column', kind='bar')  # Bar plot
plt.title('Bar Plot')
plt.show()

# Lab 4 - Visualization Snippets (Spatial and Network Analysis)

import geopandas as gpd
import osmnx as ox
import matplotlib.pyplot as plt

# Create a choropleth map of a specific variable (e.g., imd_score)
gdf.plot(column='imd_score', cmap='OrRd', legend=True)
plt.title('IMD Score Choropleth')
plt.show()

# Create a Moran Plot
plt.scatter(gdf['imd_score_std'], gdf['spatial_lag'])
plt.xlabel('Standardized IMD Score')
plt.ylabel('Spatial Lag of IMD Score')
plt.title('Moran Plot')
plt.axvline(0, color='k', linestyle='--')
plt.axhline(0, color='k', linestyle='--')
plt.show()

# OSMnx: Download and visualize a street network from OpenStreetMap
G = ox.graph_from_place('Liverpool, UK', network_type='drive')
ox.plot_graph(ox.project_graph(G), figsize=(10, 10))
plt.title('Street Network of Liverpool')
plt.show()

# Lab 5 - Visualization Snippets (Predictive Modeling)

import matplotlib.pyplot as plt

# Plotting the predicted vs actual values (Linear Regression)
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Predicted vs Actual Values (Linear Regression)')
plt.show()

# Plotting the predicted vs actual values for K-NN
plt.scatter(y_test, y_pred_knn)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Predicted vs Actual Values (K-NN Regression)')
plt.show()

# Lab 6 - Visualization Snippets (Geopandas and OSMnx Networks)

import geopandas as gpd
import matplotlib.pyplot as plt
import osmnx as ox

# Plotting with Geopandas
gdf_countries.plot()
plt.title('Country Boundaries')
plt.show()

# OSMnx: Download and visualize a street network
G = ox.graph_from_place('Liverpool, UK', network_type='drive')
ox.plot_graph(ox.project_graph(G), figsize=(10, 10))
plt.title('Street Network of Liverpool')
plt.show()

# Get a street network using bounding box
G_bbox = ox.graph_from_bbox(north, south, east, west, network_type='drive')
ox.plot_graph(G_bbox, figsize=(10, 10))

