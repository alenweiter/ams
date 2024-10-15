
# Lab 3 - Key Data Engineering Snippets with Pandas

import pandas as pd

# Creating a DataFrame
data = {'column1': [1, 2, 3], 'column2': [4, 5, 6]}
df = pd.DataFrame(data)
print(df)

# Reading a CSV file into a DataFrame
df = pd.read_csv('your_data_file.csv')
print(df.head())

# Indexing data: iloc (index-based) and loc (label-based)
# iloc example
print(df.iloc[0, 1])  # Access the first row, second column
# loc example
print(df.loc[0, 'column2'])  # Access the first row, column2 by label

# Conditional selection
filtered_df = df[df['column1'] > 2]
print(filtered_df)

# Groupwise analysis with groupby
grouped_data = df.groupby('column_to_group_by').agg({'column_to_aggregate': 'sum'})
print(grouped_data)

# Handling multi-indexes
df_multi = df.set_index(['column1', 'column2'])
print(df_multi)

# Sorting data
df_sorted = df.sort_values(by='column_to_sort')
print(df_sorted)

# Handling missing data
df.fillna(0, inplace=True)  # Fill missing values with 0
df.dropna(inplace=True)     # Drop rows with missing values

# Combining datasets: Merge and concatenate
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df_combined = pd.concat([df1, df2], ignore_index=True)
print(df_combined)

# Merge two datasets based on a common column
merged_df = pd.merge(df1, df2, on='A')
print(merged_df)

# Saving cleaned data to a CSV
df.to_csv('cleaned_data.csv', index=False)
