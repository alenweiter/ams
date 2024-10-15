
# Lab 2 - Key Data Handling and Visualization Snippets

import pandas as pd
import matplotlib.pyplot as plt

# Loading a dataset
data = pd.read_csv('your_data_file.csv')

# Displaying the first few rows of a DataFrame
print(data.head())

# Slicing a DataFrame
sliced_data = data[['column1', 'column2']]  # Selecting specific columns
print(sliced_data.head())

# Grouping data and applying aggregations
grouped_data = data.groupby('column_to_group_by').agg({'column_to_aggregate': 'sum'})
print(grouped_data)

# Transforming data - applying a function to columns
data['new_column'] = data['existing_column'].apply(lambda x: x * 2)
print(data.head())

# Pivot tables (tidy data transformation)
pivot_table = data.pivot_table(values='column_to_aggregate', index='column_index', columns='column_to_pivot')
print(pivot_table)

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

# Handling missing data
data.fillna(0, inplace=True)  # Replace missing values with 0
data.dropna(inplace=True)     # Drop rows with missing values

# Saving the cleaned data
data.to_csv('cleaned_data.csv', index=False)

