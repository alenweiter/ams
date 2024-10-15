
# Useful Snippets for Exam Preparation

### 1. Plotting a Moran's I Scatterplot (Spatial Autocorrelation)
from pysal.explore.esda.moran import Moran
import matplotlib.pyplot as plt
from pysal.viz.splot.esda import moran_scatterplot

# Function to plot Moran's I
def plot_moran(w, y):
    moran = Moran(y, w)
    fig, ax = moran_scatterplot(moran)
    plt.savefig("moran_plot.png")  # Save the plot
    return moran.I, moran.p_sim

attribute_data = gdf['Lower'].to_numpy()

# Generate the plot
moran_i, moran_p = plot_moran(distance_weights, attribute_data)

print("Moran's I:", moran_i)
print("P-value:", moran_p)


### 2. Simple Linear Regression with scikit-learn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load data
X = df[['Feature1', 'Feature2']]  # Features
y = df['Target']  # Target variable

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)


### 3. Loading and Plotting Spatial Data with GeoPandas
import geopandas as gpd
import matplotlib.pyplot as plt

# Load spatial data
gdf = gpd.read_file('path_to_shapefile.shp')

# Plot the spatial data
gdf.plot()
plt.title('Spatial Data Plot')
plt.show()


### 4. K-Nearest Neighbors Regression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

# Initialize and train the K-NN model
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train, y_train)

# Predict and evaluate the model
y_pred_knn = knn.predict(X_test)
print("R^2 Score (K-NN):", r2_score(y_test, y_pred_knn))
