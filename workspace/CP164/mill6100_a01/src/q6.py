"""
------------------------------------------------------------------------
Assignment 1, Task 6 - Transpose
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-14
------------------------------------------------------------------------
"""
from functions import transpose

matrix = [[0,1,2,3,4],[5,6,7,8,9,10]]
matrix_transposed = transpose(matrix)

print("Matrix: {}".format(matrix))
print("\nTransposed: {}".format(matrix_transposed))