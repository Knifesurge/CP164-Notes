"""
------------------------------------------------------------------------
Lab 1, Task 7 - Movie_utilities#read_movies Testing
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-14
------------------------------------------------------------------------
"""
from Movie_utilities import read_movies

file_handle = open('movies.txt', 'r')

movies = read_movies(file_handle)

file_handle.close()

for movie in movies:
    print("{}\n====================".format(movie))