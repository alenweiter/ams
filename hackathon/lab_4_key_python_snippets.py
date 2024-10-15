
# Lab 4 - Key Snippets for Spatial Autocorrelation and Network Analysis

import geopandas as gpd
import osmnx as ox
import numpy as np
import matplotlib.pyplot as plt
from pysal.explore.esda.moran import Moran
from pysal.lib import weights

# Loading a spatial dataset using GeoPandas
gdf = gpd.read_file('your_shapefile.shp')
print(gdf.head())

# Create a choropleth map of a specific variable (e.g., imd_score)
gdf.plot(column='imd_score', cmap='OrRd', legend=True)
plt.title('IMD Score Choropleth')
plt.show()

# Computing a spatial weights matrix (based on contiguity)
w = weights.contiguity.Queen.from_dataframe(gdf)
print(w)

# Standardizing a variable (IMD scores in this case)
gdf['imd_score_std'] = (gdf['imd_score'] - gdf['imd_score'].mean()) / gdf['imd_score'].std()

# Calculate spatial lag
gdf['spatial_lag'] = weights.spatial_lag.lag_spatial(w, gdf['imd_score_std'])

# Create a Moran Plot
moran = Moran(gdf['imd_score_std'], w)
plt.scatter(gdf['imd_score_std'], gdf['spatial_lag'])
plt.xlabel('Standardized IMD Score')
plt.ylabel('Spatial Lag of IMD Score')
plt.title('Moran Plot')
plt.axvline(0, color='k', linestyle='--')
plt.axhline(0, color='k', linestyle='--')
plt.show()

# Calculate Moran's I and significance level
print(f"Moran's I: {moran.I}, p-value: {moran.p_sim}")

# OSMnx: Download and visualize a street network from OpenStreetMap
G = ox.graph_from_place('Liverpool, UK', network_type='drive')
ox.plot_graph(ox.project_graph(G), figsize=(10, 10))
plt.title('Street Network of Liverpool')
plt.show()

# Saving a GeoDataFrame back to a shapefile after analysis
gdf.to_file('processed_data.shp')
