
# Lab 1 - Key Python Snippets for Quick Reference

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

# Working with lists
my_list = [1, 2, 3, 4]
my_list.append(5)  # Appending an element
print(my_list[2])  # Accessing the third element (index 2)

# Slicing a list
sliced_list = my_list[1:4]  # Slicing from index 1 to 3 (excludes 4)
print(sliced_list)

# Working with dictionaries
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key1'])  # Accessing a value using its key

# Adding and deleting entries in a dictionary
my_dict['key3'] = 'value3'  # Adding a new key-value pair
del my_dict['key2']  # Deleting a key-value pair

# Creating and using NumPy arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)  # Element-wise multiplication

# Using numpy to perform vector operations
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])
dot_product = np.dot(vector_a, vector_b)  # Dot product of two vectors
print(dot_product)

# Example of defining and using a simple function
def my_function(x):
    return x ** 2

print(my_function(4))  # Output: 16

# Lambda function for quick operations
square = lambda x: x ** 2
print(square(4))  # Output: 16

# Scipy - example of using a statistical function from scipy
data = [1, 2, 2, 3, 4]
mode = stats.mode(data)
print(f"Mode of the data: {mode.mode[0]}")

# Using defaultdict from collections
my_default_dict = defaultdict(int)
my_default_dict['key'] += 1  # Automatically initializes to 0, then increments by 1
print(my_default_dict['key'])

