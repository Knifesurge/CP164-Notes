"""
------------------------------------------------------------------------
Lab 1, Task 6 - Movie_utilities#read_movie Testing
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-14
------------------------------------------------------------------------
"""
from Movie_utilities import read_movie

movie_string = "Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8"

my_movie = read_movie(movie_string)

print(my_movie)