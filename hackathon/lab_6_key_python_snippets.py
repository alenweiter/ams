
# Lab 6 - Key Snippets for Geopandas and OSMnx Networks

import geopandas as gpd
import matplotlib.pyplot as plt
import osmnx as ox

# Geopandas: Load spatial datasets (e.g., shapefiles)
gdf_countries = gpd.read_file("path_to_countries.shp")
print(gdf_countries.head())

# Plotting with Geopandas
gdf_countries.plot()
plt.title('Country Boundaries')
plt.show()

# Coordinate Reference Systems (CRS): Reprojecting data
gdf_countries = gdf_countries.to_crs("EPSG:4326")  # Reproject to WGS84
print(gdf_countries.crs)

# OSMnx: Download and visualize a street network
G = ox.graph_from_place('Liverpool, UK', network_type='drive')
ox.plot_graph(ox.project_graph(G), figsize=(10, 10))
plt.title('Street Network of Liverpool')
plt.show()

# Get a street network using bounding box
north, south, east, west = 53.4, 53.2, -2.9, -3.0  # Example coordinates
G_bbox = ox.graph_from_bbox(north, south, east, west, network_type='drive')
ox.plot_graph(G_bbox, figsize=(10, 10))

# Simplify and save street networks
G_simplified = ox.simplify_graph(G_bbox)
ox.save_graph_shapefile(G_simplified, filepath='simplified_network')

# Calculate basic network metrics
stats = ox.basic_stats(G_simplified)
print(stats)

# Saving GeoDataFrame to file
gdf_countries.to_file('processed_countries.shp')
